import random

print("What is your name?")
name = str(input('_if a statment ends in ":" that means you need to input a value it will usaly say what the options are_ \nEnter the name you want:\n'))
def rnam():
  nameList = ["Zofia", "Yusuf", "Alejandro", "Elisabeth", "Rex", "Brady", "Montell", "Shaan", "Safwan", "Rachael", "Nel", "Mekhi", "Karol", "Maddy", "Arvin", "Maisie", "Osian", "Darrel", "Trystan", "Devan", "Nicky", "Joe", "Francis", "John"]
  return random.choice(nameList)

print("\nHello", name,"it is nice to meet you.")
input("_If you are ever hovering in a spot and no text has spawned hit enter to continue to next text this is to not bombard you with walls of text in one go for example_\n")

print("You have the option of 3 starts: the badlands, grasslands, and swamps. Depending on where you start you'll have a different experience. You can make the decision yourself or let luck do it for you.") 
input()
print("\nThree doors drop infront of you the first a sand-colored door the second a pleasant green and the last a smudgy blue with splotches of green")

print('\nwell', name, 'what is your choice?')
print("1, 2, 3 or RNG")
start = str(input('Let me go with:'))

while (start !='RNG' and start !='1' and start !='2' and start !='3'):
  start = str(input('pleas enter a corect value, 1,2,3 or RNG:'))

if (start == 'RNG'):
  start = random.randint(1,3)
else:
  start = int(start)

if(start == 1):
  print('\nAh the badlands a place that is both empty and full at the same time isnt it strange how things like that can exist.')
elif(start==2):
  print('\nthe good old grass lands a buitafl place but not without its flaws')
else:
  print('\nSwamps is a hidden gem if you ask me there is nothing quite like it in terms of looks')
  
input()
print('It was nice talking to you',name,'I prithee be careful on your journy')
def world(start):
  def grasslands():
    input()
    print('A nice breeze is the first thing that greets you the next is the feeling of grass rubing against your clothes you cant see the ground without moveing some of the grass but areas look to be more worn than others its a path walked by others')
  def badlands():
    sin=None
    def rob():
      print('The problem is worn paths have lots of trafic to get in that state and being alone is asking to be considered vunarable to anything \n suddnly your hairs stand and a chill goes up your spine \n "kekeke" \n "Look at this boys seems like we have some things for the picking" \n "Finaly i was woried we risked staing out here for nothing" \n The three suround you a dagger in each of thier hands')
      tempn=None
      th = None 
      sub = None # use this to skip the rest of rob if need
      input()
      print('"So what is your name man"')
      re = str(input('What do you say? \n Tell your name(TELL), give fake(FAKE), say nothing(press enter), ask why they stopped you(WHY):'))
      print()
      while(re !='TELL' and re!='' and re!='FAKE' and re!='WHY'):
        re = str(input('The options are (TELL),(WHY),(<enter key>),(FAKE):'))
      if(re == 'TELL'):
        print('I am',name)
        th = 1
      elif(re == ''):
        print('......')
        th=3
      elif(re == 'FAKE'):
        tempn=rnam()
        print('I am',tempn)
        th=2
      elif(re =='WHY'):
        print('Why are you stoping me?')
        th=4
      
      if (th==4):#spent to much time on this part 
        print('"Are you a fool you idiot we are going to rob you thats what"\n"Calm down he is clearly trying to doop us"\n "Its just vexing we look like robbers we are talking like they would to"\n"when did you learn such smart words"')
        input()
        print('They keep arguing amungst eachother and it just keeps going on and on')
        input()
        print('Two of them forgit about the world around them and the third looks like he regrets ever speaking to you or his partners')
        morb = str(input('You grow tierd of this you can clear your throught to get thier attention(COUGH), or you can just walk away(WALK) or you can suprise attack one of them(KILL):'))
        print()
        while (morb != 'COUGH' and morb !='WALK' and morb !='KILL'):
          morb = str(input('The options are (COUGH),(WALK),(KILL):'))
        if(morb=='WALK'):
          print('You decide to take the easy way out and just walk away') #this ends rob and go to next 
          sub = False
        elif(morb=='COUGH'):
          print('You just want this interaction over with and get thier attention "Can we just get this over with cut to the chase and tell me what you want"')
          input()
          print('"we want to rob you give us everything you have"')#go to the next part 
          sub = True
        elif(morb =='KILL'):
          print('in a swift movement you stab one of the robbers arguing with the other in the back of the neck taking him out the other two are horified some nobody just killed thier pal')#the illusion of choice they all end the rob and go to next AHHAHAHAHAH
          input()
          print('"you killed',rnam(),'we didnt even do anyhing to you we arnt barbaric we just asked your name we didnt even jump you or suprise attack you')
          input()
          print('The two leave and you have the feeling they were good people just forced to do some bad things did he deserve to die')
          input()
          input()
          input()
          print('You keep waking')
          sub = False
        
      elif(th ==2):
        print('"',tempn,'is it? Thats a wierd one boys"')
        lug = random.randint(1,5)
        if(lug ==1):
          input()
          print('"I knew someone named',tempn,' a few years back looked kinda like you wait a second\n IS THAT YOU',tempn,'"')
          input()
          print('You laguh and say I couldnt tell it was you under that mask you have on. this of cours is all a lie you dont even know anyone with the name', tempn)
          input()
          print('you and him talk a bit about something that never happend and he seems to respect this',tempn,'person and he decids to let you go')#this ends the rob and goes to next
          sub = False
        else:
          input()
          print('"whatever',tempn, 'give us everything you have or we\'ll kill you')#go to the next part
          sub = True
      elif(th==3):
        input()
        print('"Oh so we got a tuff guy dont we"')
        input()
        print('"give us all that you have"')
        sub = True
      elif(th==1):
        print('"alright',name,'give us every thing you have"')#go to next part of rob
        sub = True

      if(sub==True):#this makes you get robbed
        input()
        print('dont fight back you are 1 againts 3 you stand no chance')#ends here kek

      elif(sub==False):#you ended the encounter 
        input()
        print('Sooner or later you stumble to a shack your memorys tell you this is your home Lets end this here to save time')


    
    input()
    #start of normal badlands
    print('in an instant your mind is filled with a life you never lived experances you never had yet with your eyes open you see the last thing your memorys showed you', name, 'walking a trail in the badlands')
    input()
    print('You start walking along a small path that can only be differchiated by the worn ground if you comparit to the scraped ground near it')
    input()
    #sin=random.randint(1,3)#1 is rob 2 is sandstorm 3 is montr
    sin=1
    if(sin==1):
      rob()
      
    #if(sin==2):
      #sand()
    #if(sin==3):
      #beast()
    

  def swamps():
    input()
    print('Your first feeling is your boots filling with water and grime. next you feel your nose filling with the humid air. You notice parts where the plants seem to be vacint. its a trail walked by whoever inhabits this world. ')
  if (start == 1):
    badlands()
    

  if (start ==2):
    grasslands()

  if (start ==3):
    swamps()


world(start)

#def world(a):
#def badlands(a):

#l = random.random()
#print(l)
#options = [1, 2, 3]
