import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = ''

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@yahoo.com'
    password = ''.join(random.choice(chars) for i in range(8))

    requests.post(url, allow_redirects=False, data={
        'a;sldjf': email
        'kldjf;al': password
        })

# RegEx to put quotes around list items and a comma after each
"""
^([A-Za-z]+)$
"$1",

# Array put in a json file
[
    "Harry",
    "Moe",
    "Curly"
    ]

"""

print 'Sending username %s and password %s' % (username, password)

