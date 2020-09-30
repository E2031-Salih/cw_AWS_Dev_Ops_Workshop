a = []
for i in range(5):
    sayi = input("Please enter the " + str(i + 1) + ". number: ")
    while not sayi.isdigit():
        print("Please enter a number")
        sayi = input("Please enter the " + str(i + 1) + ". number: ")
    a.append(int(sayi))
maks = a[0]
for i in a:
    maks = (lambda x : maks if maks >= x else x)(i)
print("max number is:", maks)