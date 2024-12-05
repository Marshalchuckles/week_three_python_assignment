# Step 1: Define the function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Check if the discount is 20% or higher
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price  # Return the original price if discount is less than 20%

# Step 2: Prompt the user for inputs
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Step 3: Use the function and display results
final_price = calculate_discount(original_price, discount_percent)

if final_price == original_price:
    print(f"No discount applied. The final price is: ${original_price:.2f}")
else:
    print(f"Discount applied! The final price is: ${final_price:.2f}")
