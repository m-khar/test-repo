from functools import reduce

def prod(seq: list[int]) -> int:
  return reduce(lambda x, y: x * y, seq)


if __name__ == "__main__":
  print(prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
