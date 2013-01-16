#!/usr/bin/python -tt
# solution written by Brad Kusnir 12/12/12

"""

Ticket Lottery
Problem ID: lottery

You and your friends are in New York and are planning to go see a Broadway 
musical. Unfortunately, New York being New York, the tickets are just a tiny bit 
expensive. But one of the shows has a ticket lottery each night where 
impecunious people such as you have a chance to win the right to buy slightly 
less expensive tickets to good seats. The lottery operates as follows. First, 
everyone interested enters the lottery. Then, n lucky winners are drawn, and 
each of these is offered to buy up to t tickets.
Given the number of people p in your group (all of which entered the lottery) 
and the total number of people m that entered the lottery, what is the 
probability that you will be able to get tickets for your entire group? Assume 
that the n lucky winners are chosen uniformly at random from the m people that 
entered the lottery, and that each person can win at most once.

Input
The input consists of a single line containing four integers:

1 <= m <= 1000: the total number of people who entered the lottery.
1 <= n <= m: the total number of winners drawn.
1 <= t <= 100: the number of tickets each winner is allowed to buy.
1 <= p <= m: the number of people in your group.

Output
Output a single line containing the probability that your entire group can get 
tickets to the show. This probability should be given with an absolute error of
at most 10^-9.

Sample input 1
100 10 2 1
	
Sample output 1
0.1
	
Sample input 2
100 10 2 2
	
Sample output 2
0.1909090909

Sample input 3
10 10 5 1

Sample output 3
1.0000000000

"""

from decimal import *
import sys

def lottery(line):
  # convert the input string into a list
  inputstr_list = line.split()

  m = int(inputstr_list[0])
  # the total number of winners drawn.
  n = int(inputstr_list[1])
  # the number of tickets each winner is allowed to buy.
  t = int(inputstr_list[2])
  # the number of people in your group.
  p = int(inputstr_list[3])

  # perform input validation
  if (m < 1) or (m > 1001):
  	print '1 <= m <= 1000'
  	return
  if (n < 1) or (n > m):
  	print '1 <= n <= m'
  	return
  if (t < 1) or (t > 100):
  	print '1 <= t <= 100'
  	return
  if (p < 1) or (p > m):
  	print '1 <= p <= m'
  	return

  # compute probability

  # set precision to 10^-9
  getcontext().prec = 10
  counter = 0
  probability = 0.0
  while counter < p:
  	# calculate the probability of the current person winning, add it to the previous probability
  	probability = Decimal(probability) + Decimal(float(n-counter)/(m-counter))
  	counter = counter + 1
  print Decimal(probability)

if __name__ == '__main__':
  for line in sys.stdin:
    lottery(line.strip())