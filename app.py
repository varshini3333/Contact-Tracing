from flask import Flask, request, jsonify, render_template
import pandas as pd
from twilio.rest import Client
import json

app = Flask(__name__)

# Twilio configuration
account_sid = 'AC7058c4887f76b1aec0c8be8af110999d'
auth_token = '9f09e28aecdc6f698308b67c7de755a2'
twilio_phone_number = '+17066003284'
client = Client(account_sid, auth_token)

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/results', methods=['GET'])
def results():
    input_name = request.args.get('name')
    disease = request.args.get('disease')
    data = pd.read_json('newdataset.json')
    contacts = data[data['id'] == input_name].to_dict(orient='records')
    return render_template('result.html', contacts=contacts, disease=disease)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    phone_numbers = request.json.get('phone_numbers')
    message = request.json.get('message')
    results = []

    for number in phone_numbers:
        try:
            message = client.messages.create(
                body=message,
                from_=twilio_phone_number,
                to=number
            )
            results.append(f"Message sent to {number}")
        except Exception as e:
            results.append(f"Failed to send message to {number}: {str(e)}")

    return jsonify(results=results)

if __name__ == '__main__':
    app.run(debug=True)
