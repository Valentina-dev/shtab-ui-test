from decouple import config
import os

BASE_PATH = os.getcwd()
DOMAIN = config("DOMAIN", cast=str)
CHROMEDRIVER_PATH = config("CHROMEDRIVER_PATH", cast=str)
HEADLESS = config("HEADLESS", cast=bool)
LOGIN = config("LOGIN")
PASSWORD = config("PASSWORD")
