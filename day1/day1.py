callist = open("day1/input.txt")

elflist = []
allcals = []
for cal in callist:
  if cal.strip() == "":
    elflist.append(sum(allcals))
    allcals = []
  else:
    allcals.append(int(cal.strip()))

# puzzle 1
elflist.append(sum(allcals))
print(max(elflist))

# puzzle 2
elflist.sort(reverse=True)
top3 = elflist[0:3]
print(sum(top3))

