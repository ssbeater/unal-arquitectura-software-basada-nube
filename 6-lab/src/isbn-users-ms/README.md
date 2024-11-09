# Lab

## User Microservice

### Dev environment requirements
- Docker installed

### Run App in Docker

1. Build microservice image

```
cd isbn-usres-ms
docker build -t isbn-users-ms .
```

2. Run microservice image

```
docker run -p 4000:4000 -e DB_USER=isbn -e DB_PASSWORD=123 -e DB_HOST=IP_ADDRESS
-e DB_NAME=isbn-users-db --name isbn-users-ms isbn-users-ms
```
Change **IP_ADDRESS** to the MySQL database IP adress.

### Deploy to Google Artifact Registry

Initially, this require install [gcloud CLI](https://cloud.google.com/sdk/docs/install) and authenticate.

1. Create a tag for image

```
docker tag isbn-users-ms us-east4-docker.pkg.dev/cbse-2024ii-438402/isbn-users-ms/isbn-users-ms
```

2. Push image

```
docker push us-east4-docker.pkg.dev/cbse-2024ii-438402/isbn-users-ms/isbn-users-ms
```

## Task Microservice

This proyect is developed in the `isbn-tasks-ms/main.py` file. This code is deployed to GCP as Function as a Service (FaaS). Connected to a Firestore database.