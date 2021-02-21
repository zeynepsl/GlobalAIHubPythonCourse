
matrix = []
print("Değerleri girmeye başlayın (varsayılan olarak 2 değeri atanacak)")

for i in range(3):
    a = []
    print("{}. satır için değerleri girmeye başlayın ".format(i))
    for j in range(3):
        num = int(input("{}. sütun için değeri girin : ".format(j)))

        #asal sayı kontrolü
        for k in range(2, num):
            if (num % k) == 0:
                a.append(2)
        else:
            a.append(num)
    matrix.append(a)
    print()


for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()
