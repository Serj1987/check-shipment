from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter.font import nametofont
import sqlite3


main_win = Tk()
main_win.geometry('1000x550')
main_win.title('Перемещение деталей БП<-->ц1')

# --all tabs---

tab_control = ttk.Notebook(main_win)
tab_arrive = ttk.Frame(tab_control)
tab_send = ttk.Frame(tab_control)
tab_view = ttk.Frame(tab_control)
tab_view_date = ttk.Frame(tab_control)
tab_view_detail = ttk.Frame(tab_control)
tab_delete = ttk.Frame(tab_control)

tab_control.add(tab_arrive, text='Приход из БП')
tab_control.add(tab_send, text='Уходит в БП')
tab_control.add(tab_view, text='Просмотр общих данных')
tab_control.add(tab_view_date, text='Просмотр данных по дате')
tab_control.add(tab_view_detail, text='Просмотр данных по номеру детали')
tab_control.add(tab_delete, text='Удаление позиции')
tab_control.pack(expand=1, fill=BOTH)

# ---add data in tabs---

def add_data_arrive():
    for add_daa_table in frame_table_arrive.winfo_children():
        add_daa_table.destroy()

    con = sqlite3.connect('container.db')  # (r'G:\задачи\project\tkinter\container.db')
    cur = con.cursor()
    tag = 'приход'
    rows = (enter_detail_arrive.get(), name_detail_arrive.get(), quantity_detail_arrive.get(), note_arrive.get(), tag)
    cur.execute("INSERT INTO details VALUES(?, ?, ?, DATE('now'), ?, ?)", rows)
    # sql requests write here to add one string to table

    cur.execute("SELECT * FROM details WHERE date = DATE('now')")  # number_det/name_det/note

    all_data = cur.fetchall()
    con.commit()
    # ===================================================================

    heads = ['№ детали', 'Наименование', 'Количество', 'Дата', 'Примечание', 'Метка']
    add_daa_table = ttk.Treeview(frame_table_arrive, show='headings')
    add_daa_table['columns'] = heads
    # table['displayable'] = ['tag', '№det', 'name', 'quantity', 'date', 'note']  if you want to change the order of
    # columns
    add_daa_table.pack(side=LEFT, fill=BOTH)
    nametofont("TkHeadingFont").configure(size=11)

    for header in heads:
        add_daa_table.heading(header, text=header, anchor='center')
        add_daa_table.column(header, anchor='center')
    for row in all_data:
        add_daa_table.insert('', 'end', values=row)
    scroll_pane = Scrollbar(frame_table_arrive, command=add_daa_table.yview)
    scroll_pane.pack(side=RIGHT, fill='y')
    add_daa_table.configure(yscrollcommand=scroll_pane.set)
    add_daa_table.pack(expand=1, fill=BOTH)

    # for change width of columns use this
    add_daa_table.column('№ детали', width=90)
    add_daa_table.column('Наименование', width=75)
    add_daa_table.column('Количество', width=60)
    add_daa_table.column('Дата', width=55)
    add_daa_table.column('Примечание', width=65)
    add_daa_table.column('Метка', width=55)

 # add data sended


def add_data():
    for table in frame_table_send.winfo_children():
        table.destroy()

    con = sqlite3.connect('container.db')
    cur = con.cursor()
    tag = 'уход'
    rows = (enter_detail_send.get(), name_detail_send.get(), quantity_detail_send.get(), note_send.get(), tag)
    cur.execute("INSERT INTO send VALUES(?, ?, ?, DATE('now'), ?, ?)", rows)
    # sql requests write here to add one string to table

    cur.execute("SELECT * FROM send WHERE date = DATE('now')")  # number_det/name_det/note

    all_data = cur.fetchall()
    con.commit()

    heads = ['№ детали', 'Наименование', 'Количество', 'Дата', 'Примечание', 'Метка']
    table = ttk.Treeview(frame_table_send, show='headings')
    table['columns'] = heads
    # table['displayable'] = ['tag', '№det', 'name', 'quantity', 'date', 'note']  if you want to change the order of columns
    table.pack(side=LEFT, fill=BOTH)
    nametofont("TkHeadingFont").configure(size=11)

    for header in heads:
        table.heading(header, text=header, anchor='center')
        table.column(header, anchor='center')
    for row in all_data:
        table.insert('', 'end', values=row)
    scroll_pane = Scrollbar(frame_table_send, command=table.yview)
    scroll_pane.pack(side=RIGHT, fill='y')
    table.configure(yscrollcommand=scroll_pane.set)
    table.pack(expand=1, fill=BOTH)

    # for change width of columns use this
    table.column('№ детали', width=90)
    table.column('Наименование', width=75)
    table.column('Количество', width=60)
    table.column('Дата', width=55)
    table.column('Примечание', width=65)
    table.column('Метка', width=55)



 # view data

def doit_detail():

    if var.get() == 1:  # if change rad_btn_name
        
        for table in frame_table_detail_send.winfo_children():
            table.destroy()
        for table in frame_table_detail_arrive.winfo_children():
            table.destroy()
        #===========first table===send details=================
        con = sqlite3.connect('container.db')
        cur = con.cursor()
        det = (enter_detail.get(), name_detail.get(),)
        cur.execute(("SELECT * FROM send WHERE number_detail = ? AND name_detail = ? ORDER BY date DESC"), det) # number_det/name_det/note
        #cur.execute(request, (det)) # det
        all_data = cur.fetchall()

        cur.execute(("SELECT SUM(quantity_detail) FROM send WHERE number_detail = ? AND name_detail=? ORDER BY date DESC"), (det))   # !!!! ERROR !!! without outgoing
        outgoing_balance = cur.fetchone()[0]
        cur.execute(("SELECT SUM(quantity_detail) FROM details WHERE number_detail = ? AND name_detail=? ORDER BY date DESC"), (det))
        incoming_balance = cur.fetchone()[0]
        print(" ")
        print('Всего пришло:', incoming_balance)
        print('Всего ушло:', outgoing_balance)
        if outgoing_balance == None:
            result = incoming_balance
            print('Остаток: ', result)
        elif incoming_balance == None:
            print('Ничего не приходило!')
        else:
            result = incoming_balance - outgoing_balance
            print('Остаток: ', result)

        #   for work with table use this
        heads = ['№ детали', 'Наименование', 'Количество', 'Дата', 'Примечание', 'Метка']
        table = ttk.Treeview(frame_table_detail_send, show='headings')
        table['columns'] = heads
        
        nametofont("TkHeadingFont").configure(size=11)

        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')
        for row in all_data:
            table.insert('', 'end', values=row)
        scroll_pane = Scrollbar(frame_table_detail_send, command=table.yview)
        scroll_pane.pack(side=RIGHT, fill='y')
        table.configure(yscrollcommand=scroll_pane.set)
        table.pack(expand=1, fill=BOTH)
        #    for change width of columns use this
        table.column('№ детали', width=90)
        table.column('Наименование', width=75)
        table.column('Количество', width=60)
        table.column('Дата', width=55)
        table.column('Примечание', width=65)
        table.column('Метка', width=55)
    #===========second table===arrived details======================
        
        con = sqlite3.connect('container.db')
        cur = con.cursor()
        dat = (enter_detail.get(), name_detail.get())
        request = "SELECT * FROM details WHERE number_detail = ? AND name_detail=? ORDER BY date DESC"  # number_det/name_det/note
        cur.execute(request, dat)  # dat
        all_data = cur.fetchall()

        heads = ['№ детали', 'Наименование', 'Количество', 'Дата', 'Примечание', 'Метка']
        table = ttk.Treeview(frame_table_detail_arrive, show='headings')
        table['columns'] = heads
        # table['displayable'] = ['tag', '№det', 'name', 'quantity', 'date', 'note']  if you want to change the order of columns

        nametofont("TkHeadingFont").configure(size=11)

        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')
        for row in all_data:
            table.insert('', 'end', values=row)
        scroll_pane = Scrollbar(frame_table_detail_arrive, command=table.yview)
        scroll_pane.pack(side=RIGHT, fill='y')
        table.configure(yscrollcommand=scroll_pane.set)
        table.pack(expand=1, fill=BOTH)
        #    for change width of columns use this
        table.column('№ детали', width=90)
        table.column('Наименование', width=75)
        table.column('Количество', width=60)
        table.column('Дата', width=55)
        table.column('Примечание', width=65)
        table.column('Метка', width=55)

    elif var.get() == 0:  # if change rad_btn

        for table in frame_table_detail_send.winfo_children():
            table.destroy()
        for table in frame_table_detail_arrive.winfo_children():
            table.destroy()
        #===========first table===send details=================
        con = sqlite3.connect('container.db')
        cur = con.cursor()
        det = (enter_detail.get())#, name_detail.get())
        cur.execute(("SELECT * FROM send WHERE number_detail = ? ORDER BY date DESC"), (det,)) # number_det/name_det/note
        #cur.execute(request, (det)) # det
        all_data = cur.fetchall()

        cur.execute(("SELECT SUM(quantity_detail) FROM send WHERE number_detail = ? ORDER BY date DESC"), (det,))   # !!!! ERROR !!! without outgoing
        outgoing_balance = cur.fetchone()[0]
        cur.execute(("SELECT SUM(quantity_detail) FROM details WHERE number_detail = ? ORDER BY date DESC"), (det,))
        incoming_balance = cur.fetchone()[0]
        print(" ")
        print('Всего пришло:', incoming_balance)
        print('Всего ушло:', outgoing_balance)
        if outgoing_balance == None:
            result = incoming_balance
            print('Остаток: ', result)
        elif incoming_balance == None:
            print('Ничего не приходило!')
        else:
            result = incoming_balance - outgoing_balance
            print('Остаток: ', result)

        #   for work with table use this
        heads = ['№ детали', 'Наименование', 'Количество', 'Дата', 'Примечание', 'Метка']
        table = ttk.Treeview(frame_table_detail_send, show='headings')
        table['columns'] = heads
        # table['displayable'] = ['tag', '№det', 'name', 'quantity', 'date', 'note']  if you want to change the order of columns

        nametofont("TkHeadingFont").configure(size=11)

        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')
        for row in all_data:
            table.insert('', 'end', values=row)
        scroll_pane = Scrollbar(frame_table_detail_send, command=table.yview)
        scroll_pane.pack(side=RIGHT, fill='y')
        table.configure(yscrollcommand=scroll_pane.set)
        table.pack(expand=1, fill=BOTH)
        #    for change width of columns use this
        table.column('№ детали', width=90)
        table.column('Наименование', width=75)
        table.column('Количество', width=60)
        table.column('Дата', width=55)
        table.column('Примечание', width=65)
        table.column('Метка', width=55)
    #===========second table===arrived details======================
        
        con = sqlite3.connect('container.db')
        cur = con.cursor()
        dat = (enter_detail.get()) #, name_detail.get())
        cur.execute("SELECT * FROM details WHERE number_detail = ? ORDER BY date DESC", (dat,))# AND name_detail=? ORDER BY date DESC"  # number_det/name_det/note
        all_data = cur.fetchall()

        heads = ['№ детали', 'Наименование', 'Количество', 'Дата', 'Примечание', 'Метка']
        table = ttk.Treeview(frame_table_detail_arrive, show='headings')
        table['columns'] = heads
        # table['displayable'] = ['tag', '№det', 'name', 'quantity', 'date', 'note']  if you want to change the order of columns

        nametofont("TkHeadingFont").configure(size=11)

        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')
        for row in all_data:
            table.insert('', 'end', values=row)
        scroll_pane = Scrollbar(frame_table_detail_arrive, command=table.yview)
        scroll_pane.pack(side=RIGHT, fill='y')
        table.configure(yscrollcommand=scroll_pane.set)
        table.pack(expand=1, fill=BOTH)
        #    for change width of columns use this
        table.column('№ детали', width=90)
        table.column('Наименование', width=75)
        table.column('Количество', width=60)
        table.column('Дата', width=55)
        table.column('Примечание', width=65)
        table.column('Метка', width=55)
    

def doit_date():
    for table in frame_table_date_send.winfo_children():
        table.destroy()
    for table in frame_table_date_arrive.winfo_children():
        table.destroy()
    con = sqlite3.connect('container.db')
    cur = con.cursor()
    dat = enter_date.get()
    request = "SELECT * FROM details WHERE date = ?"  # names of columns in table sqlite: number_det/name_det/quantity/note
    cur.execute(request, (dat,))
    all_data = cur.fetchall()

    # ===================================================================

    heads = ['№ детали', 'Наименование', 'Количество', 'Дата', 'Примечание', 'Метка']
    table = ttk.Treeview(frame_table_date_arrive, show='headings')
    table['columns'] = heads
    # table['displayable'] = ['tag', '№det', 'name', 'quantity', 'date', 'note']  if you want to change the order of columns

    nametofont("TkHeadingFont").configure(size=11)

    for header in heads:

        table.heading(header, text=header, anchor='center')
        table.column(header, anchor='center')
    for row in all_data:
        table.insert('', 'end', values=row)
    scroll_pane = Scrollbar(frame_table_date_arrive, command=table.yview)
    scroll_pane.pack(side=RIGHT, fill='y')
    table.configure(yscrollcommand=scroll_pane.set)
    table.pack(expand=1, fill=BOTH)
    # ======for change width of columns use this===
    table.column('№ детали', width=90)
    table.column('Наименование', width=75)
    table.column('Количество', width=60)
    table.column('Дата', width=55)
    table.column('Примечание', width=65)
    table.column('Метка', width=55)
	# work with SQLite 
    con = sqlite3.connect('container.db')
    cur = con.cursor()
    dat = enter_date.get()
    request = "SELECT * FROM send WHERE date = ?"  # number_det/name_det/note
    cur.execute(request, (dat,))
    all_data = cur.fetchall()

    heads = ['№ детали', 'Наименование', 'Количество', 'Дата', 'Примечание', 'Метка']
    table = ttk.Treeview(frame_table_date_send, show='headings')
    table['columns'] = heads
    # table['displayable'] = ['tag', '№det', 'name', 'quantity', 'date', 'note']  if you want to change the order of columns

    nametofont("TkHeadingFont").configure(size=11)

    for header in heads:
        table.heading(header, text=header, anchor='center')
        table.column(header, anchor='center')
    for row in all_data:
        table.insert('', 'end', values=row)
    scroll_pane = Scrollbar(frame_table_date_send, command=table.yview)
    scroll_pane.pack(side=RIGHT, fill='y')
    table.configure(yscrollcommand=scroll_pane.set)
    table.pack(expand=1, fill=BOTH)
    # ======for change width of columns use this===
    table.column('№ детали', width=90)
    table.column('Наименование', width=75)
    table.column('Количество', width=60)
    table.column('Дата', width=55)
    table.column('Примечание', width=65)
    table.column('Метка', width=55)


# delete data

def del_row_send():
    con = sqlite3.connect('container.db')
    cur = con.cursor()
    row = (detail.get(), name_detail.get(), date.get())
    cur.execute("DELETE FROM send WHERE number_detail=? AND name_detail=? AND date=?;", row)  # number_det/name_det/note
    
    all_data = cur.fetchall()
    con.commit()
    print('Выполнено')

def del_row_details():
    con = sqlite3.connect('container.db')
    cur = con.cursor()
    row = (detail.get(), name_detail.get(), date.get())
    cur.execute("DELETE FROM details WHERE number_detail=? AND name_detail=? AND date=?;", row)  # number_det/name_det/note
    
    all_data = cur.fetchall()
    con.commit()
    print('Выполнено')

# =============widgets in first tab=============
frame_widgets_arrive = LabelFrame(tab_arrive, text='Детали которые пришли из БП', height=100)
frame_widgets_arrive.pack(side=TOP, fill=BOTH)

lbl_detail = Label(frame_widgets_arrive, text='№ детали', font=14)
lbl_detail.grid(column=0, row=0)

enter_detail_arrive = ttk.Combobox(frame_widgets_arrive, width=30, font=9)
enter_detail_arrive['values'] = ()  # numbers det paste here
enter_detail_arrive.grid(column=0, row=1)
enter_detail_arrive.focus()

lbl_name_det = Label(frame_widgets_arrive, text='Наименование', font=14)
lbl_name_det.grid(column=1, row=0)

name_detail_arrive = ttk.Combobox(frame_widgets_arrive, font=10, width=12)
name_detail_arrive['values'] = (' ', 'Букса', 'Вилка', 'Голова штока', 'Голова цилиндра', 'Поршень', 'Тех.узел',
                                'Труба защитная', 'Труба цилиндра', 'Фланец', 'Цилиндр', 'Шайба', 'Шток')
name_detail_arrive.current(0)
name_detail_arrive.grid(column=1, row=1, padx=5)

lbl_quantity = Label(frame_widgets_arrive, text='Количество', font=14)
lbl_quantity.grid(column=2, row=0)

quantity_detail_arrive = Spinbox(frame_widgets_arrive, from_=0, to=100, font=10, width=10)
quantity_detail_arrive.grid(column=2, row=1)

lbl_note = Label(frame_widgets_arrive, text='Примечание', font=14)
lbl_note.grid(column=3, row=0)

note_arrive = Entry(frame_widgets_arrive, width=17, font=9)
note_arrive.grid(column=3, row=1, padx=5)

# table
frame_table_arrive = Frame(tab_arrive, height=200)
frame_table_arrive.pack(side=TOP, fill=BOTH)

 # buttons
frame_button_arrive = Frame(tab_arrive, height=60)
frame_button_arrive.pack(side=BOTTOM, fill=BOTH)

btn_add = Button(frame_button_arrive, text='Добавить', bg='green', width=25, font=10, command=add_data_arrive)
btn_add.pack(side=RIGHT, padx=5)


# -----second tab--tab_send----------------------

# =============widgets of second tab=============
frame_widgets_send = LabelFrame(tab_send, text='Детали которые отправляются в БП', height=100)
frame_widgets_send.pack(side=TOP, fill=BOTH)

lbl_detail = Label(frame_widgets_send, text='№ детали', font=14)
lbl_detail.grid(column=0, row=0)

enter_detail_send = ttk.Combobox(frame_widgets_send, width=30, font=9)
enter_detail_send['values'] = ()  # numbers det paste here
enter_detail_send.grid(column=0, row=1)
enter_detail_send.focus()

lbl_name_det = Label(frame_widgets_send, text='Наименование', font=14)
lbl_name_det.grid(column=1, row=0)

name_detail_send = ttk.Combobox(frame_widgets_send, font=10, width=12)
name_detail_send['values'] = (' ', 'Букса', 'Вилка', 'Голова штока', 'Голова цилиндра', 'Поршень', 'Тех.узел',
                              'Труба защитная', 'Труба цилиндра', 'Фланец', 'Цилиндр', 'Шайба', 'Шток')
name_detail_send.current(0)
name_detail_send.grid(column=1, row=1, padx=5)

lbl_quantity = Label(frame_widgets_send, text='Количество', font=14)
lbl_quantity.grid(column=2, row=0)

quantity_detail_send = Spinbox(frame_widgets_send, from_=0, to=100, font=10, width=10)
quantity_detail_send.grid(column=2, row=1)

lbl_note = Label(frame_widgets_send, text='Примечание', font=14)
lbl_note.grid(column=3, row=0)

note_send = Entry(frame_widgets_send, width=17, font=9)
note_send.grid(column=3, row=1, padx=5)

 # table frames
frame_table_send = Frame(tab_send, height=200)
frame_table_send.pack(side=TOP, fill=BOTH)

 # buttons
frame_button_send = Frame(tab_send, height=60)
frame_button_send.pack(side=BOTTOM, fill=BOTH)

btn_add = Button(frame_button_send, text='Добавить', bg='green', width=25, font=10, command=add_data)
btn_add.pack(side=RIGHT, padx=5)

# ---------third tab---tabs view------
# ----------common view------
frame_check = Frame(tab_view, width=700, heigh=20, bg='blue')
frame_check.place(relx=0, rely=0, relwidth=1, relheigh=1)
frame_list_view = Frame(tab_view, width=700, heigh=300, bg='yellow')  # for work with table
frame_list_view.place(relx=0, rely=0, relwidth=1, relheigh=1)


con = sqlite3.connect('container.db')
cur = con.cursor()
request = "SELECT * FROM details UNION SELECT * FROM send " \
          "ORDER BY date DESC"  # number_det/name_det/note
cur.execute(request)
all_data = cur.fetchall()

heads = ['№ детали', 'Наименование', 'Количество', 'Дата', 'Примечание', 'Метка']
table = ttk.Treeview(frame_list_view, show='headings')
table['columns'] = heads
# table['displayable'] = ['tag', '№det', 'name', 'quantity', 'date', 'note']  if you want to change the order of columns

nametofont("TkHeadingFont").configure(size=11)  # change fontsize

for header in heads:
    table.heading(header, text=header, anchor='center')
    table.column(header, anchor='center')

    table.column('№ детали', width=90)
    table.column('Наименование', width=75)
    table.column('Количество', width=60)
    table.column('Дата', width=55)
    table.column('Примечание', width=65)
    table.column('Метка', width=55)

for row in all_data:
    table.insert('', 'end', values=row)
scroll_pane = Scrollbar(frame_list_view, command=table.yview)
scroll_pane.pack(side=RIGHT, fill='y')
table.configure(yscrollcommand=scroll_pane.set)
table.pack(expand=1, fill=BOTH)


# --------------fourth tab---tab_view_date

frame_widgets_date = LabelFrame(tab_view_date, text='Введите дату в формате YYYY-MM-DD', height=100)
frame_widgets_date.pack(side=TOP, fill=BOTH)

enter_date = Entry(frame_widgets_date, width=12, font=10)
enter_date.pack(side=LEFT, fill=BOTH)
enter_date.focus()

btn_add = Button(frame_widgets_date, text='OK', bg='green', width=12, font=10, command=doit_date)
btn_add.pack(side=LEFT, fill=BOTH, padx=5)

frame_table_date_arrive = LabelFrame(tab_view_date, text='Пришло из БП')  # , width=700, heigh=100)
frame_table_date_arrive.pack(side=BOTTOM, fill=BOTH)
frame_table_date_send = LabelFrame(tab_view_date, text='Отправлено в БП')
frame_table_date_send.pack(side=TOP, fill=BOTH)


# ---------fifth tab---tab_view_detail---------------

frame_widgets_detail = LabelFrame(tab_view_detail,text='Введите номер детали ХХХ  и наименование', height=100)
frame_widgets_detail.pack(side=TOP, fill=BOTH)

enter_detail = Entry(frame_widgets_detail, width=15, font=10)
enter_detail.pack(side=LEFT, fill=BOTH)
enter_detail.focus()

name_detail = Combobox(frame_widgets_detail, font=10, width=12)
name_detail['values'] = (' ', 'Букса', 'Вилка', 'Голова штока', 'Голова цилиндра', 'Поршень', 'Тех.узел',
                         'Труба защитная', 'Труба цилиндра', 'Фланец', 'Цилиндр', 'Шайба', 'Шток')
name_detail.current(0)
name_detail.pack(side=LEFT, fill=BOTH, padx=5)

btn_add = Button(frame_widgets_detail, text='OK', bg='green', width=12, font=10, command=doit_detail)
btn_add.pack(side=LEFT, fill=BOTH, padx=10)

var = IntVar()
var.set(0)

rad_btn_name = Radiobutton(frame_widgets_detail, text='с наименованием', variable = var, value = 1, padx = 1, pady = 1)
rad_btn_name.pack(side=LEFT, fill=BOTH, padx=10)
rad_btn = Radiobutton(frame_widgets_detail, text='только по номеру', variable = var, value = 0, padx = 1, pady = 1)
rad_btn.pack(side=LEFT, fill=BOTH, padx=10)


frame_table_detail_send = LabelFrame(tab_view_detail, text='Ушло в БП') #, width=700, heigh=100)
frame_table_detail_send.pack(side=BOTTOM, fill=BOTH)
frame_table_detail_arrive = LabelFrame(tab_view_detail, text='Пришло из БП')
frame_table_detail_arrive.pack(side=BOTTOM, fill=BOTH)
# -----------------sixth tab---tab delete--------------------------------


frame_entry_delete = LabelFrame(tab_delete, text='Введите № детали-----------наименование----и---дату YYYY-MM-DD', font=10, bg='green', width=400, height=100)
frame_entry_delete.pack(side=TOP, fill=BOTH)
frame_btn_delete = Frame(tab_delete, width=430, heigh=50, bg='sky blue')
frame_btn_delete.pack(side=TOP, fill=BOTH)

detail = Entry(frame_entry_delete, font=12, width=20) 
detail.pack(side=LEFT, fill=BOTH)
detail.focus()

name_detail = Combobox(frame_entry_delete, font=10, width=12)
name_detail['values'] = (' ', 'Букса', 'Вилка', 'Голова штока', 'Голова цилиндра', 'Поршень', 'Тех.узел',
                         'Труба защитная', 'Труба цилиндра', 'Фланец', 'Цилиндр', 'Шайба', 'Шток')
name_detail.current(0)
name_detail.pack(side=LEFT, fill=BOTH, padx=5)


date = Entry(frame_entry_delete, font=12, width=20)
date.pack(side=LEFT, fill=BOTH, padx=5)

btn_del_arr = Button(frame_btn_delete, text='Удалить из приходов', font=12, width=20, height=1, bg='gray', fg='red', command=del_row_details)
btn_del_arr.pack(side=RIGHT, fill=BOTH, padx=5)

btn_del_send = Button(frame_btn_delete, text='Удалить из уходящих', font=12, width=20, height=1, bg='gray', fg='red', command=del_row_send)
btn_del_send.pack(side=LEFT, fill=BOTH, padx=5)

   
   # the end of poebota

main_win.mainloop()
