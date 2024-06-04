import sqlite3
connect=sqlite3.connect('expenses.db')
cursor=connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Expenses(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               date TEXT,
               category TEXT,
               amount REAL,
               description TEXT

)''')


def Add_expense(date,category,amount,description):
    cursor.execute("INSERT INTO expenses (date,category,amount,description) VALUES(?,?,?,?)",(date,category,amount,description))
    connect.commit()
    print("add expense successfully")

def View_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses=cursor.fetchall()
    for x in expenses:
        print(x)

def Update_expense(expense_id,new_date,new_category,new_amount,new_description):
    cursor.execute("UPDATE expenses SET date = ?,category = ? ,amount = ?,description = ? WHERE id = ?",(new_date,new_category,new_amount,new_description,expense_id))
    connect.commit()
    print('your expense updated')


def Delete_expense(expense_id):
    cursor.execute("DELETE FROM expenses WHERE id = ?",(expense_id))
    connect.commit()
    print(" your expense removed")



while True :
    print(""" 
        1-add expense
        2-view expenses
        3-update expense
        4-remove expense
        5- exit      
        """)
    flag=int(input("please enter your choice:"))
    if flag==1:
        date=input("please enter date:")
        category=input("please enter category:")
        amount=float(input("please enter amount:"))
        description=input("please enter description:")
        Add_expense(date,category,amount,description)
    elif flag==2:
        View_expenses()

    elif flag==3:
        expense_id=int(input("please enter expense id:"))
        new_date=input("please enter new date:")
        new_category=input("please enter new category:")
        new_amount=float(input("please enter new amount:"))
        new_description=input("please enter new description:")
        Update_expense(expense_id,new_date,new_category,new_amount,new_description)
    elif flag==4:
        expense_id=int(input("please enter expense id:"))
        Delete_expense(expense_id)    
    elif flag==5:
            break
    else:
        print("option is invalid ,choice a valid option ")
connect.close()        