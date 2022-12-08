f = open("4-input.txt")
countOverlap = 0

class assignmentPairs:
    def __init__(self, sections = ""):
        sections = sections.strip()
        sections = sections.split(",")
        elf1Range = sections[0].split("-")
        elf2Range= sections[1].split("-")
        self.elf1 = list(range(int(elf1Range[0]), int(elf1Range[1]) + 1))
        self.elf2 = list(range(int(elf2Range[0]), int(elf2Range[1]) + 1))
    def checkDupes(self):
        checkDupesImpl(self.elf1, self.elf2)


def checkDupesImpl(elf1 = [], elf2 = []):
    overlap = False
    for num in elf1:
        if num in elf2:
            overlap = True
    if overlap:
        global countOverlap
        countOverlap += 1

for line in f:
    s = assignmentPairs(line)
    s.checkDupes()

print(countOverlap)