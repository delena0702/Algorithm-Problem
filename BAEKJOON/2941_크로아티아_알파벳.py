import sys

input = sys.stdin.readline().strip()
input = input.replace('c=', '$')
input = input.replace('c-', '$')
input = input.replace('dz=', '$')
input = input.replace('d-', '$')
input = input.replace('lj', '$')
input = input.replace('nj', '$')
input = input.replace('s=', '$')
input = input.replace('z=', '$')
print(len(input))