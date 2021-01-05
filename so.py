import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page() :
  return 0


def get_jobs():
  last_page = get_last_page()
  return []