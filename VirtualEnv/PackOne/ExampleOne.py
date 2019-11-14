import random


def rgb():
    NUMBER = random.randint(0, 255) / 255
    return NUMBER


FILE = open('sample1.csv', 'w')
FILE.write('RED, GREEN, YELLOW')

for count in range(15):
    FILE.write('\n{:0.2f},{:0.2f},{:0.2f}'.format(rgb(), rgb(), rgb()))
