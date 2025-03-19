class ArrayList :
    # 생성자 및 초기화
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
    
    #메서드
    def isEmpty(self) :
        return self.size == 0
    
    def isFull(self) :
        return self.size == self.capacity
    
    def getEnty(self,pos) :
        if( 0 <= pos < self.size) :
            return self.array[pos]
        else : 
            return None
    
    def insert(self,pos,e):
        if not self.isFull() and 0 <= pos <= self.size :
            # pos 이후의 요소들을 한칸씩 뒤로 밀어 새로운 요소를 삽입할 공간을 만든다
            for i in range(self.size,pos,-1) :
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else : 
            pass

    def delete(self,pos) :
        if not self.isEmpty() and 0 <= pos < self.size :
            # pos의 요소를 꺼낸다.
            e = self.array[pos] 
            for i in range(pos, self.size-1) :
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else :
            pass
        
    def getEntry(self, index):
            if 0 <= index < self.size:
                return self.array[index]  # 인덱스의 값 반환
            return None  # 범위 초과 시 None 반환

    # 문자열 반환
    def __str__(self):
        return str(self.array[0:self.size])