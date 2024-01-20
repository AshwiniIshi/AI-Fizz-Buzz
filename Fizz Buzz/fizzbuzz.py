from flask import Flask, jsonify
from collections import Counter

app = Flask(__name__)

# Counter to track statistics
fizz_buzz_stats = Counter()

def fizz_buzz(int1, int2, limit, str1, str2):
    result = []
    for num in range(1, limit + 1):
        if num % int1 == 0 and num % int2 == 0:
            result.append(str1 + str2)
        elif num % int1 == 0:
            result.append(str1)
        elif num % int2 == 0:
            result.append(str2)
        else:
            result.append(str(num))
    return result

@app.route('/fizzbuzz/<int:int1>/<int:int2>/<int:limit>/<string:str1>/<string:str2>', methods=['GET'])
def get_fizz_buzz(int1, int2, limit, str1, str2):
    result = fizz_buzz(int1, int2, limit, str1, str2)
    fizz_buzz_stats[(int1, int2, limit, str1, str2)] += 1
    return jsonify({"result": result})

@app.route('/statistics', methods=['GET'])
def get_statistics():
    most_used_request, hits = fizz_buzz_stats.most_common(1)[0]
    return jsonify({
        "most_used_request": {
            "int1": most_used_request[0],
            "int2": most_used_request[1],
            "limit": most_used_request[2],
            "str1": most_used_request[3],
            "str2": most_used_request[4],
        },
        "hits": hits
    })

if __name__ == '__main__':
    app.run(debug=True)
