import smtplib as s


ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login(user, password)
subject="test"
body="i love python"
massage="subject:{}\n\n{}".format(subject,body)
listadd=['pratik@gmail.com','ankus@gmail.com']


ob.sendmail(sender_email_address,listadd, massage)
print("send mail")
ob.quit()
