from distutils.log import debug
import uvicorn
from app import app, configuration
import os
_basedir = os.path.abspath(os.path.dirname(__file__))
import argparse
import sys

def script_manager(args=[]):
    code = args[1]
    if code == "run":
        if configuration.DEBUG == True:
            # For local
            uvicorn.run("app:app", host='0.0.0.0', port=8000, reload=True, debug=True)
        else:
            # For production
            uvicorn.run(app, host='0.0.0.0', port=8000, debug=False)

    if code == "order_notification_scheduler":
        from app import mail
        status = mail.order_notification_scheduler()
        print(status)

if __name__ == '__main__':
    script_manager(sys.argv)