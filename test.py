# def is_even(num):
#     return num % 2 == 0
# print(is_even(4))
# print(is_even(7))
# x=is_even(10)
# print(x)



# def is_palindrome(s):
#     return s == s[::-1]
#
# print(is_palindrome("radar"))
# print(is_palindrome("hello"))
# print(is_palindrome("12321"))

# def power(base, exponent=2):
#     return base ** exponent
# print(power(3))
# print(power(3, 3))
# print(power(2, 4))

#
# x=10
#
# def change_x():
#     x = 5
#     print(x)
# change_x()
# print(x)


#
# def quadratic_roots(a, b, c):
#     discriminant = b**2 - 4*a*c
#     if discriminant < 0:
#         return None
#     root1 = (-b + discriminant**0.5) / (2*a)
#     root2 = (-b - discriminant**0.5) / (2*a)
#     return root1, root2
# result = quadratic_roots(1, -3, 2)
# print(type(result))


# def digit_sum_math(n: int) -> int:
#     """
#     Вычисляет сумму цифр заданного целого числа, используя математические операции.
#
#     Эта функция использует оператор деления по модулю (%) для получения последней
#     цифры и оператор целочисленного деления (//) для удаления этой цифры.
#
#     Args:
#         n: Целое число (int). Функция работает с абсолютным значением числа,
#            поэтому отрицательные числа обрабатываются корректно.
#
#     Returns:
#         Сумма цифр числа.
#     """
#     # Работаем с абсолютным значением числа, чтобы обработать отрицательные числа
#     n = abs(n)
#     total_sum = 0
#
#     # Цикл продолжается, пока число не станет равно 0
#     while n > 0:
#         # 1. Получаем последнюю цифру с помощью деления по модулю 10
#         # (Например, 123 % 10 = 3)
#         last_digit = n % 10
#
#         # 2. Добавляем цифру к общей сумме
#         total_sum += last_digit
#
#         # 3. Удаляем последнюю цифру с помощью целочисленного деления на 10
#         # (Например, 123 // 10 = 12)
#         n //= 10
#
#     return total_sum
#
#
# def digit_sum_string(n: int) -> int:
#     """
#     Вычисляет сумму цифр, преобразуя число в строку.
#
#     Args:
#         n: Целое число (int).
#
#     Returns:
#         Сумма цифр числа.
#     """
#     # Работаем с абсолютным значением, затем преобразуем в строку
#     s_num = str(abs(n))
#     total_sum = 0
#
#     # Итерируемся по каждому символу в строке
#     for digit_char in s_num:
#         # Преобразуем символ обратно в целое число и складываем
#         total_sum += int(digit_char)
#
#     return total_sum
#
#
# # --- Примеры использования и проверка ---
#
# test_cases = [123, 90105, 5, 0, -456]
#
# print("--- Тестирование математического подхода (digit_sum_math) ---")
# for num in test_cases:
#     result = digit_sum_math(num)
#     print(f"digit_sum_math({num}) -> {result}")
#
# print("\n--- Тестирование строкового подхода (digit_sum_string) ---")
# for num in test_cases:
#     result = digit_sum_string(num)
#     print(f"digit_sum_string({num}) -> {result}")
#
# # В качестве основной функции используем математический подход, как более производительный
# digit_sum = digit_sum_math
#
# # Проверка, соответствующая запросу:
# print(f"\ndigit_sum(123) returns {digit_sum(123)}")


# def is_even(num):
#     return num % 2 == 0
# def count_evens(lst):
#     count = 0
#     for num in lst:
#         if is_even(num):
#             count += 1
#     return count
# result = count_evens([1, 2, 3, 4, 5, 6])
# print(result)

#
# def gcd(a, b):
#     d = min(a, b)
#     while a % d != 0 or b % d != 0:
#         d -= 1
#     return d
#
# print(gcd(12,8))
# print(gcd(15,10))

# fruits = ["apple", "banana", "cherry", "date"]
#
# print(fruits[0])
# print(fruits[2])
# print(fruits[-1])
# print(len(fruits))
# print([0] * 5)

# numbers = [10, 20, 30, 40, 50, 60]
#
# print(numbers[1:4])
# print(numbers[:3])
# print(numbers[3:])
# print(numbers[::2])
# print(numbers[::-1])

# numbers = [1,2,3,4,5]
# print(numbers[1:4])
# print(numbers[::2])
# print(numbers[::-1])


# print([1,2] + [3,4])
# print([5,6]*3)
# print("red" in ["red","blue"])
# print("green" not in ["red","blue"])

# numbers = [10, 20, 30, 40]
# numbers[1] = 99
# numbers[-1] = 77
# print(numbers)

# items = [5,2,8,1]
# items.append(3)
# print(items)
# items.sort()
# print(items)
# items.reverse()
# print(items)

# numbers = [10, 20, 30, 40, 50]
# x=numbers.pop()
# y=numbers.pop(1)
# print(x,y)
# print(numbers)

# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
#
# list1.append([4,5])
# list2.extend([4,5])
# print(list1)
# print(list2)

# numbers = [1,2,3,2,4,2,5]
# print(numbers.count(2))
# print(numbers.count(10))
# print(numbers.index(2))
# print(numbers.index(4))

# squares = [x**2 for x in range(1, 6)]
# print(squares)
#
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)

# list1 = [1, 2, 3]
# list2 = list1
# list3 = list1.copy()
#
# list1[0] = 99
#
# print(list1)
# print(list2)
# print(list3)

# def binary_search(nums, target):
#     l=0
#     r=len(nums)
#     while l <= r-1:
#         mid = (l + r) // 2
#         if nums[mid] <= target:
#             l = mid
#         else:
#             r = mid
#     if nums[l] == target:
#         return l
#     else:
#         return -1

# def binary_search(nums, target):
#     l = 0
#     r = len(nums)
#
#     while l < r - 1:
#         mid = (l + r) // 2
#         if nums[mid] <= target:
#             l=mid
#         else:
#             r=mid
#         if nums[l]==target:
#             return l
#         else:
#             return -1
#
# print(binary_search([1,2,3,4,5], 3))
# print(binary_search([1,2,3,4,5], 6))

# def count_vowels(s):
#     count = 0
#     for i in s:
#        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
#            count += 1
#     return count
# print(count_vowels("Hello World"))
# print(count_vowels("Python"))

# def count_vowels(s):
#     s = s.lower()
#     so = len(s)
#     su=0
#     for i in range(0,so-1):
#        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
#            su+=1
#     return su
# print(count_vowels("Hello World"))
# print(count_vowels("Python"))

# def is_leap_year(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# print(is_leap_year(2024))
# print(is_leap_year(1900))
# print(is_leap_year(2000))
# list1 = [10, 20, 30]
# list2 = list1
# list3 = list1.copy()
#
# list1[0] = 99
#
# print(list1)
# print(list2)
# print(list3)

# cubes = [x**3 for x in range(1, 5)]
# print(cubes)
#
# odds = [n for n in range(15) if n % 2 != 0]
# print(odds)

# values = [5, 3, 5, 7, 5, 9, 3]
# print(values.count(5))
# print(values.count(1))
# print(values.index(5))
# print(values.index(9))

# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
#
# list1.append(0)         #
# list2.insert(0, 0)
# print(list1)
# print(list2)

# items = ["a", "b", "c", "d", "e"]
# first = items.pop(0)
# last = items.pop()
# print(first, last)    #
# print(items)

# nums = [3, 1, 4, 1, 5]
# nums.append(9)
# print(nums)           # State 1
# nums.insert(0, 2)
# print(nums)           # State 2
# nums.remove(1)
# print(nums)

# def fahrenheit_to_celsius(f, rounded=True):
#     c = (f - 32) * 5 / 9
#     if rounded:
#         return round(c)
#     return c
#
# print(fahrenheit_to_celsius(32))
# print(fahrenheit_to_celsius(212))
# print(fahrenheit_to_celsius(100, False))

# def number_of_digits(n):
#     digit = 0
#     n = abs(n)
#     while n!=0:
#         n=n//10
#         digit += 1
#     return digit
# print(number_of_digits(12345))
# print(number_of_digits(7))
# print(number_of_digits(-999))

# def is_valid_triangle(a,b,c):
#     if a+b>c and c+b>a and a+c>b:
#         return True
#     else: return False
# print(is_valid_triangle(3,4,5))
# print(is_valid_triangle(1,2,10))

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# def count_primes(numbers):
#     count = 0
#     for num in numbers:
#         if is_prime(num):
#             count += 1
#     return count
#
# result = count_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(result)

# def get_hypotenuse(a, b):
#     return (a**2 + b**2) ** 0.5
#
# print(get_hypotenuse(3, 4))
# print(get_hypotenuse(5, 12))

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[2:5])
# print(letters[:4])
# print(letters[4:])
# print(letters[1::2])
# print(letters[-3:])

# data = [10,20,30,40,50,60]
# print(data[2:5])
# print(data[1::2])
# print(data[-2:])

# def normalize_fraction(num, den):
#     def gcd(a, b):
#         while b:
#             a, b = b, a%b
#         return a
#     g = gcd(abs(num), abs(den))
#
#     return num//g, den//g
# result = normalize_fraction(12, 8)
# print(result)

# def average(nums):
#     n=sum(nums)
#     length=len(nums)
#     if length<1:
#         return 0
#     av = n/length
#     return av
# print(average([10,20,30]))
# print(average([5]))
# print(average([]))

#
# def stalin_sort[T](items: list[T]) -> list[T]:
#     if not items:
#         return []
#
#     result = [items[0]]
#
#     for item in items[1:]:
#         if item >= result[-1]:
#             result.append(item)
#         # else: eliminated! (sent to gulag)
#
#     return result

# s = {3, 1, 4, 1, 5, 9, 2, 6}
# print(len(s))
# print(3 in s)
# print(7 in s)
# print(min(s))

# set_a = {1,2, (3,4)}
# set_b = {1,2, [3,4]}
# set_c = {1,2, {3,4}}
# set_d = {1,2, "hello"}

# print(set_a)
# print(set_b)
# print(set_c)
# print(set_d)

# A = {1,2,3,4}
# B = {3,4,5,6}
# print(A|B)
# print(A&B)
# print(A-B)
# print(B-A)
# print(A^B)

# s = {1,2,3}
# s.add(4)
# print(s)
#
# s.update([5,6,6])
# print(s)
#
# s.discard(2)
# s.discard(10)
# print(s)
#
# s.pop()
# print(len(s))


# A = {1,2,3}
# B = {1,2,3,4,5}
# C = {1,2,3}
#
# print(A < B)
# print(A <= C)
# print(B > A)
# print(A.isdisjoint({4,5}))


# squares = {x**2 for x in range(-3,4)}
# print(squares)
# print(len(squares))


# def list_intersection(list1, list2):
#    return list(set(list1).intersection(list2))
#
# print(list_intersection([1,2,3,4], [3,4,5,6]))
# print(list_intersection([1,2,2], [2,2,3]))

# student = {"name":"Bob","age":20, "grade":"A"}
# print(student["name"])
# print(student["grade"])
# print(len(student))

# d = {"a": 1, "b": 2, "c": 3}
# print(d["a"])
# print(d.get("b"))
# print(d.get("z"))
# print(d.get("z",0))

# d={"a":1}
# value1 = d.get("b")
# print(value1)

# student = {"name": "Alice", "age": 20}
# student["age"] = 21
# student["grade"] = "A"
# del student["name"]
# print(student)

# d={"x":10,"y":20,"z":30}
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))
# print("x" in d)
#
# prices = {"apple": 1.50, "banana": 0.75}
#
# for item in prices:
#     print(item)
#
# print("---")
#
# for fruit, price in prices.items():
#     print(f"{fruit}: ${price}")

# d1={"a":1,"b":2}
# d2={"b":3,"c":4}
#
# d3 = d1 | d2
# print(d3)
#
# d1.update(d2)
# print(d1)
#
# print(d1 == d3)

# squares = {x: x**2 for x in range(1,6)}
# print(squares)
#
# filtered = {k: v for k, v in squares.items() if v > 10}
# print(filtered)

# students = {"Alice" : {"age":20, "grades" : [85,90,88]},
#             "Bob" : {"age":22, "grades" : [78,82,80]},
#             }
# print(students["Alice"]["age"])
# print(students["Bob"]["grades"][1])
# students["Alice"]["grades"].append(95)
# print(len(students["Alice"]["grades"]))

# def word_count(sentence):
#     counts = []
#     words = sentence.split(" ")
#     for word in words:
#         words = word.lower
#         if word in counts:
#             counts[word] = +1
#         else:
#             counts[word] = 1
#     return counts
#
# result = word_count("The the THE")
# print(result)

# empty_set = set()
# print(type(empty_set))

# def list_intersection(l1,l2):
#     check={}
#     for num in l1:
#         if num in check:
#             check[num]+=1
#         else:
#             check[num]=1
#     ans = []
#     for num in l2:
#         if num in check:
#             if len(ans)>0 and ans[len(ans)-1]!=num:
#                 ans.append(num)
#     return ans
#
# print(list_intersection([1,2,3,4], [3,4,5,6])) #returns [3,4]
# print(list_intersection([1,2,2], [2,2,3])) #returns [2]


# def first_recurring(text):
#     ans = {}
#     mx = 0
#     for char in text:
#         if char in ans:
#             ans[char] += 1
#             mx = max(mx, ans[char])
#         else:
#             ans[char] = 1
#             mx = max(mx, 1)
#     if mx <= 1:
#         return None
#     for char in text:
#         if ans[char] == mx:
#             return char
#     return None
#
# print(first_recurring(("ABCA")))  #returns "A"
# print(first_recurring(("ABCBA")))  #returns "B"
# print(first_recurring(("ABC")))  #returns None


# def find_missing (numbers, numb):
#     numbers = sorted(numbers)
#     check = {}
#     ans = []
#     for num in numbers:
#         if num in check:
#             continue
#         else:
#             check[num] = 1
#     for i in range(1,numb+1):
#         if i in check:
#             continue
#         else:
#             ans.append(i)
#     return ans
#
# print(find_missing([1,2,4,6],6)) #returns {3,5}
# print(find_missing([1,2,3],5)) #returns {4,5}

# def two_sum (numbers, numb):
#     check = {}
#     i=0
#     for num in numbers:
#         qq = numb - num
#         if qq in check:
#             return [check[qq], i]
#         check[num] = i
#         i += 1
#     return check
#
# print(two_sum([2,7,11,15],9)) #returns [0,1] because 2+7=9
# print(two_sum([3,2,4],6)) #returns [1,2] because 2+4=6
