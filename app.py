'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill
from helpers import validate_fields, validate_phone_number

app = Flask(__name__)

data = {
    "experience": [
        Experience("Software Developer",
                   "A Cool Company",
                   "October 2022",
                   "Present",
                   "Writing Python Code",
                   "example-logo.png")
    ],
    "education": [
        Education("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "80%",
                  "example-logo.png")
    ],
    "skill": [
        Skill("Python",
              "1-2 Years",
              "example-logo.png")
    ],
    "user_information":
        {
            "name": "",
            "email_address": "",
            "phone_number": ""
    }
}


@app.route('/test')
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        return jsonify()

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})


@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})


@app.route('/resume/user_information', methods=['GET', 'POST', 'PUT'])
def user_information():
    '''
    Handles User Information requests
    '''
    if request.method == 'GET':
        return jsonify(data['user_information']), 200

    error = validate_fields(
        ['name', 'email_address', 'phone_number'], request.json)

    is_valid_phone_number = validate_phone_number(request.json['phone_number'])

    if not is_valid_phone_number:
        return jsonify({'error': 'Invalid phone number'}), 400
    if error:
        return jsonify({'error': ', '.join(error) + ' parameter(s) is required'}), 400

    if request.method in ('POST', 'PUT'):
        data['user_information'] = request.json
        return jsonify(data['user_information']), 201

    data['user_information'] = request.json
    return jsonify(data['user_information']), 200
