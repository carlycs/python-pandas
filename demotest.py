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
	readEmail()





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
	#media_url="", 
) 

def readEmail():
	import imaplib
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login('clientusername@gmail.com', 'clientpassword')
	mail.list()
	# Out: list of "folders" aka labels in gmail.
	mail.select("inbox") # connect to inbox.
	#Getting all mail and fetching the latest
	result, data = mail.search(None, "ALL") 
	ids = data[0] # data is a list.
	id_list = ids.split() # ids is a space separated string
	latest_email_id = id_list[-1] # get the latest
	 
	result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
	 
	raw_email = data[0][1] # here's the body, which is raw text of the whole email
	# including headers and alternate payloads
	#using uid
	result, data = mail.uid('search', None, "ALL") # search and return uids instead
	latest_email_uid = data[0].split()[-1]
	result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
	raw_email = data[0][1]

	import email
	email_message = email.message_from_string(raw_email)
	 
	print email_message['To']
	 
	print email.utils.parseaddr(email_message['From']) # for parsing "Yuji Tomita" <yuji@grovemade.com>
	 
	print email_message.items() # print all headers
	 
	# note that if you want to get text content (body) and the email contains
	# multiple payloads (plaintext/ html), you must parse each message separately.
	# use something like the following: (taken from a stackoverflow post)
	def get_first_text_block(self, email_message_instance):
	    maintype = email_message_instance.get_content_maintype()
	    if maintype == 'multipart':
	        for part in email_message_instance.get_payload():
	            if part.get_content_maintype() == 'text':
	                return part.get_payload()
	    elif maintype == 'text':
	        return email_message_instance.get_payload()

	#IMAP protocol documentation https://tools.ietf.org/html/rfc3501
	#https://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail/        
	mail.close()
	mail.logout()

if __name__ == '__main__':
	main()