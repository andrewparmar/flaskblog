import os

class Config():
	SECRET_KEY = '858d2251646011ba1936bf8ba6600f12'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	CELERY_BROKER_URL = 'redis://localhost:6379',
	CELERY_RESULT_BACKEND = 'redis://localhost:6379'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')