test:
	curl -X POST http://127.0.0.1:5000/create \
	-H 'Content-Type: application/json' \
    -d '{"email":"test@gmail.com","fname":"John","lname":"Doe"}'