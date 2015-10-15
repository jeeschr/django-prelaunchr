"""
Django settings for AB project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

try:
    from base import *
except ImportError:
    pass


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SECRET_KEY = 'SECRETS'

DEBUG = True
TEMPLATE_DEBUG = True


# EMAIL NEEDS TO BE CONFIGURED
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True


# NEED EMAIL SERVICE INFORMATION
# EMAIL_HOST = 'smtp.test.com'
# EMAIL_HOST_USER = 'testuser'
# EMAIL_PORT = 587
# DEFAULT_FROM_EMAIL = 'Bill @ test <bill@test.com>'
# SERVER_EMAIL = 'bill@test.com'
# EMAIL_HOST_PASSWORD = 'password'



# TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
















