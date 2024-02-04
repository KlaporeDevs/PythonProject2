initial_investment = float(input("Enter the initial investment amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
compounding_frequency = int(input("Enter the compounding frequency per year: "))

target_amount = initial_investment * 2
years = 0
balance = initial_investment
while balance < target_amount:
    interest = balance * (annual_interest_rate / compounding_frequency)
    balance += interest
    years += 1
print(f"It will take {years} years to double your money.")
