#!/usr/bin/python
import subprocess
import smtplib
from datetime import date, datetime, time

dt = datetime.now()
timestamp = dt.isoformat()

p = subprocess.Popen(['cat', '/sys/bus/w1/devices/28-0000079e4172/w1_slave'], stdout=subprocess.PIPE)
out, err = p.communicate()

strarr = out.split("=")
temp = float(float(strarr[2]) / 1000)

# send email if needed
if temp > 2.0:
    
    print 'sending power off IR command'
    poff = subprocess.Popen(['irsend',  'SEND_ONCE', 'onkyo', 'KEY_OFF'])
    poff.communicate()
    emailaddr = "gamm90@gmail.com"
    gmail_user = emailaddr
    gmail_pwd = "b9jmt5Qskzk"
    FROM = emailaddr
    TO = emailaddr if type(emailaddr) is list else [emailaddr]
    SUBJECT = "OVERHEATING"
    TEXT = "AIR TEMPERATURE IS TOO HIGH. SENDING IR POWER OFF COMMAND"
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

# write date to file
file = open('temperature_log.csv', 'a')

if "YES" in out:
	file.write(timestamp + ',' + str(temp) + '\n')
	print temp
else:
	file.write(timestamp + ',ERROR\n')
	print 'ERROR'

file.close()
