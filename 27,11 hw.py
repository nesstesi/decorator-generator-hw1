
def get_string():
    with open ('namefile.txt', 'r') as file:
        content = file.readlines()
        for string in content:
            yield string

if __name__ == '__main__':

    for string in get_string():
        print(string)
