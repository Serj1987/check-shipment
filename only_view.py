from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter.font import nametofont
import sqlite3


# view date tab
def doit_date():

    for table in frame_table_date_send.winfo_children():
        table.destroy()
    for table in frame_table_date_arrive.winfo_children():
        table.destroy()    
    con = sqlite3.connect(r'\\Bot01\прог\container.db')
    cur = con.cursor()
    dat = enter_date.get()
    request = "SELECT * FROM details WHERE date = ?"  # names of columns in table sqlite: number_det/name_det/quantity/note
    cur.execute(request, (dat,))
    all_data = cur.fetchall()

    #===================================================================

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
    #======for change width of columns use this===
    table.column('№ детали', width=90)
    table.column('Наименование', width=75)
    table.column('Количество', width=60)
    table.column('Дата', width=55)
    table.column('Примечание', width=65)
    table.column('Метка', width=55)
  
    con = sqlite3.connect(r'\\Bot01\прог\container.db')
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
    #======for change width of columns use this===
    table.column('№ детали', width=90)
    table.column('Наименование', width=75)
    table.column('Количество', width=60)
    table.column('Дата', width=55)
    table.column('Примечание', width=65)
    table.column('Метка', width=55)


def doit_detail():

    if var.get() == 1:  # if change rad_btn_name
        
        for table in frame_table_detail_send.winfo_children():
            table.destroy()
        for table in frame_table_detail_arrive.winfo_children():
            table.destroy()
        #===========first table===send details=================
        con = sqlite3.connect(r'\\Bot01\прог\container.db')
        cur = con.cursor()
        det = (enter_detail.get(), name_detail.get())
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
        
        con = sqlite3.connect(r'\\Bot01\прог\container.db')
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
        con = sqlite3.connect(r'\\Bot01\прог\container.db')
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
        
        con = sqlite3.connect(r'\\Bot01\прог\container.db')
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

main_win = Tk()
main_win.geometry('880x550')
main_win.title('Перемещение деталей БП<-->ц1')

#--all tabs---

tab_control = ttk.Notebook(main_win)
tab_view = ttk.Frame(tab_control)
tab_view_date = ttk.Frame(tab_control)
tab_view_detail = ttk.Frame(tab_control)
tab_delete = ttk.Frame(tab_control)

tab_control.add(tab_view, text='Просмотр общих данных')
tab_control.add(tab_view_date, text='Просмотр данных по дате')
tab_control.add(tab_view_detail, text='Просмотр данных по номеру детали')
tab_control.add(tab_delete, text='Удаление позиции')
tab_control.pack(expand=1, fill=BOTH)

#---------first tab---tabs view------
# ----------common view------

frame_check = Frame(tab_view, width=700, heigh=20, bg='blue')
frame_check.place(relx=0, rely=0, relwidth=1, relheigh=1)
frame_list_view = Frame(tab_view, width=700, heigh=300,  bg='yellow')  # for work with table
frame_list_view.place(relx=0, rely=0, relwidth=1, relheigh=1)


con = sqlite3.connect(r'\\Bot01\прог\container.db')
cur = con.cursor()
request = "SELECT * FROM details UNION SELECT * FROM send " \
          "ORDER BY date DESC"  # number_det/name_det/note
cur.execute(request)
all_data = cur.fetchall()

heads = ['№ детали', 'Наименование', 'Количество', 'Дата', 'Примечание', 'Метка']
table = ttk.Treeview(frame_list_view, show='headings')
table['columns'] = heads
# table['displayable'] = ['tag', '№det', 'name', 'quantity', 'date', 'note']  if you want to change the order of columns

nametofont("TkHeadingFont").configure(size=11)  #change fontsize

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

#-------------the end of first tab-------------
#--------------second tab---tab_view_date

frame_widgets_date = LabelFrame(tab_view_date,text='Введите дату в формате YYYY-MM-DD', height=100)
frame_widgets_date.pack(side=TOP, fill=BOTH)

enter_date = Entry(frame_widgets_date, width=12, font=10)
enter_date.pack(side=LEFT, fill=BOTH)
enter_date.focus()

btn_add = Button(frame_widgets_date, text='OK', bg='sky blue3', width=12, font=10, command=doit_date)
btn_add.pack(side=LEFT, fill=BOTH, padx=5)

frame_table_date_arrive = LabelFrame(tab_view_date, text='Пришло из БП') #, width=700, heigh=100)
frame_table_date_arrive.pack(side=BOTTOM, fill=BOTH)
frame_table_date_send = LabelFrame(tab_view_date, text='Отправлено в БП')
frame_table_date_send.pack(side=TOP, fill=BOTH)

#----------end of second tab--------

#---------third tab---tab_view_detail---------------

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

btn_add = Button(frame_widgets_detail, text='OK', bg='sky blue3', width=12, font=10, command=doit_detail)
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

#---------end of third tab-------------------------
#-------------------------------------------------

main_win.mainloop()
