This script is useful for identifying the server software used by a web server for a given list of domains. The script takes a text file as input which contains a list of domains, one per line. The script reads the file, loops through the list of domains, and for each domain, it sends a HEAD request to the domain. If the request is successful and the Server field is present in the headers, it prints the server name along with domain name. If the Server field is not present, it will print "Server Name not found in headers" along with domain name. If the request throws an exception, it will print "Not working" for that domain.
This script also checks if the domain starts with "http://" or "https://" or not, if not then it adds "http://" to the domain before sending the request.

This script can be useful for web developers, security researchers, and system administrators who need to identify the server software used by a web server for a given domain. It can help in identifying potential vulnerabilities, compatibility issues, and security risks associated with the server software. Additionally, this script can also be used to identify the servers that are not working or not accessible.

usage: python exploit.py domainlist.txt
