# Just use beautiful soup
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import re
from datetime import datetime
import pandas as pd
import psycopg2
import time



page = requests.get('https://www.sephora.com/shop/perfume?currentPage=1')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Can be illustrative to look at data directly
soup

spans = soup.find_all('span')
