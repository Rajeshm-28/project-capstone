                                    Capstone Project
Casting Agency

The Casting Agency is responsible for creating movies and managing and assigning actors to those movies.

This Flask application is hosted via Heroku and enabled role based authentication and roles-based access control(RBAC) via Auth0 (third-party authentication system).


About the Stack:

The project is hosted in Heroku. 

Endpoint for application:

https://raj-capstone-app.herokuapp.com/


Authentication:

The API uses Access tokens generated via Auth0 to authenticate requests.

Role based authentication has been setup for 3 roles using AUTH0

Roles & Permissions

1.Casting Assistant

    -Can view actors and movies

2.Casting Director

    -Can view actors and movies

    -Add or delete an actors from the database 

    -Modify actors or movies

3.Executive Producer

    -Can view actors and movies

    -Add or delete an actors & movies from the database 

    -Modify actors or movies

Endpoints:

GET    '/'

GET    '/actors'

GET    '/movies'

GET    '/actors/<actor_id>'

GET    '/movies/<movie_id>'

POST   '/actors'

POST   '/movies'

PATCH  '/actors/<actor_id>'

PATCH  '/movies/<movie_id>'

DELETE '/actors/<actor_id>'

DELETE '/movies/<movie_id>'


GET    '/'
 - A welcome message will be presented.
 - No authentication required. 
 - Sample URL: https://raj-capstone-app.herokuapp.com/
 - returns:

{

     "Message":"Welcome To Casting Agency",

     "success":true

}

GET /actors 
 - Returns details of all actors.
 - authentication required. 
 - Sample URL: https://raj-capstone-app.herokuapp.com/actors

Sample output:

{

    "actors": [

        {

            "age": 52,

            "gender": "M",

            "id": 1,

            "name": "Vin Diesel"

        },

        {

            "age": 48,

            "gender": "M",

            "id": 2,

            "name": "Dwayne johnson"

        }

    ],

    "success": true

}

GET /movies 
 - Returns details of all movies.
 - authentication required. 
 - Sample URL: https://raj-capstone-app.herokuapp.com/movies

Sample output:

{

    "movies": [

        {

            "id": 1,

            "release_date": "02/04/2021",

            "title": "F9: The Fast Saga"

        },

        {
            "id": 2,

            "release_date": "26/06/2020",

            "title": "Top Gun: Maverick"

        }

    ],

    "success": true

}

GET /actors/<actor_id> 
 - Returns actor details for the given id.
 - authentication required. 
 - Sample URL: https://raj-capstone-app.herokuapp.com/actors/1
 
Sample output:

{

    "actors":{

            "age": 52,

            "gender": "M",

            "id": 1,

            "name": "Vin Diesel"

        },

    "success": true

}

GET /movies/<movie_id> 
 - Returns movie details for the given id
 - authentication required. 
 - Sample URL: https://raj-capstone-app.herokuapp.com/movies/1
 
Sample output:

{

    "movies":{

            "id": 1,

            "release_date": "02/04/2021",

            "title": "F9: The Fast Saga"

        },

    "success": true
}

POST /actors 
 - create a new actor
 - authentication required. 
 - Sample URL: https://raj-capstone-app.herokuapp.com/actors

Sample input:

{
	"name": "jason statham ",

	"age": "52",

	"gender": "M"

}

Sample output:

{

    "actor": {

        "age": 52,

        "gender": "M",

        "id": 3,

        "name": "jason statham"

    },

    "message": "Actor Successfully Added!",

    "success": true

}

POST /movies 
 - create a new movie
 - authentication required. 
 - Sample URL: https://raj-capstone-app.herokuapp.com/movies
 
Sample input:

{

	"title": "Wonder Women 1984",

	"release_date": "14/08/2020"

}

Sample Output:

{

    "message": "Movie Successfully Added!",

    "movies": {

        "id": 1,

        "release_date": "02/04/2021",

        "title": "F9: The Fast Saga"

    },

    "success": true

}

PATCH /actors/<actor_id> 
 - Update the existing actor
 - authentication required. 
 - Sample URL: https://raj-capstone-app.herokuapp.com/actors/1

Sample input:

{

	"age": "53"

}

PATCH /movies/<movie_id> 
 - Update the existing movie
 - authentication required. 
 - Sample URL: https://raj-capstone-app.herokuapp.com/movies/1

Sample input:

{

	"release_date": "14/09/2020"

}

DELETE /actors/<actor_id> 
 - Delete an exsiting actor
 - authentication required. 
 - Sample URL: https://raj-capstone-app.herokuapp.com/actors/1

Sample Output:

{

    'success': True,

    'message': "Actor successfully deleted!"

}

DELETE /movies/<movie_id> 
 - Delete an exsiting movie
 - authentication required. 
 - Sample URL: https://raj-capstone-app.herokuapp.com/movie/1

Sample Output:

{

    'success': True,

    'message': "Movie successfully deleted!"

}

Error Handling:

Errors are returned as JSON objects in the following format:

{

    "success": False, 

    "error": 404,

    "message": "Resource Not Found"

}

Error Response:

400 Bad Request        - the request could not be understood or was missing required parameters.

401 Unauthorized       - authentication failed or user doesn't have permissions for requested operation.

403 Forbidden          - access denied.

404 Resorurce Not Found- resource was not found.

405 Method Not Allowed - requested method is not supported for resource.


Testing:

Live testing:

Application hosted in heroku can be tested using the below Bearer Token

Endpoint for application:

https://raj-capstone-app.herokuapp.com/

1.Casting Assistant Bearer Token:

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFucUh0cm5PZ254UDZjMURVNkVPaiJ9.eyJpc3MiOiJodHRwczovL3JhamZzbmQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlY2E0NDFmZWU1NmM0MGM2ZDgzYzAyMSIsImF1ZCI6IkNhcGVBdXRoIiwiaWF0IjoxNTkwODM4MTA4LCJleHAiOjE1OTA5MjQ1MDgsImF6cCI6IkRuSUZ0NW0zMmk0SHZzQndlZ0VNMjJjYVNxcERWMUFjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y2Fwc3RvbmUiXX0.N1AkEahYlyVfb526uyjWqLtwCNrtOqtjH_gsJqb8PXPJAL65rUqBuG94iw9QxMEXhRXeEG9aVHfmqsAmlBWq5NPZzdB0aeJrtEN7nghrhEYZC7hOXOTZMfX4yCOpVlrgOMkTbs_8rrQ6bRRInVv4bHAIARgFi2UW_oCj5AAXveue6FVyju-piRfueoCibu2EHcGZ95bB4lC4vNJ8I5nrdEtw0mtGeIEOfgtYJJNofIkZoiEPOGH8PexhD-mlhuJiMBvyRzCBItyARjBm8IDgDvLinD4YNKRuqlQxzRHs-IZi_gZ1GTEXVEw0XevZLFtITios5MK2JhfF990snvM8tQ

2.Casting Director Bearer Token:

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFucUh0cm5PZ254UDZjMURVNkVPaiJ9.eyJpc3MiOiJodHRwczovL3JhamZzbmQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlY2E0NDdlZWU1NmM0MGM2ZDgzYzBmNCIsImF1ZCI6IkNhcGVBdXRoIiwiaWF0IjoxNTkwODM4MTcyLCJleHAiOjE1OTA5MjQ1NzIsImF6cCI6IkRuSUZ0NW0zMmk0SHZzQndlZ0VNMjJjYVNxcERWMUFjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJnZXQ6Y2Fwc3RvbmUiLCJwYXRjaDpjYXBzdG9uZSIsInBvc3Q6YWN0b3IiXX0.MP-OOB2Yy1Y6bV6Er_rh18sOskH3QrxUf7nzzQUWaHdVoodeIN0TeO8TGmYmMIwNTvZ8eIrkaYqHC-h3h2ZV0cxdXHaalX3tKzK79AWfMkJ0Xizk9S-KvQsfTnexcp8W1yoSbuVbn56GVJ6YaDTGEoLCEzCVBfF7DVFBJyUVK1gNkXZurjLK3HUkYAq2_J0OvkWsiA5MzhSAtMaLBOAlWxZZgGpb68lLvmmmB6OOtLQOBzwEgvc6Ujjgax5icFFZnF0up-DlDRo0d0QEeD3WMg4wNgJXtatmhGU8TbDi7u6LA6ibzuPmPtG9fVhX14QYqbDXbk6UDI3jLOADyMrkiw


3.Executive Producer Bearer Token:

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFucUh0cm5PZ254UDZjMURVNkVPaiJ9.eyJpc3MiOiJodHRwczovL3JhamZzbmQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlY2E0NGFlZjc5MDhjMGM2OGE0YTlhYiIsImF1ZCI6IkNhcGVBdXRoIiwiaWF0IjoxNTkwODM4MjQyLCJleHAiOjE1OTA5MjQ2NDIsImF6cCI6IkRuSUZ0NW0zMmk0SHZzQndlZ0VNMjJjYVNxcERWMUFjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6Y2Fwc3RvbmUiLCJwYXRjaDpjYXBzdG9uZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.hkTGkskF7BUO6mtPW381Vpd0kbq-JnnIO-HsjHzgETMoCTwwjoilqL7xucp8R5R-iS_UzEdsn9IlWgLWpSX9Ryzvgtw3tPB5BMQdupj9rw8GCY-LkxFPu8_8YJUALtrn8GstaG61OPSVPguJEx0VjbJ3IfxvrzkPAO6NHlkFe6S67xK8RZ8LPhHt4gjNay7hhlIl0tqf3MHusoRfEUHpj-ixu510MDCHrI11ZBxs2WCrVDdlSu4mpvg5yNT7cqlYZ95LOUTKcSUtdJ9AFZ9B4ti12RQ02eYerXbLTbd3hcSUpjVizrqIn4tfrfXLVwErpNYch55JwWrEK7h-lPocJg


Unit Testing:

Unit test will be run using the Executive producer Bearer token which is allowed to run all the endpoints.

To run the tests locally, make sure you have PostgreSQL installed, https://www.postgresql.org/

Create a test postgre database.

Setup the 2 environment variables using export command.

1. DATABASE_URL=postgresql://username:password@localhost:5432/databasename

   replace username,password & databasename

    Example:

    export DATABASE_URL=postgresql://DELL@localhost:5432/capstonedb

2. ACCESS_TOKEN -This is the Bearer token generated from AUTH0 for the role - Executive Producer which 
   is allowed to run all endpoints.

   export ACCESS_TOKEN="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFucUh0cm5PZ254UDZjMURVNkVPaiJ9.eyJpc3MiOiJodHRwczovL3JhamZzbmQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlY2E0NGFlZjc5MDhjMGM2OGE0YTlhYiIsImF1ZCI6IkNhcGVBdXRoIiwiaWF0IjoxNTkwODM4MjQyLCJleHAiOjE1OTA5MjQ2NDIsImF6cCI6IkRuSUZ0NW0zMmk0SHZzQndlZ0VNMjJjYVNxcERWMUFjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6Y2Fwc3RvbmUiLCJwYXRjaDpjYXBzdG9uZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.hkTGkskF7BUO6mtPW381Vpd0kbq-JnnIO-HsjHzgETMoCTwwjoilqL7xucp8R5R-iS_UzEdsn9IlWgLWpSX9Ryzvgtw3tPB5BMQdupj9rw8GCY-LkxFPu8_8YJUALtrn8GstaG61OPSVPguJEx0VjbJ3IfxvrzkPAO6NHlkFe6S67xK8RZ8LPhHt4gjNay7hhlIl0tqf3MHusoRfEUHpj-ixu510MDCHrI11ZBxs2WCrVDdlSu4mpvg5yNT7cqlYZ95LOUTKcSUtdJ9AFZ9B4ti12RQ02eYerXbLTbd3hcSUpjVizrqIn4tfrfXLVwErpNYch55JwWrEK7h-lPocJg"

   
Run the unit test using the below command.

    python test_app.py


Test Result is availble in the below file:

capstone-postman-collection.postman_test_run.json

