import sys
input = sys.stdin.readline()


test_case = int(input.rstrip())
my_list = []
for p in range(test_case) :
    name, dd,mm,yyyy = list(map(str,sys.stdin.readline().split()))
    my_list.append([name,int(dd),int(mm),int(yyyy)])

my_list = sorted(my_list, key = lambda x : (x[3],x[2],x[1]))

print(my_list[-1][0])
print(my_list[0][0])
