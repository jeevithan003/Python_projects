n1 = input("persona1: ")
n1 = n1.lower().replace(" ", "")
n1l = list(n1)

n2 = input("persona2: ")
n2 = n2.lower().replace(" ", "")
n2l = list(n2)

def r1(n1l, n2l):
    for x in range(len(n1l)):
        for z in range(len(n2l)):
            if n1l[x] == n2l[z]:
                c = n1l[x]
                n1l.remove(c)
                n2l.remove(c)
                l3 = n1l + ["*"] + n2l
                return [l3, True]
    l3 = n1l + ["*"] + n2l
    return [l3, False]

p = True
while p:
    res = r1(n1l, n2l)
    result_list = res[0] 
    f1 = res[1]
    i = result_list.index("*")
    n1l = result_list[:i]
    n2l = result_list[i+1:]
    p = f1

c = len(n1l) + len(n2l)

result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

while len(result) > 1:
    si = (c % len(result)) - 1
    if si >= 0:
        right = result[si + 1:]
        left = result[:si]
        result = right + left
    else:
        result = result[:len(result) - 1]

print("Relationship status:", result[0])
