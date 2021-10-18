from bs4 import BeautifulSoup, NavigableString, Tag
import requests

html_request = requests.get("https://www.mynextjob.ro/locuri-de-munca").text
soup = BeautifulSoup(html_request, 'lxml')
jobs = soup.find_all('div', class_='job-description')
for job in jobs:
    if isinstance(job, NavigableString):
        continue
    if isinstance(job, Tag):
        job_link = job.find('h2', class_='')
        print("Job Name:"+ job.h2.text)
        print("More Information:"+ job.a['href'])
        print('------------------------------')