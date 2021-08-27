#Perform Get request on website
import requests
url = 'https://brickset.com/sets/year-2005'
r = requests.get(url)
print(r.text)

#Displays OK retun status
print("Status code:")
print("\t*",r.status_code)

#Display website header
h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("**********")

#modify the Header user-agent to display "mobile"
headers = {
    'User-Agent':'Iphone X'
}
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)

