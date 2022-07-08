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
		dtimeS = msg[comma+2:line+1]
		content = msg[line+1:-1]
		
		splitter = dtimeS.index("в")
		dateS = dtimeS[0:splitter]
		timeS = dtimeS[splitter+2:-1]
		
		print(dtimeS)
		d = dtimeS[0:dtimeS.index(" ")]
		dtimeS = dtimeS.replace(d+" ", "", 1)
		mRu = ["янв", "фев", "мар", "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
		m = mRu.index(dtimeS[0:3]) + 1
		dtimeS = dtimeS[4:-1]
		y = dtimeS[0:4]
		dtimeS = dtimeS[7:len(dtimeS)]
		H = dtimeS[0:dtimeS.index(":")]
		dtimeS = dtimeS.replace(H+":", "", 1)
		Min = dtimeS[0:dtimeS.index(":")]
		dtimeS = dtimeS.replace(Min+":", "", 1)
		S = dtimeS
		dtimeDT = datetime(int(y), int(m), int(d), int(H), int(Min), int(S), 0)
		
		print(user)
		print(dtimeDT)
		print(content)
		print(msg)
	
splitMsg(50)
