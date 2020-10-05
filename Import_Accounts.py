from tkinter import *

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
date_input_label = Label(input_frame, text="Date :-", font="ariel 12", bg="lavender")
m_weight_input_label = Label(input_frame, text="Mean Weight :-", font="ariel 12", bg="lavender")
owner_id_input_label = Label(input_frame, text="Owner ID :-", font="ariel 12", bg="lavender")
owner_name_input_label = Label(input_frame, text="Owner Name :-", font="ariel 12", bg="lavender")
quantity_input_label = Label(input_frame, text="Quantity :-", font="ariel 12", bg="lavender")
rate_input_label = Label(input_frame, text="Rate :-", font="ariel 12", bg="lavender")
weight_input_label = Label(input_frame, text="Weight :-", font="ariel 12", bg="lavender")
amount_input_label = Label(input_frame, text="Amount :-", font="ariel 12", bg="lavender")

# Packing input labels
date_input_label.grid(row=1, column=1, padx=10, pady=10)
m_weight_input_label.grid(row=1, column=3, padx=10, pady=10)
owner_id_input_label.grid(row=1, column=5, padx=10, pady=10)
owner_name_input_label.grid(row=1, column=7, padx=10, pady=10)
quantity_input_label.grid(row=2, column=1, padx=10, pady=10)
rate_input_label.grid(row=2, column=3, padx=10, pady=10)
weight_input_label.grid(row=2, column=5, padx=10, pady=10)
amount_input_label.grid(row=2, column=7, padx=10, pady=10)

# Defining input variables
date_value = StringVar()
m_weight_value = StringVar()
owner_id_value = StringVar()
owner_name_value = StringVar()
quantity_value = StringVar()
rate_value = StringVar()
weight_value = StringVar()
amount_value = StringVar()

# Making Entry Label
date_enter = Entry(input_frame, textvariable=date_value, font="ariel 12", bg="floral white")
m_weight_enter = Entry(input_frame, textvariable=m_weight_value, font="ariel 12", bg="floral white")
owner_id_enter = Entry(input_frame, textvariable=owner_id_value, font="ariel 12", bg="floral white")
owner_name_enter = Entry(input_frame, textvariable=owner_name_value, font="ariel 12", bg="floral white")
quantity_enter = Entry(input_frame, textvariable=quantity_value, font="ariel 12", bg="floral white")
rate_enter = Entry(input_frame, textvariable=rate_value, font="ariel 12", bg="floral white")
weight_enter = Entry(input_frame, textvariable=weight_value, font="ariel 12", bg="floral white")
amount_enter = Entry(input_frame, textvariable=amount_value, font="ariel 12", bg="floral white")

# Packing Entry Widget
date_enter.grid(row=1, column=2, padx=10, pady=10)
m_weight_enter.grid(row=1, column=4, padx=10, pady=10)
owner_id_enter.grid(row=1, column=6, padx=10, pady=10)
owner_name_enter.grid(row=1, column=8, padx=10, pady=10)
quantity_enter.grid(row=2, column=2, padx=10, pady=10)
rate_enter.grid(row=2, column=4, padx=10, pady=10)
weight_enter.grid(row=2, column=6, padx=10, pady=10)
amount_enter.grid(row=2, column=8, padx=10, pady=10)

# Making Output frame
output_frame = Frame(root, bg='lavender')
output_frame.pack(fill=X)

# Save Button
save_button = Button(output_frame, text="Save Data", font="Ariel 15", bg="floral white")
save_button.pack(pady=20)

# List box
scrollbar = Scrollbar(output_frame)
scrollbar.pack(side=RIGHT, fill=Y)
output_listbox = Listbox(output_frame, yscrollcommand=scrollbar, height=12, font=("Ariel", 15), bg="floral white")
output_listbox.pack(fill=X, padx=10, pady=10)
scrollbar.config(command=output_listbox.yview)

mainloop()
