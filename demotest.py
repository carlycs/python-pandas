# This program says hello and tries to beat the T test- first try.
#Written by Hoofar Pourzand
#Project Started: Fri, Nov 25, 2016  4:22:48 PM
## Type "copyright", "credits" or "license()" for more information.
# ================================ RESTART ================================
def main():
	print ('Hello World! \n')
	print('who is there \n?')
	while True:
		try:
			myName = input()
			break
		except Exception as NameError:
			print("Please put the name in quotations and try again. \n")
		

	print("It's good to meet you, "+ myName)
	print('Hi '+ myName + ', Did you know your name is %d letters long?' % len(myName))
	sendEmailSignUp(myName)
	#sendsms()





def sendEmailSignUp(myName):
	import smtplib
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	MY_SECRET_PASSWORD=input("Please type in your password")

	ai_agent_email ='developer.pourzand@gmail.com'
	client_email ='hpourzand@gmail.com'
	smtpObj.login(ai_agent_email, MY_SECRET_PASSWORD)
	#SUBJECT ='Glad we are talking ' #+ myName+'!'
	#BODY= '\n Dear'+ myName + ' glad we got connected. I will send you the list of the companies'+'to apply on a daily basis! \n Sincerely, \n Your ai agent')

	smtpObj.sendmail(ai_agent_email, client_email, 'Subject: Glad we are talking : +1 : \nDear '+ myName + ', \n Glad we got connected. I will send you the list of the companies to apply on a daily basis! \n Sincerely, \n Your ai Agent')
	smtpObj.quit()
	print('email sent')
	return('email sent')

def sendsms():
	from flask import Flask
	import twilio
	from twilio.rest import TwilioRestClient
	# Find these values at https://twilio.com/user/account
	account_sid = "ACedc1c894fd26744915d97b849XXXXXX"
	auth_token = "ec7b84e65ef0931ad7f6380dbeXXXXX"
	client = TwilioRestClient(account_sid, auth_token)

	client.messages.create(
	to="+18144043047", 
	from_="+17175430035", 
	body="Hi, this is a reminder", 
	media_url="", 
) 

if __name__ == '__main__':
	main()