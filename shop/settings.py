"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 2.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/

====================================
Файл с самими натсройками фреймворка
====================================
"""

import os # импортируем библиотеку Питона

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# распазнаем путь к нашему проекту в любых ОС
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!



# SECURITY WARNING: don't run with debug turned on in production!
# Режим распознавания ошибок с распечаткой


# Доменный адрес или ip адрес с которого только можно принимать запросы



# Application definition
# Список приложений подключенных к джанго
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',               # подключаем приложение для работы со статичными файлами
    'home',                                     # прописываем приложение домашнее основной страницы, чтобы все url не шли в блог
    'blog',                                     # прописываем наше новое приложение в джанго
    'mptt',                                     # приложение библиотека для построения бинарного дерева в django
    'menu',                                     # регистрация приложения меню
    'pages',                                    # регистрация приложения для создания статических страниц
    'django.contrib.sites',                     # это приложение помогает узнать на каком сайте мы сейчас находимся
    'feedback',                                 # приложение обратной связи с клиентами
    'ckeditor',
    'ckeditor_uploader',                        # установка специального редактора в админ панель
    'allauth',                                  # обычная авторизация
    'allauth.account',
    'allauth.socialaccount',                    # авторизация через социальные сети
    # 'allauth.socialaccount.providers.instagram', # список социальных сетей через которые можно авторизоваться
    'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.yandex',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.twitter',
]

# штука ,которая срабатывает после запроса и пока до views запрос не дошел
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'pages.middleware.PageFallbackMiddleware', # эта хуйня которая срабатывает между url запросом и Views
]

#Тут прописывается путь к главному файлу юрл запросов
ROOT_URLCONF = 'shop.urls'

# Настройка шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # указываем в какой дирректории лежат наши шаблоны
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Указываем путь, в котором будет работать файл посредник между нашим проектом и вебсервером
WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# Настройка подключения к нашей базе данных



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
# тут прописаны валидаторы паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# На каком языке будет проект
LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# как называться будет путь к статическим файлам
STATIC_URL = '/static/'
"""Подключил папку статик для загрузки стилей и фоток с корня проекта"""


# как называться будет путь к статическим файлам




# STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


CKEDITOR_UPLOAD_PATH = "/static/ckeditor/ckeditor/"
#CKEDITOR_UPLOAD_PATH = "uploads/"

# необходимые настройки для модуля авторизации пользователей
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# вместо dummy ставим протокол smtp и тому подобный
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# Allauth список настроек для модуля авторизации
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_UNIQUE = True
# ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True                             # обязательно ли подтверждение через электронную почту
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3                               # время до подтверждения регистрации
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_USERNAME_BLACKLIST = ["admin", "administrator", "moderator"]     # имена которые нельзя использовать при регистрации
ACCOUNT_USERNAME_MIN_LENGTH = 4                                          # минимальное число символов при регистрации
ACCOUNT_USERNAME_REQUIRED = False
LOGIN_REDIRECT_URL = "/"                                                 # куда направить пользователя после авторизации
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
SOCIALACCOUNT_EMAIL_VERIFICATION=False                                   # Эти два пункта нужны для того чтобы
SOCIALACCOUNT_EMAIL_REQUIRED=False                                       # не запрашивалась почта при авториз через соц сети

# Provider specific settings настройки для входа через социальные сети
SOCIALACCOUNT_PROVIDERS = {
    'vk': {
        'APP': {
            'client_id': '7310169',
            'secret': 'mSNStR9SZXkpe7swguTz',
            'key': ''
        }
    }
}

try:
    from .local_settings import *
except:
    from .prod_settings import *
