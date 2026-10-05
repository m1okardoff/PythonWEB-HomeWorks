def not_even_numbers(n1,n2):
    if n1 > n2:
        n1,n2 = n2,n1
    for i in range(n1,n2):
        if i % 2 != 0:
            yield i

def number_devided_by_5(n1,n2):
    if n1 > n2:
        n1,n2 = n2,n1
    for i in range(n1,n2):
        if i % 5  == 0:
            yield i

def palindrome_numbers(n1,n2):
    def is_palindrome(num):
        digits = []
        if num < 10:
            return False
        while num > 0:
            digits.append(num % 10)
            num = num // 10
        return digits == digits[::-1]

    if n1 > n2:
        n1, n2 = n2,n1
    for i in range(n1,n2+1):
        if is_palindrome(i):
            print(i,end=", ")
            if i % 10 == 0:
                print()






number1 = int(input("Введіть початок діапазону: "))
number2 = int(input("Введіть кінець діапазону: "))
print("Всі непаріні числа діапазону: ")
for num in not_even_numbers(number1,number2+1):
    print(num, end=", ")
print()
print("Всі числа кратні 5 з діапазону: ")
for num in number_devided_by_5(number1,number2+1):
    print(num, end=", ")
print("\nВсі числа паліндроми: ")

palindrome_numbers(number1,number2)





