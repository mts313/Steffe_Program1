def main():
    # Stores the meals cost and rates
    meal_cost = 85.97
    tax_rate = 0.085
    tip_rate = 0.20

    # Calculate the tax amount
    tax_amount = meal_cost * tax_rate

    # Calculate subtotal after tax
    subtotal = meal_cost + tax_amount

    # Calculate tip amount
    tip_amount = subtotal * tip_rate

    # Calculate final total
    final_total = subtotal + tip_amount

    # Display Results
    print(f"Meal Cost: ${meal_cost:.2f}")
    print(f"Tax Amount: ${tax_amount:.2f}")
    print(f"Tip Amount: ${tip_amount:.2f}")
    print(f"Final Total: ${final_total:.2f}")

if __name__ == "__main__":
    main()