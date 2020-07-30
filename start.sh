# For development use (simple logging, etc):
# python3 server.py
# For production use: 
gunicorn server:app -w 4 --log-file logs