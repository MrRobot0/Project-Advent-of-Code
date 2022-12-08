f = open("4-input.txt")
countDupes = 0

class assignmentPairs:
    def __init__(self, sections = ""):
        sections = sections.strip()
        sections = sections.split(",")
        elf1Range = sections[0].split("-")
        elf2Range= sections[1].split("-")
        self.elf1 = list(range(int(elf1Range[0]), int(elf1Range[1]) + 1))
        self.elf2 = list(range(int(elf2Range[0]), int(elf2Range[1]) + 1))
    def checkDupes(self):
        elf1 = set(self.elf1)
        elf2 = set(self.elf2)
        if elf1.issubset(elf2) or elf2.issubset(elf1):
            global countDupes
            countDupes += 1

def checkDupesImpl(elf1 = [], elf2 = []):
    elf1 = set(elf1)
    elf2 = set(elf2)
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        global countDupes
        countDupes += 1

for line in f:
    s = assignmentPairs(line)
    s.checkDupes()

print(countDupes)