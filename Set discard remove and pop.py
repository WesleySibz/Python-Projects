# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
s= set(map(int, input().split()))
n= int(input())
for i in range(n):
    commands = input().split()
    if len(commands)> 1:
        e = int(commands[1])
    if commands[0] == "pop":
        s.pop()
    if commands[0] == "remove":
        s.remove(e)
    if commands[0] == "discard":
        s.discard(e)
print(sum(s))
