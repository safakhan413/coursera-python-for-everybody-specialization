# 9.4 Write a program to read through the mbox-short.txt and figure out
# who has sent the greatest number of mail messages. The program looks for
# 'From ' lines and takes the second word of those lines as the person who
# sent the mail. The program creates a Python dictionary that maps the
# sender's mail address to a count of the number of times they appear '
# in the file. After the dictionary is produced, the program reads through
# the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

committers = dict()
for line in handle:
    if not line.startswith('From '):continue
    email = line.split()[1]
    committers[email] = committers.get(email,0)+1

bigCount = None
bigEmail = None
for word,count in committers.items():
    if bigEmail is None or bigCount < count:
        bigEmail = word
        bigCount = count
print(bigEmail  + ' ' + str(bigCount))