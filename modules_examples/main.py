# import myutils
import validator.validate as validate
# from validator import validate

test_data = [
    ("abc@gmail.com", "pass1234"),      # ✅ Valid email and strong password
    ("invalid_email", "password"),      # ❌ Invalid email, ❌ Weak password (no digits)
    ("user@domain.org", "12345678"),    # ✅ Valid email, ❌ Weak password (no letters)
]


for email, password in test_data:
    print(f"Testing Email: {email}")
    print("Valid Email:", validate.is_valid_email(email))

    print(f"Testing Password: {password}")
    print("Strong Password:", validate.is_strong_password(password))
    print("-" * 40)

