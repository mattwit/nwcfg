import smtplib, ssl
from email.message import EmailMessage
from datetime import datetime
import getpass

def py_delivery(out):
    date = datetime.now()
    date = (date.strftime('%c'))
    uname = getpass.getuser()
    sender = uname + '@eleadcrm.com'
    recipient = 'internal.netops@eLeadCRM.com'
    server = smtplib.SMTP('smtp.eleadcrm.com',25)
    subject = input('Email Subject:')
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content("""\
        <html>
            <head>
                <style>
                BODY{font-size:12px;
                #output TABLE{border-width: 1px;border-style: solid;border-color: black;border-collapse: collapse;
                #output TH{border-width: 1px;padding: 0px;border-style: solid;border-color: black;
                #output TD{border-width: 1px;padding: 0px;border-style: solid;border-color: black;
                .cm {border-width: 0px;border-style: none;border-color: white;border-collapse: collapse;
                </style>
            </head>
            <body>
                <div id="cm">
                <table border=0 class='cm'>
                <tr><td class='cm'><b>WHEN:</b></td><td>"""+str(date)+"""</td></tr>
                <tr><td class='cm'><b>WHAT:</b></td><td>"""+str(subject)+"""</td></tr>
                <tr><td class='cm'><b>MORE:</b></td><td></td></tr>
                <tr><td class='cm' colspan=2><pre>"""+str(out)+"""</pre>&nbsp;</td></tr>
                </table><font size="-5">py-delivery</font>
            </body>
        </html>""",subtype = 'html')
    server.send_message(msg)
    server.quit()