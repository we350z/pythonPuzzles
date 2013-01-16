#!/usr/bin/python -tt
# solution written by Brad Kusnir 12/12/12

"""

Bilateral Projects
Problem ID: bilateral

A friend of yours works at an undisclosed company in the music streaming 
industry, and needs your help. The company has offices in Stockholm and London, 
and collaboration between the two offices is extensive. The situation is that 
each of the many but small projects is handled by a two-person team with a 
member in each city. While emails, faxes, and phones are wonderful, and work 
well within each team, the CEO wants a briefing every year on the projects. For 
this purpose the CEO invites representatives from the projects to Barbados for a 
week of beach fun presentations of all the projects. However, money is tight and 
a new policy has been created: the CEO wants at least one person from each 
project, and additionally, she wants to invite as few people as possible. This 
is where you come in. In order to help your friend get a ticket to Barbados, you 
are to write a program that, given all the two-person teams, computes the 
smallest number of people that must be invited in order to get at least one 
person from each project, as well as a list of people to invite. If possible 
(subject to the set of people being smallest possible), the list of invitees 
should include your friend.

Input
The first line of input contains an integer 1 <= m <= 10 000, the number of teams. 
The following m lines each contain two integers, i, j separated by a space, being 
the employee IDs of the two employees in that team (the first one is from 
Stockholm and the second one is from London). Stockholm employees have IDs in the 
range 1000 to 1999 and London employees have IDs in the range 2000 to 2999. An 
employee can be a member of several teams, but there cannot be several teams 
consisting of the same pair of employees. Your friend has ID 1009.

Output
Output first a single line with an integer k indicating the smallest number of 
employees that must be invited to meet the requirements above. Then output k lines 
giving the IDs of employees to invite. If possible (subject to k being smallest 
possible), the list should contain your friend.
If there are several solutions subject to these constraints, anyone is acceptable.

Sample input 1
2
1009 2011
1017 2011

Sample output 1
1
2011

Sample input 2
4
1009 2000
1009 2001
1002 2002
1003 2002

Sample output 2
2
2002
1009

"""

from operator import itemgetter
import sys

def bilateral(inputs):
  # integer k indicating the smallest number of employees that must be invited
  k = 0

  # integer 1 <= m <= 10 000, the number of teams
  m = 0

  # Your friend has ID 1009.
  friend_id = 1009

  # create a list to hold each team
  curent_team_members = []
  invited_employees = []
  team_dict = {}
  teams_by_id = []
  teams_represented = {}
  stockholm_team_dict = {}
  london_team_dict = {}
  counter = 0
  current_team_number = 0
  member_of_teams = []

  for line in inputs:
    if counter == 0:
      m = int(line.strip())
      if ((m >= 1) and (m <= 10000)):
        pass
      else:
        print '1 <= m <= 10 000'
        return # input failed validation - exit routine
    else:
      current_team_number = counter
      # add current team number to a dict/list to track which have been selected so far
      teams_represented[current_team_number] = False
      current_team_members = line.split()
      # create a list of unique stockholm employee id's
      stockholm_id = int(current_team_members[0])
      if stockholm_id < 1000 or stockholm_id > 1999:
      	print 'Stockholm employees have IDs in the range 1000 to 1999'
      	return  # input failed validation - exit routine

      # update stockholm employee and associated teams in stockholm dict
      if stockholm_id not in stockholm_team_dict:
        # id does not yet exist in hash table, create inital entry
        stockholm_team_dict[stockholm_id] = str(current_team_number)
      else:
        # id already exists in hash table, update existing entry
        stockholm_team_dict[stockholm_id] = str(stockholm_team_dict[stockholm_id]) + ',' + str(current_team_number)

      # create a list of unique london employee id's
      london_id = int(current_team_members[1])
      if london_id < 2000 or london_id > 2999:
        print 'London employees have IDs in the range 2000 to 2999'
        return # input failed validation - exit routine

      # update london employee and associated teams in london dict
      if london_id not in london_team_dict:
        # id does not yet exist in hash table, create inital entry
        london_team_dict[london_id] = str(counter)
      else:
        # id already exists in hash table, update existing entry
        london_team_dict[london_id] = str(london_team_dict[london_id]) + ',' + str(current_team_number)

      # merge Stockholm and London dicts into master dict (it may not be necessary to split them out)
      team_dict = dict(stockholm_team_dict.items() + london_team_dict.items())

    counter = counter + 1
  
  total_teams = counter

  # convert dict to a list
  for employee_id, teams in team_dict.iteritems():
    employee = [employee_id, teams]
    teams_by_id.append(employee)

  # sort list by employees who are the members of the most teams first
  # todo: improve sorting efficiency by using itemgetter()
  teams_by_id.sort(key=lambda x: len(x[1]), reverse=True)

  counter = 0
  teams_not_represented = m

  # check to see if teams are still unrepresented
  while teams_not_represented > 0:

    # add employee to the invite list
    invited_employees.append(teams_by_id[counter][0])

    # determine which teams the employee is a member of 
    member_of_teams = teams_by_id[counter][1].split(',')

    for team in member_of_teams:
       if teams_represented[int(team)] == False:
         teams_represented[int(team)] = True
         teams_not_represented = teams_not_represented - 1

    counter = counter + 1

    pass

  # Output first a single line with an integer k indicating the smallest number of 
  # employees that must be invited to meet the requirements above.
  print len(invited_employees)

  # Then output k lines 
  # giving the IDs of employees to invite. If possible (subject to k being smallest 
  # possible), the list should contain your friend.

  # sort invited employees list
  invited_employees.sort(reverse=True)

  for employee in invited_employees:
    print employee

  return

if __name__ == '__main__':
  lines = []
  for line in sys.stdin:
    lines.append(line.strip())
  bilateral(lines)