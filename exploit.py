import requests
import sys

if len(sys.argv) < 2:
    print("Usage: script.py listdomains.txt")
    sys.exit()

file_name = sys.argv[1]
try:
    with open(file_name, "r") as file:
        domains = file.readlines()
    for domain in domains:
        domain = domain.strip()
        if not domain.startswith(("http://","https://")):
            domain = "http://" + domain
        try:
            r = requests.head(domain, timeout=3)
            if "server" in r.headers:
                server_name = r.headers["server"]
                print("Server Name for ", domain, " : ", server_name)
            else:
                print("Server Name not found in headers for ", domain)
        except (requests.exceptions.RequestException, requests.exceptions.ReadTimeout) as e:
            print("Not working for ", domain)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error: ",e)

