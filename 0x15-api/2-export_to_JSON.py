#!/usr/bin/python3
'''python script to export data in JSON format'''
from sys import argv
from requests import get
import json

if __name__ == '__main__':
	endpoint = 'https://jsonplaceholder.typicode.com'
	user = get(endpoint + '/users/' + argv[1]).json()['username']
	todos = get(endpoint + '/todos?userId=' + argv[1]).json()

	record, user_data, group = {}, {},[]
	for todo in todos:
		record['task'] = todo['title']
		record['completed'] = todo['completed']
		record['username'] = user
		group.append(record)
		record = {}


	user_data[argv[1]] = group

	with open('{}.json'.format(argv[1]), 'w') as file:
		json.dump(user_data, file)
