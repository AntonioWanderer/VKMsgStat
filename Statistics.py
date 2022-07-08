from bs4 import BeautifulSoup as bsp
import Config

def getMsg(n):
	msgs = []
	with open("Messages/" + Config.UID + "/messages" + str(n) + ".html", encoding = "windows-1251") as f:
		soup = bsp(f, 'html.parser')
		items = soup.find_all('div', class_="message")
		for item in items:
			msgs.append(item.get_text())	
		return msgs

def splitMsg():
	getMsg(n)
	
	
getMsg(50)
