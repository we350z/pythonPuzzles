#!/usr/bin/python -tt
# solution written by Brad Kusnir 12/12/12

"""

Best Before
Problem ID: bestbefore

Just about any product found in a grocery store has a "best before" date printed
on it. Unfortunately, the format for these dates can vary quite a bit: what is 
it supposed to mean that the bread you bought yesterday is "best before 
12/11/10"? It could mean that the bread expires on November 10, 2012 (now that's
a suspiciously durable bread and probably it is not healthy for you for other 
reasons!), or it could mean that the bread expired on December 11, 2010 (d'oh!),
or a variety of other options. To be safe, the truly paranoid (or healthily 
skeptic, depending on who you ask) person would assume that it means "best 
before November 12, 2010", since that is the earliest possible date. On the 
other hand, seeing "31/5/2012" even the truly paranoid person knows that this 
must mean May 31, 2012 since that is the only possible real date using these 
three numbers.

Given a possibly ambiguous date "A/B/C", where A,B,C are integers between 0 and
2999, output the earliest possible legal date between Jan 1, 2000 and Dec 31, 
2999 (inclusive) using them as day, month and year (but not necessarily in that 
order).

Recall that a year is a leap year (has 366 days) if the year is divisible by 4,
unless it is divisible also by 100 but not by 400 (so 2000 is a leap year, 2100
is not a leap year, and 2012 is a leap year).

Input
The input file consists of a single line containing three integers separated by
"/". There are no extra spaces around the "/". Years may be truncated to two 
digits and may in that case also omit the leading 0 (if there is one), so 2000 
could be given as "2000", "00" or "0" (but not as an empty string). Months and 
days may be zero-padded. You may assume that the year, when given with four 
digits, is between 2000 and 2999. At most one of the integers has four digits, 
and the others have one or two digits.

Output
Output a single line giving the earliest legal date possible given the above 
constraints. The output should be formatted as year-month-day, where year has 
four digits, and month and day have two digits each (zero padding), for example
"2011-07-15". If there is no legal date (subject to the above constraints) then 
output a single line with the original string followed by the words "is 
illegal".

Sample Input 1		Sample Output 1
02/4/67			      2067-02-04
31/9/73			      31/9/73 is illegal

"""

import datetime
import itertools
import sys

# constants

MIN_DATE_MONTH = 1
MIN_DATE_DAY = 1
MIN_DATE_YEAR = 2000

MAX_DATE_MONTH = 12
MAX_DATE_DAY = 31
MAX_DATE_YEAR = 2999

def year_util(year):
  # make sure the input variable is of integer data tyoe
  try:
    year = int(year)
  except ValueError:
    year = -1
  # make sure the supplied year is in range (0-99 & 2000-2999 are legal)
  if (year < 0 or year > MAX_DATE_YEAR) or (year > 99 and year < MIN_DATE_YEAR):
    year = -1
  # if 2 digit year (yy) convert to 4 digit year (yyyy)
  if year >= 0:
    if year >= 0 and year < 100:
      year = year + 2000
  return year

def best_before(date):
  # read input from stdin
  date_str = str(date)

  # record todays date for comparison
  todays_date = datetime.date.today()

  # split the date input string and create a list
  date_str_list = date_str.split('/', 3)

  # define a variable to keep track of the earliest legal date, set default value to a date far in the past so the output
  # will always evaluate even if there are no future legal dates identified
  earliest_legal_date = datetime.date(MIN_DATE_YEAR, MIN_DATE_MONTH, MIN_DATE_DAY)
  # define a variable to keep track of the earliest legal date delta, set default value to a date far in the future so that the
  # date comparison operation will run properly on it's first iteration
  earliest_legal_date_delta = datetime.date(MAX_DATE_YEAR, MAX_DATE_MONTH, MAX_DATE_DAY) - todays_date

  # create a list of every digit permutation
  digit_combos_list = list(itertools.permutations(date_str_list))
  # iterate through list of all possible digit combinations
  for combo in digit_combos_list:
    # extract year, month & date
    year = combo[0]
    month = combo[1]
    date = combo[2]
    try:
      legal_date = datetime.date(year_util(year), int(month), int(date))
      # calculate delta from todays date and the current legal date
      delta = legal_date - todays_date
      try:
        # test if the current delta is less than the previous earliest legal date data and greater than 0 (not expired)
        if (delta < earliest_legal_date_delta) and (delta > (todays_date - todays_date)):
          # update earliest legal date
          earliest_legal_date = legal_date
          # update earliest legal date delta
          earliest_legal_date_delta = delta
      except ValueError:
        # this should never fail due to outer try/catch block filtering illegal dates
        print 'delta operation failed'
    except ValueError:
      # we have encountered an illegal date since the date object could not be generated, continue processing
      pass

  # print output
  if (earliest_legal_date >= todays_date):
    # print earliest legal date
    print str(earliest_legal_date)
  else:
    # no legal date
    print date_str + ' is illegal'

if __name__ == '__main__':
  for line in sys.stdin:
    best_before(line.strip())