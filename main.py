import random
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','_']
password_list = []

letter_len = int(input("Enter how many alphabets you want in your password:"))
for i in range(1,letter_len+1):
    password_list.append(random.choice(letter))

numbers_len = int(input("Enter how many numbers you want in your password:"))
for i in range(1,numbers_len+1):
    password_list.append(random.choice(numbers))

symbols_len = int(input("Enter how many symbols you want in your password:"))
for i in range(1,symbols_len+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password=''
for j in password_list:
    password += j

print("Your password generated is:",password)
