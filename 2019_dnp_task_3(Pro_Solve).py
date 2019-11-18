num_pads = [
    [               ], #0
    [               ], #1
    ['a','b','c'    ], #2
    ['d','e','f'    ], #3
    ['g','h','i'    ], #4
    ['j','k','l'    ], #5 
    ['m','n','o'    ], #6 
    ['p','q','r','s'], #7
    ['t','u','v'    ], #8
    ['w','x','y','z']  #9
]
n = int(input())
companies_names=[]
companies_codes=[]
for i in range (0, n):
    companies_names.append(input())
    companies_codes.append('')
    for cn in companies_names[i]:
        for g in range(0,9):
            if cn in num_pads[g]:
                companies_codes[i]=companies_codes[i]+str(g)

my_list=set(companies_codes)
print(len((my_list)))