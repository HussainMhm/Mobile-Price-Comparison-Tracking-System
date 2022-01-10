from tkinter import *

def home_page_display(menu, background):
    frame_home_page = Frame(menu, width=850, height=550)

    main_bg_label = Label(frame_home_page, image=background)
    main_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    return frame_home_page
