def count(value):
    count = 0;
    for i in range(len(value)):
         if(value[i] == "1"):
                   count += 1;
    return count;

def team(n, m, biNum):
    maxOnes = 0;
    array = 0;
    for i in range(n-1):
        for j in range(i+1, n):
            temp = biNum[i] | biNum[j]
            value = '{0:500b}'.format(temp);
            countOnes = count(str(value));
            if(countOnes == maxOnes):
                array += 1;
            if(countOnes > maxOnes):
                array = 1;
                maxOnes = countOnes;

    print maxOnes;
    print array;

temp = raw_input();
nm = [int(i) for i in temp.split()];

biStr = [];
biNum = [];
for i in range(nm[0]):
    biStr.append(raw_input());
    biNum.append(int(biStr[i] , 2));

team(nm[0], nm[1], biNum)
