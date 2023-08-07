# bank operation project--------
# created account
# deposit 
# withdraw
# check balance

import random
data = {}
list1 = ["Name","Address","PhoneNo","Aadhar number","Account Type","Amount"]
print("****** Welcome to Bank Of India ******")
    

def created_Account():
    print("Create Account:-")
    
    account_num = genrate_acccount_num()
    Pin_num = genrate_Pin_num()
    
    for item in list1:
        list2.append(input("Enter %s: "%item))
        
    data[Pin_num] = dict(zip(list1,list2))
    print("-----------------------------------------------")
    
    print("*** Congratulations! Your Account Created ***")
    
    print("\nYour account Number is: %d"% account_num)
    print("Your pin Number is: %d"% Pin_num)
    print("\nMake sure you keep it safe")
    print("-----------------------------------------------")
    return


def genrate_acccount_num():
    return random.randrange(100000000000,999999999999)
    
def genrate_Pin_num():
    return random.randrange(1000,9999)

    
    
def other_option():
    
    
    ch = int(input("1.Check Balance\n2.Deposit\n3.Withdraw\nChoose any option: "))
    
    if ch == 1:
        print("Available Balance: ",data[Pin_num]["Amount"])
        print("------------------------------------------")
    elif ch == 2:
        amount = int(input("Enter Amount to Deposit: "))
        new_amount = int(data[Pin_num]["Amount"]) + amount
        data[Pin_num]["Amount"] = new_amount
        print("Deposit Successful")
        print("Available Balance: ",data[Pin_num]["Amount"])
        print("-------------------------------------------")
        
    elif ch == 3:
        amount = int(input("Enter Amount to Withdraw: "))
        new_amount = int(data[Pin_num]["Amount"]) - amount
        data[Pin_num]["Amount"] = new_amount
        print("Withdraw Successful")
        print("Available Balance: ",data[Pin_num]["Amount"])
        
    
    
while True:
    list2 = []
    do:created_Account()
      
    while True:    
        s = int(input("1.Existing Customer\n2.Exit\nSelect any option: "))
            
        if s == 1:
            PinNumber_FromUser = int(input("Enter your Pin Number: "))
            for Pin_num in data:
                if(Pin_num == PinNumber_FromUser):
                   print("Record Found")
                   other_option()
                
                else:
                   print("Record not Found ")
        elif s == 2:
            exit()
            