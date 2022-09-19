# cinema-app
App that checks the adjacent available seats of a cinema using Python and SQLite

## Run the Application
To run the app, clone the repository and run the following command:
```
python -m cinema_app.infraestructure.cinema_app_cli  
```
The database used was SQLite and it already has some information that can be used to test the code but it can be initialized running the init_db.py.
```
python init_db.py
```
That command creates the tables and insert mock data on them.

## Architecture
The code implements Hexagonal Architecture dividing the code in the following layers:
- **Domain**: It contains the business logic of the application.
    - Models
    - Repositories
- **Application**: It contains the use cases or the functionality of the application.
- **Infraestructure**: It contains the implementation of the repositories and connections to external services.

## Entity Relationship Diagram

![cinema app erd](https://i.ibb.co/1bH6V02/cinema-app-erd.png)

## UML Classes Diagram

![cinema app uml](https://i.ibb.co/gV3zrHd/cinema-app-uml.png
)