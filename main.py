import math
import random
maxim=[]
dimensiue=input("Dimensiunea populatiei:")
dimensiue=int(dimensiue)
a,b=input("Capetele intervalului:").split()
a=int(a)
b=int(b)
x,y,z=input("Parametrii functiei:").split()
x=int(x)
y=int(y)
z=int(z)
precision=int(input("Precizie:"))
crossover_percent=float(input("P_Crossover:"))
mutatie=float(input("P_mutatie:"))
stages=int(input("Etape:"))
random_numbers = [random.uniform(-1, 1) for _ in range(dimensiue)]

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left<=right:
        mid = (left + right) // 2
        if arr[mid][0]<=target and arr[mid][1]>target :
            return mid
        elif arr[mid][1]<target:
            left = mid + 1
        elif arr[mid][0]>=target:
            right = mid - 1


def lungime(a, b, precision):
    return math.log2((b - a) *( 10**precision ))

def intervale(a, b, precision):
    lun = math.ceil(lungime(a, b, precision))
    d = (b - a) / 2 ** lun
    intervale=[]
    for i in range(0,(int(abs(b-a)//d))+1):
        intervale.append(((a+d*(i),a+(d*(i+1)))))
    return intervale,lun,d,

def toBinary(x,int,lun):
    pozitie=-1
    for index,tuple in enumerate(int):
        if x>=tuple[0] and x<=tuple[1]:
            pozitie=index
    binar=bin(pozitie)
    binar=binar[2:]
    while(len(binar)<lun):
        binar="0"+binar
    return binar

def functie(ran,x,y,z):
    return x*(ran*ran*ran)+y*ran*ran+z*x

def crossover(bit,bitt,index):
    copie=bit
    copie2=bitt

    bit=bit[:index]+bitt[index:]
    bitt=bitt[:index]+copie[index:]
    # bit=bit[:index]+bitt[index:indexx]+bit[indexx:]
    # bitt=bitt[:index]+copie[index:indexx]+bitt[indexx:]
    return bit,bitt


int,lun,dim=intervale(a,b,precision)


for nr_stage in range(0,stages):
    cromozom_list = []
    fct = []
    imagine = []
    if nr_stage!=0:
        cromozom_list.append(maxim[-1][0])
        fct.append(maxim[-1][1])
        imagine.append(maxim[-1][2])
        print("Populatie initiala")
        for i in range(1,dimensiue):
            ran=random_numbers[i]
            cromozom_list.append(str(toBinary(ran,int,lun)))
            fct.append(ran)
            imagine.append(functie(ran,x,y,z))
            print("{}.".format(i+1),toBinary(ran,int,lun),"x= ",ran,"f= ",functie(ran,x,y,z),sep=" ")
    else:
        print("Populatie initiala")
        for i in range(0, dimensiue):
            ran = random_numbers[i]
            cromozom_list.append(str(toBinary(ran, int, lun)))
            fct.append(ran)
            imagine.append(functie(ran, x, y, z))
            print("{}.".format(i + 1), toBinary(ran, int, lun), "x= ", ran, "f= ", functie(ran, x, y, z), sep=" ")

    print()
    print("Probabilitate selectie")

    population_dimension=dimensiue

    fitness_values=[]
    for i in random_numbers:
        fitness_values.append(x*(i**2)+(y*i)+z)

    summ = sum(fitness_values)
    partial_values=[sum(fitness_values[:index])/summ for index in range(0,len(fitness_values)+1)]

    final_intervals=[(partial_values[i],partial_values[i+1]) for i in range(0,len(partial_values)-1) ]
    print(final_intervals)
    for index,i in enumerate(final_intervals):
        print("cromozom ",index+1,'{:.{w}f}'.format(final_intervals[index][1]-final_intervals[index][0],sep=" ",w=10))
        # if index==len(final_intervals)-1:
        #     print('{:.{w}f}'.format(final_intervals[index][1],w=10))


    random_numbers = [random.uniform(0, 1) for _ in range(dimensiue)]
    print(random_numbers)
    for index,i in enumerate(random_numbers):
        indexx=binary_search(final_intervals,i)
        print("probabilitate=",i, "selectam cromozomul", indexx+1,sep=" ")
        cromozom_list[index]=cromozom_list[indexx]
        fct[index]=fct[indexx]
        imagine[index]=imagine[indexx]



    print("Dupa selectie:")
    for index,i in enumerate(cromozom_list):
        print("{}.".format(index+1),i,"x= ",fct[index],"f= ",imagine[index],sep=" ")


    random_numbers = [random.uniform(0, 1) for _ in range(dimensiue)]
    pt_crossover=[]
    for index,i in enumerate(cromozom_list):
        if random_numbers[index]<crossover_percent:
            pt_crossover.append([str(i),index])
            print("{}.".format(index + 1), i, "u= ", random_numbers[index],"<{} participa".format(crossover_percent), sep=" ")
        else:
            print("{}.".format(index + 1), i, "u= ", random_numbers[index], sep=" ")

    random_number = [random.randint(0, len(pt_crossover)-1) for _ in range(0,len(pt_crossover))]

    if len(random_number) >=2:
        for i in range(0,len(random_number)-1,2):
            print("Recombinare dintre cromozomul {} cu cromozomul {}:".format(pt_crossover[i][1],pt_crossover[i+1][1]))

            random_index=random.randint(0,lun)
            print(pt_crossover[i][0], pt_crossover[i + 1][0], "punct ",random_index,sep=" ")
            rezultat1,rezultat2=crossover(pt_crossover[i][0], pt_crossover[i + 1][0], random_index)
            print("Rezultat", rezultat1,rezultat2,sep=" ")
            cromozom_list[pt_crossover[i][1]] = rezultat1
            cromozom_list[pt_crossover[i+1][1]] = rezultat2
            total=0
            for j in range(0, len(cromozom_list[pt_crossover[i][1]])):
                if (cromozom_list[pt_crossover[i][1]][j] == '1'):
                    total += 2 ** (len(cromozom_list[pt_crossover[i][1]]) - (j + 1))

            fct[pt_crossover[i][1]]=int[total][0]

            total = 0
            for j in range(0, len(cromozom_list[pt_crossover[i+1][1]])):
                if (cromozom_list[pt_crossover[i+1][1]][j] == '1'):
                    total += 2 ** (len(cromozom_list[pt_crossover[i+1][1]]) - (j + 1))

            fct[pt_crossover[i+1][1]] = int[total][0]

            imagine[pt_crossover[i+1][1]] = functie(fct[pt_crossover[i+1][1]],x,y,z)
            imagine[pt_crossover[i][1]] = functie(fct[pt_crossover[i][1]],x,y,z)

    print("Dupa recombinare:")
    for index,i in enumerate(cromozom_list):
        print("{}.".format(index+1),i,"x= ",fct[index],"f= ",imagine[index],sep=" ")
    print("Au fost modificati cromozomii:")
    lista_mutatii=[[random.uniform(0, 1) for _ in range(0,lun)] for _ in range(0,dimensiue)]
    print(lista_mutatii)
    for index,i in enumerate(cromozom_list):
        for indexx,j in enumerate(lista_mutatii[index]):
            if j<mutatie:
                print(index+1)
                if(i[indexx]=='1'):
                    new_string=i[:indexx]+'0'+i[indexx+1:]
                else:
                    new_string = i[:indexx] + '1' + i[indexx + 1:]
                cromozom_list[index]=new_string
                total = 0
                for j in range(0, len(cromozom_list[index])):
                    if (cromozom_list[index][j] == '1'):
                        total += 2 ** (len(cromozom_list[index]) - (j + 1))
                fct[index] = int[total][0]
                imagine[index] = functie(fct[index], x, y, z)

    print("Dupa mutatie:")
    for index,i in enumerate(cromozom_list):
        print("{}.".format(index+1),i,"x= ",fct[index],"f= ",imagine[index],sep=" ")
    val_maxima=max(imagine)
    indice_maxim=imagine.index(val_maxima)
    maxim.append([cromozom_list[indice_maxim],fct[indice_maxim],val_maxima])
    print(val_maxima)
    print()
    print()
    print()

print("Ecolutia maximului")
for i in maxim:
    print(i[2])


# [['0111011101110000111100', 0.3997011184692383, 2.2399401343636782], ['0111111011010011111110', 0.4862656593322754, 2.249811367886423], ['1000001110011001111111', 0.5422054517759629, 2.248218699840387], ['1000010101110110110000', 0.5640300442715852, 2.2459001534305787], ['1000011111011100110000', 0.5921368979979595, 2.241510792027314], ['0111110001100011101111', 0.4576904773712158, 2.2482099042949244], ['1000010001001001100110', 0.5502438545227051, 2.2474755550827012], ['0111111000110010100101', 0.4788777828216553, 2.249553851941471], ['0111111101110111011000', 0.4937458038330078, 2.249960885030305], ['0111101001010000011011', 0.43336941582623667, 2.245560365252663]]
