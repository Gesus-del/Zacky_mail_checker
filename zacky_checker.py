#developed by Zaccaria Giovanni aka Gesus-del
"""
										Disclaimer

 Legal disclaimer: Usage of zacky_checker.py for attacking targets without prior mutual consent is illegal. 
 It is the end user's responsibility to obey all applicable local,state and federal laws.
  Developers assume no liability and are not responsible for any misuse or damage caused.

"""
creator="""
************************ Developed By Zaccaria Giovanni ****************************     

            

 ██████  ███████ ███████ ██    ██ ███████       ██████  ███████ ██      
██       ██      ██      ██    ██ ██            ██   ██ ██      ██      
██   ███ █████   ███████ ██    ██ ███████ █████ ██   ██ █████   ██      
██    ██ ██           ██ ██    ██      ██       ██   ██ ██      ██      
 ██████  ███████ ███████  ██████  ███████       ██████  ███████ ███████ 
                                                                        
                                                                        


Remember to install al the requirements.
                                                                                      
Libraries Installation Command Line 

pip3 install -r requirements.txt 

"""

print(creator)

from datetime import datetime
from json2html import *
from bs4 import BeautifulSoup as BS
from urllib.request import Request, urlopen

import urllib.request
import json

now = datetime.now()
current_time = str(now.strftime("%Y-%m-%d-%H-%M-%S"))

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', 
    'Accept-Language': 'en-US,en;q=0.8'
    }


email=input("Enter Your Email Address To Check  :  ")
req = urllib.request.Request(
  'https://haveibeenpwned.com/unifiedsearch/' + email, 
    headers=hdr
    )


try:
	with urllib.request.urlopen(req) as resp:
		print("\n") 
		print("\n")
		print("Found Data Breach For Your Entered Email Address")
		print("\n")  
		print("Checking For Available Data Please Wait.....")
		print("\n") 
		print("\n")
		data = json.loads(resp.read().decode("utf-8"))
		outputtable=(json2html.convert(json=data))
		print("\n")
		print("\n")
		print("All Found Breached Details Are Save As (.html) File In .../.../Zacky_mail_checker")
		print("\n")
		saveFile = open(current_time + email + '.html', 'w')
		saveFile.write(str(outputtable))
		saveFile.close()



except Exception as e:
	pass
	print("\n")
	print("Amazing, you are clean ")
	print("\n")
	print("But Make Sure To Change Password Once For Your Safty")
	print("\n")
	print("Remember to Use Strong Password With Small And Capital Alphabet Char, symbols and numbers.")
	print("\n")
	
print("\n")	
print("Search Finished..")
print("\n")

password_choice=input("Check If Password Is Online(y/n): ")
print("\n")
if password_choice == str("y") or password_choice == str("Y"):
	url = "https://pwndb2am4tzkvold.onion.ws/"
	
	luser = email.split("@")[0]
	domain = email.split("@")[1]
	
	data = urllib.parse.urlencode({'luser': luser, 'domain': domain, 'luseropr': 0, 'domainopr': 0, 'submitform': 'em'})
	data = data.encode('ascii')
	req = Request('https://pwndb2am4tzkvold.onion.ws', headers={'User-Agent': 'Mozilla/5.0'},data=data)
	webpage = urlopen(req).read()
	

	soup = BS(webpage, 'html.parser')
	print("Nice job bro, zacky will always help you")
	for item in soup.find_all('pre'):
		arrayopt=(soup.find('pre').text.strip())
		saveFile = open(current_time + email + ' password.txt', 'w')
		saveFile.write(str(arrayopt))
		saveFile.close()
		with open(current_time + email + ' password.txt',"r") as f:
			lines = f.readlines()
			for i in range(0,8):
				del lines[0]

			with open(current_time + email + ' password.txt',"w") as f:
				for line in lines:
					if line.strip("\n") != "8":
						f.write(line)

		print("\n")
		print("\n")
		print("All Found Passwords Are Stored As (.txt) File In /.../.../Zacky_mail_checker")
		print("\n")
		print("\n")
		print("\n")

print("\n")
print("Thanks For Using This Tool.")
print("\n")
print("Watch my github for new interesting tools https://github.com/Gesus-del")
