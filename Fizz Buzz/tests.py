from flask import Flask, jsonify, request
from collections import Counter
import unittest

app = Flask(__name__)

class FizzBuzzServer:
    def __init__(self):
        self.stats_counter = Counter()

    def fizz_buzz(self, num, int1, int2, str1, str2):
        result = ""
        if num % int1 == 0:
            result += str1
        if num % int2 == 0:
            result += str2
        return result or str(num)

    def generate_fizz_buzz_list(self, int1, int2, limit, str1, str2):
        result_list = [self.fizz_buzz(i, int1, int2, str1, str2) for i in range(1, limit + 1)]
        return result_list

    def update_stats(self, int1, int2, str1, str2):
        request_params = (int1, int2, str1, str2)
        self.stats_counter[request_params] += 1

    def get_most_used_request(self):
        most_used_request, hits = self.stats_counter.most_common(1)[0]
        return {
            "int1": most_used_request[0],
            "int2": most_used_request[1],
            "str1": most_used_request[2],
            "str2": most_used_request[3],
            "hits": hits
        }

fizz_buzz_server = FizzBuzzServer()

@app.route('/fizzbuzz', methods=['GET'])
def get_fizz_buzz():
    int1 = int(request.args.get('int1'))
    int2 = int(request.args.get('int2'))
    limit = int(request.args.get('limit'))
    str1 = request.args.get('str1')
    str2 = request.args.get('str2')

    fizz_buzz_server.update_stats(int1, int2, str1, str2)

    result_list = fizz_buzz_server.generate_fizz_buzz_list(int1, int2, limit, str1, str2)
    return jsonify(result_list)

@app.route('/statistics', methods=['GET'])
def get_statistics():
    return jsonify(fizz_buzz_server.get_most_used_request())

class TestFizzBuzzServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_fizz_buzz(self):
        response = self.app.get('/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz')
        data = response.get_json()
        expected_result = ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizzbuzz"]
        self.assertEqual(data, expected_result)

    def test_get_statistics(self):
        response = self.app.get('/statistics')
        data = response.get_json()
        self.assertEqual(data, {'int1': 3, 'int2': 5, 'str1': 'fizz', 'str2': 'buzz', 'hits': 1})

if __name__ == '__main__':
    unittest.main()
