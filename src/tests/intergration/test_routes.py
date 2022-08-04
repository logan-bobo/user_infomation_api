import json


def test_main_route(test_client):
    """
    When we hit the root of the API we expect the help message
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"User Information API please see the readme.md for details on how to interact with this service!" \
        in response.data


def test_main_route_fail_on_post(test_client):
    """
    When we send a post requests to the root of the API we get a failure
    """
    response = test_client.post('/')
    assert response.status_code != 200



def test_read_users_route():
    pass


def test_read_user_route():
    pass


def test_update_route():
    pass


def test_delete_route():
    pass