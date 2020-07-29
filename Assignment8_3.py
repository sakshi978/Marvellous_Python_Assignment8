import threading

def evenfun(iplist):
    evensum = 0
    for i in range(0, len(iplist)):
        if ((iplist[i] % 2) == 0):
            print(iplist[i])
            evensum = evensum+iplist[i]
    print("Sum:", evensum)

def oddfun(iplist):
    oddsum = 0
    for i in range(0, len(iplist)):
        if ((iplist[i] % 2) != 0):
            print(iplist[i])
            oddsum = oddsum + iplist[i]
    print("Sum:" ,oddsum)

def main():
    iplist = [1,3,5,4,6,9,7,11,13,16]

    evenlist = threading.Thread(target=evenfun,args=(iplist, ))
    oddlist = threading.Thread(target=oddfun,args=(iplist, ))

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()

if __name__ == "__main__":
    main()