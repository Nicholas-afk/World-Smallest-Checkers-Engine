e,f,u,o,t='.b'*5,'b.'*5,'.w'*5,'w.'*5,range(10)
b=[list(e),list(f),list(e),list(f),['.']*10,['.']*10,list(u),list(o),list(u),list(o)]
c=lambda C:(int(C[0])-1,10-int(C[1]))
def v(x,y,X,Y):
 b[Y][X],b[y][x]=b[y][x],'.';d,D=X-x,Y-y
 if abs(d)==abs(D)==2:b[y+D//2][x+d//2]='.'
def g(C):
 d=[-1,1][C=='b']
 for y in range(10):
  for x in range(10):
   if b[y][x]==C:
    for a in(-1,1):
     for m in(1,2):
      X,Y=x+a*m,y+d*m
      if 0<=X<10>Y>=0and b[Y][X]=='.'and(m<2or b[y+d][x+a]in'wb'[C>'b']):yield x,y,X,Y
while 1:[print(*r)for r in b];k=input();v(*c(k[:2]),*c(k[2:]));v(*next(g('b'),[]))
