# mock-reviews-svc

Exposes a simple reviews REST API backed by an in-memory database.
Intended for use learning REST clients, testing frameworks

## Running Service (using conda)

    cd [project]/service
    conda create -n "mock-reviews-svc-service" python=3.6 pip
    source activate mock-reviews-svc-service
    python app.py

## Running Service (using Docker)

    cd [project]/service
    docker-compose up --build

## API Documentation

The service self-describes the API. It can be browsed at [http://localhost:5000/api](http://localhost:5000/api)

## Acknowledgements

The flask application skeleton's structure was heavily influences by Michał Karzyński's
blog post [Building beautiful REST APIs using Flask, Swagger UI and Flask-RESTPlus](http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus). Thank you, Michał!
