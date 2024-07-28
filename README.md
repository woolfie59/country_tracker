# Country Tracker API

GitHub repository: https://github.com/woolfie59/country_tracker_api


## The problem that this app will solve, and how my app addresses the problem.
A lot of people enjoy travelling and keeping track of the countries they have visited. Manually recording these visits can be tedious and inefficient. Travellers need a streamlined way to log and retrieve their travel history, allowing them to easily see which countries they have visited. My API project provides a digital solution to this problem by enabling users to:  
**Log their visits to various countries:** users can add entries for each country they visit, including the date of the visit. This removes the need for manual record-keeping and keeps a digital log of their travel history.   
**Retrieve their travel history:** Users can query the API to see which countries they have visited. They can also see the details of each visit, such as the date and what country was visited.   
**User Management:** The app supports user management, allowing multiple users to register and maintain their own travel logs. This ensures that each user has a personalised experience and can view their specific travel history.   
#### How my app does this
**Centralised travel log:** The API provides endpoints to create, read, update, and delete travel entries. Users can add new countries they have visited, retrieve a list of visited countries, and update or delete entries if needed.   
**Easy to use:** My API uses a RESTful interface which allows users to interact with their travel data using standard HTTP methods. The simplicity of the API makes it accessible to both technical and non-technical users.   
**Data integrity and security:** The use of JSON Web Tokens (JWTs) ensures that user data is secure and only accessible by authenticated users. The database schema ensures that each travel entry is associated with a valid user and country.   


## Task allocation and tracking in this project.
### Repository and Branch Management
My project is hosted on GitHub, which allows for efficient task allocation and tracking through the use of branches, pull requests, and issues.
#### Branches:
**Main:** The main branch is the primary branch where the main code can be found.   
**Feature branches:** For new features or fixes, branches are created from the main branch. Each branch focuses on a specific task or feature, ensuring that work is isolated and conflicts are minimised.   
#### Pull Requests:
Pull requests are used to merge changes from feature branches into the main branch. They facilitate code review and discussion, ensuring that all changes are reviewed before being merged. Each pull request has a commit message, which gives an explanation of the code changes.


### Third-party services, packages and dependencies.
**Flask:** Flask is a framework in Python. It is designed to be easy to learn for simple projects, and has the ability to scale up to complex applications. This serves as the core framework for this API.  
**Flask SQLAlchemy:** Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy and Object-Relational Mapping (ORM) libraries. This provides database integration and ORM capabilities, making it easier to manage database operations and relationships.  
**Flask Marshmallow:** Description: Flask-Marshmallow is an object serialisation/deserialization library for Flask that integrates with SQLAlchemy. This Helps in converting complex data types, such as objects, to and from native Python data types for easy JSON serialisation.  
**Flask JWT Extended:** An extension for Flask that adds support for secure JSON Web Tokens (JWT) handling. Provides user authentication and authorization using JWT, ensuring secure API endpoints.  
**Pandas:** Pandas is used for reading and processing CSV files to seed the database with initial data.  
**PostgreSQL:** PostgreSQL is a database system for storing and managing application data.  
**Bcrypt:** Bcrypt is a password hashing function designed for secure password storage.  
**GitHub:** GitHub is a version control platform, which hosts a project's source code, tracks issues, and manages pull requests.  
**PostgreSQL Database Service:** Provides database services for an application, managing data storage.  


## Benefits and drawbacks of the underlying database system.
My application uses PostgreSQL.
### Benefits
Free to use, custom functions, good encryption, supports JSON, easy to find resources.
### Drawbacks
Can be difficult to learn for new users, which makes it difficult to optimise, uses a lot of memory.


## Features, purpose and functionalities of the ORM used.
### Features
My application uses SQLAlchemy. Some SQLAlchemy features include mapping classes to tables, which allows the conversion of Python classes into database tables and lets you interact with the database using Python objects instead of writing SQL queries. It supports various databases, such as PostgreSQL and MySQL. It also manages database connections through session management, and defines relationships between tables, such as one-to-one, one-to-many, and many-to-many.

### Purpose
To simplify interaction with the database in a project, allowing the user to use Python to code.

### Functionalities
**CRUD operations:** Create, Read, Update, and Delete for updating information in the database.   
**Creating database schemas:** the user can automatically create schema in the database by using Python classes.  
**Creating tables and relationships:** the user can create tables and define their relationships using Python.  


## The ERD and how the relations between the diagrammed models aid the database design.
The ERD for this project looked a bit different then how the database actually ended up looking. For example, one of the tables in the ERD ‘Wishlist’ was removed due to time constraints.
The difference was also partly due to me misinterpreting how the relationships between the tables would work during the planning stage. For example, the User table and the Country table should have had a relationship, as a User can visit many Countries, and a Country can be visited by many Users.

  ![countrytrackerapi drawio (1)](https://github.com/user-attachments/assets/f2c19dac-0ec4-40db-972a-c5e7bcdc5d19)


## The implemented models and their relationships, including how the relationships aid the database implementation.
The relationships of the completed tables:   
**User and Visited:** A User can have multiple Visited entries (one-to-many relationship).   
In the Visited model, user_id is a foreign key that references the id column in the User table. The Visited model has a user attribute that establishes a relationship to the User model, and the User model has a visiteds attribute that lists all related Visited entries.   
**Country and Visited:** A Country can be associated with multiple Visited entries (one-to-many relationship).   
In the Visited model, country_id is a foreign key that references the id column in the Country table. The Visited model has a country attribute that establishes a relationship to the Country model, and the Country model has a visiteds attribute that lists all related Visited entries.   
**User and Country:** A User can be associated with multiple Country entries (one-to-many relationship).   
In the Country model, user_id is a foreign key that references the id column in the User table. The Country model has a user attribute that establishes a relationship to the User model, and the User model has a countries attribute that lists all related Country entries.   


## Application endpoints

### Create Tables   
HTTP Verb: **GET**   
Path: /db/create   
Description: Creates the necessary tables in the database.   
Required Body or Header Data: None   
Response: A message indicating whether the tables were successfully created.   

### Drop Tables   
HTTP Verb: **GET**   
Path: /db/drop   
Description: Drops all the tables in the database.   
Required Body or Header Data: None   
Response: A message indicating whether the tables were successfully dropped.   

### Seed Tables   
HTTP Verb: **GET**   
Path: /db/seed   
Description: Seeds the database with initial data from a CSV file and predefined users.   
Required Body or Header Data: None   
Response: A message indicating whether the tables were successfully seeded.   

### Check if a Country has been Visited   
HTTP Verb: **GET**   
Path: /country/<country_name>   
Description: Checks if a specified country has been visited.   
Required Body or Header Data: None   
Response: JSON response with the country name and a boolean indicating if it has been visited.   

Example Request:   
**GET** /country/France   

Example Response:   
```
{
  "country": "France",
  "visited": true
}
```

### Get All Visited Entries   
HTTP Verb: **GET**   
Path: /visiteds   
Description: Retrieves all visited entries.   
Required Body or Header Data: None   
Response: JSON array of all visited entries.   

Example Request:   
**GET** /visiteds

Example Response:   
```
[
  {
    "id": 1,
    "date": "2024-07-28",
    "user": {
      "id": 1,
      "name": "admin",
      "email": "admin@email.com"
    },
    "country": {
      "id": 1,
      "name": "France",
      "visited": true
    }
  },
  {
    "id": 2,
    "date": "2024-07-28",
    "user": {
      "id": 1,
      "name": "admin",
      "email": "admin@email.com"
    },
    "country": {
      "id": 2,
      "name": "Germany",
      "visited": true
    }
  }
]
```

### Add a New Visited Entry   
HTTP Verb: **POST**   
Path: /visiteds   
Description: Adds a new visited entry to the database.   
 
Required Body or Header Data:   
Headers: Content-Type: application/json   
Body: JSON object with the date, user_id, and country_id.   

Example Request:   
**POST** /visiteds   
```
{
  "date": "2024-07-28",
  "user_id": 1,
  "country_id": 2
}
```

Example Response:   
```
{
  "id": 3,
  "date": "2024-07-28",
  "user": {
    "id": 1,
    "name": "admin",
    "email": "admin@email.com"
  },
  "country": {
    "id": 2,
    "name": "Germany",
    "visited": true
  }
}
```
  ![POST new visit](https://github.com/user-attachments/assets/27f0128e-0342-45f0-bb6e-0c7b5d1647b2)

#### Get a Specific Visited Entry
HTTP Verb: **GET**   
Path: /visiteds/<id>   
Description: Retrieves a specific visited entry by its ID.   
Required Body or Header Data: None   
Response: JSON object of the specified visited entry.   

Example Request:   
**GET** /visiteds/1   

Example Response:   
```
{
  "id": 1,
  "date": "2024-07-28",
  "user": {
    "id": 1,
    "name": "admin",
    "email": "admin@email.com"
  },
  "country": {
    "id": 1,
    "name": "France",
    "visited": true
  }
}
```

#### Update a Visited Entry   
HTTP Verb: **PUT**   
Path: /visiteds/<id>   
Description: Updates a specific visited entry by its ID.   

Required Body or Header Data:   
Headers: Content-Type: application/json   
Body: JSON object with updated date, user_id, and/or country_id.   

Example Request:   
**PUT** /visiteds/1
```
{
  "date": "2024-07-29",
  "user_id": 2,
  "country_id": 3
}
```

Example Response:   
```
{
  "id": 1,
  "date": "2024-07-29",
  "user": {
    "id": 2,
    "name": "user1",
    "email": "user1@email.com"
  },
  "country": {
    "id": 3,
    "name": "Italy",
    "visited": true
  }
}
```
  ![PATCH visit](https://github.com/user-attachments/assets/1c5a1eeb-886a-4e41-8c20-1aeb99bdea13)

#### Delete a Visited Entry   
HTTP Verb: **DELETE**   
Path: /visiteds/<id>   
Description: Deletes a specific visited entry by its ID.   
Required Body or Header Data: None   
Response: JSON object with a message indicating whether the entry was successfully deleted.   

Example Request:   
**DELETE** /visiteds/1   

Example Response:   
```
{
    "message": "Visit deleted successfully."
  }
```
  ![DELETE visit](https://github.com/user-attachments/assets/76f24241-a7cc-4ee5-a492-d8faaad8391b)


#### Other requests and responses
**Login token**
  ![login token](https://github.com/user-attachments/assets/2b68cefb-f9f1-4fcb-9644-77bdd1eab138)
**Invalid email**
  ![invalid email](https://github.com/user-attachments/assets/95361c46-7c1d-4944-9178-ca57d6941602)
**Email already in use**
  ![email already in use](https://github.com/user-attachments/assets/f6f9d39f-c484-45ef-8599-f0330ef9fdac)


