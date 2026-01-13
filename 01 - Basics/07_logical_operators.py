# Logical operators = evaluate multiple conditions (or, and, not)

# ------------------------------------
# OR → at least ONE condition is True
# ------------------------------------
temperature = 10
is_snowing = True
is_windy = False

if temperature < 0 or is_snowing or is_windy:
    print("⚠️ Bad weather warning!")
else:
    print("✅ Weather is clear")


# ------------------------------------
# AND → ALL conditions must be True
# ------------------------------------
age = 22
has_id = True

if age >= 18 and has_id:
    print("🎟️ You are allowed to enter")
else:
    print("⛔ Entry denied")


# ------------------------------------
# AND (multiple conditions)
# ------------------------------------
score = 85
attendance = 90

if score >= 80 and attendance >= 75:
    print("🏆 You passed with distinction")
else:
    print("📘 Requirements not met")


# ------------------------------------
# NOT → inverts the condition
# ------------------------------------
is_logged_in = False

if not is_logged_in:
    print("🔐 Please log in to continue")
else:
    print("👋 Welcome back!")


# ------------------------------------
# COMBINATION (and + or + not)
# ------------------------------------
balance = 50
is_member = False

if (balance >= 100 and is_member) or not is_member:
    print("💳 Transaction approved")
else:
    print("❌ Transaction denied")
