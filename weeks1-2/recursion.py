def rFib(n):
  if n == 0: 
    return 0
  elif n == 1 or n == 2:
    return 1
  return rFib(n-1) + rFib(n-2)

#rFib is not called because the file was run in interactive mode
#python -1 "filename.py"