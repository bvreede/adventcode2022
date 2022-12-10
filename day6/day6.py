input = open("day6/input.txt", "r")
input = input.readlines()[0]

def find_start_of(data,blocksize):
  end = len(data)
  blocks = [data[e-blocksize:e] for e in range(blocksize,end+1)]

  for k,b in enumerate(blocks):
    charcount = k+blocksize
    if len(set(b)) == blocksize:
      return(charcount)

puzzle1 = find_start_of(input,4)
print(puzzle1)

puzzle2 = find_start_of(input,14)
print(puzzle2)
