#!/depot/Python/Python-3.11.2/bin/python
import main
import smtplib

output = main.extract_datas()
mail_server = ''
from_addr = ''
to_addr = ''
subject_header = 'Subject: Extracted Data'
body = output
email_message = f"From: {from_addr}\nTo: {to_addr}\n{subject_header}\n\n{body}\n"

s = smtplib.SMTP(mail_server)
s.sendmail(from_addr, to_addr, email_message)
s.quit()
