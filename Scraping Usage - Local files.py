from bs4 import BeautifulSoup

with open("info.html", 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, "html.parser")
