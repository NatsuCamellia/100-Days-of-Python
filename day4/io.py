def main():
    with open('lorem.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
        file.close()

if __name__ == '__main__':
    main()