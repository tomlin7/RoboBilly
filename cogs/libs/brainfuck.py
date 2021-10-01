import sys

def evaluate(code):
  code     = cleanup(list(code))
  bracemap = buildbracemap(code)

  cells, codeptr, cellptr = [0], 0, 0
  wlist = []
  while codeptr < len(code):
    command = code[codeptr]

    if command == ">":
      cellptr += 1
      if cellptr == len(cells): cells.append(0)

    if command == "<":
      cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "+":
      cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

    if command == "-":
      cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

    if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
    if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
    if command == ".":
      wlist.append(chr(cells[cellptr]))
      #sys.stdout.write(chr(cells[cellptr]))
    if command == ",": cells[cellptr] = ord(getch.getch())
      
    codeptr += 1
  wlist = ''.join(wlist)
  print(wlist)
  return wlist

def cleanup(code):
  return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))

def buildbracemap(code):
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    if command == "[": temp_bracestack.append(position)
    if command == "]":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap
