import random
from itertools import *
for i in range(10,0,-1):
    print(i)
print("LET'S PLAY")

RR=['Jos Buttler','Sanju Samson','Manan Vohra','David Miller','Riyan Parag','Rahul Tewatia','Shivam Dube','Shreyas Gopal','Chris Morris','Mustafizur Rahman','Chetan Sakariya']
DC=['Shikhar Dhawan','Prithvi Shaw','Ajinkya Rahane','Rishabh Pant','Marcus Stoinis','Shimron Hetmeyer','Chris Woakes','Ravichandran Ashwin','Tom Curran','Amit Mishra','Avesh Khan']
MI=['Rohit Sharma','Quinton DeCock','Surya Kumar Yadav','Ishan Kishan','Hardik Pandya','Kieron Pollard','Krunal Pandya','Macro Jansen','Trent Boult','Rahul Chahar','Jasprit Bumrah']
SRH=['David Warner','Jonny Bairstow','Kane Williamson','Virat Singh','Abhishek Sharma','Vijay Shankar','Kedar Jadhav','Rashid Khan','Bhuvaneshwar Kumar','Khaleel Ahmed','T Natarajan']
CSK=['Ruturaj Gaikwad','Faf Du Plessis','Suresh Raina','Ambati Rayudu','MS Dhoni','Moeen Ali','Ravindra Jadeja','Sam Curran','DJ Bravo','Shardul Thakur','Deepak Chahar']
RCB=['Devdutt Padikkal','Virat Kohli','Shahbaz Ahmed','Glenn Maxwell','AB Devilliers','Dan Christian','Washington Sundar','Kyle Jamieson','Mohammad Siraj','Yuzvendra Chahal','Harshal Patel']
KKR=['NitishRana','ShubmanGill','RahulTripati','ShakibAlHasan','DineshKarthik','AndreRussell','EionMorgan','PatCummins','HarbajanSingh','VarunChakravarthy','PrasidhKrishna']
PBKS=['KL Rahul','Mayank Agarwal','Chris Gayle','Deepak Hooda','Nicholas Pooran','Shahrukh Khan','Riley Meredith','Jyhe Richardson','Murugan Ashwin','Mohammad Shami','Arshdeep Singh']

class ipl:
    def __init__(self,team1,team2,matchno):
        self.hometeam=team1
        self.awayteam=team2
        self.matchno=matchno
        self.p1runs=0
        self.p2runs=0
        self.awaytotalruns=0
        self.aq=2#To choose next player i.e. DC[2]
        self.hq=2
        self.playerbatting=""
        self.hometotalruns=0
        self.player1notout=True
        self.player2notout=True
        self.strikechange=False
        self.awayteamScoresList=[]
        self.awayteamWicketsSequence=[]
        self.hometeamScoresList=[]
        self.hometeamWicketsSequence=[]
        self.homebowlerlist=[]
        self.hometeamBowlerScoresList=[]
        self.awaybowlerlist=[]
        self.awayteamBowlerScoresList=[]
        self.awaywicketscount=0
        self.homewicketscount=0
        self.isItBall5=False
        self.batsmen1TakenBalls=0
        self.batsmen2TakenBalls=0
        self.awaybatsmenTakingBallsList=[]
        self.homebatsmenTakingBallsList=[]
        #self.firstInningsScore=0
        self.secondInningsScore=0
        #self.possiblerunslist=[0,0,0,0,1,1,1,1,2,2,2,3,4,4,4,4,4,5,6,6,6,6,'w','w']
        self.possiblerunslist=['wd','wd','wd','wd','nb','nb',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,5,6,6,6,6,6,6,6,6,6,'w','w','w','w','w','w','w','w','w','w']
        #self.firstinningscore=0
        #self.secondinningscore=0
        self.secondInningsTime=False
        self.no_of_overs=20
        print("Clash Between ",self.hometeam," vs ",self.awayteam)
        fileptr=open("ipl.txt","a")
        fileptr.write("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MATCH NO. ")
        fileptr.write(str(self.matchno))
        fileptr.write(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        fileptr.write("\n")
        fileptr.write("                                    Clash Between ")
        fileptr.write(self.hometeam)
        fileptr.write(" vs ")
        fileptr.write(self.awayteam)
        fileptr.write("\n")
        fileptr.close()
        
    def homeTeamPlayers(self,hteam,homecaptain):
        self.hteam=hteam
        self.homecaptain=homecaptain
        if(self.homecaptain=="Sanju Samson"):
            self.homebowlers=['Rahul Tewatia','Shidvam Dube','Shreyas Gopal','Chris Morris','Mustafizur Rahman','Chetan Sakariya']
        elif(self.homecaptain=="Rishabh Pant"):
            self.homebowlers=['Marcus Stoinis','Chris Woakes','Ravichandran Ashwin','Tom Curran','Amit Mishra','Avesh Khan']
        elif(self.homecaptain=="David Warner"):
            self.homebowlers=['Abhishek Sharma','Vijay Shankar','Kedar Jadhav','Rashid Khan','Bhuvaneshwar Kumar','Khaleel Ahmed','T Natarajan']
        elif(self.homecaptain=="Virat Kohli"):
            self.homebowlers=['Shahbaz Ahmed','Glenn Maxwell','Dan Christian','Washington Sundar','Kyle Jamieson','Mohammad Siraj','Yuzvendra Chahal','Harshal Patel']
        elif(self.homecaptain=="MS Dhoni"):
            self.homebowlers=['Moeen Ali','Ravindra Jadeja','Sam Curran','DJ Bravo','Shardul Thakur','Deepak Chahar']
        elif(self.homecaptain=="KL Rahul"):
            self.homebowlers=['Riley Meredith','Jyhe Richardson','Murugan Ashwin','Mohammad Shami','Arshdeep Singh']
        elif(self.homecaptain=="Eion Morgan"):
            self.homebowlers=['Shakib Al Hasan','Andre Russell','Pat Cummins','Harbajan Singh','Varun Chakravarthy','Prasidh Krishna']
        elif(self.homecaptain=="Rohit Sharma"):
            self.homebowlers=['Hardik Pandya','Kieron Pollard','Krunal Pandya','Macro Jansen','Trent Boult','Rahul Chahar','Jasprit Bumrah']
    def awayTeamPlayers(self,ateam,awaycaptain):
        self.ateam=ateam
        self.awaycaptain=awaycaptain
        if(self.awaycaptain=="Sanju Samson"):
            self.awaybowlers=['Rahul Tewatia','Shivam Dube','Shreyas Gopal','Chris Morris','Mustafizur Rahman','Chetan Sakariya']
        elif(self.awaycaptain=="Rishabh Pant"):
            self.awaybowlers=['Marcus Stoinis','Chris Woakes','Ravichandran Ashwin','Tom Curran','Amit Mishra','Avesh Khan']
        elif(self.awaycaptain=="David Warner"):
            self.awaybowlers=['Abhishek Sharma','Vijay Shankar','Kedar Jadhav','Rashid Khan','Bhuvaneshwar Kumar','Khaleel Ahmed','T Natarajan']
        elif(self.awaycaptain=="Virat Kohli"):
            self.awaybowlers=['Shahbaz Ahmed','Glenn Maxwell','Dan Christian','Washington Sundar','Kyle Jamieson','Mohammad Siraj','Yuzvendra Chahal','Harshal Patel']
        elif(self.awaycaptain=="MS Dhoni"):
            self.awaybowlers=['Moeen Ali','Ravindra Jadeja','Sam Curran','DJ Bravo','Shardul Thakur','Deepak Chahar']
        elif(self.awaycaptain=="KL Rahul"):
            self.awaybowlers=['Riley Meredith','Jyhe Richardson','Murugan Ashwin','Mohammad Shami','Arshdeep Singh']
        elif(self.awaycaptain=="Eion Morgan"):
            self.awaybowlers=['Shakib Al Hasan','Andre Russell','Pat Cummins','Harbajan Singh','Varun Chakravarthy','Prasidh Krishna']
        elif(self.awaycaptain=="Rohit Sharma"):
            self.awaybowlers=['Hardik Pandya','Kieron Pollard','Krunal Pandya','Macro Jansen','Trent Boult','Rahul Chahar','Jasprit Bumrah']
    
    def toss(self):
        print("It's Toss Time")
        print(self.homecaptain,",Captain of",self.hometeam," toss up the coin")
        
        tossno=random.randint(0,1)#toss number 0  head  toss number 1 tail
        tossoutput=""
        if(tossno==0):
            tossoutput=tossoutput+"heads"
        elif(tossno==1):
            tossoutput=tossoutput+"tails"
        self.awaytoss=False
        self.hometoss=False
        print(self.awaycaptain,",Captain of",self.awayteam," says",end="")
        tosssaid=input("(heads or tails) :")
        print("It is ",tossoutput)
        if(tosssaid==tossoutput):
            self.awaytoss=True
            print(self.awaycaptain," won the toss")
            print("What do you want to choose",self.awaycaptain,"(bat/bowl):")
            self.choice=input()
        elif(tosssaid!=tossoutput):
            self.hometoss=True
            print(self.homecaptain," won the toss")
            print("What do you want to choose",self.homecaptain,"(bat/bowl):")
            self.choice=input()
        if(self.awaytoss):
            self.awayteamperform(self.choice)
            self.secondInningsTime=True
            if(self.choice=="bat"):
                self.firstInningsScore=self.awaytotalruns        #####################KKKKKKKKKKKKKKKKKKK
            elif(self.choice=="bowl"):
                self.firstInningsScore=self.hometotalruns        #####################KKKKKKKKKKKKKKKKKKK
            print("\n\n-----------INNINGS BREAK---------------\n\n")
            self.p1runs=0
            self.p2runs=0
            self.hometeamperform(self.choice)
        elif(self.hometoss):
            self.hometeamperform(self.choice)
            self.secondInningsTime=True
            if(self.choice=="bat"):
                self.firstInningsScore=self.hometotalruns        #####################KKKKKKKKKKKKKKKKKKK
            elif(self.choice=="bowl"):
                self.firstInningsScore=self.awaytotalruns        #####################KKKKKKKKKKKKKKKKKKK
            print("\n\n-----------INNINGS BREAK---------------\n\n")
            self.p1runs=0
            self.p2runs=0
            self.awayteamperform(self.choice)
    def awaybatsmenScore(self,batsmen,runs):
        self.batsmen=batsmen
        self.runs=runs
        self.awayteamScoresList.append(self.runs)
        self.awayteamWicketsSequence.append(self.batsmen)
        print(self.batsmen,":OUT for",self.runs," runs")
    def awaybatsmenNotOutScore(self,batsmen,runs):
        self.batsmen=batsmen
        self.runs=runs
        self.awayteamScoresList.append(self.runs)
        self.awayteamWicketsSequence.append(self.batsmen)
    def awayplayer1runs(self,batsmen1,r1,P1WICKET=False):
        self.r1=r1
        self.batsmen1=batsmen1
        self.p1runs=self.p1runs+self.r1
        print(self.batsmen1,":",self.p1runs," runs\n\n")
        if(P1WICKET):
            self.awaybatsmenScore(self.batsmen1,self.p1runs)
            self.p1runs=0  
    def awayplayer2runs(self,batsmen2,r2,P2WICKET=False):
        self.r2=r2
        self.batsmen2=batsmen2
        self.p2runs=self.p2runs+self.r2
        print(self.batsmen2,":",self.p2runs," runs\n\n")
        if(P2WICKET):
            self.awaybatsmenScore(self.batsmen2,self.p2runs)
            self.p2runs=0
    def awayplayerTakingBalls(self,ballsTaken):
        self.awaybatsmenTakingBallsList.append(ballsTaken)

    def homeplayerTakingBalls(self,ballsTaken):
        self.homebatsmenTakingBallsList.append(ballsTaken)

    def strikeChange(self,player1,player2):
        if(self.playerbatting==player1):
            self.playerbatting=player2
        else:
            self.playerbatting=player1
        
        
        
    def awayteamperform(self,choice):
        if(self.choice=="bat"):
            if(self.secondInningsTime):
                if(self.secondInningsScore<=self.firstInningsScore):      #$$############$$$$$$$$$$$$$$$$$$$$#########
                    #print("Openers dhawan and prithvi came into the crease")
                    def over(homebowler,twoplayers,playerbatting):
                        self.overruns=0
                        self.homebowlergivenruns=0
                        if(self.player1notout and self.player2notout):
                            self.player1=twoplayers[0]
                            self.player2=twoplayers[1]
                        elif(self.player1notout and self.player3notout):
                            self.player1=twoplayers[0]
                            self.player3=twoplayers[1]
                        self.playerbatting=playerbatting############
                        i=1
                        while(i<=self.balls_in_over):
                            if(self.playerbatting==self.player1):
                                self.batsmen1TakenBalls=self.batsmen1TakenBalls+1
                            else:
                                self.batsmen2TakenBalls=self.batsmen2TakenBalls+1
                            if(self.secondInningsScore>self.firstInningsScore):
                                break
                            print("\n")
                            print(homebowler,"to",self.playerbatting)
                            print("Enter no. of runs scored for ball",i,":")
                            r=random.choice(self.possiblerunslist)#input()
                            print(r)
                            if(r=='w'):
                                
                                self.awaywicketscount=self.awaywicketscount+1
                                print("WICKET")
                                r=0

                                if(self.playerbatting==self.player1 and self.awaywicketscount!=10):
                                    self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    
                                    
                                elif(self.playerbatting==self.player2 and self.awaywicketscount!=10):
                                    self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                                    
                                if(self.playerbatting==self.player1 and self.awaywicketscount==10):
                                    self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    self.batsmen2TakenBalls=0
                                elif(self.playerbatting==self.player2 and self.awaywicketscount==10):
                                    self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    self.batsmen2TakenBalls=0
                                if(self.overs==self.no_of_overs and i==self.balls_in_over):     ###############EXTRA PART
                                    if(self.playerbatting==self.player1):
                                        self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                        self.batsmen1TakenBalls=0
                                    elif(self.playerbatting==self.player2):
                                        self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                        self.batsmen2TakenBalls=0  
                                   
                                
                                if((self.overs==self.no_of_overs and i==self.balls_in_over) or self.awaywicketscount==10):###
                                    if(self.playerbatting==self.player1):
                                        self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                                    elif(self.playerbatting==self.player2):
                                        self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    self.printAwayScores()
                                    
                                
            
                                if(self.playerbatting==self.player1):
                                    self.awayplayer1runs(self.player1,r,True)
                                    if(self.awaywicketscount<10):
                                        self.player1=self.ateam[self.aq]
                                        self.aq=self.aq+1
                                        self.playerbatting=self.player1
                                    
                                if(self.playerbatting==self.player2):
                                    self.awayplayer2runs(self.player2,r,True)
                                    if(self.awaywicketscount<10):
                                        self.player2=self.ateam[self.aq]
                                        self.aq=self.aq+1
                                        self.playerbatting=self.player2
                                        
                                if(self.awaywicketscount==10):
                                    self.hometeamBowlerScoresList.append(self.homebowlergivenruns)###M###################MMMMMMMM
                                    self.homebowlerlist[self.overs-1]=self.homebowlerlist[self.overs-1]+"*"
                                    self.printAwayTotalScores()
                                    break
                                if(i!=self.balls_in_over):       ######++++++++++++++++++++++++++change
                                    if(i==5):
                                        self.isItBall5=True
                                    else:
                                        self.isItBall5=False
                                    i=i+1
                                
                                if(self.overs==self.no_of_overs and i==self.balls_in_over and self.isItBall5==False):
                                    self.hometeamBowlerScoresList.append(self.homebowlergivenruns)#
                                    return [self.player1,self.player2]
                                if(i!=6 or (i==6 and self.isItBall5==True)):                    ###++++++++++++++++++++++++
                                    if(i==6 and self.isItBall5==True):
                                        self.isItBall5=False
                                    continue
                                elif(self.overs!=self.no_of_overs and i==self.balls_in_over and self.isItBall5==False):
                                    self.hometeamBowlerScoresList.append(self.homebowlergivenruns)#
                                    self.printAwayScores()
                                    return [self.player1,self.player2]
                                
                            
                            elif(r=='wd'):
                                r=0
                                print("Wide")
                                self.homebowlergivenruns=self.homebowlergivenruns+1
                                self.awaytotalruns=self.awaytotalruns+1
                                self.secondInningsScore=self.secondInningsScore+1
                                
                                continue
                            elif(r=='nb'):
                                r=0
                                self.NoBallRuns=random.randint(0,6)
                                print("No Ball")
                                self.homebowlergivenruns=self.homebowlergivenruns+1+self.NoBallRuns
                                self.awaytotalruns=self.awaytotalruns+1+self.NoBallRuns
                                self.secondInningsScore=self.secondInningsScore+1+self.NoBallRuns
                                self.NoBallRuns=0
                                
                            else:
                                r=int(r)
                                self.secondInningsScore=self.secondInningsScore+r  #$$$$$$$$$$$$$$$$$$#
                            self.homebowlergivenruns=self.homebowlergivenruns+r
                            self.overruns=self.overruns+r
                            self.awaytotalruns=self.awaytotalruns+r
                            if(self.playerbatting==self.player1):
                                self.awayplayer1runs(self.player1,r)
                            if(self.playerbatting==self.player2):
                                self.awayplayer2runs(self.player2,r)
                            if(r%2!=0):
                                if(self.playerbatting==self.player1):
                                    self.playerbatting=self.player2
                                elif(self.playerbatting==self.player2):
                                    self.playerbatting=self.player1
                                
                            if(i==self.balls_in_over):#
                                self.hometeamBowlerScoresList.append(self.homebowlergivenruns)#
                            if(i==self.balls_in_over):
                                self.printAwayScores() 
                                if(self.overs==self.no_of_overs):
                                    if(self.playerbatting==self.player1):
                                        self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)
                                        self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                                        
                                    elif(self.playerbatting==self.player2):
                                        self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                                        self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    
                                    if(self.playerbatting==self.player1):                    ####LAST CHANGED
                                        self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                        self.batsmen1TakenBalls=0
                                        self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                        self.batsmen2TakenBalls=0
                                    else:
                                        self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                        self.batsmen2TakenBalls=0
                                        self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                        self.batsmen1TakenBalls=0
                                    
                                return [self.player1,self.player2]
                            if(self.secondInningsScore>self.firstInningsScore):
                                return [self.player1,self.player2]
                            if(r==0 or r==1 or r==2 or r==3 or r==4 or r==5 or r==6):
                                i=i+1
                                
                    for self.overs in range(1,self.no_of_overs+1):
                        self.balls_in_over=6
                        self.homebowler=random.choice(self.homebowlers)
                        if(self.overs!=1):
                            while(self.homebowler==self.homebowlerlist[self.overs-2]):
                                self.homebowler=random.choice(self.homebowlers)
                                
                        if(self.secondInningsScore<=self.firstInningsScore):
                            self.homebowlerlist.append(self.homebowler)#
                        if(self.awaywicketscount==10):####
                            break
                        if(self.secondInningsScore>self.firstInningsScore):
                            self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)      #$$$$$$$$$$$$$$$$$$$$$$$$$#
                            self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                            self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                            self.awayplayerTakingBalls(self.batsmen2TakenBalls)            ######SEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
                            
                            self.hometeamBowlerScoresList.append(self.homebowlergivenruns)
                            self.printAwayTotalScores()
                            break
                        if(self.overs==1):
                            self.awaytwobatsmenlist=[self.ateam[0],self.ateam[1]]
                            self.playerbatting=self.ateam[0]
                            players=over(self.homebowler,self.awaytwobatsmenlist,self.playerbatting)
                        elif(self.overs!=1 and self.overs!=self.no_of_overs):
                            #self.strikechange=True
                            self.strikeChange(players[0],players[1])
                            self.awaytwobatsmenlist=players
                            players=over(self.homebowler,players,self.playerbatting)
                        elif(self.overs==self.no_of_overs):
                            #self.strikechange=True
                            self.strikeChange(players[0],players[1])
                            self.awaytwobatsmenlist=players
                            players=over(self.homebowler,players,self.playerbatting)
                            if(self.awaywicketscount!=10 and self.secondInningsScore<=self.firstInningsScore):
                                self.printAwayTotalScores()
                
            else:
                ####print("Openers dhawan and prithvi came into the crease")
                def over(homebowler,twoplayers,playerbatting):
                    self.overruns=0
                    self.homebowlergivenruns=0
                    if(self.player1notout and self.player2notout):
                        self.player1=twoplayers[0]
                        self.player2=twoplayers[1]
                    elif(self.player1notout and self.player3notout):
                        self.player1=twoplayers[0]
                        self.player3=twoplayers[1]
                    self.playerbatting=playerbatting############
                    i=1                                   ##########++++++++++++++++++++++++++++++++++++
                    while(i<=self.balls_in_over):         ###########++++++++++++++++++++++++++++++
                    #for i in range(1,self.balls_in_over+1):
                        if(self.playerbatting==self.player1):
                            self.batsmen1TakenBalls=self.batsmen1TakenBalls+1
                        else:
                            self.batsmen2TakenBalls=self.batsmen2TakenBalls+1
                        print("\n")
                        print(homebowler,"to",self.playerbatting)
                        print("Enter no. of runs scored for ball",i,":")
                        r=random.choice(self.possiblerunslist)#input()
                        print(r)
                
                        if(r=='w'):
                            self.awaywicketscount=self.awaywicketscount+1
                            print("WICKET")
                            r=0

                            if(self.playerbatting==self.player1 and self.awaywicketscount!=10):
                                self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                self.batsmen1TakenBalls=0       
                            elif(self.playerbatting==self.player2 and self.awaywicketscount!=10):
                                self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                self.batsmen2TakenBalls=0
                            if(self.playerbatting==self.player1 and self.awaywicketscount==10):
                                self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                self.batsmen1TakenBalls=0
                                self.batsmen2TakenBalls=0
                            elif(self.playerbatting==self.player2 and self.awaywicketscount==10):
                                self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                self.batsmen1TakenBalls=0
                                self.batsmen2TakenBalls=0
                            if(self.overs==self.no_of_overs and i==self.balls_in_over):     ###############EXTRA PART
                                if(self.playerbatting==self.player1):
                                    self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                elif(self.playerbatting==self.player2):
                                    self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                            
                            if((self.overs==self.no_of_overs and i==self.balls_in_over) or self.awaywicketscount==10):
                                if(self.playerbatting==self.player1):
                                    self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                                elif(self.playerbatting==self.player2):
                                    self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)
                                self.printAwayScores()
                                
                            if(self.playerbatting==self.player1):
                                self.awayplayer1runs(self.player1,r,True)
                                if(self.awaywicketscount<10):
                                    self.player1=self.ateam[self.aq]
                                    self.aq=self.aq+1
                                    self.playerbatting=self.player1
                                
                            if(self.playerbatting==self.player2):
                                self.awayplayer2runs(self.player2,r,True)
                                if(self.awaywicketscount<10):
                                    self.player2=self.ateam[self.aq]
                                    self.aq=self.aq+1
                                    self.playerbatting=self.player2
                                
                            if(self.awaywicketscount==10):
                                self.hometeamBowlerScoresList.append(self.homebowlergivenruns)###M###################MMMMMMMM
                                self.homebowlerlist[self.overs-1]=self.homebowlerlist[self.overs-1]+"*"
                                self.printAwayTotalScores()
                                break

                            if(i!=self.balls_in_over):       ######++++++++++++++++++++++++++
                                if(i==5):
                                    self.isItBall5=True
                                else:
                                    self.isItBall5=False
                                i=i+1
                                
                            if(self.overs==self.no_of_overs and i==self.balls_in_over and self.isItBall5==False): #########++++++++++++
                                self.hometeamBowlerScoresList.append(self.homebowlergivenruns)#
                                i=i+1
                                return [self.player1,self.player2]
                            if(i!=6 or (i==6 and self.isItBall5==True)):                    ###++++++++++++++++++++++++
                                if(i==6 and self.isItBall5==True):
                                    self.isItBall5=False
                                continue
                            elif(self.overs!=self.no_of_overs and i==self.balls_in_over and self.isItBall5==False):    ###########+++++++++++++++
                                self.hometeamBowlerScoresList.append(self.homebowlergivenruns)#
                                self.printAwayScores()
                                i=i+1
                                return [self.player1,self.player2]
                            
                        elif(r=='wd'):
                            r=0
                            print("Wide")
                            self.homebowlergivenruns=self.homebowlergivenruns+1
                            self.awaytotalruns=self.awaytotalruns+1
                            
                            continue
                            
                        elif(r=='nb'):
                            r=0
                            print("No Ball")
                            self.NoBallRuns=random.randint(0,6)
                            self.homebowlergivenruns=self.homebowlergivenruns+1+self.NoBallRuns
                            self.awaytotalruns=self.awaytotalruns+1+self.NoBallRuns
                            self.NoBallRuns=0
                            continue
                            
                        else:
                            r=int(r)
                        self.homebowlergivenruns=self.homebowlergivenruns+r
                        self.overruns=self.overruns+r
                        self.awaytotalruns=self.awaytotalruns+r
                        if(self.playerbatting==self.player1):
                            self.awayplayer1runs(self.player1,r)
                        if(self.playerbatting==self.player2):
                            self.awayplayer2runs(self.player2,r)
                        if(r%2!=0):
                            if(self.playerbatting==self.player1):
                                self.playerbatting=self.player2
                            elif(self.playerbatting==self.player2):
                                self.playerbatting=self.player1
                            
                        if(i==self.balls_in_over):#
                            self.hometeamBowlerScoresList.append(self.homebowlergivenruns)#
                        if(i==self.balls_in_over):
                            self.printAwayScores()
                            if(self.overs==self.no_of_overs):
                                if(self.playerbatting==self.player1):
                                    self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                                elif(self.playerbatting==self.player2):
                                    self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                                    self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    
                                if(self.playerbatting==self.player1):                    ####LAST CHANGED
                                    self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                                else:
                                    self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                                    self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                            return [self.player1,self.player2]
                        if(r==0 or r==1 or r==2 or r==3 or r==4 or r==5 or r==6):
                            i=i+1    
                for self.overs in range(1,self.no_of_overs+1):
                    self.balls_in_over=6
                    self.homebowler=random.choice(self.homebowlers)
                    if(self.overs!=1):
                        while(self.homebowler==self.homebowlerlist[self.overs-2]):
                            self.homebowler=random.choice(self.homebowlers)
                    self.homebowlerlist.append(self.homebowler)#
                    if(self.awaywicketscount==10):
                        break
                    if(self.overs==1):
                        self.awaytwobatsmenlist=[self.ateam[0],self.ateam[1]]
                        self.playerbatting=self.ateam[0]
                        players=over(self.homebowler,self.awaytwobatsmenlist,self.playerbatting)
                    elif(self.overs!=1 and self.overs!=self.no_of_overs):
                        #self.strikechange=True
                        self.strikeChange(players[0],players[1])
                        self.awaytwobatsmenlist=players
                        players=over(self.homebowler,players,self.playerbatting)
                    elif(self.overs==self.no_of_overs):
                        #self.strikechange=True
                        self.strikeChange(players[0],players[1])
                        self.awaytwobatsmenlist=players
                        players=over(self.homebowler,players,self.playerbatting)
                        if(self.awaywicketscount!=10):
                            self.printAwayTotalScores()
                
                    
                    
        else:
            if(self.secondInningsTime):
                ####print("Openers buttler and sanju came into the crease")
                if(self.secondInningsScore<=self.firstInningsScore):      #$$############$$$$$$$$$$$$$$$$$$$$#########
                    def over(awaybowler,twoplayers,playerbatting):
                        self.overruns=0
                        self.awaybowlergivenruns=0
                        if(self.player1notout and self.player2notout):
                            self.player1=twoplayers[0]
                            self.player2=twoplayers[1]
                        elif(self.player1notout and self.player3notout):
                            self.player1=twoplayers[0]
                            self.player3=twoplayers[1]
                        self.playerbatting=playerbatting############
                        i=1                                   ##########++++++++++++++++++++++++++++++++++++
                        while(i<=self.balls_in_over):
                            if(self.playerbatting==self.player1):
                                self.batsmen1TakenBalls=self.batsmen1TakenBalls+1
                            else:
                                self.batsmen2TakenBalls=self.batsmen2TakenBalls+1
                            if(self.secondInningsScore>self.firstInningsScore):
                                break
                            print("\n")
                            print(awaybowler,"to",self.playerbatting)
                            print("Enter no. of runs scored for ball",i,":")
                            r=random.choice(self.possiblerunslist)#input()
                            print(r)
                            if(r=='w'):
                                self.homewicketscount=self.homewicketscount+1
                                print("WICKET")
                                r=0
                                if(self.playerbatting==self.player1 and self.awaywicketscount!=10):
                                    self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    
                                    
                                elif(self.playerbatting==self.player2 and self.awaywicketscount!=10):
                                    self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                                    
                                if(self.playerbatting==self.player1 and self.awaywicketscount==10):
                                    self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    self.batsmen2TakenBalls=0
                                elif(self.playerbatting==self.player2 and self.awaywicketscount==10):
                                    self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    self.batsmen2TakenBalls=0
                                if(self.overs==self.no_of_overs and i==self.balls_in_over):     ###############EXTRA PART
                                    if(self.playerbatting==self.player1):
                                        self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                        self.batsmen1TakenBalls=0
                                    elif(self.playerbatting==self.player2):
                                        self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                        self.batsmen2TakenBalls=0
                                        
                                if((self.overs==self.no_of_overs and i==self.balls_in_over) or self.homewicketscount==10):
                                    if(self.playerbatting==self.player1):
                                        self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                                    elif(self.playerbatting==self.player2):
                                        self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    self.printHomeScores()

                                
                                if(self.playerbatting==self.player1):
                                    self.homeplayer1runs(self.player1,r,True)
                                    if(self.homewicketscount<10):
                                        self.player1=self.hteam[self.hq]
                                        self.hq=self.hq+1
                                        self.playerbatting=self.player1
                                    
                                if(self.playerbatting==self.player2):
                                    self.homeplayer2runs(self.player2,r,True)
                                    if(self.homewicketscount<10):
                                        self.player2=self.hteam[self.hq]
                                        self.hq=self.hq+1
                                        self.playerbatting=self.player2
                                
                                if(self.homewicketscount==10):
                                    self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)###M###################MMMMMMMM
                                    self.awaybowlerlist[self.overs-1]=self.awaybowlerlist[self.overs-1]+"*"
                                    self.printHomeTotalScores()
                                    break
                                
                                if(i!=self.balls_in_over):       ######++++++++++++++++++++++++++
                                    if(i==5):
                                        self.isItBall5=True
                                    else:
                                        self.isItBall5=False
                                    i=i+1
                                
                                if(self.overs==self.no_of_overs and i==self.balls_in_over and self.isItBall5==False): #########++++++++++++
                                    self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)#
                                    return [self.player1,self.player2]
                                if(i!=6 or (i==6 and self.isItBall5==True)):                    ###++++++++++++++++++++++++
                                    if(i==6 and self.isItBall5==True):
                                        self.isItBall5=False
                                    continue
                                elif(self.overs!=self.no_of_overs and i==self.balls_in_over and self.isItBall5==False):
                                    self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)#
                                    self.printHomeScores()
                                    return [self.player1,self.player2]
                                
                            elif(r=='wd'):
                                r=0
                                print("Wide")
                                self.awaybowlergivenruns=self.awaybowlergivenruns+1
                                self.hometotalruns=self.hometotalruns+1
                                self.secondInningsScore=self.secondInningsScore+1
                                
                                continue
                            elif(r=='nb'):
                                r=0
                                self.NoBallRuns=random.randint(0,6)
                                print("No Ball")
                                self.awaybowlergivenruns=self.awaybowlergivenruns+1+self.NoBallRuns
                                self.hometotalruns=self.hometotalruns+1+self.NoBallRuns
                                self.secondInningsScore=self.secondInningsScore+1+self.NoBallRuns
                                self.NoBallRuns=0
                            else:
                                r=int(r)
                                self.secondInningsScore=self.secondInningsScore+r
                            self.awaybowlergivenruns=self.awaybowlergivenruns+r
                            self.overruns=self.overruns+r
                            self.hometotalruns=self.hometotalruns+r
                            if(self.playerbatting==self.player1):
                                self.homeplayer1runs(self.player1,r)
                            if(self.playerbatting==self.player2):
                                self.homeplayer2runs(self.player2,r)
                            if(r%2!=0):
                                if(self.playerbatting==self.player1):
                                    self.playerbatting=self.player2
                                elif(self.playerbatting==self.player2):
                                    self.playerbatting=self.player1
                                
                            if(i==self.balls_in_over):#
                                self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)#
                            if(i==self.balls_in_over):
                                self.printHomeScores()
                                if(self.overs==self.no_of_overs):
                                    if(self.playerbatting==self.player1):
                                        self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)
                                        self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                                    elif(self.playerbatting==self.player2):
                                        self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                                        self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    
                                    if(self.playerbatting==self.player1):                    ####LAST CHANGED
                                        self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                        self.batsmen1TakenBalls=0
                                        self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                        self.batsmen2TakenBalls=0
                                    else:
                                        self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                        self.batsmen2TakenBalls=0
                                        self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                        self.batsmen1TakenBalls=0
                                    self.HomeTotalScores()
                                return [self.player1,self.player2]
                            if(self.secondInningsScore>self.firstInningsScore):
                                return [self.player1,self.player2]
                            if(r==0 or r==1 or r==2 or r==3 or r==4 or r==5 or r==6):
                                i=i+1
                            
                    for self.overs in range(1,self.no_of_overs+1):
                        self.balls_in_over=6
                        self.awaybowler=random.choice(self.awaybowlers)
                        if(self.overs!=1):
                            while(self.awaybowler==self.awaybowlerlist[self.overs-2]):
                                self.awaybowler=random.choice(self.awaybowlers)
                        self.awaybowlerlist.append(self.awaybowler)#
                        if(self.homewicketscount==10):
                            break
                        if(self.secondInningsScore>self.firstInningsScore):
                            self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)      #$$$$$$$$$$$$$$$$$$$$$$$$$#
                            self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                            self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)
                            self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                            self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                            self.printHomeTotalScores()
                            break
                        if(self.overs==1):
                            self.hometwobatsmenlist=[self.hteam[0],self.hteam[1]]
                            self.playerbatting=self.hteam[0]
                            players=over(self.awaybowler,self.hometwobatsmenlist,self.playerbatting)
                        elif(self.overs!=1 and self.overs!=self.no_of_overs):
                            #self.strikechange=True
                            self.strikeChange(players[0],players[1])
                            self.hometwobatsmenlist=players
                            players=over(self.awaybowler,players,self.playerbatting)
                        elif(self.overs==self.no_of_overs):
                            #self.strikechange=True
                            self.strikeChange(players[0],players[1])
                            self.hometwobatsmenlist=players
                            players=over(self.awaybowler,players,self.playerbatting)
                            if(self.homewicketscount!=10 and self.secondInningsScore<=self.firstInningsScore):
                                self.printHomeTotalScores()
                            
                
            else:
                def over(awaybowler,twoplayers,playerbatting):
                    self.overruns=0
                    self.awaybowlergivenruns=0
                    if(self.player1notout and self.player2notout):
                        self.player1=twoplayers[0]
                        self.player2=twoplayers[1]
                    elif(self.player1notout and self.player3notout):
                        self.player1=twoplayers[0]
                        self.player3=twoplayers[1]
                    self.playerbatting=playerbatting############
                    i=1                                   ##########++++++++++++++++++++++++++++++++++++
                    while(i<=self.balls_in_over):
                        if(self.playerbatting==self.player1):
                            self.batsmen1TakenBalls=self.batsmen1TakenBalls+1
                        else:
                            self.batsmen2TakenBalls=self.batsmen2TakenBalls+1
                        print("\n")
                        print(awaybowler,"to",self.playerbatting)
                        print("Enter no. of runs scored for ball",i,":")
                        r=random.choice(self.possiblerunslist)#input()
                        print(r)
                        if(r=='w'):
                            self.homewicketscount=self.homewicketscount+1
                            print("WICKET")
                            r=0
                            if(self.playerbatting==self.player1 and self.homewicketscount!=10):
                                self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                self.batsmen1TakenBalls=0
                            elif(self.playerbatting==self.player2 and self.homewicketscount!=10):
                                self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                self.batsmen2TakenBalls=0
                            if(self.playerbatting==self.player1 and self.homewicketscount==10):
                                self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                self.batsmen1TakenBalls=0
                                self.batsmen2TakenBalls=0
                            elif(self.playerbatting==self.player2 and self.homewicketscount==10):
                                self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                self.batsmen1TakenBalls=0
                                self.batsmen2TakenBalls=0
                            if(self.overs==self.no_of_overs and i==self.balls_in_over):     ###############EXTRA PART
                                if(self.playerbatting==self.player1):
                                    self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                elif(self.playerbatting==self.player2):
                                    self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                            
                            if((self.overs==self.no_of_overs and i==self.balls_in_over) or self.homewicketscount==10):
                                if(self.playerbatting==self.player1):
                                    self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                                elif(self.playerbatting==self.player2):
                                    self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)
                                self.printHomeScores()
                            
                                
                            if(self.playerbatting==self.player1):
                                self.homeplayer1runs(self.player1,r,True)
                                if(self.homewicketscount<10):
                                    self.player1=self.hteam[self.hq]
                                    self.hq=self.hq+1
                                    self.playerbatting=self.player1
                                
                            if(self.playerbatting==self.player2):
                                self.homeplayer2runs(self.player2,r,True)
                                if(self.homewicketscount<10):
                                    self.player2=self.hteam[self.hq]
                                    self.hq=self.hq+1
                                    self.playerbatting=self.player2
                            if(self.homewicketscount==10):
                                self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)###M###################MMMMMMMM
                                self.awaybowlerlist[self.overs-1]=self.awaybowlerlist[self.overs-1]+"*"
                                self.printHomeTotalScores()
                                break   
                            if(i!=self.balls_in_over):       ######++++++++++++++++++++++++++
                                if(i==5):
                                    self.isItBall5=True
                                else:
                                    self.isItBall5=False
                                i=i+1
                                
                            if(self.overs==self.no_of_overs and i==self.balls_in_over and self.isItBall5==False): #########++++++++++++
                                self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)#
                                return [self.player1,self.player2]
                            if(i!=6 or (i==6 and self.isItBall5==True)):                    ###++++++++++++++++++++++++
                                if(i==6 and self.isItBall5==True):
                                    self.isItBall5=False
                                continue
                            elif(self.overs!=self.no_of_overs and i==self.balls_in_over and self.isItBall5==False):
                                self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)#
                                self.printHomeScores()
                                return [self.player1,self.player2]
                            if(self.Homewicketscount==10):
                                self.printHomeTotalScores()
                                break
                        elif(r=='wd'):
                            r=0
                            print("Wide")
                            self.awaybowlergivenruns=self.awaybowlergivenruns+1
                            self.hometotalruns=self.hometotalruns+1
                            
                            continue
                        
                        elif(r=='nb'):
                            r=0
                            print("No Ball")
                            self.NoBallRuns=random.randint(0,6)
                            self.awaybowlergivenruns=self.awaybowlergivenruns+1+self.NoBallRuns
                            self.hometotalruns=self.hometotalruns+1+self.NoBallRuns
                            self.NoBallRuns=0
                            continue
                        else:
                            r=int(r)
                            self.awaybowlergivenruns=self.awaybowlergivenruns+r
                        self.overruns=self.overruns+r
                        self.hometotalruns=self.hometotalruns+r
                        if(self.playerbatting==self.player1):
                            self.homeplayer1runs(self.player1,r)
                        if(self.playerbatting==self.player2):
                            self.homeplayer2runs(self.player2,r)
                        if(r%2!=0):
                            if(self.playerbatting==self.player1):
                                self.playerbatting=self.player2
                            elif(self.playerbatting==self.player2):
                                self.playerbatting=self.player1
                            
                        if(i==self.balls_in_over):#
                            self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)#
                        if(i==self.balls_in_over):
                            self.printHomeScores()
                            if(self.overs==self.no_of_overs):
                                if(self.playerbatting==self.player1):
                                    self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                                elif(self.playerbatting==self.player2):
                                    self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                                    self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    
                                if(self.playerbatting==self.player1):                    ####LAST CHANGED
                                    self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                                else:
                                    self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                                    self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                            return [self.player1,self.player2]
                        if(r==0 or r==1 or r==2 or r==3 or r==4 or r==5 or r==6):
                            i=i+1
                for self.overs in range(1,self.no_of_overs+1):
                    self.balls_in_over=6
                    self.awaybowler=random.choice(self.awaybowlers)
                    if(self.overs!=1):
                        while(self.awaybowler==self.awaybowlerlist[self.overs-2]):
                            self.awaybowler=random.choice(self.awaybowlers)
                    self.awaybowlerlist.append(self.awaybowler)#
                    if(self.homewicketscount==10):
                        break
                    if(self.overs==1):
                        self.hometwobatsmenlist=[self.hteam[0],self.hteam[1]]
                        self.playerbatting=self.hteam[0]
                        players=over(self.awaybowler,self.hometwobatsmenlist,self.playerbatting)
                    elif(self.overs!=1 and self.overs!=self.no_of_overs):
                        #self.strikechange=True
                        self.strikeChange(players[0],players[1])
                        self.hometwobatsmenlist=players
                        players=over(self.awaybowler,players,self.playerbatting)
                    elif(self.overs==self.no_of_overs):
                        #self.strikechange=True
                        self.strikeChange(players[0],players[1])
                        self.hometwobatsmenlist=players
                        players=over(self.awaybowler,players,self.playerbatting)
                        if(self.homewicketscount!=10):
                                self.printHomeTotalScores()
                        
                
            
    def printAwayScores(self):
        print("OVER",self.overs,"is Completed")
        print("Total Runs scored in this over by ",self.awayteam," is :",self.overruns)
        print("Total runs given by :",self.homebowler," is:", self.homebowlergivenruns)
        
        
    def printAwayTotalScores(self):
        print("_________________SCORE CARD___________________")
        print("Total Runs scored in this match by ",self.awayteam," is :",self.awaytotalruns)
        print("BATSMEN               RUNS SCORED")
        print("-------               -----------")
        for i in range(0,len(self.awayteamWicketsSequence)):
            for j in range(0,len(self.awayteamScoresList)):
                if(i==j):
                    print(self.awayteamWicketsSequence[i],end="")
                    for space in range(0,25-len(self.awayteamWicketsSequence[i])):
                        print(" ",end="")
                    print(self.awayteamScoresList[j],"(",self.awaybatsmenTakingBallsList[i],")",sep="")
        print("OVERS     BOWLER               RUNS GIVEN")
        print("-----     ------               -----------")
        for i in range(0,len(self.hometeamBowlerScoresList)):
            for j in range(0,len(self.homebowlerlist)):
                if(i==j and (i==0 or i==1 or i==2 or i==3 or i==4 or i==5 or i==6 or i==7 or i==8)):
                    print("Over0",i+1,"    ",self.homebowlerlist[j],end="",sep="")
                    for space in range(0,25-len(self.homebowlerlist[j])):
                        print(" ",end="")
                    print(self.hometeamBowlerScoresList[i])
                elif(i==j):
                    print("Over",i+1,"    ",self.homebowlerlist[j],end="",sep="")
                    for space in range(0,25-len(self.homebowlerlist[j])):
                        print(" ",end="")
                    print(self.hometeamBowlerScoresList[i])
                    
        fileptr=open("ipl.txt","a")
        fileptr.write("\n_____________________________________________SCORE CARD_____________________________________________\n")
        fileptr.write("\nTotal Runs scored in this match by ")
        fileptr.write(self.awayteam)
        fileptr.write(" is :")
        fileptr.write(str(self.awaytotalruns))
        fileptr.write("\n")
        fileptr.write("\nBATSMEN               RUNS SCORED\n")
        fileptr.write("--------              -----------\n")
        for i in range(0,len(self.awayteamWicketsSequence)):
            for j in range(0,len(self.awayteamScoresList)):
                if(i==j):
                    fileptr.write(self.awayteamWicketsSequence[i])
                    for space in range(0,25-len(self.awayteamWicketsSequence[i])):
                        fileptr.write(" ")
                    fileptr.write(str(self.awayteamScoresList[j]))
                    fileptr.write("(")
                    fileptr.write(str(self.awaybatsmenTakingBallsList[i]))
                    fileptr.write(")")
                    fileptr.write("\n")

        fileptr.write("\nOVERS     BOWLER               RUNS GIVEN\n")
        fileptr.write("-----     ------               -----------\n")
        for i in range(0,len(self.hometeamBowlerScoresList)):
            for j in range(0,len(self.homebowlerlist)):
                if(i==j):
                    if(i==j and (i==0 or i==1 or i==2 or i==3 or i==4 or i==5 or i==6 or i==7 or i==8)):
                        fileptr.write("Over0")
                    else:
                        fileptr.write("Over")
                    fileptr.write(str(i+1))
                    fileptr.write("   ")
                    fileptr.write(self.homebowlerlist[j])
                    for space in range(0,25-len(self.homebowlerlist[j])):
                        fileptr.write(" ")
                    fileptr.write(str(self.hometeamBowlerScoresList[i]))
                    fileptr.write("\n")
        fileptr.close()
        
    def printHomeScores(self):
        print("OVER",self.overs,"is Completed")
        print("Total Runs scored in this over by ",self.hometeam," is :",self.overruns)
        print("Total runs given by :",self.awaybowler," is:", self.awaybowlergivenruns)
    def printHomeTotalScores(self):
        print("\n_________________SCORE CARD___________________\n")
        print("Total Runs scored in this match by ",self.hometeam," is :",self.hometotalruns)
        print("BATSMEN               RUNS SCORED")
        print("-------               -----------")
        for i in range(0,len(self.hometeamWicketsSequence)):
            for j in range(0,len(self.hometeamScoresList)):
                if(i==j):
                    print(self.hometeamWicketsSequence[i],end="")
                    for space in range(0,25-len(self.hometeamWicketsSequence[i])):
                        print(" ",end="")
                    print(self.hometeamScoresList[j],"(",self.homebatsmenTakingBallsList[i],")",sep="")
        print("OVERS     BOWLER               RUNS GIVEN")
        print("-----     ------               -----------")
        for i in range(0,len(self.awayteamBowlerScoresList)):
            for j in range(0,len(self.awaybowlerlist)):
                if(i==j and (i==0 or i==1 or i==2 or i==3 or i==4 or i==5 or i==6 or i==7 or i==8)):
                    print("Over0",i+1,"   ",self.awaybowlerlist[j],end="",sep="")
                    for space in range(0,25-len(self.awaybowlerlist[j])):
                        print(" ",end="")
                    print(self.awayteamBowlerScoresList[i])
                elif(i==j):
                    print("Over",i+1,"   ",self.awaybowlerlist[j],end="",sep="")
                    for space in range(0,25-len(self.awaybowlerlist[j])):
                        print(" ",end="")
                    print(self.awayteamBowlerScoresList[i])
        fileptr=open("ipl.txt","a")
        fileptr.write("\n_____________________________________________SCORE CARD_____________________________________________\n")
        fileptr.write("\nTotal Runs scored in this match by ")
        fileptr.write(self.hometeam)
        fileptr.write(" is :")
        fileptr.write(str(self.hometotalruns))
        fileptr.write("\n")
        fileptr.write("\nBATSMEN               RUNS SCORED\n")
        fileptr.write("-------               -----------\n")
        for i in range(0,len(self.hometeamWicketsSequence)):
            for j in range(0,len(self.hometeamScoresList)):
                if(i==j):
                    fileptr.write(self.hometeamWicketsSequence[i])
                    for space in range(0,25-len(self.hometeamWicketsSequence[i])):
                        fileptr.write(" ")
                    fileptr.write(str(self.hometeamScoresList[j]))
                    fileptr.write("(")
                    fileptr.write(str(self.homebatsmenTakingBallsList[i]))
                    fileptr.write(")")
                    fileptr.write("\n")
        fileptr.write("\nOVERS     BOWLER               RUNS GIVEN\n")
        fileptr.write("-----     ------               -----------\n")
        for i in range(0,len(self.awayteamBowlerScoresList)):
            for j in range(0,len(self.awaybowlerlist)):
                if(i==j):
                    if(i==j and (i==0 or i==1 or i==2 or i==3 or i==4 or i==5 or i==6 or i==7 or i==8)):
                        fileptr.write("Over0")
                    else:
                        fileptr.write("Over")
                    fileptr.write(str(i+1))
                    fileptr.write("   ")
                    fileptr.write(self.awaybowlerlist[j])
                    for space in range(0,25-len(self.awaybowlerlist[j])):
                        fileptr.write(" ")
                    fileptr.write(str(self.awayteamBowlerScoresList[i]))
                    fileptr.write("\n")
        fileptr.close()        
    def homebatsmenScore(self,batsmen,runs):
        self.batsmen=batsmen
        self.runs=runs
        self.hometeamScoresList.append(self.runs)
        self.hometeamWicketsSequence.append(self.batsmen)
        print(self.batsmen,":OUT for",self.runs," runs")
    def homebatsmenNotOutScore(self,batsmen,runs):
        self.batsmen=batsmen
        self.runs=runs
        self.hometeamScoresList.append(self.runs)
        self.hometeamWicketsSequence.append(self.batsmen)
    def homeplayer1runs(self,batsmen1,r1,P1WICKET=False):
        self.r1=r1
        self.batsmen1=batsmen1
        self.p1runs=self.p1runs+self.r1
        print(self.batsmen1,":",self.p1runs," runs\n\n")
        if(P1WICKET):
            self.homebatsmenScore(self.batsmen1,self.p1runs)
            self.p1runs=0  
    def homeplayer2runs(self,batsmen2,r2,P2WICKET=False):
        self.r2=r2
        self.batsmen2=batsmen2
        self.p2runs=self.p2runs+self.r2
        print(self.batsmen2,":",self.p2runs," runs\n\n")
        if(P2WICKET):
            self.homebatsmenScore(self.batsmen2,self.p2runs)
            self.p2runs=0
        
    def hometeamperform(self,choice):
        if(self.choice=="bat"):
            if(self.secondInningsTime):
                ####print("Openers buttler and sanju came into the crease")
                if(self.secondInningsScore<=self.firstInningsScore):      #$$############$$$$$$$$$$$$$$$$$$$$#########
                    print("NOT PRINTED CORRECTLY")
                    def over(awaybowler,twoplayers,playerbatting):
                        self.overruns=0
                        self.awaybowlergivenruns=0
                        if(self.player1notout and self.player2notout):  
                            self.player1=twoplayers[0]
                            self.player2=twoplayers[1]
                        elif(self.player1notout and self.player3notout):
                            self.player1=twoplayers[0]
                            self.player3=twoplayers[1]
                        self.playerbatting=playerbatting############
                        i=1                                   ##########++++++++++++++++++++++++++++++++++++
                        while(i<=self.balls_in_over):
                            if(self.playerbatting==self.player1):
                                self.batsmen1TakenBalls=self.batsmen1TakenBalls+1
                            else:
                                self.batsmen2TakenBalls=self.batsmen2TakenBalls+1
                            if(self.secondInningsScore>self.firstInningsScore):
                                break
                            print("\n")
                            print(awaybowler,"to",self.playerbatting)
                            print("Enter no. of runs scored for ball",i,":")
                            r=random.choice(self.possiblerunslist)#input()
                            print(r)
                            if(r=='w'):
                                self.homewicketscount=self.homewicketscount+1
                                print("WICKET")
                                r=0
                                if(self.playerbatting==self.player1 and self.homewicketscount!=10):
                                    self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    
                                    
                                elif(self.playerbatting==self.player2 and self.homewicketscount!=10):
                                    self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                                    
                                if(self.playerbatting==self.player1 and self.homewicketscount==10):
                                    self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    self.batsmen2TakenBalls=0
                                elif(self.playerbatting==self.player2 and self.homewicketscount==10):
                                    self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    self.batsmen2TakenBalls=0
                                if(self.overs==self.no_of_overs and i==self.balls_in_over):     ###############EXTRA PART
                                    if(self.playerbatting==self.player1):
                                        self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                        self.batsmen1TakenBalls=0
                                    elif(self.playerbatting==self.player2):
                                        self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                        self.batsmen2TakenBalls=0
                                if((self.overs==self.no_of_overs and i==self.balls_in_over) or self.homewicketscount==10):
                                    if(self.playerbatting==self.player1):
                                        self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                                    elif(self.playerbatting==self.player2):
                                        self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    self.printHomeScores()

                                
                                if(self.playerbatting==self.player1):
                                    self.homeplayer1runs(self.player1,r,True)
                                    if(self.homewicketscount<10):
                                        self.player1=self.hteam[self.hq]
                                        self.hq=self.hq+1
                                        self.playerbatting=self.player1
                                    
                                if(self.playerbatting==self.player2):
                                    self.homeplayer2runs(self.player2,r,True)
                                    if(self.homewicketscount<10):
                                        self.player2=self.hteam[self.hq]
                                        self.hq=self.hq+1
                                        self.playerbatting=self.player2
                                
                                if(self.homewicketscount==10):
                                    self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)###M###################MMMMMMMM
                                    self.awaybowlerlist[self.overs-1]=self.awaybowlerlist[self.overs-1]+"*"
                                    self.printHomeTotalScores()
                                    break

                                    
                                if(i!=self.balls_in_over):       ######++++++++++++++++++++++++++
                                    if(i==5):
                                        self.isItBall5=True
                                    else:
                                        self.isItBall5=False
                                    i=i+1
                                
                                if(self.overs==self.no_of_overs and i==self.balls_in_over and self.isItBall5==False): #########++++++++++++
                                    self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)#
                                    return [self.player1,self.player2]
                                if(i!=6 or (i==6 and self.isItBall5==True)):                    ###++++++++++++++++++++++++
                                    if(i==6 and self.isItBall5==True):
                                        self.isItBall5=False
                                    continue
                                elif(self.overs!=self.no_of_overs and i==self.balls_in_over and self.isItBall5==False):
                                    self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)#
                                    self.printHomeScores()
                                    return [self.player1,self.player2]
                                
                            elif(r=='wd'):
                                r=0
                                print("Wide")
                                self.awaybowlergivenruns=self.awaybowlergivenruns+1
                                self.hometotalruns=self.hometotalruns+1
                                self.secondInningsScore=self.secondInningsScore+1
                                
                                continue
                            elif(r=='nb'):
                                r=0
                                self.NoBallRuns=random.randint(0,6)
                                print("No Ball")
                                self.awaybowlergivenruns=self.awaybowlergivenruns+1+self.NoBallRuns
                                self.hometotalruns=self.hometotalruns+1+self.NoBallRuns
                                self.secondInningsScore=self.secondInningsScore+1+self.NoBallRuns
                                self.NoBallRuns=0
                                
                                continue
                            else:
                                r=int(r)
                                self.secondInningsScore=self.secondInningsScore+r
                            self.awaybowlergivenruns=self.awaybowlergivenruns+r
                            self.overruns=self.overruns+r
                            self.hometotalruns=self.hometotalruns+r
                            if(self.playerbatting==self.player1):
                                self.homeplayer1runs(self.player1,r)
                            if(self.playerbatting==self.player2):
                                self.homeplayer2runs(self.player2,r)
                            if(r%2!=0):
                                if(self.playerbatting==self.player1):
                                    self.playerbatting=self.player2
                                elif(self.playerbatting==self.player2):
                                    self.playerbatting=self.player1

                            #######COPYING
                            if(i==self.balls_in_over):#
                                self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)#
                            if(i==self.balls_in_over):
                                self.printHomeScores() 
                                if(self.overs==self.no_of_overs):
                                    if(self.playerbatting==self.player1):
                                        self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)
                                        self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                                        
                                    elif(self.playerbatting==self.player2):
                                        self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                                        self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    
                                    if(self.playerbatting==self.player1):                    ####LAST CHANGED
                                        self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                        self.batsmen1TakenBalls=0
                                        self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                        self.batsmen2TakenBalls=0
                                    else:
                                        self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                        self.batsmen2TakenBalls=0
                                        self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                        self.batsmen1TakenBalls=0
                                    #self.HomeTotalScores()
                                return [self.player1,self.player2]
                    
                            if(self.secondInningsScore>self.firstInningsScore):
                                return [self.player1,self.player2]
                            if(r==0 or r==1 or r==2 or r==3 or r==4 or r==5 or r==6):
                                i=i+1
                                
                    for self.overs in range(1,self.no_of_overs+1):
                        self.balls_in_over=6
                        self.awaybowler=random.choice(self.awaybowlers)
                        if(self.overs!=1):
                            while(self.awaybowler==self.awaybowlerlist[self.overs-2]):
                                self.awaybowler=random.choice(self.awaybowlers)
                        self.awaybowlerlist.append(self.awaybowler)#
                        if(self.homewicketscount==10):
                            break
                        if(self.secondInningsScore>self.firstInningsScore):
                            self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)      #$$$$$$$$$$$$$$$$$$$$$$$$$#
                            self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                            
                            self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                            self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                            self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)
                            self.printHomeTotalScores()
                            break
                        if(self.overs==1):
                            self.hometwobatsmenlist=[self.hteam[0],self.hteam[1]]
                            self.playerbatting=self.hteam[0]
                            players=over(self.awaybowler,self.hometwobatsmenlist,self.playerbatting)
                        elif(self.overs!=1 and self.overs!=self.no_of_overs):
                            #self.strikechange=True
                            self.strikeChange(players[0],players[1])
                            self.hometwobatsmenlist=players
                            players=over(self.awaybowler,players,self.playerbatting)
                        elif(self.overs==self.no_of_overs):
                            #self.strikechange=True
                            self.strikeChange(players[0],players[1])
                            self.hometwobatsmenlist=players
                            players=over(self.awaybowler,players,self.playerbatting)
                            if(self.homewicketscount!=10 and self.secondInningsScore<=self.firstInningsScore):
                                self.printHomeTotalScores()
                
            else:
                def over(awaybowler,twoplayers,playerbatting):
                    self.overruns=0
                    self.awaybowlergivenruns=0
                    if(self.player1notout and self.player2notout):
                        self.player1=twoplayers[0]
                        self.player2=twoplayers[1]
                    elif(self.player1notout and self.player3notout):
                        self.player1=twoplayers[0]
                        self.player3=twoplayers[1]
                    self.playerbatting=playerbatting############
                    i=1                                   ##########++++++++++++++++++++++++++++++++++++
                    while(i<=self.balls_in_over):
                        if(self.playerbatting==self.player1):
                            self.batsmen1TakenBalls=self.batsmen1TakenBalls+1
                        else:
                            self.batsmen2TakenBalls=self.batsmen2TakenBalls+1
                        print("\n")
                        print(awaybowler,"to",self.playerbatting)
                        print("Enter no. of runs scored for ball",i,":")
                        r=random.choice(self.possiblerunslist)#input()
                        print(r)
                        if(r=='w'):
                            self.homewicketscount=self.homewicketscount+1
                            print("WICKET")
                            r=0
                            if(self.playerbatting==self.player1 and self.homewicketscount!=10):
                                self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                self.batsmen1TakenBalls=0
                            elif(self.playerbatting==self.player2 and self.homewicketscount!=10):
                                self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                self.batsmen2TakenBalls=0
                            if(self.playerbatting==self.player1 and self.homewicketscount==10):
                                self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                self.batsmen1TakenBalls=0
                                self.batsmen2TakenBalls=0
                            elif(self.playerbatting==self.player2 and self.homewicketscount==10):
                                self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                self.batsmen2TakenBalls=0
                                self.batsmen1TakenBalls=0
                            if(self.overs==self.no_of_overs and i==self.balls_in_over):     ###############EXTRA PART
                                if(self.playerbatting==self.player1):
                                    self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                elif(self.playerbatting==self.player2):
                                    self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                            if((self.overs==self.no_of_overs and i==self.balls_in_over) or self.homewicketscount==10):
                                if(self.playerbatting==self.player1):
                                    self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                                elif(self.playerbatting==self.player2):
                                    self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)
                                self.printHomeScores()
                            
                                
                            if(self.playerbatting==self.player1):
                                self.homeplayer1runs(self.player1,r,True)
                                if(self.homewicketscount<10):
                                    self.player1=self.hteam[self.hq]
                                    self.hq=self.hq+1
                                    self.playerbatting=self.player1
                                
                            if(self.playerbatting==self.player2):
                                self.homeplayer2runs(self.player2,r,True)
                                if(self.homewicketscount<10):
                                    self.player2=self.hteam[self.hq]
                                    self.hq=self.hq+1
                                    self.playerbatting=self.player2
                            if(self.homewicketscount==10):
                                self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)###M###################MMMMMMMM
                                self.awaybowlerlist[self.overs-1]=self.awaybowlerlist[self.overs-1]+"*"
                                self.printHomeTotalScores()
                                break
                            
                            if(i!=self.balls_in_over):       ######++++++++++++++++++++++++++
                                if(i==5):
                                    self.isItBall5=True
                                else:
                                    self.isItBall5=False
                                i=i+1
                                
                            if(self.overs==self.no_of_overs and i==self.balls_in_over and self.isItBall5==False): #########++++++++++++
                                self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)#
                                return [self.player1,self.player2]
                            if(i!=6 or (i==6 and self.isItBall5==True)):                    ###++++++++++++++++++++++++
                                if(i==6 and self.isItBall5==True):
                                    self.isItBall5=False
                                continue
                            elif(self.overs!=self.no_of_overs and i==self.balls_in_over and self.isItBall5==False):
                                self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)#
                                self.printHomeScores()
                                return [self.player1,self.player2]
                            if(self.Homewicketscount==10):
                                self.printHomeTotalScores()
                                break
                        elif(r=='wd'):
                            r=0
                            print("Wide")
                            self.awaybowlergivenruns=self.awaybowlergivenruns+1
                            self.hometotalruns=self.hometotalruns+1
                            
                            continue
                    
                        elif(r=='nb'):
                            r=0
                            print("No Ball")
                            self.NoBallRuns=random.randint(0,6)
                            self.awaybowlergivenruns=self.awaybowlergivenruns+1+self.NoBallRuns
                            self.hometotalruns=self.hometotalruns+1+self.NoBallRuns
                            self.NoBallRuns=0
                            continue
                        else:
                            r=int(r)
                            self.awaybowlergivenruns=self.awaybowlergivenruns+r
                        self.overruns=self.overruns+r
                        self.hometotalruns=self.hometotalruns+r
                        if(self.playerbatting==self.player1):
                            self.homeplayer1runs(self.player1,r)
                        if(self.playerbatting==self.player2):
                            self.homeplayer2runs(self.player2,r)
                        if(r%2!=0):
                            if(self.playerbatting==self.player1):
                                self.playerbatting=self.player2
                            elif(self.playerbatting==self.player2):
                                self.playerbatting=self.player1
                            
                        if(i==self.balls_in_over):#
                            self.awayteamBowlerScoresList.append(self.awaybowlergivenruns)#
                        if(i==self.balls_in_over):
                            self.printHomeScores() 
                            if(self.overs==self.no_of_overs):
                                if(self.playerbatting==self.player1):
                                    self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                                        
                                elif(self.playerbatting==self.player2):
                                    self.homebatsmenNotOutScore(self.player2+"*",self.p2runs)
                                    self.homebatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    
                                if(self.playerbatting==self.player1):                    ####LAST CHANGED
                                    self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                                else:
                                    self.homeplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                                    self.homeplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0  
                            return [self.player1,self.player2]
                        if(r==0 or r==1 or r==2 or r==3 or r==4 or r==5 or r==6):
                            i=i+1
                        
                for self.overs in range(1,self.no_of_overs+1):
                    self.balls_in_over=6
                    self.awaybowler=random.choice(self.awaybowlers)
                    if(self.overs!=1):
                        while(self.awaybowler==self.awaybowlerlist[self.overs-2]):
                            self.awaybowler=random.choice(self.awaybowlers)
                    self.awaybowlerlist.append(self.awaybowler)#
                    if(self.homewicketscount==10):
                        break
                    
                    if(self.overs==1):
                        self.hometwobatsmenlist=[self.hteam[0],self.hteam[1]]
                        self.playerbatting=self.hteam[0]
                        players=over(self.awaybowler,self.hometwobatsmenlist,self.playerbatting)
                    elif(self.overs!=1 and self.overs!=self.no_of_overs):
                        #self.strikechange=True
                        self.strikeChange(players[0],players[1])
                        self.hometwobatsmenlist=players
                        players=over(self.awaybowler,players,self.playerbatting)
                    elif(self.overs==self.no_of_overs):
                        #self.strikechange=True
                        self.strikeChange(players[0],players[1])
                        self.hometwobatsmenlist=players
                        players=over(self.awaybowler,players,self.playerbatting)
                        if(self.homewicketscount!=10):
                                self.printHomeTotalScores()
                        
                                
        else:
            if(self.secondInningsTime):
                if(self.secondInningsScore<=self.firstInningsScore):      #$$############$$$$$$$$$$$$$$$$$$$$#########
                    #print("Openers dhawan and prithvi came into the crease")
                    print("ERRRR BLOCK")
                    def over(homebowler,twoplayers,playerbatting):
                        self.overruns=0
                        self.homebowlergivenruns=0
                        if(self.player1notout and self.player2notout):
                            self.player1=twoplayers[0]
                            self.player2=twoplayers[1]
                        elif(self.player1notout and self.player3notout):
                            self.player1=twoplayers[0]
                            self.player3=twoplayers[1]
                        self.playerbatting=playerbatting############
                        i=1                                   ##########++++++++++++++++++++++++++++++++++++
                        while(i<=self.balls_in_over):                                   #S#######SSSSSSSSSSS
                            if(self.playerbatting==self.player1):
                                self.batsmen1TakenBalls=self.batsmen1TakenBalls+1
                            else:
                                self.batsmen2TakenBalls=self.batsmen2TakenBalls+1
                            if(self.secondInningsScore>self.firstInningsScore):
                                break
                            
                            print("\n")
                            print(homebowler,"to",self.playerbatting)
                            print("Enter no. of runs scored for ball",i,":")
                            r=random.choice(self.possiblerunslist)#input()
                            print(r)
                            if(r=='w'):
                                self.awaywicketscount=self.awaywicketscount+1
                                print("WICKET")
                                r=0
                                if(self.playerbatting==self.player1 and self.awaywicketscount!=10):
                                    self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    
                                    
                                elif(self.playerbatting==self.player2 and self.awaywicketscount!=10):
                                    self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                                    
                                if(self.playerbatting==self.player1 and self.awaywicketscount==10):
                                    self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    self.batsmen2TakenBalls=0
                                elif(self.playerbatting==self.player2 and self.awaywicketscount==10):
                                    self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    self.batsmen2TakenBalls=0
                                if(self.overs==self.no_of_overs and i==self.balls_in_over):     ###############EXTRA PART
                                    if(self.playerbatting==self.player1):
                                        self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                        self.batsmen1TakenBalls=0
                                    elif(self.playerbatting==self.player2):
                                        self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                        self.batsmen2TakenBalls=0
                                if((self.overs==self.no_of_overs and i==self.balls_in_over) or self.awaywicketscount==10):###
                                    if(self.playerbatting==self.player1):
                                        self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                                    elif(self.playerbatting==self.player2):
                                        self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    self.printAwayScores()
                                
            
                                if(self.playerbatting==self.player1):
                                    self.awayplayer1runs(self.player1,r,True)
                                    if(self.awaywicketscount<10):
                                        self.player1=self.ateam[self.aq]
                                        self.aq=self.aq+1
                                        self.playerbatting=self.player1
                                    
                                if(self.playerbatting==self.player2):
                                    self.awayplayer2runs(self.player2,r,True)
                                    if(self.awaywicketscount<10):
                                        self.player2=self.ateam[self.aq]
                                        self.aq=self.aq+1
                                        self.playerbatting=self.player2
                                        
                                if(self.awaywicketscount==10):
                                    self.hometeamBowlerScoresList.append(self.homebowlergivenruns)###M###################MMMMMMMM
                                    self.homebowlerlist[self.overs-1]=self.homebowlerlist[self.overs-1]+"*"
                                    self.printAwayTotalScores()
                                    break
                                
                                if(i!=self.balls_in_over):       ######++++++++++++++++++++++++++
                                    if(i==5):
                                        self.isItBall5=True
                                    else:
                                        self.isItBall5=False
                                    i=i+1
                                
                                if(self.overs==self.no_of_overs and i==self.balls_in_over and self.isItBall5==False): #########++++++++++++
                                    self.hometeamBowlerScoresList.append(self.homebowlergivenruns)#
                                    return [self.player1,self.player2]
                                if(i!=6 or (i==6 and self.isItBall5==True)):                    ###++++++++++++++++++++++++
                                    if(i==6 and self.isItBall5==True):
                                        self.isItBall5=False
                                    continue
                                elif(self.overs!=self.no_of_overs and i==self.balls_in_over and self.isItBall5==False):
                                    self.hometeamBowlerScoresList.append(self.homebowlergivenruns)#
                                    self.printAwayScores()
                                    return [self.player1,self.player2]
                                
                            elif(r=='wd'):                                       
                                r=0
                                print("Wide")
                                self.homebowlergivenruns=self.homebowlergivenruns+1
                                self.awaytotalruns=self.awaytotalruns+1
                                self.secondInningsScore=self.secondInningsScore+1         #$$SSSSSSSSSSSSS
                                continue
                            elif(r=='nb'):
                                r=0
                                print("No Ball")
                                self.NoBallRuns=random.randint(0,6)
                                self.homebowlergivenruns=self.homebowlergivenruns+1+self.NoBallRuns
                                self.awaytotalruns=self.awaytotalruns+1+self.NoBallRuns
                                self.secondInningsScore=self.secondInningsScore+1+self.NoBallRuns     #SSSSSSSSSSSSSS
                                self.NoBallRuns=0
                                #continue
                          
                            else:
                                r=int(r)
                                self.secondInningsScore=self.secondInningsScore+r  #$$$$$$$$$$$$$$$$$$#
                                
                                
                            self.homebowlergivenruns=self.homebowlergivenruns+r
                            self.overruns=self.overruns+r
                            self.awaytotalruns=self.awaytotalruns+r
                            if(self.secondInningsScore>self.firstInningsScore):
                                return [self.player1,self.player2]
                            
                            if(self.playerbatting==self.player1):
                                self.awayplayer1runs(self.player1,r)
                            if(self.playerbatting==self.player2):
                                self.awayplayer2runs(self.player2,r)
                            if(r%2!=0):
                                if(self.playerbatting==self.player1):
                                    self.playerbatting=self.player2
                                elif(self.playerbatting==self.player2):
                                    self.playerbatting=self.player1
                                
                            if(i==self.balls_in_over):#
                                self.hometeamBowlerScoresList.append(self.homebowlergivenruns)#
                            if(i==self.balls_in_over):
                                self.printAwayScores() 
                                if(self.overs==self.no_of_overs):
                                    if(self.playerbatting==self.player1):
                                        self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)
                                        self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                                        
                                    elif(self.playerbatting==self.player2):
                                        self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                                        self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    
                                    if(self.playerbatting==self.player1):                    ####LAST CHANGED
                                        self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                        self.batsmen1TakenBalls=0
                                        self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                        self.batsmen2TakenBalls=0
                                    else:
                                        self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                        self.batsmen2TakenBalls=0
                                        self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                        self.batsmen1TakenBalls=0
                                    
                                return [self.player1,self.player2]
                            if(self.secondInningsScore>self.firstInningsScore):
                                return [self.player1,self.player2]
                            if(r==0 or r==1 or r==2 or r==3 or r==4 or r==5 or r==6):
                                i=i+1
                                
                    for self.overs in range(1,self.no_of_overs+1):
                        self.balls_in_over=6
                        self.homebowler=random.choice(self.homebowlers)
                        if(self.overs!=1):
                            while(self.homebowler==self.homebowlerlist[self.overs-2]):
                                self.homebowler=random.choice(self.homebowlers)
                        self.homebowlerlist.append(self.homebowler)#
                        if(self.awaywicketscount==10):####
                            break
                        if(self.secondInningsScore>self.firstInningsScore):
                            self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)      #$$$$$$$$$$$$$$$$$$$$$$$$$#
                            self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                            
                            self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                            self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                            self.hometeamBowlerScoresList.append(self.homebowlergivenruns)
                            self.printAwayTotalScores()
                            break
                        if(self.overs==1):
                            self.awaytwobatsmenlist=[self.ateam[0],self.ateam[1]]
                            self.playerbatting=self.ateam[0]
                            players=over(self.homebowler,self.awaytwobatsmenlist,self.playerbatting)
                        elif(self.overs!=1 and self.overs!=self.no_of_overs):
                            #self.strikechange=True
                            self.strikeChange(players[0],players[1])
                            self.awaytwobatsmenlist=players
                            players=over(self.homebowler,players,self.playerbatting)
                        elif(self.overs==self.no_of_overs):
                            #self.strikechange=True
                            self.strikeChange(players[0],players[1])
                            self.awaytwobatsmenlist=players
                            players=over(self.homebowler,players,self.playerbatting)
                            if(self.awaywicketscount!=10 and self.secondInningsScore<=self.firstInningsScore):
                                self.printAwayTotalScores()
            else:
                ####print("Openers dhawan and prithvi came into the crease")
                def over(homebowler,twoplayers,playerbatting):
                    self.overruns=0
                    self.homebowlergivenruns=0
                    if(self.player1notout and self.player2notout):
                        self.player1=twoplayers[0]
                        self.player2=twoplayers[1]
                    elif(self.player1notout and self.player3notout):
                        self.player1=twoplayers[0]
                        self.player3=twoplayers[1]
                    self.playerbatting=playerbatting############
                    i=1                                   ##########++++++++++++++++++++++++++++++++++++
                    while(i<=self.balls_in_over):
                        if(self.playerbatting==self.player1):
                            self.batsmen1TakenBalls=self.batsmen1TakenBalls+1
                        else:
                            self.batsmen2TakenBalls=self.batsmen2TakenBalls+1
                        print("\n")
                        print(homebowler,"to",self.playerbatting)
                        print("Enter no. of runs scored for ball",i,":")
                        r=random.choice(self.possiblerunslist)#input()
                        print(r)
                        if(r=='w'):
                            self.awaywicketscount=self.awaywicketscount+1
                            print("WICKET")
                            r=0
                            if(self.playerbatting==self.player1 and self.awaywicketscount!=10):
                                self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                self.batsmen1TakenBalls=0
                            elif(self.playerbatting==self.player2 and self.awaywicketscount!=10):
                                self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                self.batsmen2TakenBalls=0
                                    
                            if(self.playerbatting==self.player1 and self.awaywicketscount==10):
                                self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                self.batsmen1TakenBalls=0
                                self.batsmen2TakenBalls=0
                            elif(self.playerbatting==self.player2 and self.awaywicketscount==10):
                                self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                self.batsmen1TakenBalls=0
                                self.batsmen2TakenBalls=0
                            if(self.overs==self.no_of_overs and i==self.balls_in_over):     ###############EXTRA PART
                                if(self.playerbatting==self.player1):
                                    self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                elif(self.playerbatting==self.player2):
                                    self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                            if((self.overs==self.no_of_overs and i==self.balls_in_over) or self.awaywicketscount==10):
                                if(self.playerbatting==self.player1):
                                    self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                                elif(self.playerbatting==self.player2):
                                    self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)
                                self.printAwayScores()
                                
                            if(self.playerbatting==self.player1):
                                self.awayplayer1runs(self.player1,r,True)
                                if(self.awaywicketscount<10):
                                    self.player1=self.ateam[self.aq]
                                    self.aq=self.aq+1
                                    self.playerbatting=self.player1
                                
                            if(self.playerbatting==self.player2):
                                self.awayplayer2runs(self.player2,r,True)
                                if(self.awaywicketscount<10):
                                    self.player2=self.ateam[self.aq]
                                    self.aq=self.aq+1
                                    self.playerbatting=self.player2
                                
                            if(self.awaywicketscount==10):
                                self.hometeamBowlerScoresList.append(self.homebowlergivenruns)###M###################MMMMMMMM
                                self.homebowlerlist[self.overs-1]=self.homebowlerlist[self.overs-1]+"*"
                                self.printAwayTotalScores()
                                break
                            
                            if(i!=self.balls_in_over):       ######++++++++++++++++++++++++++
                                if(i==5):
                                    self.isItBall5=True
                                else:
                                    self.isItBall5=False
                                i=i+1
                                
                            if(self.overs==self.no_of_overs and i==self.balls_in_over and self.isItBall5==False): #########++++++++++++
                                self.hometeamBowlerScoresList.append(self.homebowlergivenruns)#
                                return [self.player1,self.player2]
                            if(i!=6 or (i==6 and self.isItBall5==True)):                    ###++++++++++++++++++++++++
                                if(i==6 and self.isItBall5==True):
                                    self.isItBall5=False
                                continue
                            elif(self.overs!=self.no_of_overs and i==self.balls_in_over and self.isItBall5==False):
                                self.hometeamBowlerScoresList.append(self.homebowlergivenruns)#
                                self.printAwayScores()
                                return [self.player1,self.player2]
                            
                        elif(r=='wd'):
                            r=0
                            print("Wide")
                            self.homebowlergivenruns=self.homebowlergivenruns+1
                            self.awaytotalruns=self.awaytotalruns+1
                            
                            continue
                        
                        elif(r=='nb'):
                            r=0
                            print("No Ball")
                            self.NoBallRuns=random.randint(0,6)
                            self.homebowlergivenruns=self.homebowlergivenruns+1+self.NoBallRuns
                            self.awaytotalruns=self.awaytotalruns+1+self.NoBallRuns
                            self.NoBallRuns=0
                            continue
                        else:
                            r=int(r)
                        self.homebowlergivenruns=self.homebowlergivenruns+r
                        self.overruns=self.overruns+r
                        self.awaytotalruns=self.awaytotalruns+r
                        if(self.playerbatting==self.player1):
                            self.awayplayer1runs(self.player1,r)
                        if(self.playerbatting==self.player2):
                            self.awayplayer2runs(self.player2,r)
                        if(r%2!=0):
                            if(self.playerbatting==self.player1):
                                self.playerbatting=self.player2
                            elif(self.playerbatting==self.player2):
                                self.playerbatting=self.player1
                            
                        if(i==self.balls_in_over):#
                            self.hometeamBowlerScoresList.append(self.homebowlergivenruns)#
                        if(i==self.balls_in_over):
                            self.printAwayScores() 
                            if(self.overs==self.no_of_overs):
                                if(self.playerbatting==self.player1):
                                    self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                                        
                                elif(self.playerbatting==self.player2):
                                    self.awaybatsmenNotOutScore(self.player2+"*",self.p2runs)
                                    self.awaybatsmenNotOutScore(self.player1+"*",self.p1runs)
                                    
                                if(self.playerbatting==self.player1):                    ####LAST CHANGED
                                    self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                                    self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                                else:
                                    self.awayplayerTakingBalls(self.batsmen2TakenBalls)
                                    self.batsmen2TakenBalls=0
                                    self.awayplayerTakingBalls(self.batsmen1TakenBalls)
                                    self.batsmen1TakenBalls=0
                            return [self.player1,self.player2]
                        if(r==0 or r==1 or r==2 or r==3 or r==4 or r==5 or r==6):
                            i=i+1
                for self.overs in range(1,self.no_of_overs+1):
                    self.balls_in_over=6
                    self.homebowler=random.choice(self.homebowlers)
                    if(self.overs!=1):
                        while(self.homebowler==self.homebowlerlist[self.overs-2]):
                            self.homebowler=random.choice(self.homebowlers)
                    self.homebowlerlist.append(self.homebowler)#
                    if(self.awaywicketscount==10):
                        break
                    if(self.overs==1):
                        self.awaytwobatsmenlist=[self.ateam[0],self.ateam[1]]
                        self.playerbatting=self.ateam[0]
                        players=over(self.homebowler,self.awaytwobatsmenlist,self.playerbatting)
                    elif(self.overs!=1 and self.overs!=self.no_of_overs):
                        #self.strikechange=True
                        self.strikeChange(players[0],players[1])
                        self.awaytwobatsmenlist=players
                        players=over(self.homebowler,players,self.playerbatting)
                    elif(self.overs==self.no_of_overs):
                        #self.strikechange=True
                        self.strikeChange(players[0],players[1])
                        self.awaytwobatsmenlist=players
                        players=over(self.homebowler,players,self.playerbatting)
                        if(self.awaywicketscount!=10):
                            self.printAwayTotalScores()
                        
    def Result(self):
        print("First Innings Score is:",self.firstInningsScore)
        print("Second Innings Score is:",self.secondInningsScore)
        fileptr=open("ipl.txt","a")
        fileptr.write("-----------------------------------------MATCH RESULT------------------------------------------\n")
        print("-----------------------------------------MATCH RESULT------------------------------------------")
        if(self.hometoss and self.choice=="bat"):
            if(self.hometotalruns>self.awaytotalruns):
                print(self.hometeam," won by ",(self.hometotalruns-self.awaytotalruns)," runs")
                fileptr.write(self.hometeam)
                fileptr.write(" won by ")
                fileptr.write(str(self.hometotalruns-self.awaytotalruns))
                fileptr.write(" runs")
            else:
                print(self.awayteam,"won by",10-self.awaywicketscount,"wickets")
                fileptr.write(self.awayteam)
                fileptr.write(" won by ")
                fileptr.write(str(10-self.awaywicketscount))
                fileptr.write(" wickets")
        elif(self.awaytoss and self.choice=="bat"):
            if(self.awaytotalruns>self.hometotalruns):
                print(self.awayteam," won by ",(self.awaytotalruns-self.hometotalruns)," runs")
                fileptr.write(self.awayteam)
                fileptr.write(" won by ")
                fileptr.write(str(self.awaytotalruns-self.hometotalruns))
                fileptr.write(" runs")
            else:
                print(self.hometeam,"won by",10-self.homewicketscount,"wickets")
                fileptr.write(self.hometeam)
                fileptr.write(" won by ")
                fileptr.write(str(10-self.homewicketscount))
                fileptr.write(" wickets")
        elif(self.hometoss and self.choice=="bowl"):
            if(self.hometotalruns>self.awaytotalruns):
                print(self.hometeam,"won by",10-self.homewicketscount,"wickets")
                fileptr.write(self.hometeam)
                fileptr.write(" won by ")
                fileptr.write(str(10-self.homewicketscount))
                fileptr.write(" wickets")
            else:
                print(self.awayteam," won by ",(self.awaytotalruns-self.hometotalruns)," runs")
                fileptr.write(self.awayteam)
                fileptr.write(" won by ")
                fileptr.write(str(self.awaytotalruns-self.hometotalruns))
                fileptr.write(" runs")
        elif(self.awaytoss and self.choice=="bowl"):
            if(self.awaytotalruns>self.hometotalruns):
                print(self.awayteam,"won by",10-self.awaywicketscount,"wickets")
                fileptr.write(self.awayteam)
                fileptr.write(" won by ")
                fileptr.write(str(10-self.awaywicketscount))
                fileptr.write(" wickets")
            else:
                print(self.hometeam," won by ",(self.hometotalruns-self.awaytotalruns)," runs")
                fileptr.write(self.hometeam)
                fileptr.write(" won by ")
                fileptr.write(str(self.hometotalruns-self.awaytotalruns))
                fileptr.write(" runs")
        fileptr.close()

def selectHomeTeam(hometeam):
    if(hometeam=="RR"):
        hteamlist=RR
        hcaptain="Sanju Samson"
    elif(hometeam=="DC"):
        hteamlist=DC
        hcaptain="Rishabh Pant"
    elif(hometeam=="CSK"):
        hteamlist=CSK
        hcaptain="MS Dhoni"
    elif(hometeam=="MI"):
        hteamlist=MI
        hcaptain="Rohit Sharma"
    elif(hometeam=="RCB"):
        hteamlist=RCB
        hcaptain="Virat Kohli"
    elif(hometeam=="KKR"):
        hteamlist=KKR
        hcaptain="Eion Morgan"
    elif(hometeam=="PBKS"):
        hteamlist=PBKS
        hcaptain="KL Rahul"
    else:
        hteamlist=SRH
        hcaptain="David Warner"
def selectAwayTeam(awayteam):
    if(awayteam=="RR"):
        ateamlist=RR
        acaptain="Sanju Samson"
    elif(awayteam=="DC"):
        ateamlist=DC
        acaptain="Rishabh Pant"
    elif(awayteam=="CSK"):
        ateamlist=CSK
        acaptain="MS Dhoni"
    elif(awayteam=="MI"):
        ateamlist=MI
        acaptain="Rohit Sharma"
    elif(awayteam=="SRH"):
        ateamlist=SRH
        acaptain="David Warner"
    elif(awayteam=="KKR"):
        ateamlist=KKR
        acaptain="Eion Morgan"
    elif(awayteam=="PBKS"):
        ateamlist=PBKS
        acaptain="KL Rahul"
    else:
        ateamlist=RCB
        acaptain="Virat Kohli"
teams=['SRH','RCB','KKR','MI','CSK','PBKS','DC','RR']
for twoteams in list(set(combinations(teams,2))):
    matchno=1
    hometeam=twoteams[0]
    awayteam=twoteams[1]
    if(hometeam=="RR"):
        hteamlist=RR
        hcaptain="Sanju Samson"
    elif(hometeam=="DC"):
        hteamlist=DC
        hcaptain="Rishabh Pant"
    elif(hometeam=="CSK"):
        hteamlist=CSK
        hcaptain="MS Dhoni"
    elif(hometeam=="MI"):
        hteamlist=MI
        hcaptain="Rohit Sharma"
    elif(hometeam=="RCB"):
        hteamlist=RCB
        hcaptain="Virat Kohli"
    elif(hometeam=="KKR"):
        hteamlist=KKR
        hcaptain="Eion Morgan"
    elif(hometeam=="PBKS"):
        hteamlist=PBKS
        hcaptain="KL Rahul"
    else:
        hteamlist=SRH
        hcaptain="David Warner"

    if(awayteam=="RR"):
        ateamlist=RR
        acaptain="Sanju Samson"
    elif(awayteam=="DC"):
        ateamlist=DC
        acaptain="Rishabh Pant"
    elif(awayteam=="CSK"):
        ateamlist=CSK
        acaptain="MS Dhoni"
    elif(awayteam=="MI"):
        ateamlist=MI
        acaptain="Rohit Sharma"
    elif(awayteam=="SRH"):
        ateamlist=SRH
        acaptain="David Warner"
    elif(awayteam=="KKR"):
        ateamlist=KKR
        acaptain="Eion Morgan"
    elif(awayteam=="PBKS"):
        ateamlist=PBKS
        acaptain="KL Rahul"
    else:
        ateamlist=RCB
        acaptain="Virat Kohli"
    match=ipl(hometeam,awayteam,matchno)
    match.homeTeamPlayers(hteamlist,hcaptain)
    match.awayTeamPlayers(ateamlist,acaptain)
    match.toss()
    match.Result()
    matchno+=1
    
#hometeam=input("Enter Home Team :")
hometeam=hometeam.upper()
if(hometeam=="RR"):
    hteamlist=RR
    hcaptain="Sanju Samson"
elif(hometeam=="DC"):
    hteamlist=DC
    hcaptain="Rishabh Pant"
elif(hometeam=="CSK"):
    hteamlist=CSK
    hcaptain="MS Dhoni"
elif(hometeam=="MI"):
    hteamlist=MI
    hcaptain="Rohit Sharma"
elif(hometeam=="RCB"):
    hteamlist=RCB
    hcaptain="Virat Kohli"
elif(hometeam=="KKR"):
    hteamlist=KKR
    hcaptain="Eion Morgan"
elif(hometeam=="PBKS"):
    hteamlist=PBKS
    hcaptain="KL Rahul"
else:
    hteamlist=SRH
    hcaptain="David Warner"
#selectHomeTeam(hometeam)
#awayteam=input("Enter Away Team :")
awayteam=awayteam.upper()
if(awayteam=="RR"):
    ateamlist=RR
    acaptain="Sanju Samson"
elif(awayteam=="DC"):
    ateamlist=DC
    acaptain="Rishabh Pant"
elif(awayteam=="CSK"):
    ateamlist=CSK
    acaptain="MS Dhoni"
elif(awayteam=="MI"):
    ateamlist=MI
    acaptain="Rohit Sharma"
elif(awayteam=="SRH"):
    ateamlist=SRH
    acaptain="David Warner"
elif(awayteam=="KKR"):
    ateamlist=KKR
    acaptain="Eion Morgan"
elif(awayteam=="PBKS"):
    ateamlist=PBKS
    acaptain="KL Rahul"
else:
    ateamlist=RCB
    acaptain="Virat Kohli"
#selectAwayTeam(awayteam)
matchno=int(input("Enter Match No. :"))
match=ipl(hometeam,awayteam,matchno)
match.homeTeamPlayers(hteamlist,hcaptain)
match.awayTeamPlayers(ateamlist,acaptain)
match.toss()
match.Result()
