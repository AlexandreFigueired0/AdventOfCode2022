
import re

DEBUG = False

def sign(a):
  if a == 0:
    return 0
  if a > 0:
    return 1
  return -1

#--- Part One ---

# coord change for each dir
dir_dxy_map = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D":(1, 0)}
# dir change for each dir as dict of rot => new_dir
dir_rot_map = {"R":{"L":"U", "R":"D"}, "L":{"L":"D", "R":"U"}, "U":{"L":"L", "R":"R"}, "D":{"L":"R", "R":"L"}}
dir_val_map = {"R":0, "D":1, "L":2, "U":3}

input = open("input.txt").read()

# result in 0.xx sec (both parts)

#--- Part Two ---

# from square fingerprint (square# for each row) to (net#, edges)
# net# in order in https://www.mechamath.com/geometry/nets-of-a-cube/
# edges = tuple of face#U/D/L/R to connected face#/U/D/L/R
# eg. ("0L", "2U", coord-map) and so is ("2U", "0L", coord-map)
# c_map = "S" (Same) = coords increase together, "R" (Reverse) = when one face increases, the other decreases
# however tuples of edges are listed only once in random order of face-edges
# first main and all rotations right, each followed by flip horz and vert if it's new
# note: flip vert is tuple reversed
net_map = {
  # 11 nets .. fill as you wish
  # I filled completely the net configurations of interest
  # example net = 7
  # input   net = 2
  
  # net 1
  ((2,), (0,1,2,3), (2,)):1,        # main
  ((1,), (0,1,2,3), (1,)):1,        # flip horz
  ((1,), (1,), (0,1,2), (1,)):1,    # main, rot R
  ((1,), (0,1,2), (1,), (1,)):1,    # flip vert
  
  # net 2
  ((0,1), (1,2,3), (3,)):2,         # main
  ((2,3), (0,1,2), (0,)):2,         # flip horz
  ((0,), (0,1,2), (2,3)):2,         # flip vert
  ((2,), (1,2), (1,), (0,1)):2,     # main, rot R^2
  ((0,), (0,1), (1,), (1,2)):2,     # flip horz
  ((1,2), (1,), (0,1), (0,)): (2, ( # flip vert
    ("0U", "5L", "S"), ("0L", "3L", "R"), ("2L", "3U", "S"), ("1R", "4R", "R"), ("1U", "5D", "S"), ("1D", "2R", "S"), ("4D", "5R", "S")
  )),
  
  # net 7
  ((2,3), (0,1,2), (2,)):7,         # main
  ((0,1), (1,2,3), (1,)):7,         # flip horz
  ((2,), (0,1,2), (2,3)): (7, (     # flip vert
    ("0U", "1U", "R"), ("0L", "2U", "S"), ("0R", "5R", "R"), ("2D", "4L", "R"), ("1D", "4D", "R"), ("1L", "5D", "S"), ("3R", "5U", "R")
   )),
  ((1,), (1,), (0,1,2), (2,)):7,    # main, rot R
  ((1,), (1,), (0,1,2), (0,)):7,    # flip horz
  ((2,), (0,1,2), (1,), (1,)):7,    # flip vert
  ((1,), (1,2,3), (0,1)):7,         # main, rot R^2
  ((0,), (0,1,2), (1,), (1,)):7     # main, rot R^3
}

def solve3D(input):
  
  def face_id(y, x):
    id = 0
    while True:
      start_y, start_x, _ = faces[id]
      if start_x <= x < start_x+side_size and start_y <= y < start_y+side_size:
        break
      id += 1
    return id, start_y, start_x
  
  def face_starts(id):
    start_y, start_x, _ = faces[int(id)]
    return start_y, start_x
  
  def wrap(y, x, dy, dx):
    y0, x0 = y, x
    if dx == 0 and (0 <= y+dy < len(board))    and len(board[y+dy])-1 >= x and board[y+dy][x] != " ":
      return y+dy, x, dy, dx
    if dy == 0 and (0 <= x+dx < len(board[y])) and board[y][x+dx] != " ":
      return y, x+dx, dy, dx
    
    e1_id, e1_start_y, e1_start_x = face_id(y, x)
    e1 = str(e1_id)
    if dx == 0:
      e1 = e1 + ("D" if dy == 1 else "U")
    if dy == 0:
      e1 = e1 + ("R" if dx == 1 else "L")
    
    e2, c_map = edge_map[e1]
    e2_id, e2_side = e2
    e2_start_y, e2_start_x = face_starts(e2_id)
    if dx == 0:
      rel = x - e1_start_x
    if dy == 0:
      rel = y - e1_start_y
    
    if e2_side == "U":
      y, x = e2_start_y,              (e2_start_x + rel) if c_map == "S" else (e2_start_x+side_size-1-rel)
      new_dy, new_dx = 1, 0
    elif e2_side == "D":
      y, x = e2_start_y+side_size-1,  (e2_start_x + rel) if c_map == "S" else (e2_start_x+side_size-1-rel)
      new_dy, new_dx = -1, 0
    elif e2_side == "L":
      y, x = (e2_start_y + rel) if c_map == "S" else (e2_start_y+side_size-1-rel),  e2_start_x
      new_dy, new_dx = 0, 1
    elif e2_side == "R":
      y, x = (e2_start_y + rel) if c_map == "S" else (e2_start_y+side_size-1-rel),  e2_start_x+side_size-1
      new_dy, new_dx = 0, -1
    else:
      print("error, unknown e2 side", e2_side, e2_id+e2_side, "from", e1)
      exit()
    if DEBUG:
      print("wrap", y0, x0, (dy, dx), e1, "->", e2, y, x, (new_dy, new_dx))
    return y, x, new_dy, new_dx
  
  # example wraps  5,11 R -> 8,14 D  11,10 D -> 7,1 U
  
  board = []
  ops = []
  side_size = 1_000
  
  board_p = True
  for line in input.splitlines():
    #print(">>", line)
    if not line:
      board_p = False
      continue
    if board_p:
      board.append(line)
      side_size = min(side_size, len(line.strip()))
    else:
      ops = [ (rot, int(steps)) for rot, steps in re.findall("([RL-])([0-9]+)", "-"+line) ]
  
  # rescan and assign faces
  # # tuples of start_y, start_x (top-left coord) and square
  # square = square# in the row, counting includes empty squares
  faces = []
  cur_face = -1
  face_fingerprint = []
  for row in range(6):
    face_y = row*side_size
    if face_y >= len(board):
      break
    line = board[face_y]
    face_x = len(line) - len(line.strip())
    row_squares = []
    while face_x < len(line):
      square = face_x//side_size
      faces.append((face_y, face_x, square))
      row_squares.append(square)
      cur_face += 1
      face_x += side_size
    face_fingerprint.append(tuple(row_squares))
  face_fingerprint = tuple(face_fingerprint)
  net_id, net_edges = net_map[face_fingerprint]
  edge_map = {}
  for e1, e2, c_map in net_edges:
    edge_map[e1] = (e2, c_map)
    edge_map[e2] = (e1, c_map)
  if DEBUG:
    print("edge_map:", edge_map)
  
  # assign face neighbors
  # there are 11 nets, https://www.mechamath.com/geometry/nets-of-a-cube/
  # each net can be sketched in 4 rotations
  # recognize net and assign neighbor creating an edge
  # edges as ((face_id1, side1), (face_id2, side2)), eg. (2, U)
  
  # coords 0-based as row, col on global board 
  # will be changed to 1-based and to proper non-empty col at end
  start = (0, board[0].index("."))
  #print(start)
  
  dir = "R"
  y, x = start
  dy, dx = dir_dxy_map[dir]
  if DEBUG:
    print("start", y, x, dir)
  for i, op in enumerate(ops):
    if dx == 0:
      dir = "D" if dy == 1 else "U"
    if dy == 0:
      dir = "R" if dx == 1 else "L"
    rot, steps = op
    if rot != "-":
      dir = dir_rot_map[dir][rot]
    dy, dx = dir_dxy_map[dir]
    if DEBUG:
      print("op:", i, op, "dir:", dir, "steps:", steps)
    for step in range(steps):
      new_y, new_x, new_dy, new_dx = wrap(y, x, dy, dx)
      if DEBUG:
        print(step+1, "move", new_y, new_x, (dy, dx), "(wrapped)")
      # quaranteed to be in valid board position containing "." or "#" only
      if (board[new_y][new_x] == "#"):
        if DEBUG:
          print(step+1, "move", y, x, (dy, dx), "(wall)")
        break
      else:
        y, x = new_y, new_x
        dy, dx = new_dy, new_dx
        if DEBUG:
          print(step+1, "move", y, x, (dy, dx), "(free)")
  
  # adjust result col
  c_x = 0
  while board[y][c_x] == " ":
    c_x += 1
  return y+1, (x-c_x)+1, dir, dir_val_map[dir], 1000*(y+1)+4*(x+1)+dir_val_map[dir]        

row, col, dir, dir_val, passw = solve3D(input)
print(row, col, dir, dir_val, passw)
print()

# result in 0.xx sec (both parts)


#https://twitter.com/intent/tweet?text=I+just+completed+%22Monkey+Map%22+%2D+Day+22+%2D+Advent+of+Code+2022&url=https%3A%2F%2Fadventofcode%2Ecom%2F2022%2Fday%2F22&related=ericwastl&hashtags=AdventOfCode

# I just completed "Monkey Map" - Day 22 - Advent of Code 2022, https://adventofcode.com/2022/day/22
