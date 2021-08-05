coisas = ['\n', '\f']


def checkValidName(city: str):
    for char in city:
        if char.isdigit() or char == '\f':
            return False
    return True


file = 'txtFiles/dataBase.txt'
archive = open(file, 'r')
read = archive.readlines()
read.insert(0, '\x0cCALCUTTA')
upper_case = []
for line in range(len(read)):
    word = read[line].replace('\n', '')
    checkValidName(word)
    if word[0].isupper():
        upper_case.append(word[0])
print(upper_case)