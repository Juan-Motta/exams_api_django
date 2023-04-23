import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _

# represents the absolute filesystem path to the root directory of the Django project,this
# returns the absolute path of the grandparent directory of the current file.
BASE_DIR = Path(__file__).resolve().parent.parent

# provide cryptographic security for the Django project.
SECRET_KEY = os.getenv("SECRET_KEY")

# determines whether the Django project is in debug mode or production mode. debug mode in true
# provides detailed error messages and other debugging information in the event of an error.
DEBUG = True if os.environ.get("DEBUG").lower() == "true" else False

# specifies the valid hostnames or IP addresses that can be used to access the Django project.
ALLOWED_HOSTS = [
    host.strip() for host in os.getenv("ALLOWED_HOSTS").split(",")
]

# determines whether Django should append a trailing slash to URLs that do not have one. For
# example, if APPEND_SLASH in True a request to http://example.com/mypage will be redirected
# to http://example.com/mypage/.
APPEND_SLASH = False

# specifies the name of the Python module that contains the project's WSGI application object.
WSGI_APPLICATION = "core.wsgi.application"

# specifies the default primary key type to use for models.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# APPLICATION DEFINITION ==========================================================================

# specifies the names of the Django applications and third-party packages that are installed and
# should be included in the project.

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
]

LOCAL_APPS = ["apps.users", "apps.base"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE DEFINIION ============================================================================

# specifies the order in which middleware should be applied to incoming HTTP requests and
# outgoing HTTP responses.

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL DEFINITION ==================================================================================

# specifies the name of the Python module that contains the project's URL routing configuration.
ROOT_URLCONF = "core.urls"

# TEMPLATE DEFINITION =============================================================================

# a list of template engine configurations that specifies how Django should render and process
# HTML templates.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# DATABASE DEFINITION =============================================================================

# specifies the database engine configuration used in the project, if not db engine specified in
# enviroments, sqlite engine is used by default for evelopment purposes

if os.getenv("DB_ENGINE") == "POSTGRES":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME"),
            "USER": os.getenv("DB_USER"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": os.getenv("DB_PORT"),
        },
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# PASSWORD DEFINITION =============================================================================

# a list of validators that specify the requirements for passwords used in the project.

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# INTERNATIONALIZATION DEFINITION =================================================================

# a list of language options that specifies the available languages for the project.
LANGUAGES = [
    ("es-co", _("Spanish")),
    ("en-us", _("English")),
]

# a list of directories that specifies the location of translation files for the project.
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

# specifies the default language code for the project.
LANGUAGE_CODE = os.getenv("LANGUAGE")

# specifies the time zone for the project.
TIME_ZONE = os.getenv("TIME_ZONE")

# specifies whether the project should use internationalization (i18n) and localization (l10n)
# features. When USE_I18N is True, Django will enable i18n/l10n features like translation of text
# strings and localization of date and time formats.
USE_I18N = True

# specifies whether the project should use time zones in date and time calculations. To convert a
# naive timezone to an aware timezone object is posible to use make_aware method, for example
# timezone.make_aware(my_datetime, timezone.get_default_timezone())
USE_TZ = True


# STATIC FILES DEFINITION (CSS, JavaScript, Images) ===============================================

# specifies the URL prefix for static files served by the project. When a static file is requested
# by a client, Django will use the STATIC_URL setting to construct the URL that points to the
# requested file.
STATIC_URL = "static/"

# SECURITY DEFINITION =============================================================================

# HTTP-only cookies are cookies that are inaccessible to JavaScript running on the client-side of
# a web application. By marking session cookies as HTTP-only, you can help protect against certain
# types of cross-site scripting (XSS) attacks that target cookies.

# specifies whether session cookies should be marked as HTTP-only.
SESSION_COOKIE_HTTPONLY = True

# specifies whether the CSRF cookie should be marked as HTTP-only.
CSRF_COOKIE_HTTPONLY = True

# specifies whether the browser's cross-site scripting (XSS) filter should be enabled.
# When SECURE_BROWSER_XSS_FILTER is set to True, Django will set a special HTTP response header
# called X-XSS-Protection to instruct the browser to enable its built-in XSS filter. This filter
# can help protect against certain types of XSS attacks.
SECURE_BROWSER_XSS_FILTER = True

# specifies how the application should behave when embedded in an iframe on another website.
# DENY: prevents the application from being embedded in any iframe, regardless of the originating
# domain.
X_FRAME_OPTIONS = "DENY"

# AUTHENTICATION DEFINITION =======================================================================

# specifies the custom user model to use for authentication.
AUTH_USER_MODEL = "users.User"

# REST FRAMEWORK DEFINITION =======================================================================

# configures the behavior of the Django REST framework.

# DEFAULT_AUTHENTICATION_CLASSES: specifies the default authentication classes to use for all API
# views.
# DEFAULT_PAGINATION_CLASS: specifies the default pagination class to use for all API views.
# PAGE_SIZE: specifies the default page size to use for all paginated API views.
# EXCEPTION_HANDLER specifies the default exception handler class to use for all API Views.
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PAGINATION_CLASS": "core.pagination.CustomPagination",
    "EXCEPTION_HANDLER": "core.exception.custom_exception_handler",
    "PAGE_SIZE": 20,
}

# CACHE DEFINITION ================================================================================

# defines the caches that your application will use. The dictionary can contain one or more named
# cache configurations. Each cache configuration is itself a dictionary that defines the
# parameters for that cache.

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_DEFAULT_CACHE"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,
        },
    },
}

# CELERY DEFINITION ===============================================================================

# defines the time zone that Celery should use when scheduling tasks.
CELERY_TIMEZONE = os.getenv("TIME_ZONE")

# specifies the URL of the message broker that Celery should use to send and receive messages.
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")

# specifies the backend that Celery should use to store the results of executed tasks.
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

# specifies the maximum amount of time that a task is allowed to run before it is terminated.
CELERY_TASK_TIME_LIMIT = os.getenv("CELERY_TASK_TIME_LIMIT")

# specifies the maximum amount of time that Celery should keep the results of a task before
# discarding them.
CELERY_RESULT_EXPIRES = os.getenv("CELERY_RESULT_EXPIRES")

# JWT DEFINITION ==================================================================================

# specifies the expiration time of the token.
JWT_EXP = os.getenv("JWT_EXP")
