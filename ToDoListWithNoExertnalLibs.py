saveFile = open('to do list without external libs save file.txt', mode='r+')
missions = {}
indexOfMission = 1

def main():
    while True:
        print('''
        1. add mission
        2. delete item
        3. save
        4. load
        5. quit
        ''')
        selectTheAction = int(input('select the case: '))
        if selectTheAction == 1:
            addMission(task())
        elif selectTheAction == 2:
            deleteMissions()
        elif selectTheAction == 3:
            save()
        elif selectTheAction == 4:
            load()
        elif selectTheAction == 5:
            break



def task():
    task = str(input('enter the unfinished mission: '))
    return task

def addMission(task):
    global indexOfMission
    global missions
    print(task)
    missions[indexOfMission] = task
    indexOfMission += 1
    print(missions)

def deleteMissions():
    global missions
    indexToBeDeleted = int(input('index to b deleted: '))

    del missions[indexToBeDeleted]
    print(missions)

def save():
    with open('to do list without external libs save file.txt',mode='w') as saveFile:
        saveFile.write(str(missions))
    print('successfully changed! ')


def load():
    with open('to do list without external libs save file.txt',mode='r') as saveFile:
        saveFile.seek(0)
        print(saveFile.readlines())

main()


