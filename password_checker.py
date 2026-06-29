import math
COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "admin",
    "welcome",
    "letmein",
    "abc123"
}
SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
def check_password_strength(password):
    score = 0
    feedback = []
    checks = {
        "length": len(password) >= 8,
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
        "number": any(c.isdigit() for c in password),
        "special": any(c in SPECIAL_CHARS for c in password)
    }
    if checks["length"]:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")
    if checks["uppercase"]:
        score += 1
    else:
        feedback.append("Add an uppercase letter.")
    if checks["lowercase"]:
        score += 1
    else:
        feedback.append("Add a lowercase letter.")
    if checks["number"]:
        score += 1
    else:
        feedback.append("Include at least one number.")
    if checks["special"]:
        score += 1
    else:
        feedback.append("Include a special character.")
    return score, feedback, checks
def get_strength_label(score):
    labels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very Strong"
    }
    return labels.get(score, "Unknown")
def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in SPECIAL_CHARS for c in password):
        charset += len(SPECIAL_CHARS)
    if charset == 0:
        return 0
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)
def estimate_crack_time(entropy):
    if entropy < 28:
        return "Instantly"
    elif entropy < 35:
        return "Few Minutes"
    elif entropy < 45:
        return "Few Hours"
    elif entropy < 60:
        return "Few Months"
    elif entropy < 80:
        return "Many Years"
    else:
        return "Centuries"
def get_statistics(password):
    return {
        "length": len(password),
        "uppercase": sum(c.isupper() for c in password),
        "lowercase": sum(c.islower() for c in password),
        "numbers": sum(c.isdigit() for c in password),
        "special": sum(c in SPECIAL_CHARS for c in password)
    }
def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS
def analyze_password(password):
    score, feedback, checks = check_password_strength(password)
    entropy = calculate_entropy(password)
    return {
        "score": score,
        "label": get_strength_label(score),
        "feedback": feedback,
        "checks": checks,
        "statistics": get_statistics(password),
        "entropy": entropy,
        "crack_time": estimate_crack_time(entropy),
        "common": is_common_password(password)
    }
