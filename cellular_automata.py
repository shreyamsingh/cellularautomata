import sys
from random import randint
from time import sleep
rulenum = 0

# determine how many inputs
if (len(sys.argv) > 1):
    try:
        n = int(sys.argv[1])
    except:
        print("Please enter an integer for the number of generations.")
        n = 66
else:
    n = 66
if (len(sys.argv) > 2):
    try:
        rulenum = int(sys.argv[2])
    except:
        print("Please enter a rule number between 0 and 256.")
        rulenum = 90
else:
    rulenum = 90
cells = ""
for i in range(n*2):
    #non-randomized initial condition
    if (i == n-1):
        cells += "1"
    else:
        cells += "0"
    #randomized initial condition
    #cells += str(randint(0, 1))

rulestr = bin(rulenum)
rulestr = rulestr[2:]
while (len(rulestr) < 8):
    rulestr = '0' + rulestr
rule = {"111": '0', "110": '1', "101": '0', "100": '1',
        "011": '1', "010": '0', "001": '1', "000": '0'}
counter = 0
for x in rule:
    rule[x] = rulestr[counter]
    counter = counter + 1
def triplet(iterable, stride=3):
    for i in range(len(iterable) - stride + 1):
        yield iterable[i:i + stride]
def output(iterable):
    current = ""
    for i in range(len(iterable)):
        if (iterable[i] == '1'):
            current += '.'
        else:
            current += ' '
        sleep(.0001)
    print(current)
# print(list(triplet(cells)))
for i in range(int(n-2)):
    output(cells)
    new_state = ''
    for i in triplet(cells):
        new_state += rule[i]
    cells = new_state
    cells = '0{}0'.format(cells)
