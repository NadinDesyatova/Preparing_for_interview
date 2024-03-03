import pytest

from stack_package.check_brackets import check_brackets


@pytest.mark.parametrize(
    "brackets_string,expected", (
            ["(((([{}]))))", "Сбалансированно"],
            ["[([])((([[[]]])))]{()}", "Сбалансированно"],
            ["{{[()]}}", "Сбалансированно"],
            ["}{]", "Несбалансированно"],
            ["(", "Несбалансированно"],
            ["", "Передана пустая строка"],
            ["}{}", "Несбалансированно"],
            ["{{[(])]}}", "Несбалансированно"],
            ["[[{())}]", "Несбалансированно"],
            [")))(((", "Несбалансированно"],
            [")((())", "Несбалансированно"]
    )
)
def test_check_brackets_string(brackets_string, expected):
    result = check_brackets(brackets_string)

    assert result == expected


if __name__ == "__main__":
    pytest.main()