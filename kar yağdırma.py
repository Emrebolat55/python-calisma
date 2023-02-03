import random
import time

def snowflake():
    return "*" if random.random() > 0.5 else "."

def main():
    while True:
        print(" ".join(snowflake() for i in range(80)))
        time.sleep(0.1)

if __name__ == '__main__':
    main()
