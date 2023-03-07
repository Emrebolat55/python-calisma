def print_tahta(tahta):
    print(f"{tahta[0]} | {tahta[1]} | {tahta[2]}")
    print("---------")
    print(f"{tahta[3]} | {tahta[4]} | {tahta[5]}")
    print("---------")
    print(f"{tahta[6]} | {tahta[7]} | {tahta[8]}")

def check_win(tahta, oyuncu):
    # satırları kontrol et
    for i in range(0, 9, 3):
        if tahta[i:i+3] == [oyuncu]*3:
            return True
    # kontrol sütunları
    for i in range(3):
        if tahta[i::3] == [oyuncu]*3:
            return True
    # köşegenleri kontrol et
    if tahta[0] == tahta[4] == tahta[8] == oyuncu :
        return True
    if tahta[2] == tahta[4] == tahta[6] == oyuncu :
        return True
    return False

def main():
    tahta = [str(i+1) for i in range(9)]
    print_tahta(tahta)
    oyuncu = "X"
    while True:
        move = int(input(f"{oyuncu}'s turn, bir pozisyon girin (1-9): "))
        if tahta[move-1] != "X" and tahta[move-1] != "O":
            tahta[move-1] = oyuncu
            print_tahta(tahta)
            if check_win(tahta, oyuncu):
                print(f"{player} wins!")
                break
            if all([pos == "X" or pos == "O" for pos in tahta]):
                print("Tie!")
                break
            oyuncu = "O" if oyuncu == "X" else "X"
        else:
            print("O pozisyon çoktan alındı!")

if __name__ == "__main__":
    main()
