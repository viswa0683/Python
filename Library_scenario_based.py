class scenario:
    #A system checks if a user is eligible to vote based on their age.
     # Write logic to ask the user for their age and determine if they are eligible to vote based on whether they are 18 or older.
    #Age category
    def age_category():
    
        Name=input("Enter your Name")
        Age=int(input("Enter your Age"))
        if Age<=17:
            print("You are not Eligible")
        else:
            print(Name+" : You are Eligible for Vote: "+str(Age))
        return Name+str(Age)    
    #: A program processes a list of numbers and needs to find the largest value.
     # Write logic to identify and return the largest number from a given list.
    
    def list_of_numbers(a,b,c,d,e):
        numbers=[a,b,c,d,e]
        print(max(numbers))
        print("Max of number is "+ str(max(numbers)))
        return max(numbers);
    # : A company provides employees with a 10% bonus if their salary exceeds $50,000.
     # Write logic to determine the bonus amount based on the given salary
    def employee_bonus():
    
        Name=input("Enter your Name")
        Age=int(input("Enter your Age"))
        Salary=int(input("Enter your Salary"))
        if Salary>=50000:
            bonus=(Salary*10/100)
            Revised_salary=Salary+bonus
            print("Your bonus amount is :"+str(bonus))
            print("Your Revised_salary is :"+str(Revised_salary))
            return Revised_salary
        else:
            print("Your salary is not Revised "+str(Salary))
            return Salary
    
    # : A program evaluates a number to determine if it is even or odd.
    # Write logic to check whether a given number is even or odd
    def odd_even(a):
        b=a%2
        if b==1:
            print("Given number is odd :"+ str(a))
            return "Given number is odd: " + str(a)
        else:
            print("Given number is Even :"+ str(a))
            return "Given number is Even: " + str(a)
    
    #reverse list
    def print_char(word):
        empty=""
        for i in word:
            a=i
            empty=a+empty
            # print(a)
        print(empty)
        return empty
        
        # return(k)
        # return(i)
    
    def student_marks(a,b,c,d,e):
        # English=int(input("English Mark is :")+str(a))
        # Tamil=int(input("Tamil Mark is :")+str(b))
        # Maths=int(input("Maths Mark is :")+str(b))
        # Science=int(input("Science Mark is :")+str(b))
        # History=int(input("History Mark is :")+str(b))
        marks=[a,b,c,d,e]
        for i in marks:
            if i>=40:
                print("Pass: "+str(i))
            else:
                print("Fail: "+str(i))
    # A retail store offers a 20% discount if a customer’s total order exceeds $100. 
        # Write logic to calculate the final amount to be paid after applying the discount.
        
    def discount(amount):
        if amount>100:
            discount=amount*20/100;
            total_amount=amount-discount;
            print("Amount to be Pay:" + str(total_amount))
            return("Amount to be Pay:" + str(total_amount))
        else:
            print("Amount to be Pay:" + str(amount))
            return("Amount to be Pay:" + str(amount));
    
    def bank_withdraw(account_number,balance,withdraw_amount):
        if(balance>=withdraw_amount):
            print('Dont have sufficient Balance')
        else:
            print('Amount is under processing for withdraw')
    
    def list_even(a,b,c,d,e):
        i =[a,b,c,d,e]
        
        for k in i:
            if k%2==0:
                print("Even number is "+ str(k))
        # return ("Even number R is "+ str(k)) 