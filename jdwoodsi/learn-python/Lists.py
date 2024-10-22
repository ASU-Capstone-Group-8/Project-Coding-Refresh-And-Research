thisisalist = ["no", "it", "is", "not", 1, 2, -1, True]
yesitis = ["oh", "okay"]

print(thisisalist)

thisisalist.extend(yesitis)

print(thisisalist)

thisisalist.remove(1)
thisisalist.remove(2)
thisisalist.remove(-1)
thisisalist.remove(True)

thisisalist.sort()

print(thisisalist)

