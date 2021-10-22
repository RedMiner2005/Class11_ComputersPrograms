principal = eval(input("Enter the value of Principal: "))
rate = eval(input("Enter the annual rate of interest: "))
time = 5

simple_interest = principal * rate * time / 100
amount = principal + simple_interest
print("Simple interest = ₹", simple_interest)
print("Amount payable = ₹", amount)
