#!/bin/bash
export SMTP_HOST=smtp.gmail.com
export SMTP_USER=linuxtampa@gmail.com
export SMTP_PASS=ddnetmxbttfjmvfw

python3 ./send_mail.py --html \
    tim@timjones.com \
    adam@adamjones.tech,linuxtampa@gmail.com \
    "Affinitiv Test Email" \
    ./test.html
