import os 
print(os.environ.setdefault("DJANGO_SETTINGS_MODULE",f"{os.curdir}.first_django.settings"))

