
from pathlib import Path
import os
import openai
from dotenv import load_dotenv
# base dir 설정

BASE_DIR = Path(__file__).resolve().parent.parent

# .env 파일로드
load_dotenv(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = 'django-insecure-p+u01mq5w&^l+cubq^78#ont(=or5@1oi8hno%0f6rgf#$fm^4'
DEBUG = os.getenv('DEBUG') == 'True'
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

ALLOWED_HOSTS = []

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Application definition

INSTALLED_APPS = [
    'myapp',  # 생성한 앱 추가
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'commons',  
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myapp', 'templates')],  # ✅ 경로 추가
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'suyeon',
        'USER': 'suyeon',
        'PASSWORD': '0419',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')  # 기본은 Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')  # .env에서 불러오기
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'myapp' / 'static' ]
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = 'redis://localhost:6379/0'

LOGIN_REDIRECT_URL = '/'  # 로그인 성공 후 이동할 페이지
LOGOUT_REDIRECT_URL = '/'  # 로그아웃 후 이동할 페이지

MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = BASE_DIR / 'media'

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "A Letter to Myself API",
    "DESCRIPTION": "감정 분석 기반 편지 서비스 API 문서",
    "VERSION": "1.0.0",
    # 선택: 인증 설정
    "SERVE_INCLUDE_SCHEMA": False,
}
