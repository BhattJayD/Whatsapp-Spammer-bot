from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import speech_recognition as sr
import os


driver=webdriver.Chrome()
driver.get('https://web.whatsapp.com/')


name=input("name:- ")
count=int(input("how mannt time u want to send message:-"))
strr=input("your message:- ")
input("any key to continue")

time.sleep(15)
#split=driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div/span')
#cutie=driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div/span')
#cutie.click()
u=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
u.click()
#split.click()

time.sleep(5)
#msg=driver.find_element_by_class_name('_2S1VP copyable-text selectable-text')
msgbx=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

time.sleep(3)
for i in range(count):
	msgbx.send_keys(strr,i)
	time.sleep(1)
	sennd=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]')
	sennd.click()
	emo=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[1]/div/button[2]/span')
	emo.click()
	#sticker=driver.find_element_by_xpath('//span[@data-icon="sticker"]')
	#sticker.click()
	#time.sleep(6)
	#ast=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/img')
	#ast.click()
	#time.sleep(3)
	#gifsendb=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
	#gifsendb.click()


	'''//*[@id="pane-side"]/div[1]/div/div/div[13]/div/div/div[2]/div[1]/div[1]/span/span
	/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[13]/div/div/div[2]/div[1]/div[1]/span/span'''