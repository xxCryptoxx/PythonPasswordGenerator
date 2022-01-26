import secrets

password_length = int(input('length:'))
token = secrets.token_urlsafe(password_length)
print(token)