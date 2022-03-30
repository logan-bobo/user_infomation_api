# User Infomation Api
A RESTful API built with Python and Flask allowing us to mannage user infromation such as name, date of birth, address and more through CRUD opperations agaisnt a persistent database. 

This project will be used as a catalyst to improve my software enginnering skills along with practicing new skills via project based learning so as you can immagine is ever evolving! The infrastcurue acompanying this project can be found at - https://github.com/logan-bobo/user_infomation_api_infrastructure.

Objectives of this project from an application perspective are.
- Build a RESTful API using Flask and Python that is able to perform CRUD opperations against a NoSQL backend to mannage user infromation.
- Write a set of unit tests for each function within our codebase 
- Containerize our API 
- Work on the local developer experaince, how do we make it so new developer can easly work on this project locally?
- Create a Continous Intergration system for the application to allow developers to validate change and merge in code at a faster rate. 
- Write Intergration tests to prove our API responds to requiests sucsesfully. Along with creating, reading, updateing and deleting data from our database.
- Getting our application working on kubernetes
- Write some end to end tests that we can use in a staging enviroment to have validation in a automation deployment. Do I need this? This suggests I do not trust my tests come back to this come back to this when I have worked on a deployment pattern?
- Create a Continuous Deployment pipeline so every merge to main will produce a deployment to staging where all tests are again ran then an automate deployment to production should those tests pass.


Required Functionality
- Respond to HTTP requests and take an action given a request
- Auth? (come back to this)
- Create a record of user information 
- Read records of user infomration
- Update a record of user inforamtion 
- Delete a users inforamtion

The Architechure will be:
Client --HTTP/S(443)--> API --mongod(27017)--> Postgres

