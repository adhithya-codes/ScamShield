def analyze_url(url):
    score = 0
    reasons = []

    # Check 1: No HTTPS
    if not url.startswith('https'):
        score += 25
        reasons.append("No HTTPS - unsafe connection")

    # Check 2: URL too long
    if len(url) > 75:
        score += 20
        reasons.append("URL too long")

    # Check 3: Too many dots
    if url.count('.') > 2:
        score += 20
        reasons.append("Too many subdomains")

    # Check 4: Suspicious words
    suspicious_words = ['free', 'winner', 'lucky', 'verify', 'bank', 'login', 'secure', 'update']
    for word in suspicious_words:
        if word in url.lower():
            score += 15
            reasons.append(f"Suspicious word found: {word}")

    # Final verdict
    if score >= 60:
        verdict = "DANGEROUS"
    elif score >= 30:
        verdict = "SUSPICIOUS"
    else:
        verdict = "SAFE"

    return {
        "url": url,
        "score": min(score, 100),
        "verdict": verdict,
        "reasons": reasons
    }


# Test with real examples
test_urls = [
    "https://google.com",
    "http://free-lucky-winner.verify.xyz/bank",
    "http://sbi-secure-login-update.com"
]

for test_url in test_urls:
    result = analyze_url(test_url)
    print(f"\nURL: {result['url']}")
    print(f"Score: {result['score']}/100")
    print(f"Verdict: {result['verdict']}")
    print(f"Reasons: {result['reasons']}")