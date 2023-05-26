from tkinter import *
import backEnd

window = Tk()
window.title('مدیریت کتابخانه - راد')
# ===============================Labels=========================
L1 = Label(window, text='عنوان')
L1.grid(row=0, column=0)
L2 = Label(window, text='نویسنده')
L2.grid(row=0, column=2)
L3 = Label(window, text='سال انتشار')
L3.grid(row=1, column=0)
L4 = Label(window, text='شماره سریال')
L4.grid(row=1, column=2)

# ===============================Entries=========================
title_text = StringVar()
E1 = Entry(window, textvariable=title_text)
E1.grid(row=0, column=1)

author_text = StringVar()
E2 = Entry(window, textvariable=author_text)
E2.grid(row=0, column=3)

year_text = StringVar()
E3 = Entry(window, textvariable=year_text)
E3.grid(row=1, column=1)

isbn_text = StringVar()
E4 = Entry(window, textvariable=isbn_text)
E4.grid(row=1, column=3)

list1 = Listbox(window, width=35, height=6)
list1.grid(row=2, column=0, rowspan=5, columnspan=2)

scrollBar1 = Scrollbar(window)
scrollBar1.grid(row=2, column=2, rowspan=5)
list1.configure(yscrollcommand=scrollBar1.set)
scrollBar1.configure(command=list1.yview)

def get_selected_row(event):
    global selected_book
    if len(list1.curselection())>0:
        index = list1.curselection()[0]
        selected_book = list1.get(index)
        E1.delete(0, END)
        E1.insert(END, selected_book[1])
        E2.delete(0, END)
        E2.insert(END, selected_book[2])
        E3.delete(0, END)
        E3.insert(END, selected_book[3])
        E4.delete(0, END)
        E4.insert(END, selected_book[4])



list1.bind("<<ListboxSelect>>", get_selected_row)

def clear():
    list1.delete(0, END)
def fill(books):
    for book in books:
        list1.insert(END, book)



def view_command():
    clear()
    books = backEnd.view()
    fill(books)
b1 = Button(window, text='نمایش همه', width=12, command=lambda: view_command())
b1.grid(row=2, column=3)


def search_command():
    clear()
    books = backEnd.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    fill(books)
b2 = Button(window, text='جستجو کتاب', width=12, command=search_command)
b2.grid(row=3, column=3)


def add_command():
    backEnd.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()
b3 = Button(window, text='اضافه کردن کتاب', width=12, command=add_command)
b3.grid(row=4, column=3)

def update_command():
    backEnd.update(selected_book[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

b4 = Button(window, text='به روز رسانی', width=12, command=update_command)
b4.grid(row=5, column=3)

def delete_command():
    backEnd.delete(selected_book[0])
    view_command()
b5 = Button(window, text='حذف کتاب', width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text='خروج', width=12, command=window.destroy)
b6.grid(row=7, column=3)

list1.configure()
view_command()
window.mainloop()
