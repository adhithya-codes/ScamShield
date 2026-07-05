import cv2
from url_checker import analyze_url

def analyze_qr(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Create QR code detector
    detector = cv2.QRCodeDetector()
    
    # Detect and decode QR code
    data, bbox, _ = detector.detectAndDecode(image)
    
    if not data:
        return {
            "verdict": "UNKNOWN",
            "reason": "No QR code found in image"
        }
    
    print(f"QR Code contains: {data}")
    
    # Check if it's a URL
    if data.startswith('http'):
        result = analyze_url(data)
        return {
            "qr_data": data,
            "score": result['score'],
            "verdict": result['verdict'],
            "reasons": result['reasons']
        }
    else:
        return {
            "qr_data": data,
            "verdict": "SAFE",
            "reasons": ["QR contains text, not a URL"]
        }

# Test
result = analyze_qr("test_qr.png")
print(f"\nScore: {result.get('score', 'N/A')}/100")
print(f"Verdict: {result.get('verdict')}")
print(f"Reasons: {result.get('reasons', [])}")