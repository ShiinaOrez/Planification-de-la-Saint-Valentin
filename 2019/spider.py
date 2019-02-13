import requests
import base64
from bs4 import BeautifulSoup

pastebin = requests.get("https://paste.ubuntu.com/p/Wjf7DshpWp/")
soup = BeautifulSoup(pastebin.text)

for pre in soup.find_all("pre"):
    if pre.contents[0] != "1":
        code = pre.contents[0][:pre.contents[0].find("\n")].encode("ascii")

wife = base64.b64decode(code).decode("ascii").split("\n")
with open("test.html", "w") as f:
    f.write("""<!DOCTYPE html>
<html>
<body>""")
    for line in wife:
        f.write("<a>"+line+'''\n</a>''')
    f.write("""
</body>
</html>""")
