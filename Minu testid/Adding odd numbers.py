"""Adding odd number's from 0 to n"""
print("This program finds the sum of all odd numbers from 1 to n (n > 0)")
n = input("n:")
n = int(float(n))
if n == 0:
    print("invalid input.")
elif n % 2 == 1:
    # n on paaritu arv
    number_of_odd_numbers = int((n+1)/2)
    print(int(number_of_odd_numbers**2))
else:
    number_of_odd_numbers = n/2
    print(int(number_of_odd_numbers**2))
