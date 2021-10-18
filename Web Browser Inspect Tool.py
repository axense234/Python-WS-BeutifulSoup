from bs4 import BeautifulSoup

with open("info.html", 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, "html.parser")
    course_cards = soup.find_all('ul', class_='ex1')
    for course in course_cards:
        course_name = course.h1.text.split()[-1]
        print(f'{course_name} is random')