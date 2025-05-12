import pytest
from {{ cookiecutter.project_slug }}.example import Message

from pydantic import ValidationError


@pytest.mark.parametrize("text", ["some", "test", "data"])
@pytest.mark.parametrize("num", [0, 1.5, -3.14])
def test_message(text, num):
    message = Message(text_field=text, number=num)

    assert message.text_field == text
    assert message.number = num


@pytest.mark.parametrize("text, num", [(0, 0), ("test", "1"), (0, "0")])
def test_message_error(text, num):
    with pytest.raises(ValidationError):
        Message(text_field=text, number=num)
