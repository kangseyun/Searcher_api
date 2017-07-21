#!/usr/bin/env python
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QAxContainer import *

from api.views.kiwoon import MyWindow

if __name__ == "__main__":
    
    print("runinmain")
    print(sys.argv)
    #myWindow = MyWindow.__call__()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "searcher_api.settings")
    try:
        print("run in first try")
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            print("run in second try")
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
        
    execute_from_command_line(sys.argv)
    

