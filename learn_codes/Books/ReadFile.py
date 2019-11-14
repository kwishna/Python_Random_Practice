file_to_read = input("Enter The .txt File Name To Read In directory ./files : ")

if file_to_read == "" or file_to_read is None:
    file_to_read = 'readme.txt'

if not file_to_read[-4:].__eq__('.txt'):  # __eq__(str) means equals
    print("Adding .txt Extension Into The Provided File Name")
    file_to_read = file_to_read + '.txt'

data = open("./files/" + file_to_read, 'r')  # Opening File In Read Mode
print(data.read(3))  # Reading 'int' number Characters Content Of The File
print(data.__sizeof__())  # size of object in memory in bytes
print(data.readlines())  # Reading As List
print(data.tell())  # No Of The Characters

print('*******************************************')

with open("./files/" + file_to_read, 'r') as d:  # Assigning Long Expression Into small 'd'
    for i in range(4):
        print(d.readline())  # Reads Line By Line
    d.close()

print('*******************************************')
data.seek(10) # Rewind To Some Bytes. Just Like DVD Or Cassette
print(data.readline(), end='') # By Default readline Adds \n At The End Of The Line
