from tkinter import *

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
fare_label = Label(search_frame, text="Fare :- ", font="Ariel 15 ", bg="lavender")

# Packing Labels
date_label.grid(row=1, column=1, pady=7, padx=20)
expo_label.grid(row=1, column=3, pady=7, padx=20)
fare_label.grid(row=1, column=5, pady=7, padx=20)

# Defining Variables for Entry
date_value = StringVar()
expo_value = StringVar()
fare_value = StringVar()

# Making Entry Widgets
date_entry = Entry(search_frame, textvariable=date_label, font="Ariel 15 ")
expo_entry = Entry(search_frame, textvariable=expo_label, font="Ariel 15 ")
fare_entry = Entry(search_frame, textvariable=fare_label, font="Ariel 15 ")

# Packing Entry Widgets
date_entry.grid(row=1, column=2, pady=7, padx=20)
expo_entry.grid(row=1, column=4, pady=7, padx=20)
fare_entry.grid(row=1, column=6, pady=7, padx=20)

# Making button for Search
search_button = Button(search_frame, text="SEARCH", font="Ariel 13 ", bg="lavender",
                       relief='solid', padx=50)
search_button.grid(row=2, column=2, pady=5)

# Making Calc button
calc_button = Button(search_frame, text="F.A.Calc", font="Ariel 13 ", bg="lavender",
                     relief='solid', padx=50)
calc_button.grid(row=2, column=3, pady=5)

# Making Save button
save_button = Button(search_frame, text="SAVE", font="Ariel 13 ", bg="lavender",
                     relief='solid', padx=50)
save_button.grid(row=2, column=4, pady=5)

# Making Clear button
clear_button = Button(search_frame, text="CLEAR", font="Ariel 13 ", bg="lavender",
                      relief='solid', padx=50)
clear_button.grid(row=2, column=5, pady=5)

# Making Table frame
table_frame = Frame(root, bg='lavender', relief='solid', borderwidth=3)
table_frame.pack()

# Making labels of main row
bill_label = Label(table_frame, text="Bill No.", font="Ariel 15 ", bg="lavender", relief="solid",
                   borderwidth=1, padx=27)
cust_name_label = Label(table_frame, text="Customer Name", font="Ariel 15 ", bg="lavender", relief="solid",
                        borderwidth=1, padx=27)
w1_label = Label(table_frame, text="Weight 1", font="Ariel 15 ", bg="lavender", relief="solid",
                 borderwidth=1, padx=27)
w2_label = Label(table_frame, text="Weight 2", font="Ariel 15 ", bg="lavender", relief="solid",
                 borderwidth=1, padx=27)
w3_label = Label(table_frame, text="Weight 3", font="Ariel 15 ", bg="lavender", relief="solid",
                 borderwidth=1, padx=27)
w4_label = Label(table_frame, text="Weight 4", font="Ariel 15 ", bg="lavender", relief="solid",
                 borderwidth=1, padx=27)
total_label = Label(table_frame, text="Total", font="Ariel 15 ", bg="lavender", relief="solid",
                    borderwidth=1, padx=27)
received_label = Label(table_frame, text="Received", font="Ariel 15 ", bg="lavender",
                       relief="solid", borderwidth=1, padx=27)
fare_label = Label(table_frame, text="Fare", font="Ariel 15 ", bg="lavender", relief="solid",
                   borderwidth=1, padx=27)
due_label = Label(table_frame, text="Due", font="Ariel 15 ", bg="lavender", relief="solid",
                  borderwidth=1, padx=27)

# Packing labels
bill_label.grid(row=1, column=1)
cust_name_label.grid(row=1, column=2)
w1_label.grid(row=1, column=3)
w2_label.grid(row=1, column=4)
w3_label.grid(row=1, column=5)
w4_label.grid(row=1, column=6)
total_label.grid(row=1, column=7)
received_label.grid(row=1, column=8)
fare_label.grid(row=1, column=9)
due_label.grid(row=1, column=10)

mainloop()
