import pytest
import hanger

@pytest.fixture()
def test_bot():
    test_bot = hanger.AI([], 4)
    test_bot.secret_word = "test"
    return test_bot