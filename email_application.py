import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailApp:

    gmail_smtp = "smtp.gmail.com"
    gmail_imap = "imap.gmail.com"

    def __init__(self, login, password, subject, recipients, message, header):
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header

    def send_message(self):
        # send message
        message_for_send = MIMEMultipart()
        message_for_send['From'] = self.login
        message_for_send['To'] = ', '.join(self.recipients)
        message_for_send['Subject'] = subject
        message_for_send.attach(MIMEText(self.message))

        message_sending = smtplib.SMTP(self.gmail_smtp, 587)
        # identify ourselves to smtp gmail client
        message_sending.ehlo()
        # secure our email with tls encryption
        message_sending.starttls()
        # re-identify ourselves as an encrypted connection
        message_sending.ehlo()

        message_sending.login(self.login, self.password)
        message_sending.sendmail(
            self.login,
            message_sending,
            message_for_send.as_string()
        )

        message_sending.quit()
        # send end

    def recieve_message(self):
        # recieve
        mailbox = imaplib.IMAP4_SSL(self.gmail_imap)
        mailbox.login(self.login, self.password)
        mailbox.list()
        mailbox.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mailbox.uid('search', None, criterion)

        assert data[0], 'There are no letters with current header'

        latest_email_uid = data[0].split()[-1]
        result, data = mailbox.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)

        mailbox.logout()
        # end recieve

if __name__ == '__main__':
    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None

    email_session = EmailApp(login, password, subject, recipients, message, header)


