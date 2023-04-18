import requests
from colorama import Fore, Style
from datetime import datetime

def fetch_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        return None

def save_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)

def main():
    target_url = input("Enter the target URL: ")
    if not target_url.startswith("http"):
        target_url = "http://" + target_url

    files_to_check = ["robots.txt", "sitemap.xml", "humans.txt", "security.txt"]
    output_filename = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    for file in files_to_check:
        file_url = f"{target_url}/{file}"
        file_contents = fetch_url(file_url)

        if file_contents:
            print(f"{Fore.GREEN}{file_url} contents:{Style.RESET_ALL}")
            print(file_contents)
            save_to_file(output_filename, f"{file_url} contents:\n{file_contents}\n")
        else:
            print(f"{Fore.RED}{file_url} not found{Style.RESET_ALL}")
            save_to_file(output_filename, f"{file_url} not found\n")

if __name__ == "__main__":
    main()
