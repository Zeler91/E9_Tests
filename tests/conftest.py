import pytest
import hanger

@pytest.fixture()
def test_bot():
    test_bot = hanger.AI(['test'], 4)
    return test_bot