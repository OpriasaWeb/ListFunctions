prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]
#your code goes here

sum_of_all = 0
average = 0
length_of_prices = 0
arr_length = []

for i in prices:
    sum_of_all = sum_of_all + i
    length_of_prices = length_of_prices + 1
  
# print(sum_of_all)
# print(length_of_prices)

average = sum_of_all / length_of_prices
# print(average)

for k in prices:
    if int(k) > average:
      # print(f"Greater than {k}")
      arr_length.append(k)

print(len(arr_length))

