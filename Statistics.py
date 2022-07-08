import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bsp
from datetime import datetime
import os
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
	yourMsgs = []
	yourT = []
	friendMsgs = []
	friendT = []
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
		
		#print(dtimeS)
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
		S = dtimeS[0:2]
		dtimeDT = datetime(int(y), int(m), int(d), int(H), int(Min), int(S), 0)
		
		if user == "Вы":
			yourMsgs.append(content)
			yourT.append(dtimeDT)
		else:
			friendMsgs.append(content)
			friendT.append(dtimeDT)
	return(yourMsgs, yourT, friendMsgs, friendT)

yM = []
yT = []
fM = []
fT = []
for ind in range(len(os.listdir("Messages/" + Config.UID + "/"))):
	yourMsgs, yourT, friendMsgs, friendT = splitMsg(50*ind)
	for item in yourMsgs:
		yM.append(item)
	for item in yourT:
		yT.append(item)
	for item in friendMsgs:
		fM.append(item)
	for item in friendT:
		fT.append(item)
	print(100 * ind/len(os.listdir("Messages/" + Config.UID + "/")))


yT = sorted(yT)
l = [0]
d = [yT[0].date()] 
for i in range(len(yT)):
	if yT[i].date() == d[-1]:
		l[-1] = l[-1] + 1
	else:
		d.append(yT[i].date())
		l.append(0)

plt.plot(d, l)
plt.show()
