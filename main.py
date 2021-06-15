# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name3 = name1.lower() + name2.lower()
count_true = "true"
total_true = 0
count_love = "love"
total_love = 0

for x in count_true:
  total_true += name3.count(x)
for y in count_love:
  total_love += name3.count(y)

total_comb = int(str(total_true) + str(total_love))

if total_comb < 10 or total_comb > 90:
  print(f"Your score is {total_comb}, you go together like coke and mentos.")
elif total_comb >40 and total_comb <50:
  print(f"Your score is {total_comb}, you are alright together.")
else:
  print(f"Your score is {total_comb}.")
