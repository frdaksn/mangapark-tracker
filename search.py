import requests
from bs4 import BeautifulSoup

def find_title_or_div(url, title_or_div_id, page_number=1):
    while True:
        page_url = f'{url}&page={page_number}'
        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        element = soup.find('a', {'title': title_or_div_id})
        if element is not None:
            return element.text, page_url 
        else:
            page_number += 1

def main():
    url = 'https://mangapark.net/browse?sort=update'
    current_title = input("Enter the title you want to search for: ")
    page_number = int(input("Enter the page number to start searching from: "))  
    while True:
        result = find_title_or_div(url, current_title, page_number)
        if result is not None:
            text, link = result 
            print(f'Found {current_title}: {text} at {link}')  
            user_input = input("Enter 'next' to search for the next occurrence or 'start' to search for a new title: ")
            if user_input.lower() == "start":
                current_title = input("Enter the title you want to search for: ")
                page_number = int(input("Enter the page number to start searching from: "))  
            elif user_input.lower() == "next":
                page_number += 1
            else:
                print("Invalid command.")
        else:
            print(f"No results found for {current_title}.")
            current_title = input("Enter the title you want to search for: ")
            page_number = int(input("Enter the page number to start searching from: ")) 

if __name__ == '__main__':
    main()
