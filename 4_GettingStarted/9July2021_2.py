"""
Lokesh has taken a loan of INR 40000 from Vinod at the rate of 8% per annum. After 6
years, he wants to repay the loan in full including interest. Write the Python code
(in script mode) to calculate and display the interest and total amount to be paid by
Lokesh to settle his accounts.
"""

principal = 40000
rate = 8
time = 6

interest = (principal * rate * time) / 100
total = principal + interest
print(f"Simple Interest = Rs. {interest}, Amount payable = Rs. {total}")
