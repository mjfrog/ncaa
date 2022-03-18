#this is for generating weighted random predictions for the NCAA tourney 

bracket_start = [1,16,8,9,5,12,4,13,6,11,3,14,7,10,2,15]
current_round = []
next_round = []
final_four = []
final_four_teams = []
#have array of names for each corner in order of seed, then can make an array of these arrays
""" 2021 teams
west = ['Gonzaga', 'Iowa', 'Kansas', 'Virginia', 'Creighton', 'USC', 'Oregon', 'Oklahoma', 'Missouri', 'VCU', 'Witchita St', 'UCSB', 'Ohio', 'E Washington', 'Grand Canyon', 'random 16 seed']
east = ['Michigan', 'Alabama', 'Texas', 'FSU', 'Colorado', 'BYU', 'UConn', 'LSU', 'St. Bonaventure', 'Maryland', 'MSU/UCLA', 'Georgetown', 'UNC Greensboro', 'Abil Christian,', 'Iona', 'MSM']
south = ['Baylor', 'OSU', 'Arkansas', 'Purdue', 'Villanova', 'Texas Tech', 'Florida', 'UNC', 'Wisconsin', 'VT', 'Utah State', 'Winthrop', 'North Texas', 'Colgate', 'Oral Roberts', 'Hartford']
midwest = ['Illinois', 'Houston', 'WVU', 'Oklahoma St', 'Tennessee', 'SDSU', 'Clemson', 'Loyola', 'GT', 'Rutgers', 'Syracuse', 'Oregon State', 'Liberty', 'Morehead St', 'Cleveland State', 'Drexel']
"""
west = ['Gonzaga', 'Duke', 'Texas Tech', 'Arkansas', 'UConn', 'Alabama', 'Michigan State', 'Boise State', 'Memphis', 'Davidson', 'Rutgers/Notre Dame', 'New Mexico State', 'Vermont', 'Montana State', 'CS Fullerton', 'Georgia State']
east = ['Baylor', 'Kentucky', 'Purdue', 'UCLA', 'St. Marys', 'Texas', 'Murray State', 'North Carolina', 'Marquette', 'San Francisco', 'Virgina Tech', 'Indiana', 'Akron', 'Yale', 'St. Peters', 'Norfolk State']
south = ['Arizona', 'Villanova', 'Tennessee', 'Illinois', 'Houston', 'Colorado State', 'Ohio State', 'Seton Hall', 'TCU', 'Loyola', 'Michigan', 'UAB', 'Chattanooga', 'Longwood', 'Delaware', 'Wright State/Bryant']
midwest = ['Kansas', 'Auburn', 'Wisconsin', 'Providence', 'Iowa', 'LSU', 'USC', 'San Diego State', 'Creighton', 'Miami (FL)', 'Iowa State', 'Richmond', 'South Dakota State', 'Colgate', 'Jacksonville State', 'Texas Southern']


teams = [west, east, south, midwest]


import random

#generate the final four

for r in range(4):
	print('\nRound: ' + str(r))
	#have another while loop for each corner
	current_round = bracket_start
	while len(current_round) != 1:
		#until there is a reigonal champ, run the loop
		#print(current_round)
		print('ROUND OF ' + str(len(current_round) * 4))
		i = 0
		while i < (len(current_round) - 1):
			#print('in loop')
			#interate over each round and produce a winner
			result = random.randint(1, (current_round[i] + current_round[i+1]) )
			if result > current_round[i]:
				next_round.append(current_round[i])
				#print('result is ' + str(result))
				print ('#' + str(current_round[i]) + ' ' + teams[r][current_round[i] - 1] + ' beats #' + str(current_round[i+1]) + ' ' + teams[r][current_round[i+1] - 1])
			else:
				#print('result is ' + str(result))
				print ('#' + str(current_round[i+1]) + ' ' + teams[r][current_round[i+1] - 1] + ' beats #' + str(current_round[i]) + ' ' + teams[r][current_round[i] - 1])
				next_round.append(current_round[i+1])
			#go to next pair of matchups
			#print (next_round)
			i = i + 2
		#now, the round is done, need to do the next round
		#print (next_round)
		current_round = next_round.copy()
		next_round.clear()

	#loop is over, print the winner
	#print('round over, winner is ' + str(current_round[0]))
	final_four.append(current_round[0])
	final_four_teams.append(teams[r][current_round[0] - 1])

print('\nFINAL FOUR')
#print(final_four)
#print(final_four_teams)

finals = []
finals_teams = []

#now compute winner of tourney
result = random.randint(1, (final_four[0] + final_four[1]))
if result > final_four[0]:
	finals.append(final_four[0])
	#print('result is ' + str(result))
	print ('#' + str(final_four[0]) + ' ' + final_four_teams[0] + ' beats #' + str(final_four[1]) + ' ' + final_four_teams[1])
	finals_teams.append(final_four_teams[0])
else:
	finals.append(final_four[1])
	#print('result is ' + str(result))
	print ('#' + str(final_four[1]) + ' ' + final_four_teams[1] + ' beats #' + str(final_four[0]) + ' ' + final_four_teams[0])
	finals_teams.append(final_four_teams[1])

#this is kind of ugly, but i dont feel like setting up a loop for code that's going to only ever run twice
result = random.randint(1, (final_four[2] + final_four[3]))
if result > final_four[2]:
	finals.append(final_four[2])
	#print('result is ' + str(result))
	print ('#' + str(final_four[2]) + ' ' + final_four_teams[2] + ' beats #' + str(final_four[3]) + ' ' + final_four_teams[3])
	finals_teams.append(final_four_teams[2])
else:
	finals.append(final_four[3])
	#print('result is ' + str(result))
	print ('#' + str(final_four[3]) + ' ' + final_four_teams[3] + ' beats #' + str(final_four[2]) + ' ' + final_four_teams[2])
	finals_teams.append(final_four_teams[3])

print('\nFINALS')
#print(finals)

result = random.randint(1, (finals[0] + finals[1]))
if result > finals[0]:
	#print('result is ' + str(result))
	print ('#' + str(finals[0]) + ' ' + finals_teams[0] + ' beats #' + str(finals[1]) + ' ' + finals_teams[1])
	print ('#' + str(finals[0]) + ' ' + finals_teams[0] + ' wins the tourney ' )
else:
	#print('result is ' + str(result))
	print ('#' + str(finals[1]) + ' ' + finals_teams[1] + ' beats #' + str(finals[0]) + ' ' + finals_teams[0])
	print ('#' + str(finals[1]) + ' ' + finals_teams[1] + ' wins the tourney ' )

print('Tiebreaker final score: ' + str(random.randint(55,85)) + ' to ' + str(random.randint(55,85)))

