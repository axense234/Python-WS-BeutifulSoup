from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://ro.indeed.com/jobs?q=Part+Time").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find('div', class_="slider_container")
job_name = jobs.find('span', class_="").text.replace(" ", "")
skills = jobs.find('span', class_="date").text
print(job_name)
print(skills)