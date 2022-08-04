# User Infomation Api
A RESTful API built with Python and Flask allowing us to manage user information such as first name, last name and email 
through CRUD operations against a persistent database. 

This project will be used as a catalyst to improve my software engineering skills along with practicing new skills via 
project based learning so as you can immagine is ever evolving! The infrastructure accompanying this project can be 
found at - https://github.com/logan-bobo/user_infomation_api_infrastructure.

Objectives of this project from an application perspective are.
- Build a RESTful API using Flask and Python that is able to perform CRUD operations against a persistent database
- Write a set of unit tests for each function within our codebase 
- Containerize our API 
- Work on the local developer experience, how do we make it so new developer can easily work on this project locally?
- Create a Continuous Integration pipeline for the application to allow developers to validate change and merge in 
code at a faster rate. 
- Write Integration tests to prove our API responds to request successfully. Along with creating, reading, updating and 
deleting data from our database.
- Deploy the application to kubernetes.
- Create a Continuous Deployment pipeline so every merge to main will produce a deployment to production as we know all 
unit and integration tests have passed

Functionality required from the API
- Respond to HTTP requests and take an action given a request
- Auth to the API via a key
- Create a record of user information 
- Read records of user information
- Update a record of user information 
- Delete a users information

Interesting Extra TODO:-
[ ] Investigate lru_cache for caching function output on users or maybe even add a full caching layer with redis
[ ] Move away from SQLite to PostgreSQL 
[ ] Docker compose for backend, caching layer and API
[ ] Think about application metrics we can get
