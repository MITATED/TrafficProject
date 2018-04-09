from xelenium import Driver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = Driver(executable_path="/usr/lib/chromium-browser/chromedriver")
				 						# Open chromedriver
driver.get("http://google.com")			# Go to google.com

input1 = driver.css("input#lst-ib") 	# Search inputarea
question = input("Question: ")
input1.send_keys(question, Keys.ENTER) 	# Write to input

answers = driver.csses(".g .r a") 		# Search titles answers
for i in range(len(answers)): 
	answer = answers[i].text
	print("%s) %s" % (i, answer)) 		# Print titles as choice
ask = int(input("Make your choice: "))
driver.click(answers[ask]) 				# Click on your choice


input("Close the browser?")
driver.quit()							# Close driver


