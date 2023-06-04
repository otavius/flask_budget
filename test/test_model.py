from .budget.src.models import User

def test_new_user():
    """
    Given a User model 
    It's going to test when a new user is created. 
    """
    user = User("Nesia", "Whitehead", "nesiawhitehead@yahoo.", "flask", "nesia123")
    assert user.first_name == "Nesia"
    assert user.last_name == "Whitehead"
    assert user.email == "nesiawhitehead@yahoo.com"
    assert user.password == "flask"
    assert user.username == "nesia123"
    