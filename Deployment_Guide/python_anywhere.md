## Deploying on pythonanywhere by ANACONDA

**Please note to replace username with your username in below path/code.**

1. Create a free account on python_anywhere.com
2. Go to Files tab and copy folder contents under */home/< username >/flask_random_data*
3. click on app.py file and update the path to yaml file under load_schema function (line 10) with your path *'/home/< username >/flask_random_data/schema.yaml'*
4. Make sure your working directory is */home/< username >*
5. Now go to your WSGI configuration file (/var/www/username_pythonanywhere_com_wsgi.py) and update the code as below
```python

import sys
sys.path.insert(0, '/home/< username >/flask_random_data')
from app import app as application

```

6. Click on deploy to get a endpoint
7. For debugging please check the Log files section under web tab