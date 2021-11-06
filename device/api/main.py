from flask import Flask, json
import os

api = Flask(__name__)

@api.route('/lights-on', methods=['GET'])
def lights_on():
    os.system('raspi-gpio set 4 op dl pd');
    return json.dumps({'status': 'ok'})


@api.route('/lights-off', methods=['GET'])
def lights_off():
    os.system('raspi-gpio set 4 op dh pd');
    return json.dumps({'status': 'ok'})

if __name__ == '__main__':
        api.run(host='0.0.0.0', port=80) 
