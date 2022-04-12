# User Infomation Api
A RESTful API built with Python and Flask allowing us to mannage user infromation such as first name, last name and email through CRUD opperations agaisnt a persistent database. 

This project will be used as a catalyst to improve my software enginnering skills along with practicing new skills via project based learning so as you can immagine is ever evolving! The infrastcurue acompanying this project can be found at - https://github.com/logan-bobo/user_infomation_api_infrastructure.

Objectives of this project from an application perspective are.
- Build a RESTful API using Flask and Python that is able to perform CRUD opperations against a database
- Write a set of unit tests for each function within our codebase 
- Containerize our API 
- Work on the local developer experaince, how do we make it so new developer can easly work on this project locally?
- Create a Continous Intergration pipeline for the application to allow developers to validate change and merge in code at a faster rate. 
- Write Intergration tests to prove our API responds to requests sucsesfully. Along with creating, reading, updateing and deleting data from our database.
- Deploy the application to kubernetes
- Create a Continuous Deployment pipeline so every merge to main will produce a deployment to staging where all tests are again ran then an automate deployment to production should those tests pass.

Required Functionality
- Respond to HTTP requests and take an action given a request
- Auth to the API via a key
- Create a record of user information 
- Read records of user infomration
- Update a record of user inforamtion 
- Delete a users inforamtion
