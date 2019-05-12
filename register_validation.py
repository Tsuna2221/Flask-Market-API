import re

def v_email(email):
    test = bool(re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email))
    if test:
        return True
    return False

def v_pass_match(password, confirmation):
    if password == confirmation:
        return True
    return False

def v_pass(password):
    if len(password) >= 6:
        digitTest = bool(re.search(r"[0-9]", password))
        if digitTest:
            letterTest = bool(re.search(r"[a-zA-Z]", password))

            if letterTest:
                return True
            else:
                return False
        else:
            return False
    return False

