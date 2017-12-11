__version__ = '0.1.0'

m = [0, 3, 1, 7, 5, 9, 8, 6, 4, 2, 0, 0, 0, 0, 0, 0, 7, 0, 9, 2, 1, 5, 4, 8, 6, 3, 0, 0, 0, 0, 0, 0, 4, 2, 0, 6, 8, 7, 1, 3, 5, 9, 0, 0, 0, 0, 0, 0, 1, 7, 5, 0, 9, 8, 3, 4, 2, 6, 0, 0, 0, 0, 0, 0, 6, 1, 2, 3, 0, 4, 5, 9, 7, 8, 0, 0, 0, 0, 0, 0, 3, 6, 7, 4, 2, 0, 9, 5, 8, 1, 0, 0, 0, 0, 0, 0, 5, 8, 6, 9, 7, 2, 0, 1, 3, 4, 0, 0, 0, 0, 0, 0, 8, 9, 4, 5, 3, 6, 2, 0, 1, 7, 0, 0, 0, 0, 0, 0, 9, 4, 3, 8, 6, 1, 7, 2, 0, 5, 0, 0, 0, 0, 0, 0, 2, 5, 8, 1, 4, 3, 6, 7, 9, 0, 0, 0, 0, 0, 0, 0]

def digit(msg):
  try:
    x = 0
    for d in list(msg):
      x = m[(x << 4) + int(d)]

    return x
  except ValueError:
    return None
  except IndexError:
    return None

def validate(msg):
  return digit(msg) == 0

def generate(msg):
  d = digit(msg)
  if d:
    return msg + str(d)
  else:
    return None
