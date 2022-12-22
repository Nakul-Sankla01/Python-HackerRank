
if __name__ == '__main__':
    N = int(input())
    l=[]
    while N:
        ch=input().split()
        if ch[0]=='insert':
            l.insert(int(ch[1]),int(ch[2]))
                    
        
        elif ch[0]=='append':
            l.append(int(ch[1]))
        
        elif ch[0]=='pop':
            l.pop()   
        elif ch[0]=='print':
            print(l)
        
        elif ch[0]=='remove':
            l.remove(int(ch[1]))
            
        elif ch[0]=='sort':
            l.sort()
            
        elif ch[0]=='reverse':
            l.reverse()
        else:
            break
            
        N-=1
