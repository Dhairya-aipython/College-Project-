import math
import random
print ('Welcome')
print ("Banking Simulation")
_rate=random.randint(5,10)
customer_accountnumber = int(input("Enter your account number : "))
balance=random.randint(100000,10000000)
lt=['RTGS','Saving Account','Deposit section','Withdrawl section','Balance check','Paying bills']
print (lt)
print ("Enter your choice from the given option of the list",end='')
ch=int(input("Enter you choice"))
print (lt[ch] if ch>=0 and ch<6 else "Wrong Input")
indexes_lt=[0,1,2,3,4,5]
if (ch==1):
    print ("Saving Account" )
    print ("Available Balance ",balance) 
    print (f"Your rate of Interest on your deposits ia {_rate}")
elif (ch==2):
    print ("Deposit section")
    d=int(input("Enter the amount you want to add in your bank account "))
    print ("Initial Balance",balance)
    print ("Deposit amount",d)
    balance = balance+d
    print ("The new balance of the bank account after the deposit = ",balance)
elif (ch==3):
    print ("Withdrawal section")
    withdrawal_amount=int(input("Enter the amount you want to withdraw from your bank account "))
    print (f"Initial Balance = {balance}")
    if (withdrawal_amount>balance):
        print ("Insufficient Balance")
    else:
        print ("Your Withdrawal is under Process" + 'Please wait')
        balance = balance-withdrawal_amount
        print ("The new Account Balance after the withdrawal of money is = ",balance)
elif (ch==4):
    print ("Balance check")
    print (f"Your Account Balance ={balance}")
elif (ch==5):
    print ("Enter the details of the person to whome you want to pay the bill")
    customer_details=input("Enter the name of that person ")
    print (f"Enter the account number of {customer_details} ")
    customer_accountnumber=int(input())
    bill=int(input("Enter the amount you want to pay : "))
    if (bill>balance):
        print ("Insufficient balance in your account for this payment")
        print ("You can either do the top up in your account or eitherly you can also take loan from us to process this payment")
        print ("Enter your Choice")
        print ("1 for top up or 2 for loan from the bank")
        choice=int(input())
        if (choice==1):
            print ("Directing to the Deposit section")
            print ("Deposit section")
            d=int(input("Enter the amount you want to add in your bank account"))
            balance = balance+d
            print ("The new balance of the bank account after the deposit = ",balance)
            print ("Now proceeding to your payment")
            if (balance>bill):
                print ("Payment is Done")
                print (f" Amount {bill} is transfered to {customer_details}")
                balance = balance-bill
                print (f"Balance after in your Account after the payment {balance}")
            else:
                print ("Still insufficient balance for the payment")
                print ("You can either do the top up in your account or eitherly you can also take loan from us to process this payment")
        if (choice==2):
            s=int(input("Enter the minimum sufficient balance that should be there in the bank account : "))
            m=(bill-balance+s)
            print ("Directing you to the loan section")
            if (m>100000 and m<750000):
                interest = 12
            elif (m>750000):
                interest = 18
                print ("For such a big loan you should mortgage any collateral")
                print ("We expect that you will cooperate with our rules and regulation")
                print ("We are providing you loan on 18 percent rate of interest on the mortgage value of your collateral")
            else:
                interest = 9
                print ("The amount you have asked is provided to you on the given interest rate of the bank which is negotiable")
                print ("Please tell the time in which you are going to pay the amount back to us ")
                t=int(input("How much time you will take to pay your loan to the bank:"))
                print ("Your interest will be calculated from the day itself you recieve the money from us till the day you return money")
                print ("The net payable amount = ",(m+((m*interest* t)/100)))
    else:
        print ("Paying bill")
        balance = balance-bill
        print (f"Your New Account balance after the payment is {balance}")
elif (ch==0):
    print ("Submit the details of the person to whom you want to rtgs the money")
    amount_rtgs=int(input("Enter the amount to be rtgs : "))
    if (amount_rtgs<balance):
        print ("Processing your Payment")
        balance = balance-amount_rtgs
    else:
        print ("Insufficient Balance")
        print ("Go to the main menu")
elif (ch not in indexes_lt):
    print ("Invalid Input")
    print ("Please try again")
    print ("Go to the main menu")
print ("Thank You for visiting")
print ("Have a Good Day")
