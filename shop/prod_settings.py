import os # импортируем библиотеку Питона

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# распазнаем путь к нашему проекту в любых ОС
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Секретный ключ для хеширования данных
SECRET_KEY = '^3p7qggajurnrbtb+jd*0-uv@s%w3f4)2(1hi3oiu*kzb1_^uuhq6qe&(g@'

# SECURITY WARNING: don't run with debug turned on in production!
# Режим распознавания ошибок с распечаткой
DEBUG = False

# Доменный адрес или ip адрес с которого только можно принимать запросы
ALLOWED_HOSTS = ['http://lifehuman.ru/']

STATIC_ROOT = os.path.join(BASE_DIR, "static")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'course',
        'USER': 'john',
        'PASSWORD': 'Q1W2e3r4T5',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}