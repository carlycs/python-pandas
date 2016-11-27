import webbrowser, sys
import requests
#for Cygwin add 
#export BRWOSER=cygwin
webbrowser.open('http://inventwithpython.com/')

if len(sys.argv) > 1 :
	#get address from command line
	address=' '.join(sys.argv[1:])
	


res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
