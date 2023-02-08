"""Created: 2023-02-08
Purpose: Extract the input data from the https://adventofcode.com website,
and store it in an easy machine readable file structure for the individual
solutions to read from. Used for testing code.

The online data have the following link structure:
https://adventofcode.com/20YY/day/DD/input

YY >= 15, in [15,<This Year>]
DD in [1,25]
"""

import requests

session_uid = input("Cookie UID:")
data_url = "https://adventofcode.com/2022/day/1/input"

session = requests.session()
session.cookies.set("session", session_uid, domain=".adventofcode.com")

request = session.get(data_url)

with open("input.txt",'wb') as file:
    file.write(request.content)