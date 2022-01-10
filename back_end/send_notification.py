import smtplib
from tkinter import messagebox

def notifications(product_name, product_link, targeted_price, receiver_mail):
    sender = 'sender@gmail.com'
    password = 'ewqjeqwijeqwjdpioasdas'
    receiver = receiver_mail

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender, password)

        subject = "PRICE FELL DOWN"

        mailContent = f"The price has become less than {targeted_price}, \n\n" \
                      f"Product Name: {product_name}\n\nBuy now at: {product_link}"

        server.sendmail(sender, receiver, mailContent)
        messagebox.showinfo(title="Sending", message="Notification Sent")
        server.quit()

    except smtplib.SMTPException as e:
        print(e)
