import sys
k = int(sys.stdin.readline().rstrip())

for i in range(k) :
    num_list = list(map(int,sys.stdin.readline().split()))
    num_list = sorted(num_list[1:])
    for p in range(0, len(num_list)) :

        if p == 0  :
            skew_max = 0
            max = num_list[p]
            min = num_list[p]
            last_value = num_list[p]

        else :
            if num_list[p] > max :
                max = num_list[p]
            if num_list[p] < min :
                min = num_list[p]

            if num_list[p] - last_value > skew_max :
                skew_max = num_list[p] - last_value
            last_value = num_list[p]
    print('Class',i+1, sep = ' ')
    print('Max ',max,', ','Min ',min,', ','Largest gap ',skew_max, sep= '')

