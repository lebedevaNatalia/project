cube_list = []
for i in range(1, 1000):
    if i % 2 != 0:
        n = i**3
        i += 1
        cube_list.append(n)

print(cube_list)

for m, n in enumerate(cube_list):
    sum_n = 0
    all_sum = 0
    while n > 0:
        sum_n += n % 10
        n //= 10
    if sum_n % 7 == 0:
        all_sum += cube_list[m]
    print(all_sum)
