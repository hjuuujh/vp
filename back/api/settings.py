"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') #개발자가 관리하는 파일들

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!5qmq=9e+wdf%xd&+vlhq+#p_x09!-^b@7&t1b^z&s0vvknwi5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

APPEND_SLASH = False
# Application definition

JWT_AUTH = { # 추가
   'JWT_SECRET_KEY': SECRET_KEY,
   'JWT_ALGORITHM': 'HS256',
   'JWT_VERIFY_EXPIRATION' : True, #토큰검증
   'JWT_ALLOW_REFRESH': True, #유효기간이 지나면 새로운 토큰반환의 refresh
   'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=30),  # Access Token의 만료 시간
   'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=3), # Refresh Token의 만료 시간
   'JWT_RESPONSE_PAYLOAD_HANDLER': 'api.custom_responses.my_jwt_response_handler'
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vp',
    'mypage',
    'user',
    'localstatus',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',     # 추가
    'django.middleware.common.CommonMiddleware', # 추가
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        "ENGINE": "django.db.backends.mysql",
        "NAME": "vpdb",
        "USER": "vpuser",
        "PASSWORD": "1234",
        "HOST": "3.15.69.19",
        "PORT": "3306",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# REST_FRAMEWORK = { # 추가
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',  #인증된 회원만 액세스 허용
    #     'rest_framework.permissions.AllowAny',         #모든 회원 액세스 허용
    #
    # ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': ( #api가 실행됬을 때 인증할 클래스를 정의해주는데 우리는 JWT를 쓰기로 했으니
    #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # 이와 같이 추가해준 모습이다.
    #     # 'rest_framework.authentication.BasicAuthentication',
    #     # 'rest_framework.authentication.SessionAuthentication',
    # ),
# }

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.AllowAny',         #모든 회원 액세스 허용
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ],
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
       'http://127.0.0.1:8000',
       'http://127.0.0.1:3000',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.naver.com"
EMAIL_HOST_USER = 'multicam_msa@naver.com'
EMAIL_HOST_PASSWORD ='msacloud10!' # 2단계 보안 인증 비밀번호 = (앱 비밀번호)
EMAIL_PORT = 587 # 권장 naver smtp포트
EMAIL_USE_TLS = True #tls 보안 설정
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER