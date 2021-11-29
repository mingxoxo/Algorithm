#https://www.acmicpc.net/problem/1764
n, m = map(int, input().split())

n_person = []
m_person = []

for i in range(n):
    n_person.append(input())

for j in range(m):
    m_person.append(input())

nm_person = sorted(list(set(n_person)&set(m_person)))

print(len(nm_person))
for name in nm_person:
    print(name)
