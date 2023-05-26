alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(direction, text, shift):
    final_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        position = alphabet.index(letter)
        final_text += alphabet[(position + shift) % 26]
    print(f"{text} --> {final_text}\n")


while True:
    restart = 0
    direction = input(
        "\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)
        restart = 1
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)
        restart = 1
    else:
        print("Wrong entry. Try again.\n")

    if restart == 1:
        while True:
            choice = input(
                "Type 'yes' if you want to go again. Otherwise, type 'no':")
            if choice == "yes":
                restart = 1
                break
            elif choice == "no":
                restart = 0
                break
            else:
                print("Wrong entry. Try again.\n")
        if restart == 0:
            break
