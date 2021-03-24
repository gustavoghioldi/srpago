Architecture
============
In the design, time to market was prioritized.

I used a non-relational database (MongoDB) in the cloud in Atlas

I use eve as a framework (https://docs.python-eve.org/en/stable/)

The development runs on GCP, in cloud run and the pipeline is solved with cloudbuild

User authentication is done with Basic Auth.

URL en Google Cloud Platfom: https://srpago-yxa7tosfca-uc.a.run.app/api/v1/ 

Features
========
- accounts

the user can create his own account, for this he must pass his credentials in the body of the message identical to those of the basic auth and he can only interact with his own account

admin and superadmin: can read and interact with all accounts created all accounts

only superadmin can create admin users
(in cloud superadmin:password)
- countries
admin y super admin RW

users RO

- movies

admin y super admin RW

users RO

- cinemas 

admin y super admin RW

users RO

- calendar

admin y super admin RW

users RO

Search
======
You can search in every resource for field, for example:

/api/v1/movies?where=country==ARG

Logger
======
logger implements OPLOG that performs database logging all requests and responses are logged

to local run
============
docker-compose build && docker-compose up

environment variables
====================
example:
- MONGO_URI=mongodb://mongo/db
- SU_USERNAME=superuser
- SU_PASSWORD=password


what is missing (backlog?)
======
- Implements Unit tests
- encrypt passwords in database
- more detail in field validate
- implement S3 or other storage to avoid persistence of photos in the database