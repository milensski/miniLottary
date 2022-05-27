import random

print("---------------WELCOME TO TOTO 5/35------------------\n")

bet = int(input("Place your bet to start to play: "))

print(f"Please choose 5 numbers between 1 to 35\n")

count = 1
player_numbers = []
lucky_numbers = []
matched_numbers = []
matches = 0

while count != 6:
    number = int(input(f"Choose number {count}: "))
    if 1 <= number <= 35:
        if number not in player_numbers:
            player_numbers.append(number)
            count += 1
        else:
            print(f"Number {number} already exists!")
    else:
        print("Number must be between 1 and 35 !")

while len(lucky_numbers) != 5:
    current_number = random.randint(1, 35)
    if current_number not in lucky_numbers:
        lucky_numbers.append(current_number)

for j in range(5):  # first loop for current player digit
    for k in range(5):  # loop through all lucky numbers list
        if player_numbers[j] == lucky_numbers[k]:
            matched_numbers.append(player_numbers[j])

if len(matched_numbers) > 0:
    if len(matched_numbers) == 1:
        print(f"Congratulations your price is x10 {bet * 10}")
    elif len(matched_numbers) == 2:
        print(f"Congratulations your price is x20 -> {bet * 20}")
    elif len(matched_numbers) == 3:
        print(f"Congratulations your price is x300 --> {bet * 300}")
    elif len(matched_numbers) == 4:
        print(f"Congratulations your price is x500{bet * 500}")
    elif len(matched_numbers) == 5:
        print(f"Congratulations MEGA PRICE JACKPOT WON x1000 {bet * 1000}")
else:
    print(f"Sorry no matches!")

print(f"Lucky numbers: {lucky_numbers}")
print(f"Your numbers: {player_numbers}")
print(f"Matched numbers: {matched_numbers}")
