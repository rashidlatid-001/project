users = {
    "admin": "1234",   # valid username and password
}

def check_user(username, password):
    return users.get(username) == password
