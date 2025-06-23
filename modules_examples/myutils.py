# myutils.py

def is_valid_email(email):
    """
    Very basic email check:
    - Contains exactly one '@'
    - The domain part (after '@') contains a dot '.'
    """
    if email.count('@') != 1:
        return False

    username, domain = email.split('@')
    
    if len(username) == 0 or len(domain) == 0:
        return False

    if '.' not in domain:
        return False 
    
    domain, domain_id = domain.split('.')
    
    if len(domain) == 0 or len(domain_id) == 0:
        return False

    return True

# is_valid_email using regex

import re

def is_valid_email_regex(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)




def is_strong_password(password):
    """
    Basic password check:
    - At least 8 characters
    - Contains both letters and digits
    """
    return (
        len(password) >= 8 and
        any(char.isdigit() for char in password) and
        any(char.isalpha() for char in password)
    )



