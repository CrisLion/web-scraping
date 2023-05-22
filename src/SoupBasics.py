from bs4 import BeautifulSoup

with open('./src/home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')

    for course_card in course_cards:
        print(f"{course_card.h5.text} costs {course_card.a.text.split()[-1]}")

