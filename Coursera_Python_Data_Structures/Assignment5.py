# Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the string
# a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

timeCounts = dict()
for line in handle:
    if not line.startswith('From '):continue
    pos = line.find(':')
    time = line[pos-2:pos]
    timeCounts[time] = timeCounts.get(time,0)+1

# vkpairs = [(k,v) for k,v in timeCounts.items()]
# # print(sorted(vkpairs))
# print(vkpairs)
for k,v in sorted(timeCounts.items()):
    print(k + ' ' + str(v))

