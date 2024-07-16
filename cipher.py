alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode(plane_text,shift_key):   
  encoded_text=""
  for char in plane_text: 
    if char in alphabets: 
     position=alphabets.index(char) 
     new_position=(position+shift_key)%26 
     encoded_text+=alphabets[new_position] 
    else:
      encoded_text+=char 
  print(f"The encoded text is {encoded_text}") 

def decode(cipher_text,shift_key): 
  plane_text=""
  for char in cipher_text: 
    if char in alphabets:
     position=alphabets.index(char) 
     new_position=(position-shift_key)%26 
     plane_text+=alphabets[new_position] 
    else:
      plane_text+=char
  print(f"The encoded text is {plane_text}") 
end_game=False
while not end_game:
  what_to_do=input("What do you want to do? encode or decode: ")
  text=input("Enter the text: ")
  shift=int(input("Enter the shift: "))
  if what_to_do=="encode":
    encode(plane_text=text,shift_key=shift)
  elif what_to_do=="decode":
    decode(text,shift)
  play_again=input("type 'yes' to continue and 'no' to exit:")
  if play_again=="no":
    end_game=True
    print("HAVE A NICE DAY!")