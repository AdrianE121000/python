import random

def generate_password():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbols = "!@#$%*/\?.,:;"

    Use_for =  lower_case + upper_case + number + symbols 
    length_for_pass = 16

    password = "".join(random.sample(Use_for,length_for_pass))

    print(password,"\n")

def main():
    while True:
        generate_password()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()