def main():
    print('''
          1. Open New Account
          2. Deposite amount
          3. Withdraw amount
          4. Balance Enquiry 
          5. Display Customer details
          6. Close an account
          ''')
    
    choices = input("Enter the task you want to perform ")
    if(choices=="1"):
        openAcc()
    elif(choices=="2"):
        despoAmount()
    elif(choices=="3"):
        withdrawAmount()
    elif(choices=="4"):
        balanceEnquiry()
    elif(choices=="5"):
        displayCustomer()
    elif(choices=="6"):
        closeAccount()
    else:
        print("Invalid choice")

main()
