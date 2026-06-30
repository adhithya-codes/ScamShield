def analyze_sms(message):
    score = 0
    reasons = []

    # Convert to lowercase for checking
    message_lower = message.lower()

    # Check 1: Urgency words
    urgency_words = ['urgent', 'immediately', 'expires', 'limited time', 'act now', 'hurry']
    for word in urgency_words:
        if word in message_lower:
            score += 15
            reasons.append(f"Urgency word: {word}")

    # Check 2: Money/prize words
    money_words = ['won', 'winner', 'prize', 'cash', 'reward', 'free', 'lucky draw', 'lottery']
    for word in money_words:
        if word in message_lower:
            score += 20
            reasons.append(f"Money/prize word: {word}")

    # Check 3: Suspicious links
    link_words = ['click here', 'bit.ly', 'tinyurl', 'visit now', 'http://', 'claim now']
    for word in link_words:
        if word in message_lower:
            score += 20
            reasons.append(f"Suspicious link/action: {word}")

    # Check 4: Personal info requests
    personal_words = ['otp', 'password', 'bank account', 'aadhar', 'pan card', 'kyc']
    for word in personal_words:
        if word in message_lower:
            score += 25
            reasons.append(f"Requests personal info: {word}")

    # Final verdict
    if score >= 60:
        verdict = "SCAM"
    elif score >= 30:
        verdict = "SUSPICIOUS"
    else:
        verdict = "SAFE"

    return {
        "message": message[:50] + "...",
        "score": min(score, 100),
        "verdict": verdict,
        "reasons": reasons
    }


# Test messages
test_messages = [
    "Your OTP is 4521. Do not share with anyone.",
    "Congratulations! You won Rs 50,000 in lucky draw. Click here to claim now: bit.ly/win50k",
    "Dear customer your KYC is expired. Update immediately or your account will be blocked. Visit now: http://sbi-kyc.xyz",
    "Your Amazon order #12345 has been shipped and will arrive tomorrow."
]

for sms in test_messages:
    result = analyze_sms(sms)
    print(f"\nSMS: {result['message']}")
    print(f"Score: {result['score']}/100")
    print(f"Verdict: {result['verdict']}")
    print(f"Reasons: {result['reasons']}")