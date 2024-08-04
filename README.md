Send email to user (client-side exploit)
Remove username and password flags if you don't have any.

Run the script with the following command:

python3 send_email.py \
    --smtp_server IP \
    --smtp_port PORT \
    --username sender@email.com.com \
    --password password \
    --to_email receiver@email.com \
    --subject "Ticket" \
    --body "Here is your ticket: http:/url:8000/malicious.doc" \
    --file /path/file.txt
