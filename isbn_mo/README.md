# Delivery 1 - Software Engineering - ISBN_MO

## Running App

### Dev environment requirements
- Python installed
- Docker installed

### Run App in Dev environment
1. Install dependencies

    `pip install -r requirements`
2. Create the *.env* file and set database url in

    ```
    DB_URL=mysql+mysqlconnector://user:123456@localhost:3306/isbn_db
    ```
    Use *localhost* in database IP in this case
3. Setup database in docker

    `docker compose -p "isbn_dev" -f "docker-compose.dev.yml" up`
4. Run database seed to create Task table

    `python .\seed\db-seed.py`
5. Run app

    `python .\app.py`
6. Visit [localhost:4200](http://127.0.0.1:4200/)

### Run App in Docker
1. Install dependencies

    `pip install -r requirements`
2. Create the *.env* file and set database url in

    ```
    DB_URL=mysql+mysqlconnector://user:123456@172.18.0.2:3306/isbn_db
    ```
    Use *172.18.0.2* in database IP in this case

3. Run project using docker

    `docker compose -p "isbn_mo" -f "docker-compose.yml" up --build -d`
4. Run database seed to create Task table

    `python .\seed\db-seed.py`
5. Visit [localhost:4200](http://127.0.0.1:4200/)

### App Running Recomendations
If you have problems with the database connection, try to delete the database volume created in the project root `./mysql` and run again the docker compose command

---

## Engineering Flow
