import os, sys

# override stdout
sys.stdout = sys.stderr

# import site directives for virtualenv
import site

ALLDIRS = ['/var/www/venv_bottle/lib/python2.6/site-packages']

# Remember original sys.path.
prev_sys_path = list(sys.path) 

# Add each new site-packages directory.
for directory in ALLDIRS:
    site.addsitedir(directory)

# Reorder sys.path so new directories at the front.
new_sys_path = [] 
for item in list(sys.path): 
    if item not in prev_sys_path: 
        new_sys_path.append(item) 
        sys.path.remove(item) 
sys.path[:0] = new_sys_path 

# append project root directory path
path = '/var/www/bottle_096'
if path not in sys.path:
    sys.path.append(path)

os.environ['PYTHON_EGG_CACHE'] = '/var/www/.python-eggs'

os.chdir(os.path.dirname(__file__))

import bottle
import bottle_app
application = bottle.default_app()

