import mysql.connector

dbConn = mysql.connector.connect(host='localhost', user='root', password='', database='BANK_MANAGEMENT')

def openAcc():
    name = input("Enter customer name: ")
    account = input("Enter customer account number: ")
    DOB = input("Enter customer Date of Birth: ")
    address = input("Enter customer address: ")
    contact = int(input("Enter customer contact: "))  # Convert to an integer
    openBalance = int(input("Enter customer open balance: "))
    data1 = (name, account, DOB, address, contact, openBalance)
    data2 = (name, account, openBalance)
    sql_query1 = 'INSERT INTO ACCOUNT VALUES(%s, %s, %s, %s, %s, %s)'
    sql_query2 = 'INSERT INTO Amount VALUES(%s, %s, %s)'
    x = dbConn.cursor()
    x.execute(sql_query1, data1)
    x.execute(sql_query2, data2)
    dbConn.commit()
    print("Data Entered Successfully")

def despoAmount():

    return None

def withAmount():
  
    return None

def balanceEnquiry():
   
    return None

def displayCustomer():
  
    return None

def closeAccount():
   
    return None

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
        despoAmount()
    elif choices == "3":
        withAmount()
    elif choices == "4":
        balanceEnquiry()
    elif choices == "5":
        displayCustomer()
    elif choices == "6":
        closeAccount()
    else:
        print("Invalid choice")

main()
