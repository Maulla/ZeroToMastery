import smtplib
from email.message import EmailMessage
from string import Template 
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Testing Testerson'
email['to'] = 'mathosaulla@gmail.com'
email['subject'] = 'A Prince is Going to Give You Money!>!'

email.set_content(html.substitute(name='Max'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('testingtesterson1234567@gmail.com', 'Numbers123')
	smtp.send_message(email)
	print('AG')

