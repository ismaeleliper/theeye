#THE EYE

This is a practical test to the hiring proccess of ConsumerAffairs Company.
The test consists in a collecting data of interactive events of user.
The posts requests to the THE EYE API can be send by JavaScripts Events and will be sent to processing queues to be saved.

Instructions to run this project locally (Windows):

    * Require Docker Installed

    - Clone the repository
    
    - Create a virtual environment
        - python.exe -m venv theeye-env
        - theeye-env\Scripts\activate.bat
        - pip install -r requirements.txt

    - Run the containers
        - docker-compose up
    - In other terminal tab create admin user
        - docker exec -it theeyetest_web_1 python3 manage.py createsuperuser

    - Access the inteface at your browser 
        - http://127.0.0.1:18000/user-session/

    
#API - THE EYE SIMPLE DOCUMENTATION

    - Create a new UserSession 

    - POST: http://127.0.0.1:18000/user-sessions/
    - Basic Auth - username and password
    
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
    {"Server Response": "Your data has been sent to a proccessing queue!"}

    --------------------------------------------------------------------------
    
    - Search for all User Sessions
    
    - GET - http://127.0.0.1:18000/user-sessions/

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
