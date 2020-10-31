import requests
from rich.console import Console
from html5print import HTMLBeautifier

link = input("Which website do you want to get the HTML codes of ? (example: google.com) : ")
url = "http://" + link

console = Console()

console.print("\n=> Getting HTML codes of " + link + " for you :smiley: ... :\n", style="bold green")

req = requests.get(url)
code = req.content
print(HTMLBeautifier.beautify(code))
