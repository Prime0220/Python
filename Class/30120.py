import smtplib
from email.mime.text import MIMEText

rmail = "sangilmhs@gmail.com"
smail = "zmwhwa@naver.com"

password = "zzmmww1020j"

s= smtplib.SMTP('smtp.naver.com', 587)

r = s.starttls()

s.login(smail, password)

msg = MIMEText('안녕하세요')
msg['Subject'] = '제목 : 파이썬으로 메일 보내기'
msg['From'] = smail
msg['To'] = rmail

response = s.sendmail(smail, rmail, msg.as_string())
if not response : 
    print("response : ", response)
    print("메일 보내기 성공 ! ")
else :
    print("메일 보내기 실패..", response)

s.quit
