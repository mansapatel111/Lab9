def encoder(string):
    for i in string:
        i = int(i)
        i += 3
    return string

# def decoder(string):
#     for i in string:
#         i = int(i)
#         i -= 3
#     return string

def main():
    while True:
        main_menu = ("""Menu
        -------------
        1. Encode
        2. Decode
        3. Quit""")
        print(main_menu)

        option_input = int(input("Please enter an option: "))



        if option_input == 1:
            encode_input = input("Please enter your password to encode: ")
            encoded_password = encoder(encode_input)
            print("Your password has been encoded and stored!")
        elif option_input == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {encode_input}")
        elif option_input == 3:
            break



if __name__ == "__main__":
     main()