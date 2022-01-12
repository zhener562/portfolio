import pygame
from pygame.locals import *
import sys
import random


#player,cardtype,cardname,target player,target field,target indivisual

#permanent description(card type,name,mana cost,original power,original hp,)
screensize=(1300,600)
step=[
    "mss",
    "mms1",
    "msbs",
    "macs",
    "mbcs",
    "mbs",
    "mms2",
    "mes",
    "ess",
    "ems1",
    "esbs",
    "eacs",
    "ebcs",
    "ebs",
    "ems2",
    "ees",
]
nstep=step[0]
pr=[0,0,]
stack=[]
target=[]
result="gamestart"
def preceed():
    global nstep
    global pr
    global result
    if pr[0]==0 and pr[1]==0:
        if len(stack)!=0:

            if stack[-1][1]=="creature":
                stack[-1][0].permanent.append(stack[-1][2])
                creaturec=0
                for j in creaturename:
                    for k in stack[-1][0].permanent:
                        creaturec+=k.name==j
                    
                if stack[-1][0]==p1:
                    stack[-1][2].rect.move_ip(stack[-1][2].rect.width*(creaturec-1)-stack[-1][2].rect[0],200-stack[-1][2].rect[1])
                    stack[-1][2].cc=creaturec+1
                else:
                    stack[-1][2].player=p2
                    stack[-1][2].rect.move_ip(stack[-1][2].rect.width*(creaturec-1)-stack[-1][2].rect[0],100-stack[-1][2].rect[1])
                    stack[-1][2].image = pygame.transform.rotate(stack[-1][2].image, 180)
                    stack[-1][2].cc=creaturec+1
                n=stack[-1][0]
                stack.remove(stack[-1])
                
                
            elif stack[-1][2]=="counter spell":
                print(stack[stack[-1][3]][2]+" countered")
                stack[stack[-1][3]][0].tomb.append(stack[stack[-1][3]][2])
                stack.remove(stack[stack[-1][3]])
                n=stack[-1][0]
                n.tomb.append(stack[-1][2])
                stack.remove(stack[-1])
                
            elif stack[-1][2]=="marder":
                print(stack[-1][3].stack[-1][4].stack[-1][5]+" destroyed")
                stack[-1][3].tomb.append(stack[-1][3].stack[-1][4].stack[-1][5])
                stack[-1][3].stack[-1][4].remove(stack[-1][3].stack[-1][4].stack[-1][5])
                n=stack[-1][0]
                n.tomb.append(stack[-1][2])
                stack.remove(stack[-1])
            
        else:
            
            if nstep=="ees":
                
                for l in p1.permanent:
                    
                    if l.name in creaturename==True:
                        print(l.name)
                        l.creature_get_data()
                        l.attackable=1
                    l.untap()
                    for i in p2.permanent:
                        if i.name in creaturename:
                            i.creature_get_data()
                            i.attackable=1
                p1.drow()
                p1.playableland=1
                p1.attacktime=1
                p1.mana=0
                p2.mana=0
            elif nstep=="mbcs":
                for index,item in enumerate(p1.permanent):
                    if item.name in creaturename and item.attacking:
                        if len(item.blocked)!=0:

                            
                                item.combat()
                                p1.sortpermanent()
                                p2.sortpermanent()
                                p1.attacking.remove(item)
                        else:
                            p2.hp-=item.power
                            print(p2.hp)
                            p1.attacking.remove(item)
                    item.attacking=0
                    
                        
            elif nstep=="mes":
                for i in p2.permanent:
                    if i.name in creaturename:
                        i.creature_get_data()
                    i.untap()
                for i in p1.permanent:
                    if i.name in creaturename:
                        i.creature_get_data()
                        i.attackable=1
                p2.drow()
                p2.playableland=1
                p2.attacktime=1
                p2.mana=0
                p1.mana=0
    
                        


            nstep=step[(step.index(nstep)+1)%16]
        result=nstep
        pr=[1,1]
        print(pr)
        if nstep[0]=="e":
            if pr[1]:
                pr[1]=0
                if nstep=="ems1":
                    p2.outplay()
            elif pr[0]:
                pr[0]=0
            
def go():
    if nstep[0]=="m":
        if pr[0]:
            pr[0]=0
            pr[1]=0
        if nstep=="macs":
            print("bitch")
            if len(p1.attacking)!=0:
                p2.ChooseBlockCreature()
        

            

        
        
    elif nstep[0]=="e":
        if pr[1]:
            pr[1]=0
            if nstep=="ems1":
                p2.outplay()
            
        elif pr[0]:
            pr[0]=0
    if pr[0]==0 and pr[1]==0:
        preceed()
    print(pr)






        
 
def counterspell(player,target):
    if player.mana>=3:
        stack.append([player,"instant","counter spell",target,])
        print("counter spell casted")
        
def marder(player,targetplayer,targetfield,targetindivisual):
    if player.mana>=3:
        stack.append([player,"instant","marder",targetplayer,targetfield,targetindivisual])
        print("marder casted")
        


        
        
deck1=[]

elf=["creature","elf",1,1,1]
bear=["creature","bear",2,2,2]
dear=["creature","dear",3,3,3]
angel=["creature","angel",5,4,4]
dragon=["creature","dragon",6,5,5]
giant=["creature","giant",6,6,6]
demon=["creature","demon",8,7,7]
land=[
    "swamp",
    "mountain",
    "plain",
    "island",
    "forest",
]
creature=[
    elf,
    bear,
    dear,
    angel,
    dragon,
    giant,
    demon,
] 
creaturename=[]
for i in range(len(creature)):   
    creaturename.append(creature[i][1])


for i in range(24):
    deck1.append("swamp")
for i in range(4):
    deck1.append("cancel")
for i in range(8):
    deck1.append("elf")
for i in range(7):
    deck1.append("marder")
for i in range(6):
    deck1.append("bear")
for i in range(5):
    deck1.append("dear")
for i in range(4):
    deck1.append("angel")
for i in range(3):
    deck1.append("dragon")
for i in range(2):
    deck1.append("giant")
for i in range(1):
    deck1.append("demon")
 

class player:
    def __init__(self,name,hp,deck,):
        self.name=name
        self.mana=0
        self.hp=hp
        self.deck=deck
        self.hand=[]
        self.permanent=[]
        self.tapped=[]
        self.tomb=[]
        self.playableland=1
        self.attacktime=1
        self.attacking=[]
        self.landc=0
        self.allcards=[
            self.hand,
            self.permanent
        ]
        random.shuffle(self.deck)
        for i in range(7):
            self.hand.append(self.deck[0])
            self.deck.remove(self.deck[0])
    
    
    def shuffle(self):
        random.shuffle(self.deck)
    def drow(self,times=0):
        if self==p1:
            p1.deck[0]=Hand(p1.deck[0],len(p1.hand))
        self.hand.append(self.deck[0])
        self.deck.remove(self.deck[0])

    def sorthand(self):
        for i in range(len(p1.hand)):
            p1.hand[i].rect.move_ip(p1.hand[i].rect.width*(i)-p1.hand[i].rect[0],0)
    def sortpermanent(self):
        hage=0
        for index,item in enumerate(self.permanent):
            p1c=1
            p2c=1
            if self==p1:
                if item.name in land:
                    item.rect.move_ip(item.rect.width*hage-item.rect.left,300-item.rect.top)
                    hage+=1
                else:
                    item.rect.move_ip(item.rect.width*(index-hage)-item.rect.left,200-item.rect.top)
                    item.cc=p1c
                    p1c+=1

            else:
                if item.name in land:
                    item.rect.move_ip(item.rect.width*hage-item.rect.left,-item.rect.top)
                    hage+=1
                else:
                    item.rect.move_ip(item.rect.width*(index-hage)-item.rect.left,100-item.rect.top)
                    item.cc=p2c
                    p2c+=1
                #item.image = pygame.transform.rotate(item.image, 180)
    def playland(self):
        for i in land:
            for j in range(len(self.hand)):
                if self.hand[j]==i and self.playableland>=1:
                    yju=len(self.permanent)
                    self.permanent.append(i)
                    self.permanent[yju]=Hand(i)
                    hage=self.permanent[yju]
                    landc=0
                    for l in land:
                        for k in self.permanent:
                            landc+=k.name==l
                    hage.rect.move_ip(hage.rect.width*(landc-1),-hage.rect.top)
                    hage.image = pygame.transform.rotate(hage.image, 180)
                    hage.player=p2
                    self.hand.remove(i)
                    self.playableland-=1
                    break
                    
    def outplay(self):
        self.playland()
        print(p2.hand)
        print(p2.permanent)
        self.countland()
        if self.landc!=0:

            self.sumon()
    def countland(self):   
        self.landc=0
        for j in land:
            for k in self.permanent:
                if k.name==j and k.t==0:
                    self.landc+=1
        print(self.landc)
    def sumon(self):
        mc=[]
        hage=self.landc
        print(hage)
        while hage>=1:
            for j in creature:
                for i in range(len(self.hand)):
                
                    
                    if self.hand[i]==j[1] and hage==j[2]:
                        self.hand[i]=Hand(self.hand[i])
                        stack.append([p2,"creature",self.hand[i]])
                        self.hand[i].rect.move_ip(1300-self.hand[i].rect.width-self.hand[i].rect[0],self.hand[i].rect.height*(len(stack)-1)-self.hand[i].rect[1])
                        self.hand.remove(self.hand[i])
                        for p in range(j[2]):
                            for l in land:
                                for k in self.permanent:
                                    if k.name==l and k.t==0:
                                        k.tap()
                                        hage-=1
                                        break
                        break
                        
                        
            hage-=1

    def ChooseBlockCreature(self):
        '''
        BOX=[]
        for index,item in enumerate(p2.permanent):
            for INDEX,ITEM in enumerate(p1.permanent):
                BOX.append([item,ITEM])
            BOX.append([item,None])
        HAGE=[]
        Valuation=[]
        for i in range((INDEX+1)^index):
            kane=[]
            Num=hage(i,INDEX+1)
            for j in range(index):
                if len(Num)<j+1:
                    kane.append(BOX[0])
                else:
                    kane.append(BOX[Num[-(1+j)]+j*(INDEX+1)])
            HAGE.append(kane)
            for i in kane:
                kane[i][0].power
                kane[i][0].health
                if kane[i][1]!=None:
                    kane[i][1].power
                    kane[i][1].health
            


                
                
            
            
        


        '''
        #uncomplate
        for index,item in enumerate(p2.permanent):
            
            print(item.name)
            print(item.t)
            estimatebox=[]
            r=[]
            k=item.name in creaturename
            if item.t==0 and k:
                for in2,it2 in enumerate(p1.attacking):
                

                    value=0
                    
                    if item.power>=it2.toughness:
                        value+=it2.power+it2.toughness/2
                    if it2.power>=item.toughness:
                        value-=item.power+item.toughness/2
                    value+=it2.power/2
                    estimatebox.append(value)
                    r.append(value)
                    print(value)
                    r.sort(reverse=True)
                    
                if r[0]>0:
                    p1.attacking[estimatebox.index(r[0])].blocked.append(item) 
                    print(r)
                    r.clear()    
                    estimatebox.clear()
                      
def hage(x,n):
    if (int(x/n)):
        return hage(int(x/n,n)+str(x%n))
    return str(x%n)

                
            
            
        
        

p1=player("you",20,deck1)
p2=player("enemy",20,deck1)
class Hand(pygame.sprite.Sprite):
    
    def __init__(self,name,number=0,x=0,y=0,p=p1):
        
        # デフォルトグループをセット
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(name+".png").convert_alpha()
        self.name=name
        self.t=0
        self.player=p
        w = self.image.get_width()
        h = self.image.get_height()
        for i in range(len(creaturename)):
            if name==creature[i][1]:
                self.power=creature[i][3]
                self.toughness=creature[i][4]
                self.damage=0
                self.attacking=0
                self.blocked=[]
                self.attackable=0
                self.cc=0


        x=number*w
        y=500-h
        self.rect = Rect(x, y, w, h)
    def creature_get_data(self):
        for i in range(len(creaturename)):
            if self.name==creaturename[i]:
                self.power=creature[i][3]
                self.toughness=creature[i][4]
                self.damege=0
                
                
                
    def tap(self):
        if self.t==0:
            self.image = pygame.transform.rotate(self.image, 90)
            self.t=1
    def untap(self):
        if self.t==1:
            self.t=0
            self.image = pygame.transform.rotate(self.image, 3*90)
    def combat(self):
        print("combat")
        print(self.power)
        print(self.blocked[0].power)
        self.blocked[0].damage+=self.power
        self.damage+=self.blocked[0].power
        if self.damage>=self.toughness:
            self.player.tomb.append(self)
            self.player.permanent.remove(self)
            self.kill()
            
        if self.blocked[0].damage>=self.blocked[0].toughness:
            self.blocked[0].player.tomb.append(self.blocked[0])

            self.blocked[0].player.permanent.remove(self.blocked[0])
            self.blocked[0].kill()
            
        

            

    

def main():
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((screensize))    # 大きさ400*300の画面を生成
    group = pygame.sprite.OrderedUpdates()
    
    Hand.containers = group
   

    for i in range(len(p1.hand)):
        p1.hand[i]=Hand(p1.hand[i],i)
    font = pygame.font.Font(None,45)
    


    
    while (1):
        
        screen.fill((255, 255, 255))  # 画面の背景色
        # スプライトグループを更新
        mystatus = font.render(p1.name+str(p1.hp), True, (150,0,0),(0,0,0)) 
        enemystatus = font.render(p2.name+str(p2.hp), True, (0,0,0),(150,0,0))
        phase=font.render(result, True, (150,0,0),(0,0,0))
        screen.blit(mystatus, [0, 500])# 文字列の表示位置
        screen.blit(enemystatus,[0,530])
        screen.blit(phase,[0,560])
        group.update()
        # スプライトを描画
        group.draw(screen)
        pygame.display.update()
        mouse_pressed = pygame.mouse.get_pressed()
        x,y=pygame.mouse.get_pos()
       
            
        # イベント処理
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_d:
                    p1.drow()
                    p1.playableland=1
                if event.key==K_a:
                    if nstep=="macs" and len(target)!=0 and p1.attacktime==1:

                        for index,item in enumerate(target):
                            if item.attackable==1:
                                item.attacking=1

                                item.tap()
                                print(item.name+" is attaking")
                                p1.attacktime=0
                                p1.attacking.append(item)
                            else:
                                print(item.name+" cant attack")
                        target.clear()
                        print(target)
                if event.key==K_b:
                    if nstep=="mbcs" and target.attaking:
                        for l in p1.permanent:
                            if l.rect.right>x>l.rect.left and l.rect.top<y<l.rect.bottom:
                                target.blocked.append(l)


                if event.key==K_t:
                    for l in p1.permanent:
                        if l.rect.right>x>l.rect.left and l.rect.top<y<l.rect.bottom:
                            if l.t==0:
                                hage=l.name in land
                                if hage==1:
                                    p1.mana+=1
                                    l.image = pygame.transform.rotate(l.image, 90)
                                    print(p1.mana)
                                    l.t=1
                if event.key==K_y:
                        p2.outplay()
                 
                if event.key==K_k:
                    target.clear()
                    print(target)
                if event.key==K_c:
                    for l in group:
                        if l.rect.right>x>l.rect.left and l.rect.top<y<l.rect.bottom:
                            target.append(l)
                            for i in target:
                                print(i.name)
                if event.key==K_g:
                    go()
                if event.key==K_j:                       
                    try:                       
                        p1.permanent.append(target[0])
                        target[0].rect.move_ip(target[0].rect.width*(len(p1.permanent)-1)-target[0].rect[0],-100)
                        p1.hand.remove(target[0])
                        target.clear()
                    except :
                        print("select a target")
                if event.key==K_p:
                    for l in p1.hand:
                        if l.rect.right>x>l.rect.left and l.rect.top<y<l.rect.bottom:
                            hage=l.name in land 
                            hage2= l.name in creaturename
                            
                            if hage==1 and p1.playableland>=1 and (nstep=="mms1" or nstep=="mms2"):
                                p1.permanent.append(l)
                                landc=0
                                for j in land:
                                    for k in p1.permanent:
                                        landc+=k.name==j
                                l.rect.move_ip(l.rect.width*(landc-1)-l.rect[0],-100)
                                p1.hand.remove(l)
                                p1.sorthand()
                                p1.playableland-=1
                            elif hage2==1:
                                for i in creature:
                                    if i[1]==l.name and i[2]<=p1.mana and (nstep=="mms1" or nstep=="mms2"):
                                        
                                        stack.append([p1,"creature",l])
                                        l.rect.move_ip(1300-l.rect.width-l.rect[0],l.rect.height*(len(stack)-1)-l.rect[1])
                                        
                                        p1.hand.remove(l)
                                        p1.mana-=i[2]
                                        p1.sorthand()

                                        
                            

                                
                               

           
                    


                            
                                

                

            # 終了用のイベント処理
            if event.type == QUIT:        # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
'''
        if mouse_pressed[0]:  
            for l in p1.hand:
                if l.rect.right>x>l.rect.left and l.rect.top<y<l.rect.bottom:
                        l.rect.move_ip(x-l.rect.left-l.rect.width/2,y-l.rect.top-l.rect.height/2)
                        hage=l
                        p1.hand.remove(l)
                        p1.hand.insert(0,hage)
                        break
                    '''
                            
if __name__ == "__main__":
    main()
    