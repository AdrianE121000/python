import string
import secrets

def generar():
    alfabeto = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alfabeto) for i in range(4,16))

    print(password,"\n")

def main():
    while True:
        generar()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()