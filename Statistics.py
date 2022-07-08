from bs4 import BeautifulSoup as bsp
from datetime import datetime
import Config

def getMsg(n):
	msgs = []
	with open("Messages/" + Config.UID + "/messages" + str(n) + ".html", encoding = "windows-1251") as f:
		soup = bsp(f, 'html.parser')
		items = soup.find_all('div', class_="message")
		for item in items:
			msgs.append(item.get_text())	
		return msgs

def splitMsg(n):
	messages = getMsg(n)
	for msg in messages:
		msg = msg.replace("\n", "", 1)
		comma = msg.index(",")
		user = msg[0:comma]
		line = msg.index("\n")
		timeS = msg[comma+2:line]
		#timeDT = datetime.strptime(timeS, "%Y-%m-%d")
		content = msg[line+1:-1]
		print(user)
		print(timeS)
		print(content)
	
splitMsg(50)
