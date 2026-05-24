# Simple tool to analyze digital template sales
def calculate_net_profit(price, tax_rate, platform_fee):
    """
    Calculates the final profit after deducting taxes and platform fees.
    """
    fees = price * (platform_fee / 100)
    tax = price * (tax_rate / 100)
    final_profit = price - fees - tax
    return round(final_profit, 2)

# Example Usage:
# Template Price: 150 SAR
# Platform Fee (e.g., Gumroad/Etsy): 10%
# Tax: 15%
template_price = 150
profit = calculate_net_profit(template_price, 15, 10)

print(f"Original Price: {template_price} SAR")
print(f"Net Profit after fees: {profit} SAR")
