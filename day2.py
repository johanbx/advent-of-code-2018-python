
from collections import Counter
from itertools import combinations

f = 'day2_input.txt'
box_ids = [x.strip() for x in open(f).readlines()]

def part1():
	twos = 0
	threes = 0
	for box_id in box_ids:
		counter = Counter(box_id.strip())
		unique_counts = set(counter.values())
		if 2 in unique_counts:
			twos += 1
		if 3 in unique_counts:
			threes += 1
	return twos * threes

def part1_min():
	a=[set(Counter(x).values()) for x in open(f).readlines()]
	return len([3 for x in a if 3 in x]) * len([2 for x in a if 2 in x])

def part2():
	id_len = len(box_ids[0])
	for box_id_1 in box_ids:
		for box_id_2 in box_ids:
			if box_id_1 == box_id_2:
				continue
			wrong_match = 0
			for i in range(id_len):
				if box_id_1[i] != box_id_2[i]:
					wrong_match += 1
					if wrong_match > 1:
						break
			if wrong_match == 1:
				box_id_1_letter_diff = ''.join(set(box_id_1) - set(box_id_2))
				return box_id_1.replace(box_id_1_letter_diff, '')

def part2_min():
	for x in combinations(open(f).readlines(), 2):
		h=[(a,b) for a,b in zip(x[0], x[1]) if a!=b]
		if len(h)==1:
			return x[0].replace(h[0][0],'')