# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib 

s = smtplib.SMTP('smtp.gmail.com', 587) 

s.starttls() 
 
s.login("sender email id", "sender password") 

message = "Message"

 
s.sendmail("sender email id", "receiver email id", message) 
 
s.quit() 
