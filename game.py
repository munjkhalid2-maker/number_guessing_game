import random

print("Number Guessing Game me Welcome! 🎮")
print("Maine 1 se 20 tak ka ek number socha hai.")
print("Kya tum guess kar sakti ho?")

secret_number = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("\nApna guess likho: "))
    attempts = attempts + 1
    
    if guess < secret_number:
        print("Bohat chota hai! Bara number socho 📈")
    elif guess > secret_number:
        print("Bohat bara hai! Chota number socho 📉")
    else:
        print(f"Shabash! Sahi guess kiya 🎉")
        print(f"Tumne {attempts} attempts me jeet liya!")
        break

print("Game khatam. Phir khelna!")
