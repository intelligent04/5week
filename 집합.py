import sys
s = set()
m = int(sys.stdin.readline())
for i in range(m):
        do_val = sys.stdin.readline().strip()
        li = do_val.split()
        do  = li[0]
        if len(li)>1:
            value = li[1]
        elif len(li) == 1:
            value = 0
        value = int(value)
        if do == "add" and not value in s:
            s.add(value)
        if do == 'remove' and value in s:
            s.remove(value)
        if do == 'check':
            if value in s :
                print(1)
            elif not value in s:
                print(0)    
        if do == 'toggle':
            if value in s:
                s.remove(value)
            elif not value in s:
                s.add(value)
        if do == 'all':
            s.update(range(1,21))
        if do == 'empty':
            s = set() 
      


