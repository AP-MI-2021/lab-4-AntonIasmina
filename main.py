
def citeste_lista_float():
    list=[]
    list_str=input('Cititi numere separate printr-un spatiu:')
    list_str_split=list_str.split(' ')
    for numar_str in list_str_split:
        list.append(float(num_str))
    return list

def get_parte_intreaga(lst):
    """
    Adauga intr-o lista noua partea intreaga a tuturor elementelor din lista initiala
    :param lst: lista de floaturi
    :return: lst de intregi
    """
    lista_noua=[]
    for numar in lst:
        lista_noua.append(int(numar))
    return lista_noua

def test_get_parte_intreaga():
    assert get_parte_intreaga([])==[]
    assert get_parte_intreaga([-1,32.56,0,-0.5,23])==[-1,32,0,0,23]


def get_apartine_intervalului(lst,st,dr):
    """
    Afiseaza numerele care care apartin unui interval deschis citit de la tastatura:
    :param lst: lista -float
    :param st: capatul din stanga al intervalului
    :param dr: capatul din dreapta al intervalului
    :return: lista(elementele care apartin intervalului citit)

    """
    rezultat=[]
    for element in lst:
        if element >st and element <dr:
            rezultat.append(element)
    return rezultat

def test_get_apartine_intervalului():

    assert get_apartine_intervalului([],12,13)==[]
    assert get_apartine_intervalului([1.4,6,7,9],5,10)==[6,7,9]


def get_toate_numerele_cu_partea_intreaga_divizor_al_partii_fractionare(lst):
    """
    Afiseaza toate numerele a caror parte intreaga este divizor al partii fractionare:
    :param lst: lista(float)
    :return: lista
    """
    rezultat=[]
    for element in lst:
        string_element=str(element)
        decimale= string_element.split('.')[1]
        intreg= string_element.split('.')[0]
        fract=int(decimale)
        i=int(intreg)
        if fract&i==0 and fract!=0:
            rezultat.append(element)
    return rezultat

def test_get_toate_numerele_cu_partea_intreaga_divizor_al_partii_fractionare():
     assert get_toate_numerele_cu_partea_intreaga_divizor_al_partii_fractionare([])==[]





if __name__=="__main__":
    test_get_toate_numerele_cu_partea_intreaga_divizor_al_partii_fractionare()
    test_get_apartine_intervalului()
    test_get_parte_intreaga()

    while True:
        print("1.Citire date:")
        print("2.Adauga intr-o lista noua partea intreaga a tuturor elementelor din lista initiala:")
        print("3.Afiseaza numerele care care apartin unui interval deschis citit de la tastatura:")
        print("4.Afiseaza toate numerele a caror parte intreaga este divizor al partii fractionare:")
        print("")
        print("6.Iesire:")

        optiune=input("Alege optiunea:")

        if optiune=='1':
            sir=citeste_lista_float()
        elif optiune=='2':
            intreg=get_parte_intreaga()
            print(intreg)
        elif optiune=='3':
            stanga=float(input('Dati capatul din stanga al intervalului:'))
            dreapta=float(input('Dati capatul din dreapta al intervalului:'))
            interval=get_apartine_intervalului(sir,stanga,dreapta)
            print(interval)
        elif optiune=='4':
            divizor= get_toate_numerele_cu_partea_intreaga_divizor_al_partii_fractionare(sir)
            print(divizor)
        elif optiune=='5':
            pass
        elif optiune=='x':
            break
        else:
            print('Optiune gresita:')

