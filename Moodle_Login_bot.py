from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
def readno(s):
	z=''
	oper=['first','second','add','subtract']
	num=['0','1','2','3','4','5','6','7','8','9']
	dop=[]
	c=[]
	for i in range(len(s)):
		if s[i] in num and s[i+1] not in num:
			z+=s[i]
			c+=[z]
			z=''
		elif s[i] in num:
			z+=s[i]
	for j in range(len(oper)):
		if oper[j] in s:
			dop+=[oper[j]]
	return (c,dop)
def do_Operation(l):
	num=l[0]
	oper=l[1][0]
	a=int(num[0])+int(num[1])
	b=int(num[0])-int(num[1])
	g=''
	if oper=='first':
		g=num[0]
	elif oper=='second':
		g=num[1]
	elif oper=='add':
		g=str(a)
	elif oper=='subtract':
		g=str(b)
	return g
readno('subtract 1234 ')
user_id=input('Enter your ID for moodle:')
user_pass=input('Enter your Password for the respective ID:')
driver = webdriver.Firefox()
driver.get("https://moodle.iitd.ac.in/login/index.php")
assert 'IIT Delhi Moodle' in  driver.title
elem1=driver.find_element(By.NAME, 'username')
elem1.clear()
elem1.send_keys(user_id)
elem2=driver.find_element(By.NAME, 'password')
elem2.clear()
elem2.send_keys(user_pass)
elem3=driver.find_element(By.ID, 'login')
c=elem3.text
m=readno(c)
n=do_Operation(m)
elem4=driver.find_element(By.NAME, 'valuepkg3')
elem4.clear()
elem4.send_keys(n)
elem4.send_keys(Keys.RETURN)
