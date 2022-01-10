from tkinter import *
from tkinter import messagebox

from back_end.fetch_price import fetch_name_price
from back_end.send_notification import *

def track_product_display(menu, background):

    def check_price_button():
        link = url_entry.get()
        if link == "":
            messagebox.showerror(title="Error", message="Enter URL")
        else:
            info = fetch_name_price(link)
            messagebox.showinfo(title="Price", message=f"The Price of this product is: {info['Price']} TL")

    def notification_button():
        link = url_entry.get()
        receiver_mail = receiver_mail_entry.get()
        targeted_price = -1
        try:
            targeted_price = float(target_price_entry.get())
        except Exception:
            messagebox.showerror(title="Error", message="Enter a number")

        if receiver_mail != "" and url_entry != "":
            info = fetch_name_price(link)
            if info['Price'] < targeted_price:
                notifications(info['Name'], link, targeted_price, receiver_mail)

# Background for page
    frame_track_product = Frame(menu, width=850, height=550)
    bg_label = Label(frame_track_product, image=background)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Check Price Part
    guide_label = Label(frame_track_product, text="ENTER THE URL OF A PRODUCT YOU WANT TO CHECK", bg='#fff')
    guide_label.place(x=380, y=195)

    url_entry = Entry(frame_track_product, width=56)
    url_entry.place(x=310, y=230)

    check_price_button = Button(frame_track_product, text='Check Price', command=check_price_button, pady=2, width=20)
    check_price_button.place(x=450, y=270)

# Notification Part
    guide2_label = Label(frame_track_product, text="SEND ME NOTIFICATIONS TO: ", bg='#fff').place(x=325, y=351)
    receiver_mail_entry = Entry(frame_track_product, width=30)
    receiver_mail_entry.place(x=525, y=350)

    guide3_label = Label(frame_track_product, text="IF PRICE IS LESS THAN:", bg='#fff').place(x=365, y=390)
    target_price_entry = Entry(frame_track_product, width=10)
    target_price_entry.place(x=525, y=390)

    send_notification_button = Button(frame_track_product, text='Send Notification',
                                      command=notification_button, width=15, pady=2)
    send_notification_button.place(x=635, y=389)

    return frame_track_product
