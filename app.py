from flask import Flask, render_template, request, jsonify
from url_checker import analyze_url
from sms_checker import analyze_sms
from job_scam_checker import analyze_job

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check-url', methods=['POST'])
def check_url():
    data = request.json
    url = data.get('url', '')
    result = analyze_url(url)
    return jsonify(result)

@app.route('/check-sms', methods=['POST'])
def check_sms():
    data = request.json
    message = data.get('message', '')
    result = analyze_sms(message)
    return jsonify(result)

@app.route('/check-job', methods=['POST'])
def check_job():
    data = request.json
    job_text = data.get('job_text', '')
    result = analyze_job(job_text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)