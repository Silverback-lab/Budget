from tkinter import *
import sqlite3


root = Tk()
root.title('Dataentry for budget')
root.geometry("550x500")

# Databases

# Create a databse or connect to one
conn = sqlite3.connect('budget.db')

# Create cursor
c = conn.cursor()

# Create Table(Commented out)

'''
c.execute("""CREATE TABLE Budgets (
        Date_Of_Transaction integer,
        label text,
        descriptionriton text,        
        amount integer
        )""")
'''

# create submitt function for database

def submit():
        # Create a databse or connect to one
        conn = sqlite3.connect('budget.db')
        # Create cursor
        c = conn.cursor()

        #insert into Table
        c.execute("INSERT INTO Budgets VALUES (:dot, :lab, :descriptio, :amount)", 
                {
                        'dot': dot.get(),
                        'lab': lab.get(),
                        'descriptio': descriptio.get(),
                        'amount': amount.get()
                })


        #commit Changes
        conn.commit()

        # Close Connection
        conn.close()


        #clear the text boxes
        dot.delete(0, END)
        lab.delete(0, END)
        descriptio.delete(0, END)        
        amount.delete(0, END)

# Create Query Function
def query():
         # Create a databse or connect to one
        conn = sqlite3.connect('budget.db')

        # Create cursor
        c = conn.cursor()

        #query the database
        c.execute("SELECT *, oid FROM Budgets")
        records = c.fetchall()
        # print(records)

        # Loop Thru Results
        print_records = ''
        for record in records:
                print_records += str(record) + "\n"

        query_label = Label(root, text=print_records)
        query_label.grid(row=13, column=1, columnspan=1)
        

        #commit Changes
        conn.commit()

        # Close Connection
        conn.close()

#Create Text button
dot = Label(root, text="Date of Transaction", font=('Hack', 12, 'bold', 'underline'))
dot.grid(row=0, column=0)
lab = Label(root, text="Catagagory", font=('Hack', 12, 'bold', 'underline'))
lab.grid(row=1, column=0)
descriptio = Label(root, text="description", font=('Hack', 12, 'bold', 'underline'))
descriptio.grid(row=2, column=0)
amount = Label(root, text="Cost of Transaction", font=('Hack', 12, 'bold', 'underline'))
amount.grid(row=3, column=0)

# Create text Box
dot = Entry(root, width=20)
dot.grid(row=0, column=1, padx=40)
lab = Entry(root, width=20)
lab.grid(row=1, column=1, padx=40)
descriptio = Entry(root, width=20)
descriptio.grid(row=2, column=1, padx=40)
amount = Entry(root, width=20)
amount.grid(row=3, column=1, padx=40)


#create Label list
label_legend = Label(root, text="Catagagory Legend", fg="Black", font=('Hack', 15, 'bold', 'underline'))
label_legend.grid(row=6, column=1, columnspan=1)
bill = Label(root, text="Bill", fg="Black", font=('Hack', 10))
bill.grid(row=7, column=0, columnspan=1)
credit = Label(root, text="Credit", fg="Black", font=('Hack', 10))
credit.grid(row=7, column=1, columnspan=1)
groceries = Label(root, text="Groceries", fg="Black", font=('Hack', 10))
groceries.grid(row=7, column=2, columnspan=1)
gas = Label(root, text="Gas", fg="Black", font=('Hack', 10))
gas.grid(row=8, column=0, columnspan=1)
date_night = Label(root, text="Date Night", fg="Black", font=('Hack', 10))
date_night.grid(row=8, column=1, columnspan=1)
tenley_fun = Label(root, text="Tenley Fun", fg="Black", font=('Hack', 10))
tenley_fun.grid(row=8, column=2, columnspan=1)
michael_fun = Label(root, text="Michael Fun", fg="Black", font=('Hack', 10))
michael_fun.grid(row=9, column=0, columnspan=1)
saving = Label(root, text="Savings", fg="Black", font=('Hack', 10))
saving.grid(row=9, column=1, columnspan=1)
necessities = Label(root, text="Necessities", fg="Black", font=('Hack', 10))
necessities.grid(row=9, column=2, columnspan=1)
pay_towards_debt= Label(root, text="Pay Towards debt", fg="Black", font=('Hack', 10))
pay_towards_debt.grid(row=10, column=0, columnspan=1)
no_label = Label(root, text="NO LABEL", fg="red", font=('Hack', 10))
no_label.grid(row=10, column=1, columnspan=1)

results = Label(root, text="History", fg="Black", font=('Hack', 12, 'bold', 'underline'))
results.grid(row=11, column=1, columnspan=1)



# create submit button

submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=4, column=0, columnspan=3, pady=10, padx=10, ipadx=72)


#create a query Button

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=5, column=0, columnspan=3, pady=10, padx=10, ipadx=100)


#commit Changes
conn.commit()

# Close Connection
conn.close()




root.mainloop()
