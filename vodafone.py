'\n'
'\n'
while True:
    tam=print('''Hellooo! I am VIC, your service assistant. I'm here to help you with our services. Let's get started!
    1. Balance
    2. Data Balance
    3. Activate Plan
    4. Find a store
    5. Pay Bill
    6. Past Payments
    7. Recharge
    8. More Recharge offers

    Reply with the option number (eg. 1 for Activate Plan) to select the option''')
    operator=int(input())
    if operator==1:
        print("Main Balance ₹ 39.5.Valid till 15-Jun-2020.\n ")
    elif operator==2:
        print("No data Balance \n")
    elif operator==3:
        print("No Active plans \n")
    elif operator==4:
        print('''I am seeing that you have some concern for which  you will have to visit our Store. You can find our nearest store here. I would suggest to carry all the relevant documents (Original ID Proof, Original Address Proof etc.) for instant support
    Click Here for Vodafone ➡️ http://bit.ly/VodafoneStores \n''')
    elif operator==5:
        print('pay bills https://www.vodafone.in/postpaid/quick-online-bill-payment \n')
    elif operator==6:
        print('''Date Of Recharge    Time    Price Of Recharge 
    16-Jun-2020              05:10          ₹ 50
    07-Apr-2020              07:29          ₹ 499 \n''')
    elif operator==7:
        print('''1. Double data! Now get Truly Unlimited Local/National Calls to all Networks+4GB/Day+100SMS/Day. Validi...
    Price 299.0
     

    2. Double Data Offer. Now get Truly Unlimited Local/National Calls to all Networks+1.5GB/Day+ Extra1.5G...
    Price 399.0
     

    3. Now get Truly Unlimited Local/National Calls+1.5GB/Day+100SMS/Day.Validity:28Days \n
    Price 249.0
     
    ''')
    elif operator==8:
        print('Click Here for Show more packs ➡️ http://bit.ly/VodafoneRecharge2 \n')
    else:
        print('Enter the correct value \n')

