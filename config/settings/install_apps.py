DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

LOCAL_APPS = [
    'apps.general',
    'apps.users',
    'apps.sponsors',
    'apps.appeals',
    'apps.authentication',
    'apps.permissions',
    'drf_yasg',
]



THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',

]

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS