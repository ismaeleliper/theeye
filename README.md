THE EYE

This is a practical test to the hiring proccess of ConsumerAffairs Company.
The test consist in a collecting data of interactive events of user.

Instructions to run this project locally:

    - Clone the repository

    - Run the containers
        - docker-compose up

    - Create an admin user
        - docker exec -it theeyetest_web_1 python3 manage.py createsuperuser

    - Access the inteface at your browser 
        - http://127.0.0.1:18000

    
API - THE EYE SIMPLE DOCUMENTATION

    - Create a new User Session 

    - POST: http://127.0.0.1:18000/user-sessions
    
    | PARAMETER | TYPE        | DESCRIPTION                                 |
    |-----------------------------------------------------------------------|
    | category  | VARCHAR     | Category of the session                     |
    |-----------------------------------------------------------------------|
    | name      | VARCHAR     | Name of the session                         |
    |-----------------------------------------------------------------------|
    | data      | JSON_OBJECT | Impostant data may be inserted in this json |

    - Payload
    {
        "category": "Clicks",
        "name": "Click Discount Button",
        "data": {
            "host": "https://www.cool-shop.com",
            "path": "/discount",
            "element": "button-discount-10-percent"
        }
    }

    - Response
    # TODO

    --------------------------------------------------------------------------
    
    - Search for all User Sessions
    
    - GET - http://127.0.0.1:18000/user-sessions

    - Response
    {
        "session_id": "cc046e45-2c42-485d-90ff-b6697e799eb9",
        "category": "Clicks",
        "name": "Click Discount Button",
        "data": {
            "host": "https://www.cool-shop.com",
            "path": "/discount",
            "element": "button-discount-10-percent"
        },
        "timestamp: "2021-09-28T19:57:47.802120Z"
    }
