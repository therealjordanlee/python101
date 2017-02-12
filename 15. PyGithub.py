#!/usr/bin/python
#Demonstration of how to use the PyGithub library
#Reference: http://pygithub.readthedocs.io/en/latest/index.html
#
#Make sure you install the PyGithub library:
#pip install PyGithub

import getpass
from github import Github

varUser = raw_input("GitHub account: ")
varPassword = getpass.getpass("Password of oauth token: ")

# Login to GitHub
g = Github(varUser, varPassword)

# Current User
user = g.get_user()

# Get all user repos
repos = user.get_repos()

# Print out all the repos
for repo in repos:
	print repo.full_name
