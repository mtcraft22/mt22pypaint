import sys, datetime


Entry=sys.argv[1]
def key_gen(seed):
    return seed

print("")




key={
    "Q":999,
    "W":888,
    "E":352,
    "R":110,
    "T":189,
    "Y":302,
    "U":653,
    "I":178,
    "O":732,
    "P":987,
    "A":257,
    "S":138,
    "D":000,
    "F":830,
    "G":1,
    "H":11,
    "J":13,
    "K":16,
    "L":2343324,
    "Ñ":1611,
    "Z":124353443543,
    "X":344443432122321,
    "C":9892182398329,
    "V":1928,
    "B":1456,
    "N":38875,
    "M":123445,
    "À":213321325,
    "È":546555656,
    "Ì":55343123,
    "Ò":235661,
    "Ù":12456,
    "Á":64667,
    "É":224124,
    "Í":798898,
    "Ó":123123,
    "Ú":4654646,
    " ":400099111,
}
result=""

for i in Entry:
    result += str(key[i])

print(result)