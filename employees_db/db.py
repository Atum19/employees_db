import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'HOST': 'localhost',
        'USER': 'employees_db_user',
        'PASSWORD': 'employee0',
        'NAME': 'employees_db',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB',
        }
    },
    # 'OPTIONS': {
    #    'init_command': 'SET default_storage_engine=XTRADB',
    # }
 }
