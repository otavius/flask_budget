import pytest 
from budget.src.models import User


@pytest.fixture
def test_new_user():
    """
    Given a User model 
    It's going to test when a new user is created. 
    """
    user = User("Chris", "Head", "chrishead@yahoo.", "flask", "head123")
    assert user.first_name == "Chris"
    assert user.last_name == "Head"
    assert user.email == "chrishead@yahoo.com"
    assert user.password == "flask"
    assert user.username == "head123"
    