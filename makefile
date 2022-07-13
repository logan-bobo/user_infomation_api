test-create:
	curl -X POST http://127.0.0.1:5000/create-user \
	-H 'Content-Type: application/json' \
    -d '{"email":"barry1@gmail.com","fname":"barry1","lname":"barry1"}'
	curl -X POST http://127.0.0.1:5000/create-user \
	-H 'Content-Type: application/json' \
    -d '{"email":"barry2@gmail.com","fname":"barry2","lname":"barry2"}'

test-read-all:
	curl http://127.0.0.1:5000/read-users

test-read-user:
	curl http://127.0.0.1:5000/read/1