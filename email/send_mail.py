#!/usr/bin/env python3
# Script to send emails using Python using the command-line.
# Copyright 2020 Álvaro Justen [alvarojusten at gmail dot com]
# License: GPL <http://www.gnu.org/copyleft/gpl.html>
import argparse
import os
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(
    smtp_host, smtp_port, smtp_user, smtp_pass, from_address, to_addresses,
    subject, text, html=False
):
    # TODO: use `emails_utils` code
    message = MIMEMultipart()
    message["From"] = from_address
    message["To"] = ",".join(to_addresses)
    message["Subject"] = subject
    if html:
        message.attach(MIMEText(text, "html", "utf-8"))
    else:
        message.attach(MIMEText(text, "plain", "utf-8"))
    server = smtplib.SMTP(host=smtp_host, port=smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.sendmail(from_address, to_addresses, message.as_string())
    server.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--html", action="store_true")
    parser.add_argument("--smtp-host", default=os.environ.get("SMTP_HOST"))
    parser.add_argument("--smtp-port", default=os.environ.get("SMTP_PORT", 587))
    parser.add_argument("--smtp-user", default=os.environ.get("SMTP_USER"))
    parser.add_argument("--smtp-pass", default=os.environ.get("SMTP_PASS"))
    parser.add_argument("from_address")
    parser.add_argument("to_addresses", help="If more than one, separate by comma")
    parser.add_argument("subject")
    parser.add_argument("message")
    args = parser.parse_args()

    if None in (args.smtp_host, args.smtp_port, args.smtp_user, args.smtp_pass):
        print("ERROR: missing SMTP configuration", file=sys.stderr)
        exit(1)

    to_addresses = [
        address.strip()
        for address in args.to_addresses.split(",")
        if address.strip()
    ]
    print("args", args)
    send_mail(
        smtp_host=args.smtp_host,
        smtp_port=args.smtp_port,
        smtp_user=args.smtp_user,
        smtp_pass=args.smtp_pass,
        from_address=args.from_address,
        to_addresses=to_addresses,
        subject=args.subject,
        text=open(args.message, 'r').read(),
        html=args.html,
    )
