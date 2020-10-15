import requests

url = input("Enter the target url: ")
with open("strings.txt", 'r') as search:
    for line in search:
        # Strip empty lines
        if(line == '\n'):
            continue

        req = requests.get("{}{}".format(url, line))
