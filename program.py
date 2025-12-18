def calculate_bill(units):
    bill = 0
    
    # Example slab rates (you can adjust as per your state/region)
    if units <= 100:
        bill = units * 1.5   # ₹1.5 per unit for first 100 units
    elif units <= 200:
        bill = (100 * 1.5) + (units - 100) * 2.5   # ₹2.5 per unit for next 100
    elif units <= 500:
        bill = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4   # ₹4 per unit for next 300
    else:
        bill = (100 * 1.5) + (100 * 2.5) + (300 * 4) + (units - 500) * 6   # ₹6 per unit above 500
    
    # Add fixed charges
    fixed_charge = 50
    total_bill = bill + fixed_charge
    
    return total_bill


# Example usage
units_consumed = int(input("Enter the number of units consumed: "))
amount = calculate_bill(units_consumed)
print(f"Your electricity bill is: ₹{amount:.2f}")
