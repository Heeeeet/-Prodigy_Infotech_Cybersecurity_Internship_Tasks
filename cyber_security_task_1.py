def caesar_cipher(text, shift, mode):
    result = ""
    if mode.lower() == "decrypt":
        shift = -shift  # Reverse the shift for decryption
    
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Apply the shift and wrap around using modulo
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result


def main():
    print("Caesar Cipher Tool")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    
    choice = input("Choose an option (1 or 2): ")
    if choice not in ['1', '2']:
        print("Invalid choice. Exiting...")
        return

    text = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Exiting...")
        return

    mode = "encrypt" if choice == '1' else "decrypt"
    result = caesar_cipher(text, shift, mode)
    print(f"Result ({mode.title()}ed Message): {result}")


if __name__ == "__main__":
    main()