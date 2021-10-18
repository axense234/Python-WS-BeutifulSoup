from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.workopolis.com/jobsearch/find-jobs?ak=&l=Work+From+Home&job=4iwcydSNaAWM7JstPogqbLqbjgZTD-m6_8HhtikkE049Ia9NSfeAOg').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('article', class_='JobCard')
for job in jobs:
    job_name = job.a.text
    job_salary = job.find('span', class_='Salary').text.replace("Estimated: ", '')
    print(f'''
    Job Name:{job_name}
    Job Salary:{job_salary}
    ''')