from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://ro.indeed.com/jobs?q=Part+Time").text
