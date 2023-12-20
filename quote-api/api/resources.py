from flask import jsonify
from flask_restful import Resource
import json
from random import randint

#Put outside of the function to improve performance
f = open('quotes.json', 'r', errors='ignore')
QUOTES = json.load(f)

def get_random_quote():
    return QUOTES[randint(0,5421)] #return a ramdom quote in 5421 quotes of the list

class Quotes(Resource):
    def get(self):
        try:
            return jsonify(get_random_quote())
        except Exception as ex:
            return {
                'msg': "Something's happened",
                'exception': ex
            }
