'''

''' 

import urllib.request

# where should we obtain data from?


url_war_and_peace = "http://www.gutenberg.org/files/2600/2600-0.txt"

# initiate request to URL
response = urllib.request.urlopen(url_war_and_peace)

# read data from URL as a string, making sure
# that the string is formatted as a series of ASCII characters
data = response.read().decode('utf-8')

# output
print (len(data) )
print ("="*10)
print (data[:100])
print ("="*10)
print (data[10000:10100])