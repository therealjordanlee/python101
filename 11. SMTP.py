#!/usr/bin/python
# Demonstrating how to send e-mail using the smtplib library
# We use gmail as the SMTP server in this example
#
# References:
# 1. https://www.mkyong.com/python/how-do-send-email-in-python-via-smtplib/
# 2. http://naelshiab.com/tutorial-send-email-python/
# 3. http://www.aventistech.com/2016/03/07/python-send-email-via-office-365-tls/

import smtplib
import getpass

varFrom = raw_input("Your Email Address: ")
varPass = getpass.getpass("Password: ")
varDest = raw_input("Destination Address: ")
varSubject = raw_input("Subject:  ")
varSMTP = "smtp.gmail.com"

# Header (To, From, Subject)
varHeader = "To:" + varDest + "\n" + "From: " + varFrom + "\n" + "Subject: " + varSubject + "\n"

# Body (Body of the email)
varBody = """Hello
This email is sent
from Python!!!"""

# Point to smtp.gmail.com:587
varServer = smtplib.SMTP(varSMTP,587)

# Transport security is important
varServer.starttls()

# Login to the smtp server
varServer.login(varFrom,varPass)

# Send the mail!
varServer.sendmail(varFrom,varDest,varHeader + varBody)

# Finish the connection
varServer.quit()
