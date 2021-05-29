import string
import threading

value = 1

def checkChangeValue():
    global value
    while True:
        newValue = input()
        if newValue.isdigit():
            value = int(newValue)

def main():
    print("Value is {}".format(value))


if __name__ == '__main__':
    threading.Thread(target=checkChangeValue).start()
    while True:
       main()
