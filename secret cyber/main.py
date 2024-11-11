#avery secret cyber


def encode_message(message, shift):
   """Encodes a message using a shift cipher."""
   encoded_message = ""
   for char in message:
       if char.isalpha():
           # Preserve case (upper or lower)
           start = ord('A') if char.isupper() else ord('a')
           # Shift character and wrap around alphabet if necessary
           encoded_char = chr(start + (ord(char) - start + shift) % 26)
           encoded_message += encoded_char
       else:
           # Non-alphabet characters stay the same
           encoded_message += char
   return encoded_message


def decode_message(encoded_message, shift):
   """Decodes a message encoded with a shift cipher."""
   decoded_message = ""
   for char in encoded_message:
       if char.isalpha():
           # Preserve case (upper or lower)
           start = ord('A') if char.isupper() else ord('a')
           # Reverse shift to decode
           decoded_char = chr(start + (ord(char) - start - shift) % 26)
           decoded_message += decoded_char
       else:
           # Non-alphabet characters stay the same
           decoded_message += char
   return decoded_message


# Example usage
user_message = input("Enter a message to encode: ")
shift_value = int(input("Enter shift amount: "))


encoded = encode_message(user_message, shift_value)
print("Encoded message:", encoded)


# Decode to verify
decoded = decode_message(encoded, shift_value)
print("Decoded message:", decoded)
