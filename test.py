# importing the requests library 
import requests 
import json  

# your source code here 
source_code = ''' 
print("Hello, world!") 
a = 1 
b = 2 
print(a + b) 
'''
  
# data to be sent to api 
data = {'name':"test", 
        'value':0}
  
# sending post request and saving response as response object 
r = requests.post(url = 'http://127.0.0.1:5000/postjson', json = data) 
  
# extracting response text  
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url) 