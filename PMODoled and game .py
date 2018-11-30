
# coding: utf-8

# In[ ]:


from pynq.overlays.base import BaseOverlay 
from pynq.lib import Pmod_OLED 
from time import sleep
import random
random.randint(12, 20)
base = BaseOverlay("base.bit") 
pmodoled=Pmod_OLED(base.PMODA,'Hello PYNQ !')
pmodoled.clear()

x=0
y=0#人物位置
ms=0#时间
s=0#子弹位置
def people(x,y):
    pmodoled.draw_rect(0+x,0+y,4+x,3+y)
    pmodoled.draw_line(2+x,3+y,2+x,6+y)
    pmodoled.draw_line(2+x,3+y,0+x,6+y)
    pmodoled.draw_line(2+x,3+y,4+x,6+y)   
i=1
sleep(2)
while 1:
    pmodoled.write(str(ms))#游戏时间
    #移动控制
    if base.buttons[2].read()==1:
        if x<255:
            x=x+1
    elif base.buttons[3].read()==1:
        if x>0:
            x=x-1
    elif base.buttons[0].read()==1: 
        if y<31:
            y=y+1
    elif base.buttons[1].read()==1:
        if y>0:
            y=y-1      
    people(x,y)
    #生成子弹
    if(s==0):
        n1=random.randint(0, 31)
        n2=random.randint(0, 31)
        n3=random.randint(0, 31)
        n4=random.randint(0, 31)
    s=s+1
    if(s%100!=0):
        pmodoled.draw_line(124-s,n1,127-s,n1)
        pmodoled.draw_line(124-s,n2,127-s,n2)
        pmodoled.draw_line(124-s,n3,127-s,n3)
        pmodoled.draw_line(124-s,n4,127-s,n4)
    else:
        s=0
    
    #游戏结束条件
    if((4+x)==(124-s)):
        if((3+y)<(n1+3)):
            if((3+y)>(n1)):
                pmodoled.clear()
                pmodoled.write("game over")
                sleep(100)
        if((3+y)<(n2+3)):
            if((3+y)>(n2)):
                pmodoled.clear()
                pmodoled.write("game over")
                sleep(100)
        if((3+y)<(n3+3)):
            if((3+y)>(n3)):
                pmodoled.clear()
                pmodoled.write("game over")
                sleep(100)
        elif((3+y)<(n4+3)):
            if((3+y)>(n4)):
                pmodoled.clear()
                pmodoled.write("game over")
                sleep(100)
            
    sleep(0.1)
    pmodoled.clear()
    i=i+1
    
    if(i%10==0):
        ms=ms+1
        
    

