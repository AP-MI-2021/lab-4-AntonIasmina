def citirelista() -> list[int]:
    lst = []
    n = int(input("Dati un numar de elemente:"))
    for i in range(n):
        lst.append(int(input("l["+str(i)+"]=")))
    return lst


if __name__ == "__main__":

    while True:
        print("1.Citire date")
        print("2. :")
        print("3. :")
        print("4. :")
        print("5.")

        optiune = input("Alege optiunea:")

        if optiune =='1' :
            sir=citirelista()
        elif optiune=='2':
            break