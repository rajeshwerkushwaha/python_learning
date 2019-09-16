# read all at once
f = open('sample.txt', 'r')
print(f.read())


# read line by line when file is small
f = open('sample.txt', 'r')
for line in f:
	print(line)

# read line by line when file is big
f = open('sample.txt', 'r')
while True:
	line = f.readline()
	print(line)
	if ("" == line):
		break;


# new file create move
f = open('sample1.txt', 'x')
f.write('This msg writes through f.write()')
f = open('sample1.txt', 'r')
print(f.read())


# append mode
f = open('sample.txt', 'a')
f.write('\nThis line written by f.write() in append mode')


# write mode
f = open('sample2.txt', 'w')
f.write('\nThis line written by f.write() in wite mode (overwrite mode)')


# delete a file
import os
os.remove('sample1.txt')