#!/usr/bin/python -tt
# solution written by Brad Kusnir 01/15/13

"""

Reversed Binary Numbers
Problem ID: reversebinary

Yi has moved to Sweden and now goes to school here. The first years of schooling 
she got in China, and the curricula do not match completely in the two 
countries. Yi likes mathematics, but now... The teacher explains the algorithm 
for subtraction on the board, and Yi is bored. Maybe it is possible to perform 
the same calculations on the numbers corresponding to the reversed binary 
representations of the numbers on the board? Yi dreams away and starts 
constructing a program that reverses the binary representation, in her mind. As 
soon as the lecture ends, she will go home and write it on her computer.

Task
Your task will be to write a program for reversing numbers in binary. For 
instance, the binary representation of 13 is 1101, and reversing it gives 1011, 
which corresponds to number 11.

Input
The input contains a single line with an integer N, 1 <= N <= 1000000000.

Output
Output one line with one integer, the number we get by reversing the binary 
representation of N.

Sample Input 1		Sample Output 1
13					11

Sample Input 2		Sample Output 2
47					61

"""

import sys

def reverse_binary(N):
	N = int(N)
	if 1 <= N <= 1000000000:
		pass
	else:
		print 'input error: 1 <= N <= 1000000000'
	# convert int to binary string representation
	binary = '{0:08b}'.format(N)

	# remove leading 0's
	first_one = binary.find('1')
	binary_truncated = binary[first_one:]
	reverse_binary = binary_truncated[::-1]

	# add leading 0's
	prefix_zeros = 8 - len(reverse_binary)
	counter = 0
	while counter <= prefix_zeros:
	  reverse_binary = '0' + reverse_binary
	  counter = counter + 1

	# convert string representation to int
	print int(reverse_binary, 2)

if __name__ == '__main__':
  for line in sys.stdin:
    reverse_binary(line.strip())