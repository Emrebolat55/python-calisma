import time

def main():
    message = "İyi ki doğdun Furkan"
    for i in range(len(message)):
        print(message[:i+1])
        time.sleep(0.5)

if __name__ == '__main__':
    main()
