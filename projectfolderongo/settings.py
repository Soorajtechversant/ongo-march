import os
import projectfolderongo
import environ
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kmcz)4tg&^^1+_$3vkyn=_67otw&%=5^4u_dx0)9e@5(fk0%7+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']

env = environ.Env()
environ.Env.read_env()

AUTH_USER_MODEL="ongoappfolder.UserLoginDetails"
# Application definition

INSTALLED_APPS = [
 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites' ,
    'django.contrib.staticfiles',
  
    
    'ongoappfolder',
    'cart',
    'chat',
    'payments',
    'subscription',
    'channels',
    'django_celery_beat',
    'django_celery_results',
    
    
    'whoosh',
    'haystack',
    'social_django',
    
    
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
 
]


SITE_ID = 2


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'social_django.middleware.SocialAuthExceptionMiddleware',
    
]



ROOT_URLCONF = 'projectfolderongo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                'social_django.context_processors.backends', # added
                'social_django.context_processors.login_redirect', # added
                'django.template.context_processors.request',#allauth
            ],
        },
    },
]



AUTHENTICATION_BACKENDS = (
   
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
   
    # 'social_core.backends.google.GoogleOAuth2',
)


SOCIAL_AUTH_FACEBOOK_KEY = '527436869573060' # App ID
SOCIAL_AUTH_FACEBOOK_SECRET ='e1921cffea0013b34281f85223f67982'  # App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

WSGI_APPLICATION = 'projectfolderongo.wsgi.application'
ASGI_APPLICATION = 'projectfolderongo.asgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER':env('DB_USER'),
        'PASSWORD':env('DB_PASSWORD'),
        'HOST':env('DB_HOST'),
        'PORT':env('DB_PORT'),


    }
}

SOCIAL_AUTH_JSONFIELD_ENABLED = True

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

WHOOSH_INDEX = os.path.join( 'projectfolderongo/whoosh') 

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': WHOOSH_INDEX,
    },
}


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#CELERY SETTINGS
CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULTS_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
CELERY_RESULT_BACKEND = 'django-db'
#CELERY  BEAT SETTINGS
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'



STATIC_URL = '/static/'
STATIC_DIR=os.path.join(BASE_DIR,"static")
STATICFILES_DIRS= [os.path.join(BASE_DIR, "static")]
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='media/'


CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]



if DEBUG:
    STRIPE_PUBLISHABLE_KEY = 'pk_test_51KqHH8SIeyPpwH6U9sammw0PglKR5v5RNymdmNU5RgdjmUAtteTaToqCX5xcTlmQsxnx3GJnp1lBGPnEE5WPL95W00sHDJ3szs'
    STRIPE_SECRET_KEY = 'sk_test_51KqHH8SIeyPpwH6UXIU6JXkww9X4NkNqJsgypvtpbgWFPud2v4S3os3WcjgE3lARykc8vVSfkr9mj4TW458VYYV30094N3JEMN'



CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
      
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER ='codewithsoorajpkd@gmail.com'
EMAIL_HOST_PASSWORD ='sjsiytngoaibhlls'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email, picture.type(large), link'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
]




SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.11'
LOGIN_REDIRECT_URL = 'auth/login/'
LOGOUT_REDIRECT_URL = 'auth/logout/'
SOCIALACCOUNT_QUERY_EMAIL=True
SOCIALACCOUNT_PROVIDERS = {
    'google': {
     
        'APP': {
            'client_id': '500068293346-2gp00332dfq1nfpch3e7a377bntg5vk5.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}
SOCIALACCOUNT_LOGIN_ON_GET = True #django allauth google login prevent extra page

LOGIN_REDIRECT_URL = '/'


SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.user.update_user_details',
    'auth_pipelines.pipelines.get_user_avatar',
)

