'''

Implement the following functions based on the question. Retain the name of the functions, and parameters as is in the question. 

=================


1. compute_top2_players(player_list) --> 50% 
Get the player_list as input, compute the total score as sum of the 5 rounds, and return top 2 players. 

------------------------------------------------

2. search_netflix_dict(netflix_dict, column_name, value) --> 50%
 
Get the column names, and value from the user and return all the records with those value.  If none, return False. 
For the dataset, use get_netflix_files() function in util.

TIP: listed_in column is tricky and not straightforward 

Input:
column_name = [director, listed_in]
value = ["David Fincher", "Cult Movies']
Output:
return_list = ['show_id': 's7775', 'title': 'Zodiac', 'director': 'David Fincher', 'country': 'United States', 'listed_in': 'Cult Movies, Dramas, Thrillers'}, ....]

'''