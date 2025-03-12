import time

def hanoi_tower(n,fr,tmp,to) :
    if n == 1 : #종료조건
        print("원판 1: %s -> %s"%(fr,to))
        return 1

    else :
        cnt = 0
        cnt += hanoi_tower(n-1,fr,to,tmp)
        print("원판 %d: %s -> %s" %(n,fr,to))
        cnt += 1
        cnt += hanoi_tower(n-1,tmp,fr,to)
        return cnt

n = int(input(" 원판의 개수를 입력하세요 : "))
start = time.time()
cnt = hanoi_tower(n,'A','B','C')
end = time.time()
print("총 이동 횟수 : %d" %cnt)
print("총 소요 시간: ", end - start,"s")