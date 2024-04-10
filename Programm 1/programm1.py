# Write a function that take amount in dollar as input and convert it into rupees.

# Non-Void Function
def dollar_to_rupees(amount):
    amount_in_rupees = 81.25*amount
    return amount_in_rupees

rupees = dollar_to_rupees(float(input("Enter the amount (in US dollar) you want to convert in rupees: ")))
print(rupees)
print("Yash Sharma")
