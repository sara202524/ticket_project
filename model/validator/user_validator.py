import re


def en_name_validator(name):
    return re.match(r'^[a-zA-Z\s]{3,10}$', name, re.IGNORECASE)


def en_family_validator(family):
    return re.match(r'^[a-zA-Z\s]{3,10}$', family, re.IGNORECASE)


def birthday_validator(birthday):
    return re.match(r'^13[0-9]{2}/(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])$', birthday)


def username_validator(username):
    return re.match(r'^[a-zA-Z0-9_]{8,}$', username, re.IGNORECASE)


def password_validator(password):
    return re.match(r'^[a-zA-Z0-9_#@&*$]{8,}$', password)


def role_validator(role):
    return re.match(r'(user|admin)$', role, re.IGNORECASE)
