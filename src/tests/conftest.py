import pytest

from src.user_info import app
from src.user_info.models import User


@pytest.fixture(scope='module')
def new_user():
    user = User(id=1, fname='test', lname='user', email='test@user.com')
    return user


@pytest.fixture(scope='module')
def test_client():
    flask_app = app

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client
