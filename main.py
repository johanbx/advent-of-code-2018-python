import day1
import day2
import sys

help_text = '''Usage:
  main.py [day] [part]

Example:
  main.py 1 2
'''

db = {
	'1': { '1': day1.part1, '2': day1.part2, '2x': day1.part2_min },
	'2': { '1': day2.part1, '1x': day2.part1_min, '2': day2.part2, '2x': day2.part2_min }
}

if len(sys.argv) != 3:
	print(help_text)
	sys.exit()

day = sys.argv[1]
part = sys.argv[2]
try:
	print(db[day][part]())
except KeyError:
	print('Not in database, try one of theese:')
	for day, solutions in db.items():
		print('== Day %s ==' % day)
		print('Solutions: %s' % ', '.join(solutions))