import sys
n = int(input())
couple_n = int(input())
couple = []
infected = 1
have_infacted = [1]
for _ in range (couple_n):
    one_couple = list(map(int,sys.stdin.readline().split()))
    couple.append(one_couple)

for i in range(len(couple)):
    for p in range(2):
        if couple[i][p] == infected:
            if p ==0 :
                infected = couple[i][1]

                if infected not in have_infacted:
                    have_infacted.append(infected)
            
            elif p ==1 :
                infected = couple[i][0]

                if infected not in have_infacted:
                    have_infacted.append(infected)
print(len(have_infacted))
