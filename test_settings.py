# Minimal settings file to allow the running of testsand other useful
# management commands.

SECRET_KEY = 'abcde12345'

# Needs to point to something to allow tests to perform url resolving. The
# referenced file doesn't actually need to contain any urls (but does need to
# define "urlpatterns").
# ROOT_URLCONF = ''

MIDDLEWARE_CLASSES = ()

INSTALLED_APPS = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True
}]

# Add django-extensions to INSTALLED_APPS if it is present. This provides extra
# dev tools, e.g. shell_plus, but isn't required - e.g. for testing.
try:
    import django_extensions  # noqa: F401 (import unused)
except ImportError:
    pass
else:
    INSTALLED_APPS.append('django_extensions')
