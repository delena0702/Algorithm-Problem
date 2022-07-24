from collections import Counter
arr = Counter(input().upper()).most_common(2)
if len(arr) == 0 or (len(arr) >= 2 and arr[0][1] == arr[1][1]):
    print("?")
else:
    print(arr[0][0])