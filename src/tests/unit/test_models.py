import pytest

def test_user_model(new_user):
    """
    We can create a new user based on the user model and check that the attributes for that user are correct.
    """
    assert new_user.id == 1
    assert new_user.fname == "test"
    assert new_user.lname == "user"
    assert new_user.email == "test@user.com"
