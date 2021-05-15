web: daphne yonayona.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python3 manage.py runworker channels --settings=yonayona.settings -v2