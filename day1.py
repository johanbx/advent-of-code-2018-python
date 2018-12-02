f = 'day1_input.txt'
freqs = [int(x) for x in open(f).readlines()]
freqs_length = len(freqs)

def part1():
  return sum(freqs)

def part2():
  history = set()
  current = 0
  index = 0
  while current not in history:
    freq = freqs[index % freqs_length]
    history.add(current)
    current += freq
    index += 1
  return current

def part2_min():
  k=[int(x) for x in open(f).readlines()]
  l,h,c,i=len(k),set(),0,0
  while c not in h:
    g=k[i%l]; h.add(c); c+=g; i+=1
  return c