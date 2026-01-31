# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

day = input("Enter the day that you want ticket for: ").lower()
age = int(input("Enter your age: "))

adult_ticket_cost = 12
children_ticket_cost = 8
discount = 2

if age >= 18:
    price = adult_ticket_cost
    ticket_type = "Adult"
else:
    price = children_ticket_cost
    ticket_type = "Children"

if day == "wednesday":
    price -= discount
    print(f"Discounted Ticket Price ({ticket_type}): ${price}")
else:
    print(f"Ticket Price ({ticket_type}): ${price}")
