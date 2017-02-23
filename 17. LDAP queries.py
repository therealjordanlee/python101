#!/usr/bin/python
# This script reads in a list of accounts from a simple text file,
# and queries AD to determine the status of each account (active, disabled, not-found).
# Finally, an e-mail alert is sent out with a list of disabled or 'not found' accounts
#
# This script relies on the following libraries:
# - python-ldap:	pip install python-ldap
# - base64
# - re
# - os
# - smtplib
# - getpass
#
# python-ldap: https://www.python-ldap.org/

import ldap
import base64
import re
import os
import smtplib
import getpass


# Connect to AD
def BindAD(username,password,ad):
	# The Python-LDAP API connects and binds in two stages.
	# Initializing the LDAP system is done with the ldap.initialize() function.
	# The initialize() method returns an LDAPObject object, which contains
	# methods for performing LDAP operations and retrieving information about the LDAP connection and transactions.
	l = ldap.initialize(ad)
	try:
		l.protocol_version = ldap.VERSION3
		l.simple_bind_s(username, password)
		valid = True
	except Exception, error:
		print error
		exit()
	return l

# Search LDAP
def SearchLDAP(searchFilter,l,baseDN):
	result_set = []
	searchScope = ldap.SCOPE_SUBTREE
	retrieveAttributes = ["userAccountControl","cn"]
	try:
		ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
		while 1:
			result_type, result_data = l.result(ldap_result_id, 0)
			if (result_data == []):
				break
			else:
				if result_type == ldap.RES_SEARCH_ENTRY:
					result_set.append(result_data)
	except:
		print "Error in LDAP search"

	if len(result_set) > 0:
		accountState = re.search('(?<=userAccountControl\': \[\')\d*', str(result_set[0]))
		if accountState:
			return int(accountState.group())
	else:
		return "User not found"
	return 0


def ReadFile(fileName):
	Content = None
	with open (fileName) as File:
		Content = File.readlines()
		Content = [i.strip() for i in Content]
	File.close()
	return Content

		
def sendMail(msg,smtpsrv,user,password,sendto):
	smtpserver = smtplib.SMTP(smtpsrv,587)
	smtpserver.starttls()
	smtpserver.login(user, password)
	header = "To:" + sendto + "\n" + "From: " + user + "\n" + "Subject:GitHub Disabled Accounts Alert \n"
	print header
	smtpserver.sendmail(user, sendto, header + msg)
	print "done!"
	smtpserver.close()
	


##### MAIN FUNCTION #####


# Prompt user for AD login credentials
# Note: UPN can be determined using dsquery. See https://technet.microsoft.com/en-us/library/cc725702(v=ws.11).aspx
username = raw_input("Enter User-Principal-Name to connect with (e.g. CN=Mike Danseglio,CN=Users,DC=Contoso,DC=Com): ")
password = getpass.getpass("Enter password: ")
domain = raw_input("Enter domain name (e.g. contoso.int): ")
baseDN = raw_input("Enter BaseDN to search (e.g. OU=Users,DC=contoso,DC=int)")

# Prompt user for SMTP details
smtpsrv = raw_input("SMTP Server (e.g. smtp.gmail.com): ")
smtpuser = raw_input("SMTP Username: ")
smtppass = getpass.getpass("SMTP Password: ")
sendto = raw_input("Destination address: ")

# Prompt user for file to read from
filename = raw_input("File to read from: ")

# rewrite in ldap format
ad = "ldap://" + domain

# Connect to AD
l = BindAD(username,password,ad)

# Read in list of accounts from file
names = ReadFile(filename)
disabledAccounts = []
activeAccounts = []
notfoundAccounts = []


# Format initial email body
msg = "\nAccounts Alert\n"
msg += "==============\n\n"

# Loop through each account and check their status in AD
for i in names:
	#ignore blank lines
	if i == "":
		continue

	searchFilter = "userPrincipalName=" + i + "@" + domain
	#print searchFilter
	searchResult = SearchLDAP(searchFilter,l,baseDN)
	
	# useraccountcontrol values:
	# 514 = disabled
	# 512 = active account
	# 544 = active account, password change required
	#
	# http://rajnishbhatia19.blogspot.com.au/2008/11/active-directory-useraccountcontrol.html
	if searchResult == 514:	
		disabledAccounts.append(i)
	elif searchResult == 512 or searchResult == 544:
		activeAccounts.append(i)
	else:
		notfoundAccounts.append(i)


print "Disabled accounts:"
msg += "Disabled accounts: %i\n" % len(disabledAccounts)
for i in disabledAccounts:
	print i
	msg += i + "\n"

print "Accounts not found:"
msg += "\nAccounts not found: %i\n" % len(notfoundAccounts)
for i in notfoundAccounts:
	print i
	msg += i + "\n"

print "Active Accounts:"
for i in activeAccounts:
	print i
	
sendMail(msg,smtpsrv,smtpuser,smtppass,sendto)
