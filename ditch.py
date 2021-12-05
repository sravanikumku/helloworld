n=int(input())
for i in range(n):
     F,D,T,FD,BD=[int(x) for x in input("ENTER F D T FD BD").split()]
     P=F-D
     d=F+D
     c=1
     while(True):
            P=P+F
            P1=P
            if P1>0 and P1==FD :
                d=c*(F+D)+F       #if position of robot after moving F distance forward is equal to or  FD the robot will fall in ditch
                print(T*d,end=' ')
                print('F')
                break
            if P1>0 and (P1>FD ) :
                d=c*(F+D)+(F-(P-FD))
                print(T*d,end=' ')  
                print("F")
                break
            P=P-D
            P2=P
            c=c+1#one complete forward and backward moment  of robot
            if P2<0 and abs(P2)==BD :
                d=c*(F+D)
                print(T*d,end=' ')   #if position of robot is equal to or greater BD the robot will fall in ditch
                print('B')
                break
            if P2<0 and abs(P2)>BD :
                d=c*(F+D)-(abs(P2)-BD)
                print(T*d,end=' ')
                print('B')
                break
            if(P==0):
                print('No Ditch')
                break      
    
