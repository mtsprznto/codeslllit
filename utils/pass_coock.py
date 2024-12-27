import secrets

def generate_pass():

    password = secrets.token_urlsafe(16)
    #print(password)
    return password
