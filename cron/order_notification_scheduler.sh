## // For every day at 00:00
# 0 0 * * * (COMMAND TO RUN ex: python3 manage.py order_notification_scheduler)

## This script below need to paste on bash (dont forget to add script to activate the virtualenv)
python3 manage.py order_notification_scheduler
python3 manage.py check_order_status