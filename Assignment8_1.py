import threading

def evenfun(number):
    for i in range(0, number):
        if ((i % 2) == 0):
            print(i)

def oddfun(number):
    for i in range(0, number):
        if ((i % 2) != 0):
            print(i)

def main():
    number = 10

    even = threading.Thread(target=evenfun,args=(number,))
    odd = threading.Thread(target=oddfun,args=(number,))

    print("Even:")
    even.start()
    print("Odd:")
    odd.start()

    even.join()
    odd.join()

if __name__ == "__main__":
    main()