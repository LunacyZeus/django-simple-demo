import os
from configs.default import *

# DEBUG设置
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR.parent, 'db.sqlite3'),
    }
}