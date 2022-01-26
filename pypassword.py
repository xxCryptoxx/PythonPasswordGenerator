import secrets

password_length = int(input('length:'))
token = secrets.token_urlsafe(password_length)
counter = 0
for x in token:
    counter=+1
print(token)