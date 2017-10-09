from __future__ import absolute_import, division, print_function, unicode_literals
import random
next=0
line1=[]
line2=[]
line3=[]
count=9
first=["  1  ","  2  ","  3  ","  4  ","  5  ","  6  ","  7  ","  8  ","  9  "," 10  "]
second=[" 11  "," 12  "," 13  "," 14  "," 15  "," 16  "," 17  "," 18  "," 19  "," 20  "]
third=[" 21  "," 22  "," 23  "," 24  "," 25  "," 26  "," 27  "," 28  "," 29  "," 30  "]
print("________  ________      _____    ________   _____     _____       ")
print("\___  __\ \___  __\    /  ___\   \___  __\  | __ \   /  ___\      ")
print("    \ \       \ \     (  /           \ \    | |_\ \ (  /          ")
print("     \ \       \ \     \ \            \ \   | ____ \ \ \          ")
print("      \ \     __\ \___  \ `-_____      \ \  | |   \ \ \ `-_____   ")
print("       \_\    \_______\   `-_____\      \_\ |_|    \_\  `-_____\  ")
print("                                ___                               ")
print("                               /__/                               ")
print("__   __  __   __  __     ___  ______  ______       _    ______  ")
print("\ `- \ \ \ \  \ \ \ `-,  |  \ \  ___\ \  __ `,    / _`\ \    |  ")
print(" \  `-\ \ \ \  \ \ \   `-|   \ \ \____ \ \_)  )  ( | \ \ \   |  ")
print("  \      \ \ \  \ \ \         \ \  ___\ \  _  \   \ \ \ \ \__|  ")
print("   \ \-,  \ \ \__\ \ \ \-,  |\ \ \ \____ \ \ `- `, \ \_| )  __  ")
print("    \_\ `-_\ `-____/  \_\ `-| \_\ \_____\ \_\  `-_\  `-_/   \_\ ")
print()
print()
while count>6:
    next=random.randrange(count)
    line1.append(first[next-1])
    first.pop(next-1)
    count=count-1

while count>3:
    next=random.randrange(count)
    line2.append(first[next-1])
    first.pop(next-1)
    count=count-1

while count>0:
    next=random.randrange(count)
    line3.append(first[next-1])
    first.pop(next-1)
    count=count-1


line1.append("        ")
line2.append("        ")
line3.append("        ")

count=9
while count>6:
    next=random.randrange(count)
    line1.append(second[next-1])
    second.pop(next-1)
    count=count-1

while count>3:
    next=random.randrange(count)
    line2.append(second[next-1])
    second.pop(next-1)
    count=count-1

while count>0:
    next=random.randrange(count)
    line3.append(second[next-1])
    second.pop(next-1)
    count=count-1


line1.append("        ")
line2.append("        ")
line3.append("        ")

count=9
while count>6:
    next=random.randrange(count)
    line1.append(third[next-1])
    third.pop(next-1)
    count=count-1
print("".join(str(x) for x in line1))
print()
while count>3:
    next=random.randrange(count)
    line2.append(third[next-1])
    third.pop(next-1)
    count=count-1
print("".join(str(x) for x in line2))
print()
while count>0:
    next=random.randrange(count)
    line3.append(third[next-1])
    third.pop(next-1)
    count=count-1
print("".join(str(x) for x in line3))
print()

print()
print()

next=0
line1=[]
line2=[]
line3=[]
count=9
first=[" 31  "," 32  "," 33  "," 34  "," 35  "," 36  "," 37  "," 38  "," 39  "," 40  "]
second=[" 41  "," 42  "," 43  "," 44  "," 45  "," 46  "," 47  "," 48  "," 49  "," 50  "]
third=[" 51  "," 52  "," 53  "," 54  "," 55  "," 56  "," 57  "," 58  "," 59  "," 60  "]
while count>6:
    next=random.randrange(count)
    line1.append(first[next-1])
    first.pop(next-1)
    count=count-1

while count>3:
    next=random.randrange(count)
    line2.append(first[next-1])
    first.pop(next-1)
    count=count-1

while count>0:
    next=random.randrange(count)
    line3.append(first[next-1])
    first.pop(next-1)
    count=count-1


line1.append("        ")
line2.append("        ")
line3.append("        ")

count=9
while count>6:
    next=random.randrange(count)
    line1.append(second[next-1])
    second.pop(next-1)
    count=count-1

while count>3:
    next=random.randrange(count)
    line2.append(second[next-1])
    second.pop(next-1)
    count=count-1

while count>0:
    next=random.randrange(count)
    line3.append(second[next-1])
    second.pop(next-1)
    count=count-1


line1.append("        ")
line2.append("        ")
line3.append("        ")

count=9
while count>6:
    next=random.randrange(count)
    line1.append(third[next-1])
    third.pop(next-1)
    count=count-1
print("".join(str(x) for x in line1))
print()
while count>3:
    next=random.randrange(count)
    line2.append(third[next-1])
    third.pop(next-1)
    count=count-1
print("".join(str(x) for x in line2))
print()
while count>0:
    next=random.randrange(count)
    line3.append(third[next-1])
    third.pop(next-1)
    count=count-1
print("".join(str(x) for x in line3))
print()

print()
print()

next=0
line1=[]
line2=[]
line3=[]
count=9
first=[" 61  "," 62  "," 63  "," 64  "," 65  "," 66  "," 67  "," 68  "," 69  "," 70  "]
second=[" 71  "," 72  "," 73  "," 74  "," 75  "," 76  "," 77  "," 78  "," 79  "," 80  "]
third=[" 81  "," 82  "," 83  "," 84  "," 85  "," 86  "," 87  "," 88  "," 89  "," 90  "]
while count>6:
    next=random.randrange(count)
    line1.append(first[next-1])
    first.pop(next-1)
    count=count-1

while count>3:
    next=random.randrange(count)
    line2.append(first[next-1])
    first.pop(next-1)
    count=count-1

while count>0:
    next=random.randrange(count)
    line3.append(first[next-1])
    first.pop(next-1)
    count=count-1


line1.append("        ")
line2.append("        ")
line3.append("        ")

count=9
while count>6:
    next=random.randrange(count)
    line1.append(second[next-1])
    second.pop(next-1)
    count=count-1

while count>3:
    next=random.randrange(count)
    line2.append(second[next-1])
    second.pop(next-1)
    count=count-1

while count>0:
    next=random.randrange(count)
    line3.append(second[next-1])
    second.pop(next-1)
    count=count-1


line1.append("        ")
line2.append("        ")
line3.append("        ")

count=9
while count>6:
    next=random.randrange(count)
    line1.append(third[next-1])
    third.pop(next-1)
    count=count-1
print("".join(str(x) for x in line1))
print()
while count>3:
    next=random.randrange(count)
    line2.append(third[next-1])
    third.pop(next-1)
    count=count-1
print("".join(str(x) for x in line2))
print()
while count>0:
    next=random.randrange(count)
    line3.append(third[next-1])
    third.pop(next-1)
    count=count-1
print("".join(str(x) for x in line3))
print()

print()
print()

next=0
line1=[]
line2=[]
line3=[]
count=9
first=[" 91  "," 92  "," 93  "," 94  "," 95  "," 96  "," 97  "," 98  "," 99  "," 100 "]
second=[" 101 "," 102 "," 103 "," 104 "," 105 "," 106 "," 107 "," 108 "," 109 "," 110 "]
third=[" 111 "," 112 "," 113 "," 114 "," 115 "," 116 "," 117 "," 118 "," 119 "," 120 "]
while count>6:
    next=random.randrange(count)
    line1.append(first[next-1])
    first.pop(next-1)
    count=count-1

while count>3:
    next=random.randrange(count)
    line2.append(first[next-1])
    first.pop(next-1)
    count=count-1

while count>0:
    next=random.randrange(count)
    line3.append(first[next-1])
    first.pop(next-1)
    count=count-1


line1.append("        ")
line2.append("        ")
line3.append("        ")

count=9
while count>6:
    next=random.randrange(count)
    line1.append(second[next-1])
    second.pop(next-1)
    count=count-1

while count>3:
    next=random.randrange(count)
    line2.append(second[next-1])
    second.pop(next-1)
    count=count-1

while count>0:
    next=random.randrange(count)
    line3.append(second[next-1])
    second.pop(next-1)
    count=count-1


line1.append("        ")
line2.append("        ")
line3.append("        ")

count=9
while count>6:
    next=random.randrange(count)
    line1.append(third[next-1])
    third.pop(next-1)
    count=count-1
print("".join(str(x) for x in line1))
print()
while count>3:
    next=random.randrange(count)
    line2.append(third[next-1])
    third.pop(next-1)
    count=count-1
print("".join(str(x) for x in line2))
print()
while count>0:
    next=random.randrange(count)
    line3.append(third[next-1])
    third.pop(next-1)
    count=count-1
print("".join(str(x) for x in line3))
print()
