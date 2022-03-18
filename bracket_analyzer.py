#bracket analyzer
#docs: https://sportsreference.readthedocs.io/en/stable/ncaab.html

from datetime import datetime
from sportsipy.ncaab.boxscore import Boxscores
from operator import itemgetter
import time

dates = {
	1985 : [[3,14],[4,1]],
	1986 : [[3,13],[3,31]],
	1987 : [[3,12],[3,30]],
	1988 : [[3,17],[4,4]],
	1989 : [[3,16],[4,3]],
	1990 : [[3,15],[4,2]],
	1991 : [[3,14],[4,1]],
	1992 : [[3,19],[4,6]],
	1993 : [[3,18],[4,5]],
	1994 : [[3,17],[4,4]],
	1995 : [[3,16],[4,3]],
	1996 : [[3,14],[4,1]],
	1997 : [[3,13],[3,31]],
	1998 : [[3,12],[3,30]],
	1999 : [[3,11],[3,29]],
	2000 : [[3,16],[4,3]],
	2001 : [[3,13],[4,2]],
	2002 : [[3,12],[4,1]],
	2003 : [[3,18],[4,7]],
	2004 : [[3,16],[4,5]],
	2005 : [[3,15],[4,4]],
	2006 : [[3,14],[4,3]],
	2007 : [[3,13],[4,2]],
	2008 : [[3,18],[4,7]],
	2009 : [[3,17],[4,6]],
	2010 : [[3,16],[4,5]],
	2011 : [[3,15],[4,4]],
	2012 : [[3,13],[4,2]],
	2013 : [[3,19],[4,8]],
	2014 : [[3,18],[4,7]],
	2015 : [[3,17],[4,6]],
	2016 : [[3,15],[4,4]],
	2017 : [[3,14],[4,3]],
	2018 : [[3,13],[4,2]],
	2019 : [[3,19],[4,8]],
	2021 : [[3,18],[4,5]],
}

seed0 = []
seed1 = [666, 0.5, 0.539, 0.634, 0.711, 0.839, 0.706, 0.857, 0.798, 0.901, 0.857, 0.556, 1, 1, 0, 0, 0.993]
seed2 = [666, 0.461, 0.5, 0.603, 0.444, 0.167, 0.722, 0.694, 0.444, 0.5, 0.645, 0.833, 1, 0, 0, 0.938, 0]
seed3 = [666, 0.366, 0.397, 0.5, 0.625, 0.5, 0.576, 0.611, 1, 1, 0.692, 0.679, 0 ,0, 0.847, 1, 0]
seed4 = [666, 0.289, 0.556, 0.375, 0.5, 0.563, 0.333, 0.333, 0.364, 0.5, 1, 0, 0.69, 0.79, 0, 0, 0]
seed5 = [666, 0.161, 0.833, 0.5, 0.438, 0.5, 1, 0, 0.25, 0.25, 1, 0, 0.671, 0.842, 0, 0, 0]
seed6 = [666, 0.294, 0.278, 0.424, 0.667, 0, 0, 0.667, 0.25, 0, 0.6, 0.634, 0, 0, 0.875, 0, 0]
seed7 = [666, 0.143, 0.306, 0.389, 0.667, 0, 0.333, 0, 0.5, 0, 0.601, 0, 0, 0, 1, 0.5, 0]
seed8 = [666, 0.202, 0.556, 0, 0.636, 0.75, 0.75, 0.5, 0, 0.518, 0, 1, 0, 1, 0, 0, 0]
seed9 = [666, 0.099, 0.5, 0, 0.5, 0.75, 0, 0, 0.482, 0, 1, 0, 0, 1, 0, 0, 1]
seed10 = [666, 0.143, 0.355, 0.308, 0, 0, 0.4, 0.399, 0, 0, 0, 0.333, 0, 0, 1, 1, 0]
seed11 = [666, 0.444, 0.167, 0.321, 0, 0, 0.366, 1, 0, 1, 0.667, 0, 0, 0, 1, 0, 0]
seed12 = [666, 0, 0, 0, 0.31, 0.329, 0, 0, 1, 0, 0, 0, 0, 0.75, 0, 0, 0]
seed13 = [666, 0, 0, 0, 0.21, 0.158, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0]
seed14 = [666, 0, 0, 0.153, 0, 0, 0.125, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
seed15 = [666, 0, 0.063, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0]
seed16 = [666, 0.007, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#this is a list of lists representing win %. E.g. win_percentages[1][8] will return the win percetage of 1 seeds against 8 seeds (0.798)
win_percentages = [seed0, seed1, seed2, seed3, seed4, seed5, seed6, seed7, seed8, seed9, seed10, seed11, seed12, seed13, seed14, seed15, seed16]

#for x in win_percentages:
#	print(len(x))

#time.sleep(10)

#games = Boxscores(datetime(2010, 3, 13), datetime(2010, 4, 2))
#print(games)
upsets_by_year = []
likeliness_by_year_sum = []
likeliness_by_year_product = []



for k,v in dates.items():
	games_now = Boxscores(datetime(k, v[0][0], v[0][1]), datetime(k, v[1][0],v[1][1]))
	print(k)

#games_today = Boxscores(datetime.today())
#print(games_today.games)  # Prints a dictionary of all matchups for today

#games = Boxscores(datetime(2021, 3, 18), datetime(2021, 4, 5))
#print(games)
	game_data = games_now.games

	upsets = 0
	coinflips = 0 # i guess the earliest a coinflip can possibly occur is the final four, and there can only be a max of 3 coinflip games
	processed = 0
	likeliness_sum = 0
	likeliness_product = 1

	for date in game_data:
		#print(game_data[date])
		for score in game_data[date]:
			#print(score)
			if score['away_rank'] == None or score['away_score'] == None: #skip non tourney games or forfeits
				continue
			elif score['away_rank'] == score['home_rank'] and score['away_rank'] > 10: #skip play in games, since we dont guess the outcomes of those
				continue

			processed += 1
			if score['home_score'] > score['away_score']: #home team won
				#print(str(score['home_rank']) + ' ' + score['home_name'] + ' beat ' + str(score['away_rank']) + ' ' + score['away_name'])
				#print('this had a win percentage of + ' + str(win_percentages[score['home_rank']][score['away_rank']]))
				likeliness_sum += win_percentages[score['home_rank']][score['away_rank']] #for the team that won, add the probability of that win
				likeliness_product *= win_percentages[score['home_rank']][score['away_rank']]
				if score['home_rank'] > score['away_rank']:
					upsets += 1
				elif score['home_rank'] == score['away_rank']:
					coinflips += 1
			else: #away team won
				#print(str(score['away_rank']) + ' ' + score['away_name'] + ' beat ' + str(score['home_rank']) + ' ' + score['home_name'])
				#print('this had a win percentage of + ' + str(win_percentages[score['away_rank']][score['home_rank']]))
				likeliness_sum += win_percentages[score['away_rank']][score['home_rank']]
				likeliness_product *= win_percentages[score['away_rank']][score['home_rank']]
				if score['home_rank'] < score['away_rank']:
					upsets += 1
				elif score['home_rank'] == score['away_rank']:
					coinflips += 1
			#print('running likeliness total: ' + str(likeliness))
			#print (score['winning_name'])

	print('Number of games processed: ' + str(processed))
	print('Number of upsets: ' + str(upsets))
	print('Number of coinflips: ' + str(coinflips))
	upsets_by_year.append([k,upsets]) #append a two-element list containing the year and the number of upsets
	likeliness_by_year_sum.append([k,likeliness_sum])
	likeliness_by_year_product.append([k,likeliness_product])

#sorted(upsets_by_year, key=itemgetter(1))
#print(upsets_by_year)
print(sorted(upsets_by_year, key=itemgetter(1)))
print(sorted(likeliness_by_year_sum, key=itemgetter(1)))
print(sorted(likeliness_by_year_product, key=itemgetter(1)))
