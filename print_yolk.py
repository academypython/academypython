N = int(raw_input("N="))
for i in range(N+1):
    # print i
    print ' '*(N-i) + "*" * i + '|' + "*" * i + ' '*(N-i)