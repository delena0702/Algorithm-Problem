from collections import defaultdict

N, cnt = input(), defaultdict(int)
for ch in N:
    cnt[int(ch)] += 1
cnt[6] = cnt[9] = (cnt[6] + cnt[9] + 1) // 2
print(max(cnt.values()))