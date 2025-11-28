import db

def login(username, password):
    return db.check_user(username, password)
