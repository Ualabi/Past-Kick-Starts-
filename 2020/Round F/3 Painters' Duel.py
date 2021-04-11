# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f47fb

T = int(input())
for t in range(T):
    S, RA, PA, RB, PB, C = map(int,input().split())
    board = [[True for _ in range(2*S)] for __ in range(S)]
    board[RA-1][PA-1] = False
    board[RB-1][PB-1] = False
    for c in range(C):
        a,b = map(int,input().split())
        board[a-1][b-1] = False

    def minmax(ra, ca, rb, cb, turno, suma, poss, minim, maxim):
        if poss == 3:
            return suma
        # print(board,suma,turno)
        if turno: # Search for the biggest value
            turno = not turno
            flag = False
            value = -100

            if 0 < ca and board[ra][ca-1]:
                flag = True
                board[ra][ca-1] = False
                aux = minmax(ra, ca-1, rb, cb, turno, suma+1, poss, minim, maxim)
                board[ra][ca-1] = True
                value = max(aux, value)
                # 
                minim = max(minim, value)
                if minim <= maxim:
                    return value
                
            if ca < 2*ra and board[ra][ca+1]:
                flag = True
                board[ra][ca+1] = False
                aux = minmax(ra, ca+1, rb, cb, turno, suma+1, poss, minim, maxim)
                board[ra][ca+1] = True
                value = max(aux, value)
                # 
                minim = max(minim, value)
                if minim <= maxim:
                    return value
                
            if ca%2 == 0 and ra < S-1 and board[ra+1][ca+1]:
                flag = True
                board[ra+1][ca+1] = False
                aux = minmax(ra+1, ca+1, rb, cb, turno, suma+1, poss, minim, maxim)
                board[ra+1][ca+1] = True
                value = max(aux, value)
                # 
                minim = max(minim, value)
                if minim <= maxim:
                    return value
                
            if ca%2 == 1 and board[ra-1][ca-1]:
                flag = True
                board[ra-1][ca-1] = False
                aux = minmax(ra-1, ca-1, rb, cb, turno, suma+1, poss, minim, maxim)
                board[ra-1][ca-1] = True
                value = max(aux, value)
                # 
                minim = max(minim, value)
                if minim <= maxim:
                    return value
                
            if flag:
                return value
            else:
                return minmax(ra, ca, rb, cb, turno, suma, poss|1, minim, maxim)
        
        else: # Search for the smallest value
            turno = not turno
            flag = False
            value = 100

            if 0 < cb and board[rb][cb-1]:
                flag = True
                board[rb][cb-1] = False
                aux = minmax(ra, ca, rb, cb-1, turno, suma-1, poss, minim, maxim)
                board[rb][cb-1] = True
                value = min(aux, value)
                # 
                maxim = min(maxim, value)
                if minim <= maxim:
                    return value
                
            if cb < 2*rb and board[rb][cb+1]:
                flag = True
                board[rb][cb+1] = False
                aux = minmax(ra, ca, rb, cb+1, turno, suma-1, poss, minim, maxim)
                board[rb][cb+1] = True
                value = min(aux, value)
                # 
                maxim = min(maxim, value)
                if minim <= maxim:
                    return value
                
            if cb%2 == 0 and rb < S-1 and board[rb+1][cb+1]:
                flag = True
                board[rb+1][cb+1] = False
                aux = minmax(ra, ca, rb+1, cb+1, turno, suma-1, poss, minim, maxim)
                board[rb+1][cb+1] = True
                value = min(aux, value)
                #
                maxim = min(maxim, value)
                if minim <= maxim:
                    return value

            if cb%2 == 1 and board[rb-1][cb-1]:
                flag = True
                board[rb-1][cb-1] = False
                aux = minmax(ra, ca, rb-1, cb-1, turno, suma-1, poss, minim, maxim)
                board[rb-1][cb-1] = True
                value = min(aux, value)
                #
                maxim = min(maxim, value)
                if minim <= maxim:
                    return value
                
            if flag:
                return value
            else:
                return minmax(ra, ca, rb, cb, turno, suma, poss|2, minim, maxim)

    print('Case #{}: {}'.format(t+1, minmax(RA-1, PA-1, RB-1, PB-1, True, 0, 0, 100, -100)))