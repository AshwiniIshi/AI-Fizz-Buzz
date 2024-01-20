# flask_fizzbuzz
simple REST API fizzbuzz

## install Flask
pip install Flask

## run
python fizzbuzz.py

## request
Generic request we can change the value for varables
http://127.0.0.1:5000/fizzbuzz/<int:int1>/<int:int2>/<int:limit>/<string:str1>/<string:str2>

Example usage:

Request: http://127.0.0.1:5000/fizzbuzz/3/5/100/fizz/buzz
         http://127.0.0.1:5000/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz

Response: {
  "result": [
    "1",
    "2",
    "fizz",
    "4",
    "buzz",
    "fizz",
    "7",
    "8",
    "fizz",.......]} (depending on the requests you made)


Request: http://127.0.0.1:5000/statistics
Response: {
  "hits": 4,
  "most_used_request": {
    "int1": 3,
    "int2": 5,
    "limit": 100,
    "str1": "fizz",
    "str2": "buzz"
  }
} (depending on the requests you made)
