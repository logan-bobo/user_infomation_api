import json


def test_main_route(test_client):
    """
    When we hit the root of the API we expect the help message.
    """
    response = test_client.get('/v1/')
    assert response.status_code == 200
    assert b"User Information API please see the readme.md for details on how to interact with this service!" \
        in response.data


def test_main_route_fail_on_post(test_client):
    """
    When we send a post requests to the root of the API we get a failure.
    """
    response = test_client.post('/')
    assert response.status_code != 200


def test_user_creation(test_client):
    """
    We can create a user with the correct parameters passed.
    """
    response = test_client.post(
        '/v1/create-user',
        data=json.dumps({
            "fname": "test",
            "lname": "test",
            "email": "test@test.com"
        }),
        content_type='application/json'
    )
    assert response.status_code == 200
    assert b"user created successfully" \
        in response.data


def test_user_creation_fails_when_no_email_in_request_to_create_user(test_client):
    """
    User creation will fail when we send a post request to the `create-user` endpoint with no email in request.
    """
    response = test_client.post(
        '/v1/create-user',
        data=json.dumps({
            "fname": "test",
            "lname": "test",
        }),
        content_type='application/json'
    )
    assert response.status_code == 400
    assert b"request did not contain the user email" \
        in response.data


def test_user_creation_fails_when_no_fname_in_request_to_create_user(test_client):
    """
    User creation will fail when we send a post request to the `create-user` endpoint with no first name in request.
    """
    response = test_client.post(
        '/v1/create-user',
        data=json.dumps({
            "lname": "test",
            "email": "test@test.com"
        }),
        content_type='application/json'
    )
    assert response.status_code == 400
    assert b"request did not contain the users first name" \
        in response.data


def test_user_creation_fails_when_no_lname_in_request_to_create_user(test_client):
    """
    User creation will fail when we send a post request to the `create-user` endpoint with no last name in request.
    """
    response = test_client.post(
        '/v1/create-user',
        data=json.dumps({
            "fname": "test",
            "email": "test@test.com"
        }),
        content_type='application/json'
    )
    assert response.status_code == 400
    assert b"request did not contain the users last name" \
        in response.data


def test_user_can_not_be_created_due_to_non_unique_email(test_client):
    """
    User creation will fail when we send a post request to the `create-user` endpoint does not contain a unique email.
    """
    test_client.post(
        '/v1/create-user',
        data=json.dumps({
            "fname": "test",
            "lname": "test",
            "email": "test@test.com"
        }),
        content_type='application/json'
    )

    response = test_client.post(
        '/v1/create-user',
        data=json.dumps({
            "fname": "test",
            "lname": "test",
            "email": "test@test.com"
        }),
        content_type='application/json'
    )
    assert response.status_code == 500
    assert b"unable to create user due to:" \
        in response.data


def test_read_users_route_with_no_users_in_the_system_returns_empty_json():
    pass


def test_read_user_route():
    pass


def test_update_route():
    pass


def test_delete_route():
    pass