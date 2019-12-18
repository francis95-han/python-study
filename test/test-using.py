import base64
import os


def main():
    print(os.path.abspath(__file__))
    a = "aa"
    for i in range(1, 10):
        a = base64.b64encode(bytes(str(a), encoding="utf-8"))
    print(a)


if __name__ == '__main__':
    main()
