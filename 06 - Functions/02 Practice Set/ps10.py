# WAF to convert USD to INR

def convert(value):
    rupee = 90.60 * value
    return rupee

usd = float(input("Enter amount in $: "))
print(f"Indian Rupee: \u20B9{convert(usd)}")