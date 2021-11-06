from flask import Flask, json
import os

api = Flask(__name__)

@api.route('/discover', methods=['POST'])
def discover():
    pass


if __name__ == '__main__':
        api.run(host='0.0.0.0', port=80)
