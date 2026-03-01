username = "vivek" # Global Scope

def function():
    username = "michael" # Functional Scope
    print(username)

print(username)
function()


x = 99

def function2(y):
    z = x + y
    return z

result = function2(5)
print(result)