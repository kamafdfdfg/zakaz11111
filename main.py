import requests
from bs4 import BeautifulSoup

def parse_phone_numbers(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем все теги <div> с классом 'show_phone' и атрибутом 'data-content'
    phone_elements = soup.find_all('div', class_='show_phone', attrs={'data-content': True})

    # Извлекаем номера телефонов
    phone_numbers = [phone['data-content'] for phone in phone_elements]

    return phone_numbers

def save_to_file(phone_numbers, file_name='phone_numbers.txt'):
    with open(file_name, 'w') as file:
        for phone in phone_numbers:
            file.write(f"{phone}\n")

if __name__ == "__main__":
    # URL вашего веб-сайта
    url = "https://cargo-cards.com/ru/directory/russia/"

    # Парсим номера телефонов
    phone_numbers = parse_phone_numbers(url)

    # Сохраняем номера в текстовый файл
    save_to_file(phone_numbers, file_name='phone_numbers.txt')

    print("Номера телефонов сохранены в файл 'phone_numbers.txt'")
