price=int(input("Enter the price of the amount:"))
discount=int(input("Enter the discount rate:"))

def calculate_discount(price,discount):
    dis_amt=(price*discount)/100
    total_amt=price-dis_amt
    print("The total price is::",price)
    print("The total discount is",dis_amt)
    print("The total amount payable after discount is:",total_amt)

calculate_discount(price,discount)
