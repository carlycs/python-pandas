# This program says hello and tries to beat the T test- first try.
#Written by Hoofar Pourzand
#Project Started: Fri, Nov 25, 2016  4:22:48 PM
## Type "copyright", "credits" or "license()" for more information.
# ================================ RESTART ================================

print ('Hello World! \n')
print('who is there?')
while True:
	try:
		myName = input()
		break
	except Exception as NameError:
		print("Please put the name in quotations and try again.")
	

print("It's good to meet you, "+ myName)
print('Hi '+ myName + ', Did you know your name is %d letters long?' % len(myName))


import smptlib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()

smtpObj.starttls()
MY_SECRET_PASSWORD=input("Please type in your password")

smtpObj.login('developer.pourzand@gmail.com', MY_SECRET_PASSWORD)

smtpObj.sendmail('developer.pourzand@gmail.com', 'hpourzand@gmail.com', 
 	'Subject: Glad we are talking! \nDear'+ myName+' , \nDear'+ myName+' glad we got connected. I will send you the list of the companies to apply on a daily basis! \n Sincerely, \n your ai agent')

smtpObj.quit()