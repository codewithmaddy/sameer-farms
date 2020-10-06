from tkinter import *
import mysql.connector
import datetime

my_db = mysql.connector.connect(host="localhost", user="root", password="root123",
                                auth_plugin="mysql_native_password", database="test")

my_cursor = my_db.cursor()


def clear():
    date = f"{datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}"
    customer_name_value.set("")
    exporter_name_value.set("")
    received_by_value.set("")
    date_value.set(date)
    owner1_value.set("")
    quantity1_value.set("0")
    weight1_value.set("0")
    rate1_value.set("0")
    amount1_value.set("0")
    owner2_value.set("")
    quantity2_value.set("0")
    weight2_value.set("0")
    rate2_value.set("0")
    amount2_value.set("0")
    owner3_value.set("")
    quantity3_value.set("0")
    weight3_value.set("0")
    rate3_value.set("0")
    amount3_value.set("0")
    owner4_value.set("")
    quantity4_value.set("0")
    weight4_value.set("0")
    rate4_value.set("0")
    amount4_value.set("0")
    owner5_value.set("")
    quantity5_value.set("0")
    weight5_value.set("0")
    rate5_value.set("0")
    amount5_value.set("0")
    total_value.set("0")
    fare_value.set("0")
    received_value.set("0")
    due_value.set("0")

    root.update()


def save():
    d, m, y = map(int, (date_value.get()).split('/'))
    date = datetime.date(y, m, d)
    my_cursor.execute("INSERT INTO `sameer_farms`.`export` (`bill_no`, `cust_name`, `expo_name`, `paid_to`, `date`, "
                      "`owner_id_1`, `quantity_1`, `weight_1`, `rate_1`, `amount_1`,"
                      " `owner_id_2`, `quantity_2`, `weight_2`, `rate_2`, `amount_2`,"
                      " `owner_id_3`, `quantity_3`, `weight_3`, `rate_3`, `amount_3`,"
                      " `owner_id_4`, `quantity_4`, `weight_4`, `rate_4`, `amount_4`,"
                      " `owner_id_5`, `quantity_5`, `weight_5`, `rate_5`, `amount_5`,"
                      " `total`, `fare`, `received`, `due`)"
                      f" VALUES ({int(bill_value.get())}, '{customer_name_value.get()}', '{exporter_name_value.get()}',"
                      f" '{received_by_value.get()}', '{date}',"
                      f" '{owner1_value.get()}', {int(quantity1_value.get())}, {float(weight1_value.get())}, "
                      f" {float(rate1_value.get())}, {float(amount1_value.get())},"
                      f" '{owner2_value.get()}', {int(quantity2_value.get())}, {float(weight2_value.get())}, "
                      f"{float(rate2_value.get())}, {float(amount2_value.get())}, "
                      f"'{owner3_value.get()}', {int(quantity3_value.get())}, {float(weight3_value.get())}, "
                      f"{float(rate3_value.get())}, {float(amount3_value.get())},"
                      f" '{owner4_value.get()}', {int(quantity4_value.get())}, {float(weight4_value.get())}, "
                      f"{float(rate4_value.get())}, {float(amount4_entry.get())},"
                      f" '{owner5_value.get()}', {int(quantity5_value.get())}, {float(weight5_value.get())}, "
                      f"{float(rate5_value.get())}, {float(amount5_value.get())},"
                      f" {float(total_value.get())}, {float(fare_value.get())}, {float(received_value.get())}, "
                      f"{float(due_value.get())});")
    my_db.commit()
    b_num = int(bill_value.get()) + 1
    bill_value.set(b_num)
    root.update()


def calculate():
    amount1_value.set(f"{float(weight1_value.get()) * float(rate1_value.get())}")
    amount2_value.set(f"{float(weight2_value.get()) * float(rate2_value.get())}")
    amount3_value.set(f"{float(weight3_value.get()) * float(rate3_value.get())}")
    amount4_value.set(f"{float(weight4_value.get()) * float(rate4_value.get())}")
    amount5_value.set(f"{float(weight5_value.get()) * float(rate5_value.get())}")
    root.update()
    total = float(amount1_value.get()) + float(amount2_value.get()) + float(amount3_value.get())
    total = total + float(amount4_value.get()) + float(amount5_value.get())
    total_value.set(total)
    root.update()


def search():
    pass


def edit():
    d, m, y = map(int, (date_value.get()).split('/'))
    date = datetime.date(y, m, d)
    my_cursor.execute("UPDATE `sameer_farms`.`export` SET"
                      f" `bill_no` = {int(bill_value.get())}, `cust_name` = '{customer_name_value.get()}', "
                      f"`expo_name` = '{exporter_name_value.get()}', `paid_to` = '{received_by_value.get()}', "
                      f"`date` = '{date}', "
                      f"`owner_id_1` = '{owner1_value.get()}', `quantity_1` = {int(quantity1_value.get())}, "
                      f"`weight_1` = {float(weight1_value.get())}, `rate_1` = {float(rate1_value.get())}, "
                      f"`amount_1` = {float(amount1_value.get())}, "
                      f"`owner_id_2` = '{owner2_value.get()}', `quantity_2` = {int(quantity2_value.get())}, "
                      f"`weight_2` = {float(weight2_value.get())}, `rate_2` = {float(weight2_value.get())}, "
                      f"`amount_2` = {float(amount2_value.get())}, "
                      f"`owner_id_3` = '{owner3_value.get()}', `quantity_3` = {int(quantity3_value.get())}, "
                      f"`weight_3` = {float(weight3_value.get())}, `rate_3` = {float(rate3_value.get())}, "
                      f"`amount_3` = {float(amount3_value.get())}, "
                      f"`owner_id_4` = '{owner4_value.get()}', `quantity_4` = {int(quantity4_value.get())}, "
                      f"`weight_4` = {float(weight4_value.get())}, `rate_4` = {float(rate4_value.get())}, "
                      f"`amount_4` = {float(amount5_value.get())}, "
                      f"`owner_id_5` = '{owner5_value.get()}', `quantity_5` = {int(quantity5_value.get())}, "
                      f"`weight_5` = {float(weight5_value.get())}, `rate_5` = {float(rate5_value.get())}, "
                      f"`amount_5` = {float(amount5_value.get())}, "
                      f"`total` = {float(total_value.get())}, `fare` = {float(fare_value.get())}, "
                      f"`received` = {float(received_value.get())}, `due` = {float(due_value.get())} "
                      f"WHERE (`bill_no` = {int(bill_value.get())});")
    my_db.commit()


if __name__ == '__main__':

    root = Tk()

    font_entry = "ariel 10"
    font_1 = "ariel 18"

    root.geometry("1200x600")
    root.title("Import Accounts ")

    # Making Heading Frame
    head_frame = Frame(root, bg='lavender', relief='solid', borderwidth=3)
    head_frame.pack(fill=X)

    Main_head = Label(head_frame, text="Sameer Poultry Farms", font="algerian 40 bold", bg="lavender")
    Main_head.pack(fill=X)

    add_head = Label(head_frame, text="Industrial area, ludhawali shivpuri (MP) - 473551 ",
                     font="Ariel 15 bold", bg="lavender")
    add_head.pack(fill=X)

    # Making Sub-Heading Frame
    sub_head_frame = Frame(root, bg='lavender')
    sub_head_frame.pack(fill=X)

    accounts = Label(sub_head_frame, text="Export Accounts ", font="Ariel 30 bold", bg="lavender")
    accounts.pack(fill=X, pady=20)

    # Making Name frame
    name_frame = Frame(root, bg='lavender', relief='solid', borderwidth=3, padx=10, pady=10)
    name_frame.pack(fill=X)

    # Defining Name frame labels
    bill_label = Label(name_frame, text="Bill no. :- ", font="Ariel 11 ", bg="lavender")
    customer_name_label = Label(name_frame, text="Customer Name :- ", font="Ariel 11 ", bg="lavender")
    exporter_name_label = Label(name_frame, text="Exporter Name :- ", font="Ariel 11 ", bg="lavender")
    received_by_label = Label(name_frame, text="Received by :-", font="Ariel 11 ", bg="lavender")
    date_label = Label(name_frame, text="Date :- ", font="Ariel 11 ", bg="lavender")

    # Packing Labels of name frame
    bill_label.grid(row=1, column=1, pady=10)
    customer_name_label.grid(row=1, column=3, pady=10)
    exporter_name_label.grid(row=1, column=5, pady=10)
    received_by_label.grid(row=1, column=7, pady=10)
    date_label.grid(row=1, column=9, pady=10)

    # Making Entry Variables
    bill_value = StringVar()
    customer_name_value = StringVar()
    exporter_name_value = StringVar()
    received_by_value = StringVar()
    date_value = StringVar()

    # Making Entry Widget for name frame
    bill_entry = Entry(name_frame, textvariable=bill_value, font="Ariel 11", bg="floral white")
    customer_name_entry = Entry(name_frame, textvariable=customer_name_value, font="Ariel 11", bg="floral white")
    exporter_name_entry = Entry(name_frame, textvariable=exporter_name_value, font="Ariel 11", bg="floral white")
    received_by_entry = Entry(name_frame, textvariable=received_by_value, font="Ariel 10", bg="floral white")
    date_entry = Entry(name_frame, textvariable=date_value, font="Ariel 10", bg="floral white")

    # Packing Entry Widget of name frame
    bill_entry.grid(row=1, column=2)
    customer_name_entry.grid(row=1, column=4)
    exporter_name_entry.grid(row=1, column=6)
    received_by_entry.grid(row=1, column=8)
    date_entry.grid(row=1, column=10)

    # Making Input Frame
    input_frame = Frame(root, bg='lavender')
    input_frame.pack(fill=X)

    # making Input labels
    owner_label = Label(input_frame, text="Owner ID", font=font_1, bg="lavender",
                        relief='solid', borderwidth=2, padx=80, pady=10)
    quantity_label = Label(input_frame, text="Quantity", font=font_1, bg="lavender",
                           relief='solid', borderwidth=2, padx=80, pady=10)
    weight_label = Label(input_frame, text=" Weight ", font=font_1, bg="lavender",
                         relief='solid', borderwidth=2, padx=80, pady=10)
    rate_label = Label(input_frame, text="  Rate   ", font=font_1, bg="lavender",
                       relief='solid', borderwidth=2, padx=80, pady=10)
    amount_label = Label(input_frame, text=" Amount ", font=font_1, bg="lavender",
                         relief='solid', borderwidth=2, padx=80, pady=10)

    # Packing Input Labels
    owner_label.grid(row=1, column=1)
    quantity_label.grid(row=1, column=2)
    weight_label.grid(row=1, column=3)
    rate_label.grid(row=1, column=4)
    amount_label.grid(row=1, column=5)

    # Defining Variable for input frame
    owner1_value = StringVar()
    quantity1_value = StringVar()
    weight1_value = StringVar()
    rate1_value = StringVar()
    amount1_value = StringVar()
    owner2_value = StringVar()
    quantity2_value = StringVar()
    weight2_value = StringVar()
    rate2_value = StringVar()
    amount2_value = StringVar()
    owner3_value = StringVar()
    quantity3_value = StringVar()
    weight3_value = StringVar()
    rate3_value = StringVar()
    amount3_value = StringVar()
    owner4_value = StringVar()
    quantity4_value = StringVar()
    weight4_value = StringVar()
    rate4_value = StringVar()
    amount4_value = StringVar()
    owner5_value = StringVar()
    quantity5_value = StringVar()
    weight5_value = StringVar()
    rate5_value = StringVar()
    amount5_value = StringVar()

    # Defining Entry Widget for input
    owner1_entry = Entry(input_frame, textvariable=owner1_value, font=font_entry, bg="white",
                         relief='solid', borderwidth=1)
    quantity1_entry = Entry(input_frame, textvariable=quantity1_value, font=font_entry, bg="white",
                            relief='solid', borderwidth=1)
    weight1_entry = Entry(input_frame, textvariable=weight1_value, font=font_entry, bg="white",
                          relief='solid', borderwidth=1)
    rate1_entry = Entry(input_frame, textvariable=rate1_value, font=font_entry, bg="white",
                        relief='solid', borderwidth=1)
    amount1_entry = Entry(input_frame, textvariable=amount1_value, font=font_entry, bg="white",
                          relief='solid', borderwidth=1)
    owner2_entry = Entry(input_frame, textvariable=owner2_value, font=font_entry, bg="white",
                         relief='solid', borderwidth=1)
    quantity2_entry = Entry(input_frame, textvariable=quantity2_value, font=font_entry, bg="white",
                            relief='solid', borderwidth=1)
    weight2_entry = Entry(input_frame, textvariable=weight2_value, font=font_entry, bg="white",
                          relief='solid', borderwidth=1)
    rate2_entry = Entry(input_frame, textvariable=rate2_value, font=font_entry, bg="white",
                        relief='solid', borderwidth=1)
    amount2_entry = Entry(input_frame, textvariable=amount2_value, font=font_entry, bg="white",
                          relief='solid', borderwidth=1)
    owner3_entry = Entry(input_frame, textvariable=owner3_value, font=font_entry, bg="white",
                         relief='solid', borderwidth=1)
    quantity3_entry = Entry(input_frame, textvariable=quantity3_value, font=font_entry, bg="white",
                            relief='solid', borderwidth=1)
    weight3_entry = Entry(input_frame, textvariable=weight3_value, font=font_entry, bg="white",
                          relief='solid', borderwidth=1)
    rate3_entry = Entry(input_frame, textvariable=rate3_value, font=font_entry, bg="white",
                        relief='solid', borderwidth=1)
    amount3_entry = Entry(input_frame, textvariable=amount3_value, font=font_entry, bg="white",
                          relief='solid', borderwidth=1)
    owner4_entry = Entry(input_frame, textvariable=owner4_value, font=font_entry, bg="white",
                         relief='solid', borderwidth=1)
    quantity4_entry = Entry(input_frame, textvariable=quantity4_value, font=font_entry, bg="white",
                            relief='solid', borderwidth=1)
    weight4_entry = Entry(input_frame, textvariable=weight4_value, font=font_entry, bg="white",
                          relief='solid', borderwidth=1)
    rate4_entry = Entry(input_frame, textvariable=rate4_value, font=font_entry, bg="white",
                        relief='solid', borderwidth=1)
    amount4_entry = Entry(input_frame, textvariable=amount4_value, font=font_entry, bg="white",
                          relief='solid', borderwidth=1)
    owner5_entry = Entry(input_frame, textvariable=owner5_value, font=font_entry, bg="white",
                         relief='solid', borderwidth=1)
    quantity5_entry = Entry(input_frame, textvariable=quantity5_value, font=font_entry, bg="white",
                            relief='solid', borderwidth=1)
    weight5_entry = Entry(input_frame, textvariable=weight5_value, font=font_entry, bg="white",
                          relief='solid', borderwidth=1)
    rate5_entry = Entry(input_frame, textvariable=rate5_value, font=font_entry, bg="white",
                        relief='solid', borderwidth=1)
    amount5_entry = Entry(input_frame, textvariable=amount5_value, font=font_entry, bg="white",
                          relief='solid', borderwidth=1)

    # Packing Entry Widget
    owner1_entry.grid(row=2, column=1, pady=10)
    quantity1_entry.grid(row=2, column=2, pady=10)
    weight1_entry.grid(row=2, column=3, pady=10)
    rate1_entry.grid(row=2, column=4, pady=10)
    amount1_entry.grid(row=2, column=5, pady=10)
    owner2_entry.grid(row=3, column=1, pady=10)
    quantity2_entry.grid(row=3, column=2, pady=10)
    weight2_entry.grid(row=3, column=3, pady=10)
    rate2_entry.grid(row=3, column=4, pady=10)
    amount2_entry.grid(row=3, column=5, pady=10)
    owner3_entry.grid(row=4, column=1, pady=10)
    quantity3_entry.grid(row=4, column=2, pady=10)
    weight3_entry.grid(row=4, column=3, pady=10)
    rate3_entry.grid(row=4, column=4, pady=10)
    amount3_entry.grid(row=4, column=5, pady=10)
    owner4_entry.grid(row=5, column=1, pady=10)
    quantity4_entry.grid(row=5, column=2, pady=10)
    weight4_entry.grid(row=5, column=3, pady=10)
    rate4_entry.grid(row=5, column=4, pady=10)
    amount4_entry.grid(row=5, column=5, pady=10)
    owner5_entry.grid(row=6, column=1, pady=10)
    quantity5_entry.grid(row=6, column=2, pady=10)
    weight5_entry.grid(row=6, column=3, pady=10)
    rate5_entry.grid(row=6, column=4, pady=10)
    amount5_entry.grid(row=6, column=5, pady=10)

    # Making Output Labels
    total_label = Label(input_frame, text="     Total :-     ", font=font_entry, bg="lavender",
                        relief='solid', borderwidth=2, padx=50)
    fare_label = Label(input_frame, text="     Fare :-      ", font=font_entry, bg="lavender",
                       relief='solid', borderwidth=2, padx=50)
    received_label = Label(input_frame, text="  Received :-   ", font=font_entry, bg="lavender",
                           relief='solid', borderwidth=2, padx=50)
    due_label = Label(input_frame, text="      Due :-      ", font=font_entry, bg="lavender",
                      relief='solid', borderwidth=2, padx=50)

    # Packing labels
    total_label.grid(row=7, column=4, pady=10)
    fare_label.grid(row=8, column=4, pady=10)
    received_label.grid(row=9, column=4, pady=10)
    due_label.grid(row=10, column=4, pady=10)

    # Defining Variables for Output
    total_value = StringVar()
    fare_value = StringVar()
    received_value = StringVar()
    due_value = StringVar()

    # Making Entry widget
    total_entry = Entry(input_frame, textvariable=total_value, font=font_entry, bg="white",
                        relief='solid', borderwidth=1)
    fare_entry = Entry(input_frame, textvariable=fare_value, font=font_entry, bg="white",
                       relief='solid', borderwidth=1)
    received_entry = Entry(input_frame, textvariable=received_value, font=font_entry, bg="white",
                           relief='solid', borderwidth=1)
    due_entry = Entry(input_frame, textvariable=due_value, font=font_entry, bg="white",
                      relief='solid', borderwidth=1)

    # Packing Entry Widget
    total_entry.grid(row=7, column=5)
    fare_entry.grid(row=8, column=5)
    received_entry.grid(row=9, column=5)
    due_entry.grid(row=10, column=5)

    # Creating Search button
    search_button = Button(input_frame, text="    Search    ", font=font_entry, bg="lavender",
                           relief='solid', borderwidth=1, padx=20, command=search)
    search_button.grid(row=7, column=1)

    # Creating Edit button
    edit_button = Button(input_frame, text="     Edit     ", font=font_entry, bg="lavender",
                         relief='solid', borderwidth=1, padx=20, command=edit)
    edit_button.grid(row=7, column=2)

    # Creating Calculate button
    calc_button = Button(input_frame, text="  Calculate  ", font=font_entry, bg="lavender",
                         relief='solid', borderwidth=1, padx=20, command=calculate)
    calc_button.grid(row=8, column=1)

    # Creating Button save
    save_button = Button(input_frame, text="    Save    ", font=font_entry, bg="lavender",
                         relief='solid', borderwidth=1, padx=20, command=save)
    save_button.grid(row=8, column=2)

    # Creating Button clear
    clear_button = Button(input_frame, text="    Clear    ", font=font_entry, bg="lavender",
                          relief='solid', borderwidth=1, padx=20, command=clear)
    clear_button.grid(row=8, column=3)

    clear()

    mainloop()
