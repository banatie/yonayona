web: daphne yonayona.asgi:communicate --port $PORT --bind 0.0.0.0 -v2
worker: python3 manage.py runworker channels --settings=yonayona.settings -v2