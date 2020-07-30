#!/usr/bin/env python
# coding: utf-8

# This script asks your name, email, password, SMTP server and destination
# name/email. It'll send an email with this script's code as attachment and
# with a plain-text message. You can also pass `message_type='html'` in
# `Email()` to send HTML emails instead of plain text.
# You need email_utils.py to run it correctly. You can get it on:
#                 https://gist.github.com/1455741
# Copyright 2011-2020 Álvaro Justen [alvarojusten at gmail dot com]
# License: GPL <http://www.gnu.org/copyleft/gpl.html>

import sys
from getpass import getpass
from email_utils import EmailConnection, Email


print 'I need some information...'
name = raw_input(' - Your name: ')
email = raw_input(' - Your e-mail: ')
password = getpass(' - Your password: ')
mail_server = raw_input(' - Your mail server: ')
to_email = raw_input(' - Destination email: ')
to_name = raw_input(' - Name of destination: ')
subject = 'Sending mail easily with Python'
message = 'here is the message body'
attachments = [sys.argv[0]]

print 'Connecting to server...'
server = EmailConnection(mail_server, email, password)
print 'Preparing the email...'
email = Email(from_='"%s" <%s>' % (name, email), #you can pass only email
              to='"%s" <%s>' % (to_name, to_email), #you can pass only email
              subject=subject, message=message, attachments=attachments)
print 'Sending...'
server.send(email)
print 'Disconnecting...'
server.close()
print 'Done!'