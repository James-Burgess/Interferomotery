#!/usr/bin/python3 

from array_viability_test import viable
from array_creator import makeArrays

def main():
	all_combinations = makeArrays()

	for co_ords in all_combinations:
    	if not(viable(*single)):
        	co_ords.push(single)

if __name__ == '__main__':
	main()
	