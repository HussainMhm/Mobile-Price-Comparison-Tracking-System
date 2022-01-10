from tkinter import *
from tkinter import messagebox
import webbrowser

from back_end.cheapest_price import best_price_sorted_list

def cheapest_price_display(menu, background):

    def erase_all_fields():
        best_price_entry.delete(0, END)
        from_website_entry.delete(0, END)
        product_name_entry.delete(0, END)
        product_link_entry.delete(0, END)
        gittigidiyor_entry.delete(0, END)
        gittigidiyor_name.delete(0, END)
        hepsiburada_entry.delete(0, END)
        hepsiburada_name.delete(0, END)
        trendyol_entry.delete(0, END)
        trendyol_name.delete(0, END)
        n11_entry.delete(0, END)
        n11_name.delete(0, END)

    def fill_best_product(liste: list):
        best_price_entry.insert(0, f"{liste[0]['Price']} ₺")
        from_website_entry.insert(0, liste[0]['Website'])
        product_name_entry.insert(0, liste[0]['Name'])
        product_link_entry.insert(0, liste[0]['Link'])

    def fill_price_name_fields(liste: list):
        sort_alphabetic = sorted(liste, key=lambda x: x['Website'])
        # [Gittigidiyor, Hepsiburada, N11, Trendyol]

        gittigidiyor_entry.insert(0, f"{sort_alphabetic[0]['Price']} ₺")
        gittigidiyor_name.insert(0, sort_alphabetic[0]['Name'])

        hepsiburada_entry.insert(0, f"{sort_alphabetic[1]['Price']} ₺")
        hepsiburada_name.insert(0, sort_alphabetic[1]['Name'])

        trendyol_entry.insert(0, f"{sort_alphabetic[3]['Price']} ₺")
        trendyol_name.insert(0, sort_alphabetic[3]['Name'])

        n11_entry.insert(0, f"{sort_alphabetic[2]['Price']} ₺")
        n11_name.insert(0, sort_alphabetic[2]['Name'])

    def bind_entries(liste: list):
        sort_alphabetic = sorted(liste, key=lambda x: x['Website'])

        gittigidiyor_name.bind("<Button-1>", lambda e: callback(sort_alphabetic[0]['Link']))
        hepsiburada_name.bind("<Button-1>", lambda e: callback(sort_alphabetic[1]['Link']))
        trendyol_name.bind("<Button-1>", lambda e: callback(sort_alphabetic[3]['Link']))
        n11_name.bind("<Button-1>", lambda e: callback(sort_alphabetic[2]['Link']))

    def callback(url):
        webbrowser.open_new_tab(url)

    def button_clicked(event=0):
        searched_model = search_entry.get().replace(' ', '%20')
        if searched_model == "":
            messagebox.showerror("Error", message="Enter A Mobile Model To Search For")
            erase_all_fields()
        else:
            erase_all_fields()
            sorted_list = best_price_sorted_list(searched_model)
            messagebox.showinfo("Info", message=f"Best price is {sorted_list[0]['Price']} TL "
                                                f"from {sorted_list[0]['Website']}!")
            fill_best_product(sorted_list)
            fill_price_name_fields(sorted_list)
            bind_entries(sorted_list)
            product_link_entry.bind("<Button-1>", lambda e: callback(product_link_entry.get()))


    # Background for page
    frame_cheapest_price = Frame(menu, width=850, height=550)
    main_bg_label = Label(frame_cheapest_price, image=background)
    main_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Search bar
    search_label = Label(frame_cheapest_price, text="Mobile Model:", font=("Helvetica bold", 14), bg='#fff')
    search_entry = Entry(frame_cheapest_price, width=32)
    search_button = Button(frame_cheapest_price, text='Compare', command=button_clicked, pady=2)

    search_entry.bind('<Return>', button_clicked)
    search_label.place(x=320, y=151)
    search_entry.place(x=435, y=150)
    search_button.place(x=740, y=149)

# Best Product
    best_price_label = Label(frame_cheapest_price, text="Best Price:", font=("Helvetica bold", 14), bg="#fff")
    best_price_label.place(x=320, y=226)
    best_price_entry = Entry(frame_cheapest_price, width=10, fg="#0a5ef2", font=("Helvetica bold", 14), justify=CENTER)
    best_price_entry.place(x=435, y=224)

    from_website_label = Label(frame_cheapest_price, text="From Where:", font=("Helvetica bold", 14), bg="#fff")
    from_website_label.place(x=320, y=256)
    from_website_entry = Entry(frame_cheapest_price, width=11, fg="#0a5ef2", font=("Helvetica bold", 14),
                               justify=CENTER)
    from_website_entry.place(x=435, y=254)

    product_name_entry = Entry(frame_cheapest_price, width=32)
    product_name_entry.place(x=540, y=254)

    product_link_label = Label(frame_cheapest_price, text="Product Link:", font=("Helvetica bold", 14), bg="#fff")
    product_link_label.place(x=320, y=286)
    product_link_entry = Entry(frame_cheapest_price, width=43, fg="#0a5ef2")
    product_link_entry.place(x=435, y=284)

# All other products
    gittigidiyor_label = Label(frame_cheapest_price, text="Gittigidiyor:", font=("Helvetica bold", 14), bg="#fff")
    gittigidiyor_label.place(x=320, y=350)
    gittigidiyor_entry = Entry(frame_cheapest_price, width=10, justify=CENTER)
    gittigidiyor_entry.place(x=435, y=350)
    gittigidiyor_name = Entry(frame_cheapest_price, width=31)
    gittigidiyor_name.place(x=540, y=350)

    hepsiburada_label = Label(frame_cheapest_price, text="Hepsiburada:", font=("Helvetica bold", 14), bg="#fff")
    hepsiburada_label.place(x=320, y=380)
    hepsiburada_entry = Entry(frame_cheapest_price, width=10, justify=CENTER)
    hepsiburada_entry.place(x=435, y=380)
    hepsiburada_name = Entry(frame_cheapest_price, width=31)
    hepsiburada_name.place(x=540, y=380)

    trendyol_label = Label(frame_cheapest_price, text="Trendyol:", font=("Helvetica bold", 14), bg="#fff")
    trendyol_label.place(x=320, y=410)
    trendyol_entry = Entry(frame_cheapest_price, width=10, justify=CENTER)
    trendyol_entry.place(x=435, y=410)
    trendyol_name = Entry(frame_cheapest_price, width=31)
    trendyol_name.place(x=540, y=410)

    n11_label = Label(frame_cheapest_price, text="N11:", font=("Helvetica bold", 14), bg="#fff")
    n11_label.place(x=320, y=440)
    n11_entry = Entry(frame_cheapest_price, width=10, justify=CENTER)
    n11_entry.place(x=435, y=440)
    n11_name = Entry(frame_cheapest_price, width=31)
    n11_name.place(x=540, y=440)



    return frame_cheapest_price
