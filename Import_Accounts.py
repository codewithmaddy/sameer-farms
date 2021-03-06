from tkinter import *
import mysql.connector
import datetime


my_db = mysql.connector.connect(host="localhost", user="root", password="root123",
                                auth_plugin="mysql_native_password", database="SAMEER_FARMS")

my_cursor = my_db.cursor()


def calc():
    amount = float(rate_value.get())*float(weight_value.get())
    amount_value.set(f"{amount}")


def clear():
    date = f"{datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}"
    owner_id_value.set("")
    owner_name_value.set("")
    m_weight_value.set("")
    date_value.set(f"{date}")
    quantity_value.set("")
    weight_value.set("")
    rate_value.set("")
    amount_value.set("")
    root.update()


def save():
    d, m, y = map(int, (date_value.get()).split('/'))
    date = datetime.date(y, m, d)
    my_cursor.execute("INSERT INTO `sameer_farms`.`import` (`owner_id`, `owner_name`, `mean_weight`, `date`, "
                      "`quantity`, `rate`, `weight`, `amount`, `left`) VALUES "
                      f"('{owner_id_value.get()}', '{owner_name_value.get()}', {float(m_weight_value.get())}, "
                      f"'{date}', {float(quantity_value.get())}, {float(rate_value.get())}, "
                      f"{float(weight_value.get())}, {float(amount_value.get())}, {float(weight_value.get())});")
    my_db.commit()


root = Tk()

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

accounts = Label(sub_head_frame, text="IMPORT Accounts ", font="Ariel 30 bold", bg="lavender")
accounts.pack(fill=X, pady=20)

# Input frame
input_frame = Frame(root, bg='lavender')
input_frame.pack(fill=X)

# Making input labels
owner_id_input_label = Label(input_frame, text="Owner ID :-", font="ariel 12", bg="lavender")
owner_name_input_label = Label(input_frame, text="Owner Name :-", font="ariel 12", bg="lavender")
m_weight_input_label = Label(input_frame, text="Mean Weight :-", font="ariel 12", bg="lavender")
date_input_label = Label(input_frame, text="Date :-", font="ariel 12", bg="lavender")
quantity_input_label = Label(input_frame, text="Quantity :-", font="ariel 12", bg="lavender")
rate_input_label = Label(input_frame, text="Rate :-", font="ariel 12", bg="lavender")
weight_input_label = Label(input_frame, text="Weight :-", font="ariel 12", bg="lavender")
amount_input_label = Label(input_frame, text="Amount :-", font="ariel 12", bg="lavender")

# Packing input labels
owner_id_input_label.grid(row=1, column=1, padx=10, pady=10)
owner_name_input_label.grid(row=1, column=3, padx=10, pady=10)
m_weight_input_label.grid(row=1, column=5, padx=10, pady=10)
date_input_label.grid(row=1, column=7, padx=10, pady=10)
quantity_input_label.grid(row=2, column=1, padx=10, pady=10)
rate_input_label.grid(row=2, column=3, padx=10, pady=10)
weight_input_label.grid(row=2, column=5, padx=10, pady=10)
amount_input_label.grid(row=2, column=7, padx=10, pady=10)

# Defining input variables
owner_id_value = StringVar()
owner_name_value = StringVar()
m_weight_value = StringVar()
date_value = StringVar()
quantity_value = StringVar()
rate_value = StringVar()
weight_value = StringVar()
amount_value = StringVar()

# Making Entry Label
owner_id_enter = Entry(input_frame, textvariable=owner_id_value, font="ariel 12", bg="floral white")
owner_name_enter = Entry(input_frame, textvariable=owner_name_value, font="ariel 12", bg="floral white")
m_weight_enter = Entry(input_frame, textvariable=m_weight_value, font="ariel 12", bg="floral white")
date_enter = Entry(input_frame, textvariable=date_value, font="ariel 12", bg="floral white")
quantity_enter = Entry(input_frame, textvariable=quantity_value, font="ariel 12", bg="floral white")
rate_enter = Entry(input_frame, textvariable=rate_value, font="ariel 12", bg="floral white")
weight_enter = Entry(input_frame, textvariable=weight_value, font="ariel 12", bg="floral white")
amount_enter = Entry(input_frame, textvariable=amount_value, font="ariel 12", bg="floral white")

# Packing Entry Widget
owner_id_enter.grid(row=1, column=2, padx=10, pady=10)
owner_name_enter.grid(row=1, column=4, padx=10, pady=10)
m_weight_enter.grid(row=1, column=6, padx=10, pady=10)
date_enter.grid(row=1, column=8, padx=10, pady=10)
quantity_enter.grid(row=2, column=2, padx=10, pady=10)
rate_enter.grid(row=2, column=4, padx=10, pady=10)
weight_enter.grid(row=2, column=6, padx=10, pady=10)
amount_enter.grid(row=2, column=8, padx=10, pady=10)
clear()

# Making Output frame
output_frame = Frame(root, bg='lavender')
output_frame.pack(fill=X)

# Calculate Button
calc_button = Button(output_frame, text="Calculate", font="Ariel 15", bg="floral white", command=calc)
calc_button.pack(pady=10)

# Save Button
save_button = Button(output_frame, text="Save Data", font="Ariel 15", bg="floral white", command=save)
save_button.pack(pady=10)

# Clear Button
clear_button = Button(output_frame, text="Clear Data", font="Ariel 15", bg="floral white", command=clear)
clear_button.pack(pady=10)
mainloop()
