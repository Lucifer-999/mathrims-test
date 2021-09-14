# Mathrithms API test
API program for mathrims

This programs reads data from a json file and creates a server using flask on localhost:5001


The server has 2 api endpoint `/users` and `/users/{id}`

`/users` will give the json output with all the users present in data.json.

`/users/{id}` will only give the details of the specefic user-id from the data.json file.


# Usage

To run the program, fir installl the required libraries from requirements.txt with
>pip3 install -r requirements.txt


And then simply run the script with
>python3 api.py

Open your browser and go to `http://localhost:5001/users` to view all users and `http://localhost/users/{id}` to search for a specefic user id.
