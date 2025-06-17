
import string

ALPHABET = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

def shift_char(c: str, shift: int) -> str:
    """Shift a single character by `shift` positions, preserving case."""
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        # modulo 26 keeps shift in alphabet range
        return chr((ord(c) - base + shift) % 26 + base)
    return c  # non-letters unchanged

def caesar_cipher(text: str, shift: int) -> str:
    """Return text after applying Caesar shift (positive = encrypt, negative = decrypt)."""
    return ''.join(shift_char(ch, shift) for ch in text)

def main():
    print("=== Caesar Cipher ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()
    if choice not in ('e', 'd'):
        print("Invalid option. Exiting.")
        return

    message = input("Enter the message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Shift must be an integer. Exiting.")
        return

    # For decryption we invert the shift
    if choice == 'd':
        shift = -shift

    result = caesar_cipher(message, shift)
    print("\nResult:", result)

if __name__ == "__main__":
    main()

