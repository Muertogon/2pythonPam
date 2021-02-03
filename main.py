# # Python3 implementation of
# # above approach
#
# # Function to count the number
# # of carry operations
# def count_carry(a, b):
#     # Initialise the value of
#     # carry to 0
#     carry = 0;
#
#     # Counts the number of carry
#     # operations
#     count = 0;
#
#     # Initialise len_a and len_b
#     # with the sizes of strings
#     len_a = len(a);
#     len_b = len(b);
#
#     while (len_a != 0 or len_b != 0):
#
#         # Assigning the ascii value
#         # of the character
#         x = 0;
#         y = 0;
#         if (len_a > 0):
#             x = int(a[len_a - 1]) + int('0');
#             len_a -= 1;
#
#         if (len_b > 0):
#             y = int(b[len_b - 1]) + int('0');
#             len_b -= 1;
#
#             # Add both numbers/digits
#         sum = x + y + carry;
#
#         # If sum > 0, icrement count
#         # and set carry to 1
#         if (sum >= 10):
#             carry = 1;
#             count += 1;
#
#             # Else, set carry to 0
#         else:
#             carry = 0;
#
#     return count;
#
#
# # Driver code
# a = "955847895";
# b = "556545";
#
# count = count_carry(a, b);
# if (count == 0):
#     print("0");
# elif (count == 1):
#     print("1");
# else:
#     print(count);
#
# print(count_carry(a,b))
#exercise 3
c = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = int(input("input number: "))
for i in range(len(a)):
    if a[i] < b:
        c.append(a[i])

for i in range(len(c)):
    print(c[i])

#exercise 2
num = int(input("inter number: "))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")
check = int(input("inter number: "))
if num % check == 0:
    print("skaicius graziai issidalina is kito duoto")
else:
    print("nop")

#exercise 4
#neuzbaigta
dalsk = int(input("skaiciu kurio norite suzinoti daliklius"))
while dalsk > i:
    if dalsk % i== 0:
        print(str((i))+("=dalinasi"))
    else:
        print(str((i))+("=nesidalina"))
    i -= 1

#exercise 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


