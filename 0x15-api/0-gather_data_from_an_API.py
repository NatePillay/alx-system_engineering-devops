#!/usr/bin/python3
'''gather the data from an api'''

import requests
from sys import argv

if __name__ == "__main__":
	#get employee response [used to get name]
	endpoint = 'https://jsonplaceholder.typicode.com'
	user_response = requests.get(endpoint + '/users/' + argv[1]).json()

	#get total number of tasks / len of all tasks
	todos = requests.get(endpoint + '/todos?userId=' + argv[1]).json()

	#get number completed tasks and their titles
	titles_comp = [todo['title'] for todo in todos if todo['completed']]

	print('Employee {} is done with tasks {}/{}:'
		.format(user_response['name'], len(titles_comp), len(todos)))

	[print('\t {}'.format(title)) for title in titles_comp]
