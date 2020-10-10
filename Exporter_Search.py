from tkinter import *
import mysql.connector
import datetime


my_db = mysql.connector.connect(host="localhost", user="root", password="root123",
                                auth_plugin="mysql_native_password", database="SAMEER_FARMS")

my_cursor = my_db.cursor()


def search():
    # Making labels of main row
    bill_label = Label(table_frame, text="Bill No.", font="Ariel 16 ", bg="lavender", relief="solid",
                       borderwidth=1, padx=10)
    cust_name_label = Label(table_frame, text="Customer Name", font="Ariel 16 ", bg="lavender", relief="solid",
                            borderwidth=1, padx=15)
    w1_label = Label(table_frame, text="Weight 1", font="Ariel 16 ", bg="lavender", relief="solid",
                     borderwidth=1, padx=15)
    w2_label = Label(table_frame, text="Weight 2", font="Ariel 16 ", bg="lavender", relief="solid",
                     borderwidth=1, padx=15)
    w3_label = Label(table_frame, text="Weight 3", font="Ariel 16 ", bg="lavender", relief="solid",
                     borderwidth=1, padx=15)
    w4_label = Label(table_frame, text="Weight 4", font="Ariel 16 ", bg="lavender", relief="solid",
                     borderwidth=1, padx=15)
    w5_label = Label(table_frame, text="Weight 5", font="Ariel 16 ", bg="lavender", relief="solid",
                     borderwidth=1, padx=15)
    total_label = Label(table_frame, text="Total", font="Ariel 16 ", bg="lavender", relief="solid",
                        borderwidth=1, padx=25)
    received_label = Label(table_frame, text="Received", font="Ariel 16 ", bg="lavender",
                           relief="solid", borderwidth=1, padx=20)
    fare_label = Label(table_frame, text="Fare", font="Ariel 16 ", bg="lavender", relief="solid",
                       borderwidth=1, padx=25)
    due_label = Label(table_frame, text="Due", font="Ariel 16 ", bg="lavender", relief="solid",
                      borderwidth=1, padx=25)

    # Packing labels
    bill_label.grid(row=1, column=1)
    cust_name_label.grid(row=1, column=2)
    w1_label.grid(row=1, column=3)
    w2_label.grid(row=1, column=4)
    w3_label.grid(row=1, column=5)
    w4_label.grid(row=1, column=6)
    w5_label.grid(row=1, column=7)
    total_label.grid(row=1, column=8)
    received_label.grid(row=1, column=9)
    fare_label.grid(row=1, column=10)
    due_label.grid(row=1, column=11)
    i = 2
    font = "Ariel 15"
    d, m, y = map(int, (date_value.get()).split('/'))
    date = datetime.date(y, m, d)
    my_cursor.execute(f'''SELECT bill_no, cust_name, weight_1, weight_2, weight_3, weight_4, weight_5, total,
                          fare, received, due FROM export
                          WHERE expo_name='{expo_value.get()}' and date='{date}';''')

    for k in my_cursor:
        i = i+1
        bill_no = StringVar()
        cust_name = StringVar()
        weight_1 = StringVar()
        weight_2 = StringVar()
        weight_3 = StringVar()
        weight_4 = StringVar()
        weight_5 = StringVar()
        total = StringVar()
        fare = StringVar()
        received = StringVar()
        due = StringVar()

        # making entry widgets
        bill_no_entry = Entry(table_frame, textvariable=bill_no, font=font, bg="white",
                              relief='solid', borderwidth=1, width=5)
        cust_name_entry = Entry(table_frame, textvariable=cust_name, font=font, bg="white",
                                relief='solid', borderwidth=1, width=15)
        weight_1_entry = Entry(table_frame, textvariable=weight_1, font=font, bg="white",
                               relief='solid', borderwidth=1, width=7)
        weight_2_entry = Entry(table_frame, textvariable=weight_2, font=font, bg="white",
                               relief='solid', borderwidth=1, width=7)
        weight_3_entry = Entry(table_frame, textvariable=weight_3, font=font, bg="white",
                               relief='solid', borderwidth=1, width=7)
        weight_4_entry = Entry(table_frame, textvariable=weight_4, font=font, bg="white",
                               relief='solid', borderwidth=1, width=7)
        weight_5_entry = Entry(table_frame, textvariable=weight_5, font=font, bg="white",
                               relief='solid', borderwidth=1, width=7)
        total_entry = Entry(table_frame, textvariable=total, font=font, bg="white",
                            relief='solid', borderwidth=1, width=7)
        fare_value_entry = Entry(table_frame, textvariable=fare, font=font, bg="white",
                                 relief='solid', borderwidth=1, width=7)
        received_entry = Entry(table_frame, textvariable=received, font=font, bg="white",
                               relief='solid', borderwidth=1, width=7)
        due_entry = Entry(table_frame, textvariable=due, font=font, bg="white",
                          relief='solid', borderwidth=1, width=7)

        # packing the entry
        bill_no_entry.grid(row=i, column=1, pady=2)
        cust_name_entry.grid(row=i, column=2, pady=2)
        weight_1_entry.grid(row=i, column=3, pady=2)
        weight_2_entry.grid(row=i, column=4, pady=2)
        weight_3_entry.grid(row=i, column=5, pady=2)
        weight_4_entry.grid(row=i, column=6, pady=2)
        weight_5_entry.grid(row=i, column=7, pady=2)
        total_entry.grid(row=i, column=8, pady=2)
        fare_value_entry.grid(row=i, column=9, pady=2)
        received_entry.grid(row=i, column=10, pady=2)
        due_entry.grid(row=i, column=11, pady=2)

        # filling values
        bill_no.set(f"{k[0]}")
        cust_name.set(f"{k[1]}")
        weight_1.set(f"{k[2]}")
        weight_2.set(f"{k[3]}")
        weight_3.set(f"{k[4]}")
        weight_4.set(f"{k[5]}")
        weight_5.set(f"{k[6]}")
        total.set(f"{k[7]}")
        fare.set(f"{k[8]}")
        received.set(f"{k[9]}")
        due.set(f"{k[10]}")
        root.update()


def fa_calc():
    pass


def clear():
    for widget in table_frame.winfo_children():
        widget.destroy()


def save():
    my_cursor.execute("UPDATE `sameer_farms`.`export` SET `bill_no` = '121', `cust_name` = 'daddy'," 
                      "`weight_1` = '12', `weight_2` = '12', `weight_3` = '12', `weight_4` = '12', `weight_5` = '12', "
                      "`total` = '12', `fare` = '12', `received` = '12', `due` = '12' WHERE (`bill_no` = '122');")


if __name__ == '__main__':

    root = Tk()

    root.geometry("1200x600")
    root.title("Import Accounts ")

    # Making Heading Frame
    head_frame = Frame(root, bg='lavender', relief='solid', borderwidth=3)
    head_frame.pack(fill=X)

    main_head = Label(head_frame, text="Sameer Poultry Farms", font="algerian 40 bold", bg="lavender")
    main_head.pack(fill=X)

    add_head = Label(head_frame, text="Exporter Search (AUTO) ",
                     font="Ariel 15 bold", bg="lavender")
    add_head.pack(fill=X)

    # Creating Frame for exporter search
    search_frame = Frame(root, bg='lavender', relief='solid', borderwidth=3)
    search_frame.pack(fill=X, pady=5)

    # Making labels
    date_label = Label(search_frame, text="Date :- ", font="Ariel 15 ", bg="lavender")
    expo_label = Label(search_frame, text="Exporter Name :- ", font="Ariel 15 ", bg="lavender")
    total_fare_label = Label(search_frame, text="Fare :- ", font="Ariel 15 ", bg="lavender")

    # Packing Labels
    date_label.grid(row=1, column=1, pady=7, padx=20)
    expo_label.grid(row=1, column=3, pady=7, padx=20)
    total_fare_label.grid(row=1, column=5, pady=7, padx=20)

    # Defining Variables for Entry
    date_value = StringVar()
    expo_value = StringVar()
    total_fare_value = StringVar()

    # Making Entry Widgets
    date_entry = Entry(search_frame, textvariable=date_value, font="Ariel 15 ")
    expo_entry = Entry(search_frame, textvariable=expo_value, font="Ariel 15 ")
    total_fare_entry = Entry(search_frame, textvariable=total_fare_value, font="Ariel 15 ")

    # Packing Entry Widgets
    date_entry.grid(row=1, column=2, pady=7, padx=20)
    expo_entry.grid(row=1, column=4, pady=7, padx=20)
    total_fare_entry.grid(row=1, column=6, pady=7, padx=20)

    # Making button for Search
    search_button = Button(search_frame, text="SEARCH", font="Ariel 13 ", bg="lavender",
                           relief='solid', padx=50, command=search)
    search_button.grid(row=2, column=2, pady=5)

    # Making Calc button
    calc_button = Button(search_frame, text="F.A.Calc", font="Ariel 13 ", bg="lavender",
                         relief='solid', padx=50, command=fa_calc)
    calc_button.grid(row=2, column=3, pady=5)

    # Making Save button
    save_button = Button(search_frame, text="SAVE", font="Ariel 13 ", bg="lavender",
                         relief='solid', padx=50, command=save)
    save_button.grid(row=2, column=4, pady=5)

    # Making Clear button
    clear_button = Button(search_frame, text="CLEAR", font="Ariel 13 ", bg="lavender",
                          relief='solid', padx=50, command=clear)
    clear_button.grid(row=2, column=5, pady=5)

    # Making Table frame
    table_frame = Frame(root)
    table_frame.pack()

    mainloop()
