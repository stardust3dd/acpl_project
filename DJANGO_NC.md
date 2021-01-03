## VIRTUAL ENVIRONMENT SETUP
1. Log into CPanel, Setup Python App, Create Application
2. Select Python version
  - In the Application root text box, type MYAPP.
  - In the Application URL list box, select the domain. Leave the rest of the URL blank.
  - Leave the Application startup file text box and Application Entry point text box blank. When these text boxes are blank, cPanel automatically creates a passenger_wsgi.py startup file and default application object for you.
  - In the Passenger log file text box, you can optionally specify a log file for the application.
3. Create Application and copy the command.
4. Open Terminal, execute copied command to activate the Python virtual environment.

## DJANGO PROJECT SETUP
1. `cd ~` # go to home directory 
2. `pip install django==2.1.8` 
3. `django-admin --version` # check if proper django version is installed
4. `django-admin startproject myapp ~/myapp` # create project MYAPP inside directory myapp in home folder
5. `mkdir -p ~/myapp/templates/static_pages`
6. `mkdir ~/myapp/static_files`
7. `mkdir ~/myapp/static_media`

8. Open the **~/myapp/myapp/settings.py** file, and make the following changes:
`ALLOWED_HOSTS = ['example.com', 'https://www.example.com', 'www.example.com']`
```
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
      ],
    },
  },
]
```
```
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
```
```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static_media")
```

8. Open the **~/myapp/myapp/urls.py** file, delete everything & paste following code:
```
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='static_pages/index.html'), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

8. Open the **~/myapp/passenger_wsgi.py** file, delete everything & paste following code:
```
import os
import sys

import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application

# Set up paths and environment variables
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'myapp.settings'

# Set script name for the PATH_INFO fix below
SCRIPT_NAME = os.getcwd()

class PassengerPathInfoFix(object):
    """
        Sets PATH_INFO from REQUEST_URI because Passenger doesn't provide it.
    """
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        from urllib.parse import unquote
        environ['SCRIPT_NAME'] = SCRIPT_NAME
        request_uri = unquote(environ['REQUEST_URI'])
        script_name = unquote(environ.get('SCRIPT_NAME', ''))
        offset = request_uri.startswith(script_name) and len(environ['SCRIPT_NAME']) or 0
        environ['PATH_INFO'] = request_uri[offset:].split('?', 1)[0]
        return self.app(environ, start_response)

# Set the application
application = get_wsgi_application()
application = PassengerPathInfoFix(application)
```
9. Create a basic `index.html` file in the ~/myapp/templates/static_pages directory.
10. `python ~/myapp/manage.py migrate` # make migrations
11. `python ~/myapp/manage.py createsuperuser` # create admin
12. `python ~/myapp/manage.py collectstatic` # static files
13. Restart the Python application.

## TROUBLESHOOTING
- If the web site does not appear in your browser, try running the passenger_wsgi.py file manually. To do this, type the following command:
  `python ~/myapp/passenger_wsgi.py`
There should not be any text output to the console when you run this file. If there are any errors, check the syntax in the configuration files.
- [SEE HERE]('https://www.a2hosting.com/kb/developer-corner/python/installing-and-configuring-django-on-linux-shared-hosting#Step-1.3A-Create-a-Python-application-in-cPanel)