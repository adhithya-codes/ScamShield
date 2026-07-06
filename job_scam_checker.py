def analyze_job(job_text):
    score = 0
    reasons = []
    
    text = job_text.lower()
    
    # Check 1: Unrealistic salary promises
    money_words = [
        'earn from home', 'work from home', 
        'no experience needed', 'no qualification',
        'earn daily', 'weekly payment', 'guaranteed salary'
    ]
    for word in money_words:
        if word in text:
            score += 20
            reasons.append(f"Suspicious promise: {word}")
    
    # Check 2: Registration/payment request
    payment_words = [
        'registration fee', 'pay to join', 
        'deposit required', 'training fee',
        'security deposit', 'pay now to confirm'
    ]
    for word in payment_words:
        if word in text:
            score += 30
            reasons.append(f"Asks for money: {word}")
    
    # Check 3: Urgency tactics
    urgency_words = [
        'limited seats', 'apply immediately',
        'last date today', 'only today',
        'hurry', 'urgent requirement'
    ]
    for word in urgency_words:
        if word in text:
            score += 15
            reasons.append(f"Urgency tactic: {word}")
    
    # Check 4: Fake company signs
    fake_signs = [
        'no interview', 'direct selection',
        'guaranteed job', 'instant joining',
        'whatsapp to apply', 'contact on telegram'
    ]
    for word in fake_signs:
        if word in text:
            score += 25
            reasons.append(f"Fake job sign: {word}")
    
    # Final verdict
    if score >= 60:
        verdict = "FAKE JOB SCAM"
    elif score >= 30:
        verdict = "SUSPICIOUS"
    else:
        verdict = "LOOKS GENUINE"
    
    return {
        "score": min(score, 100),
        "verdict": verdict,
        "reasons": reasons
    }


# Test with real examples
test_jobs = [
    """Urgent requirement! Work from home job. 
    No experience needed. Earn Rs 50,000 monthly. 
    Limited seats. Pay registration fee of Rs 1,500 
    to confirm. WhatsApp to apply now.""",
    
    """Software Engineer at Google. 
    Requirements: 2 years Python experience. 
    Apply at careers.google.com. 
    CTC: 18 LPA. Interview process: 4 rounds.""",
    
    """Data Entry job. Work from home. 
    Weekly payment guaranteed. No interview. 
    Direct selection. Contact on Telegram. Hurry!"""
]

for job in test_jobs:
    result = analyze_job(job)
    print(f"\nJob Post: {job[:60]}...")
    print(f"Score: {result['score']}/100")
    print(f"Verdict: {result['verdict']}")
    print(f"Reasons: {result['reasons']}")