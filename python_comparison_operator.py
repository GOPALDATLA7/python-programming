#Enter the values
num1 = int(input("Enter num1 value : "))
num2 = int(input("Enter num2 value : "))
#Arithmetic operators
#returns True for correct, False for incorrect
print("Equal : ",num1==num2)
print("Not equal : ",num1!=num2)
print("Greater than : ",num1>num2)
print("Less than : ",num1<num2)
print("Greater than or equal to : ",num1>=num2)
print("Less than or equal to : ",num1<=num2)

"""
output:
Enter num1 value : 10
Enter num2 value : 20
Equal :  False                         #since num1 is not equal to num2 so equal condition fails so it returns False
Not equal :  True                      #since num1 is not equal to num2 so not equal condition True so it returns True
Greater than :  False                  #since num1 is not greater than num2 so greater than condition fails so it returns False
Less than :  True                      #since num1 is less than num2 so lessthan condition True so it returns True
Greater than or equal to :  False      #since num1 is not greater than or equal to num2 so greater than or equal condition fails so it returns False
Less than or equal to :  True          #since num1 is less than or equal to num2 so less than or equal condition is true so it returns True
"""