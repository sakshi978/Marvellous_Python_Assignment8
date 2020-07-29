import threading

def smallfun(str):
    smallsum = 0
    for i in range(0, len(str)):
        if((str[i] >= 'a') and (str[i] <= 'z')):
           smallsum = smallsum+1
    print("Sum of small letters:", smallsum)

def capitalfun(str):
    capitalsum = 0
    for i in range(0, len(str)):
        if ((str[i] >= 'A') and (str[i] <= 'Z')):
            capitalsum = capitalsum + 1
    print("Sum of capital letters:", capitalsum)

def digitfun(str):
    digitsum = 0
    for i in range(0, len(str)):
        if ((str[i] >= '0') and (str[i] <= '9')):
            digitsum = digitsum + 1
    print("Sum of digits:", digitsum)

def main():
    str = input("Enter string: ")

    smallthread = threading.Thread(target=smallfun,args=(str, ))
    capitalthread = threading.Thread(target=capitalfun,args=(str, ))
    digitthread = threading.Thread(target=digitfun,args=(str, ))

    smallthread.start()
    capitalthread.start()
    digitthread.start()

    smallthread.join()
    capitalthread.join()
    digitthread.join()

if __name__ == "__main__":
    main()