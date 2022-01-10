from tkinter import *
from tkinter import messagebox
import webbrowser

from back_end.quick_search import get_links

def search_platform_display(menu, background):

    # URL Functions
    def erase_urls():
        amazon_entry.delete(0, END)
        gittigidiyor_entry.delete(0, END)
        hepsiburada_entry.delete(0, END)
        trendyol_entry.delete(0, END)
        n11_entry.delete(0, END)

    def fill_urls(links: dict):
        amazon_entry.insert(0, links['amazon'])
        gittigidiyor_entry.insert(0, links['gittigidiyor'])
        hepsiburada_entry.insert(0, links['hepsiburada'])
        trendyol_entry.insert(0, links['trendyol'])
        n11_entry.insert(0, links['n11'])

    def bind_entries(links: dict):
        amazon_entry.bind("<Button-1>", lambda e: callback(links['amazon']))
        gittigidiyor_entry.bind("<Button-1>", lambda e: callback(links['gittigidiyor']))
        hepsiburada_entry.bind("<Button-1>", lambda e: callback(links['hepsiburada']))
        trendyol_entry.bind("<Button-1>", lambda e: callback(links['trendyol']))
        n11_entry.bind("<Button-1>", lambda e: callback(links['n11']))

    def callback(url):
        webbrowser.open_new_tab(url)

    def open_all_links():
        webbrowser.open_new_tab(amazon_entry.get())
        webbrowser.open_new_tab(gittigidiyor_entry.get())
        webbrowser.open_new_tab(hepsiburada_entry.get())
        webbrowser.open_new_tab(trendyol_entry.get())
        webbrowser.open_new_tab(n11_entry.get())


    def button_clicked(event=0):
        searched_model = search_entry.get()
        if searched_model == "":
            messagebox.showerror("Error", message="Enter A Mobile Model To Search For")
            erase_urls()
        else:
            erase_urls()
            messagebox.showinfo("Info", message="You can click on the links below!")
            website_links = get_links(search_entry.get())
            fill_urls(website_links)
            bind_entries(website_links)

# Background for page
    frame_search_platforms = Frame(menu, width=850, height=550)
    main_bg_label = Label(frame_search_platforms, image=background)
    main_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Search bar
    search_label = Label(frame_search_platforms, text="Mobile Model:", font=("Helvetica bold", 14), bg='#fff')
    search_entry = Entry(frame_search_platforms, width=32)
    search_entry.bind('<Return>', button_clicked)
    search_button = Button(frame_search_platforms, text='Search', command=button_clicked, pady=2)

    search_label.place(x=320, y=151)
    search_entry.place(x=445, y=150)
    search_button.place(x=750, y=149)

# Websites
    amazon_label = Label(frame_search_platforms, text="Amazon Link:", bg="#fff")
    amazon_label.place(x=320, y=225)
    amazon_entry = Entry(frame_search_platforms, width=40, fg="#0a5ef2")
    amazon_entry.place(x=445, y=224)

    gittigidiyor_label = Label(frame_search_platforms, text="Gittigidiyor Link:", bg="#fff")
    gittigidiyor_label.place(x=320, y=265)
    gittigidiyor_entry = Entry(frame_search_platforms, width=40, fg="#0a5ef2")
    gittigidiyor_entry.place(x=445, y=264)

    hepsiburada_label = Label(frame_search_platforms, text="Hepsiburada Link:", bg="#fff")
    hepsiburada_label.place(x=320, y=305)
    hepsiburada_entry = Entry(frame_search_platforms, width=40, fg="#0a5ef2")
    hepsiburada_entry.place(x=445, y=304)

    trendyol_label = Label(frame_search_platforms, text="Trendyol Link:", bg="#fff")
    trendyol_label.place(x=320, y=345)
    trendyol_entry = Entry(frame_search_platforms, width=40, fg="#0a5ef2")
    trendyol_entry.place(x=445, y=344)

    n11_label = Label(frame_search_platforms, text="N11 Link:", bg="#fff")
    n11_label.place(x=320, y=385)
    n11_entry = Entry(frame_search_platforms, width=40, fg="#0a5ef2")
    n11_entry.place(x=445, y=384)

    open_all_button = Button(frame_search_platforms, text="OPEN ALL LINKS AT ONCE", command=open_all_links, width= 52, pady=2)
    open_all_button.place(x=318, y=430)

    return frame_search_platforms
