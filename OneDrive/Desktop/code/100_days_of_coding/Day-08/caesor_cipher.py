import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser_cipher(original_text, shift, encode_or_decode):
  output=""
  if encode_or_decode=="decode":
    shift*=-1
  
  for i in original_text:
    if i not in alphabet:
      output+=i
    else:
      position=alphabet.index(i) + shift
      position%=len(alphabet)
      output+=alphabet[position]
      
  print(f"the {encode_or_decode}d text is {output}")


should_try=True

while should_try:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  ceaser_cipher(text, shift, direction)
  restart=input("type yes to continue or no to end \n")
  if restart=="no":
    should_try=False
    print("thank you")




# def encrypt(original_text, shift_amoutnt):
#   cipher_text=""
#   for letter in original_text:
#     position=alphabet.index(letter) + shift_amoutnt
#     position%=len(alphabet)
#     cipher_text+=alphabet[position]
#   print(f"Here is the encoded result {cipher_text}")

# encrypt(original_text="lava", shift_amoutnt=7)

# def encrypt(original_text, shift_amoutnt):
#   cipher_text=""
#   for letter in original_text:
#     position=alphabet.index(letter) + shift_amoutnt
#     position%=len(alphabet)
#     cipher_text+=alphabet[position]
#   print(f"Here is the encoded result {cipher_text}")

# encrypt(original_text="lava", shift_amoutnt=7)

# def decrypt(original_text, shift_amoutnt):
#   cipher_text=""
#   for letter in original_text:
#     position=alphabet.index(letter) - shift_amoutnt
#     position%=len(alphabet)
#     cipher_text+=alphabet[position]
#   print(f"Here is the decoded result {cipher_text}")

# decrypt(original_text="lava", shift_amoutnt=7)
