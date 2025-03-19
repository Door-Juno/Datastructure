from ArrayList import ArrayList

list = ArrayList()

print("LINE EDITTER !\n")
while True :
    command = input("i : 입력 , d : 삭제, r : 변경, p : 출력, l : 파일열기, s : 저장, q : 종료 =>")
    if command == 'i' :
        pos = int(input("행 번호 입력 : "))
        str = input("내용 입력 :")
        list.insert(pos,str)
    elif command == 'd' :
        pos = int(input("행 번호 입력 : "))
        list.delete(pos)
    elif command == 'r' :
        pos = int(input("행 번호 입력 : "))
        re = input("변경할 내용 입력 : ")
        list.insert(pos,str)
    elif command == 'p' :
        for i in range(list.size) :
            print("[ %d] %s" %(i,list.array[i]))
    elif command == 'l' :
        filename = input("  읽어들일 파일 이름: ")
        infile = open(filename , "r")
        lines = infile.readlines();
        for line in lines:
            list.insert(list.size, line.rstrip('\n'))
        infile.close()
    elif command == 's' :
        filename = input("  저장할 파일 이름: ")
        outfile = open(filename , "w")
        len = list.size
        for i in range(len) :
            outfile.write(list.getEntry(i)+'\n')
        outfile.close()
    elif command == 'q' :
        exit()