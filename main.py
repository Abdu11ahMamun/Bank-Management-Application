import datetime
import mysql.connector

dbConn = mysql.connector.connect(host='localhost', user='root', password='', database='BANK_MANAGEMENT')

def openAcc():
    name = input("Enter customer name: ")
    account = input("Enter customer account number: ")
    DOB = input("Enter customer Date of Birth (YYYY-MM-DD): ")
    address = input("Enter customer address: ")
    contact = input("Enter customer contact: ")
    openBalance = int(input("Enter customer open balance: "))
    
    data1 = (name, account, DOB, address, contact, openBalance)
    data2 = (name, account, openBalance)
   
    sql_query1 = 'INSERT INTO ACCOUNT (name, accNo, DOB, address, contactNo, openingBal) VALUES(%s, %s, %s, %s, %s, %s)'
    sql_query2 = 'INSERT INTO Amount (name, accNo, balance) VALUES(%s, %s, %s)'
    x = dbConn.cursor()
    x.execute(sql_query1, data1)
    x.execute(sql_query2, data2)
    dbConn.commit()
    print("Data Entered Successfully")

def depoAmount():
    amount = input("Enter the amount you want to deposit: ")
    account = input("Enter customer account number: ")
    
    # Select the current balance
    select_query = 'SELECT balance FROM amount WHERE AccNo = %s'
    data = (account,)
    
    x = dbConn.cursor()
    x.execute(select_query, data)
    
    # Fetch the current balance
    result = x.fetchone()
    
    if result is not None:
        current_balance = result[0]
        
        # Calculate the new balance
        new_balance = current_balance + int(amount)
        
        # Update the balance in the database
        update_query = 'UPDATE amount SET balance = %s WHERE AccNo = %s'
        data1 = (new_balance, account)
        
        x.execute(update_query, data1)
        dbConn.commit()
        print("Amount deposited successfully.")
    else:
        print("Account not found or balance not available.")

    
def withdrawAmount():
    amount = input("Enter the amount you want to withdraw: ")
    account = input("Enter customer account number: ")
    
    # Select the current balance
    select_query = 'SELECT balance FROM Amount WHERE accNo = %s'
    data = (account,)
    
    x = dbConn.cursor()
    x.execute(select_query, data)
    
    # Fetch the current balance
    result = x.fetchone()
    
    if result is not None:
        current_balance = result[0]
        
        if current_balance >= int(amount):
            # Calculate the new balance
            new_balance = current_balance - int(amount)
        
            # Update the balance in the database
            update_query = 'UPDATE Amount SET balance = %s WHERE accNo = %s'
            data1 = (new_balance, account)
        
            x.execute(update_query, data1)
            dbConn.commit()
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found or balance not available.")

def balanceEnquiry():
     account = input("Enter customer account number: ")
     select_query = 'SELECT balance FROM amount WHERE AccNo = %s'
     data = (account,)
     x = dbConn.cursor()
     x.execute(select_query, data)
     # Fetch the current balance
     result = x.fetchone()
    
     if result is not None:
         current_balance = result[0]
         print("Balance: %s" % current_balance)
     else:
         print("Account not found or balance not available.")

def displayCustomer():
    account = input("Enter customer account number: ")
    
    # Select customer details
    select_query = 'SELECT * FROM ACCOUNT WHERE accNo = %s'
    data = (account,)
    
    x = dbConn.cursor()
    x.execute(select_query, data)
    
    # Fetch the customer details
    result = x.fetchone()
    
    if result is not None:
        print("Customer Details:")
        print("Name:", result[1])
        print("Account Number:", result[2])
        print("Date of Birth:", result[3])
        print("Address:", result[4])
        print("Contact Number:", result[5])
        print("Opening Balance:", result[6])
    else:
        print("Account not found.")



def closeAccount():
     account = input("Enter customer account number: ")
     select_query = 'SELECT * FROM ACCOUNT WHERE AccNo = %s'
     data = (account,)
     x = dbConn.cursor()
     x.execute(select_query, data)
     # Fetch the current balance
     result = x.fetchone()
    
     if result is not None:
         delete_query = 'DELETE FROM ACCOUNT WHERE AccNo = %s'
         data = (account,)
         x = dbConn.cursor()
         x.execute(delete_query,data)
         dbConn.commit()
         print("Account deleted successfully.")
         
     else:
         print("Account not found.")

def main():
    print('''
          1. Open New Account
          2. Deposit amount
          3. Withdraw amount
          4. Balance Enquiry 
          5. Display Customer details
          6. Close an account
          ''')
    
    choices = input("Enter the task you want to perform: ")
    if choices == "1":
        openAcc()
    elif choices == "2":
        depoAmount()
    elif choices == "3":
        withdrawAmount()
    elif choices == "4":
        balanceEnquiry()
    elif choices == "5":
        displayCustomer()
    elif choices == "6":
        closeAccount()
    else:
        print("Invalid choice")

main()
