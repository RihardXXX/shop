import os # импортируем библиотеку Питона

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# распазнаем путь к нашему проекту в любых ОС
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Секретный ключ для хеширования данных
SECRET_KEY = '^3p7q%)+jd*0-uv@s%w3f4)2(1hi3oiu*kzb1_^uuhq6qe&(g@'

# как называться будет путь к статическим файлам
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Настройка подключения к нашей базе данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
# Режим распознавания ошибок с распечаткой
DEBUG = True

# Доменный адрес или ip адрес с которого только можно принимать запросы
ALLOWED_HOSTS = ['127.0.0.1']