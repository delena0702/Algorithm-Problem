data = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
arr = [data.index(input()) for _ in range(3)]
print((10 * arr[0] + arr[1]) * (10 ** arr[2]))
