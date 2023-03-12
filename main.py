import bs4
import requests

while True:
    usrInpt = input("Enter a command: ")

    if usrInpt.lower() == 'hi':
        print("Hey there!")
    elif usrInpt.lower() == 'hello':
        print("What's up")
    elif usrInpt.lower() == 'who is this':
        print("I am a Python Bot")
    else:
        googlesearch = usrInpt.lower()
        url = f"https://google.com/search?q={googlesearch}"
        request_results = requests.get(url)
        soup = bs4.BeautifulSoup(request_results.text, "html.parser")
        result = soup.find("div", class_ = "BNeawe").text
        print(result)