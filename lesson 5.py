# height = 180
# print(f"My height: {height} cm")

# height=180
# print(height)

# height=int(180)
# print(int("height"))

# print("My name is 'Aliia'")

# age=int(input("enter your age:"))
# print(type(age))

# age=input("enter your age:")
# print(age)
# print(type(age))
# age=34
# myAge=str(age)
# age=34.0
# print(type(age))


#Home work

total_money = 1500

print("Welcome to the supermarket!")
print(f"You have {total_money} com.")

apple_price = 150
mandarin_price = 100
greens_price = 50
chocolate_price = 200

buy_apple = input("Do you want to buy an apple for 150 com? (yes/no): ")
buy_apple = buy_apple == "yes"

buy_mandarin = input("Do you want to buy an orange for 100 com? (yes/no): ")
buy_mandarin = buy_mandarin == "yes"

buy_greens = input("Do you want to buy greens for 50 com? (yes/no): ")
buy_greens = buy_greens== "yes"

buy_chocolate = input("Do you want to buy chocolate for 200 com? (yes/no): ")
buy_chocolate = buy_chocolate == "yes"

expenses = 0

if buy_apple:
    expenses += apple_price
if buy_mandarin:
    expenses += mandarin_price
if buy_greens:
    expenses += greens_price
if buy_chocolate:
    expenses += chocolate_price

remaining_money = total_money - expenses

print("--- Results ---")
print(f"You spent: {expenses} com.")
print(f"You have: {remaining_money} com.")
print("Thank you for your purchase!")

if remaining_money > 0:
    print("You have enough money.")
else:
    print("You are out of money.")

