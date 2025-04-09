# Guideline working on database

## Approach: database -first 

Database is stored on ./instance/database.db

Models for that database is in models.py

**In case you want to make changes, just change the database**

Then

Install _sqlacodegen_

Then

On terminal, types this command. Please change the path to match your local environment.

`` sqlacodegen sqlite:///C:/personal_files/staff_management/instance/database.db > models.py ``

``models.py`` will be automatically updated based on your database. 