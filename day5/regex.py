import re

def main():
    username = input('Username：')
    id = input('ID：')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('Please enter valid username.')
    m2 = re.match(r'^[A-Z]\d{9}$', id)
    if not m2:
        print('Please enter valid id.')
    if m1 and m2:
        print('Valid!')


if __name__ == '__main__':
    main()