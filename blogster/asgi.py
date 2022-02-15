# BLOGSTER by Alexander Abraham
# a.k.a. "The Black Unicorn" a.k.a. "Angeldust Duke".
# Licensed under the MIT license.

import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogster.settings')
application = get_asgi_application()
