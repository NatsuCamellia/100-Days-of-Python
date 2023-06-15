import json

def main():
    mydict = {
        'name': 'Eve',
        'age': 19,
        'friends': ['Alice', 'Bob'],
        'score': [
            {'subject': 'English', 'point': 80},
            {'subject': 'Chinese', 'point': 90},
            {'subject': 'Science', 'point': 85}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(mydict, file)
    except IOError as e:
        print(e)
    print('Done')


if __name__ == '__main__':
    main()