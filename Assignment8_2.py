import threading

def evenfactorfun(no):
    evensum = 0
    for i in range(1, no):
        if ((no % i) == 0):
            if ((i % 2) == 0):
                evensum = evensum+i
    print("EvenSum:", evensum)

def oddfactorfun(no):
    oddsum = 0
    for i in range(1, no):
        if ((no % i) == 0):
            if ((i % 2) != 0):
                oddsum = oddsum + i
    print("OddSum:", oddsum)

def main():
    no = int(input("Enter no.: "))

    evenfactor = threading.Thread(target=evenfactorfun,args=(no,))
    oddfactor = threading.Thread(target=oddfactorfun,args=(no, ))

    evenfactor.start()
    oddfactor.start()

    evenfactor.join()
    oddfactor.join()

if __name__ == "__main__":
    main()