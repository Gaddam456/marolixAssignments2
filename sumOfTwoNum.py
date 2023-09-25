list_a = [4,5,6,7,8,10,11]
list_b = []
for i in range(len(list_a)):
    for j in list_a[i+1:]:
        if list_a[i] + j == 18:
            list_b.append([list_a[i],j])
print(list_b)