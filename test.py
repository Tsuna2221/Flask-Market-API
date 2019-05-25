try:
    from key import db
    print('success')
except:
    from os import environ
    db = environ.get('DB')
    