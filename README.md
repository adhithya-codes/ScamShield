# 🛡️ AI ScamShield India

An AI-powered scam detection platform built to protect Indians from digital fraud.

## 🚨 Problem
India loses crores every year to digital scams — fake URLs, scam SMS, QR frauds, and fake job offers.

## ✅ Features
- **URL Phishing Detector** — Detects fake and dangerous URLs
- **SMS Scam Analyzer** — Identifies scam text messages  
- **QR Code Scanner** — Detects malicious QR codes
- **Fake Job Detector** — Identifies fraudulent job postings

## 🖥️ Web Interface

ScamShield has a live web interface built with Flask:

```bash
python3 app.py
# Visit http://127.0.0.1:5000
```

Features:
- Paste URL and get instant analysis
- Check SMS messages for scams
- Validate job offers

All with real-time scoring and detailed reasons.

## 🛠️ Tech Stack
- Python 3.14
- OpenCV
- Machine Learning (coming soon)

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/adhithya-codes/ScamShield.git
cd ScamShield

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install opencv-python Pillow qrcode

# Run URL checker
python3 url_checker.py

# Run SMS checker
python3 sms_checker.py

# Run Job scam checker
python3 job_scam_checker.py
```

## 👨‍💻 Developer
**Adhithya Krishna** — CSE Cybersecurity, SRM University Chennai  
GitHub: [@adhithya-codes](https://github.com/adhithya-codes)