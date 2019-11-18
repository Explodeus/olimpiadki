n = int(input())
coms=[]
num_coms=[]
final_coms=[]
for p in range(0, n):
    coms.append(input())
for i in range(0, len(coms)):
    num_coms.append('')
    for k in range(0, len(coms[i])):
        if(coms[i][k] == 'a' or coms[i][k] == 'b' or coms[i][k] == 'c'):
            num_coms[i]=num_coms[i]+'2'
        if(coms[i][k] == 'd' or coms[i][k] == 'e' or coms[i][k] == 'f'):
            num_coms[i]=num_coms[i]+'3'
        if(coms[i][k] == 'g' or coms[i][k] == 'h' or coms[i][k] == 'i'):
            num_coms[i]=num_coms[i]+'4'
        if(coms[i][k] == 'j' or coms[i][k] == 'k' or coms[i][k] == 'l'):
            num_coms[i]=num_coms[i]+'5'
        if(coms[i][k] == 'm' or coms[i][k] == 'n' or coms[i][k] == 'o'):
            num_coms[i]=num_coms[i]+'6'
        if(coms[i][k] == 'p' or coms[i][k] == 'q' or coms[i][k] == 'r' or coms[i][k] == 's'):
            num_coms[i]=num_coms[i]+'7'
        if(coms[i][k] == 't' or coms[i][k] == 'u' or coms[i][k] == 'v'):
            num_coms[i]=num_coms[i]+'8'
        if(coms[i][k] == 'w' or coms[i][k] == 'x' or coms[i][k] == 'y' or coms[i][k] == 'z'):
            num_coms[i]=num_coms[i]+'9'
    if num_coms[i] not in final_coms:
        final_coms.append(num_coms[i])
print(len(final_coms))