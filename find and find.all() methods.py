from bs4 import BeautifulSoup

with open("info.html", 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, "html.parser")
    tags = soup.find('h1')
    courses_html_tags = soup.find_all('h1')
    for course in courses_html_tags:
        print(course.text)