import requests
import base64
from bs4 import BeautifulSoup

# https://paste.ubuntu.com/p/D6FzJPbQ9T/
pastebin = requests.get("https://paste.ubuntu.com/p/943B4zxSYv/")
soup = BeautifulSoup(pastebin.text)

for pre in soup.find_all("pre"):
    if pre.contents[0] != "1":
        code = pre.contents[0][:pre.contents[0].find("\n")].encode("ascii")
print("Crawler")

wife = base64.b64decode(code).decode("ascii").split("\n")
with open("wife.html", "w") as f:
    f.write("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <body>
	<div id="outerColumnContainer" style="color: #000">
	      <div id="contentColumn">
		      <div class="inside">
	    
<table class="pastetable"><tbody><tr><td class="linenos"><div class="linenodiv"></div></td><td class="code"><div class="paste"><pre>""")
    for line in wife:
        f.write(line+"\n")
    f.write("""
</pre></div>
</td></tr></tbody></table>
</div>
</div>




		    </div>
	    </div>
	</div>



</body></html>
""")