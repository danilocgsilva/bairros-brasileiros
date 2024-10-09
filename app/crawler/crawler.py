# from flask import request
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.scrapingcourse.com/ecommerce/")
