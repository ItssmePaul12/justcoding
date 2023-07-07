print('Welcome to the Paul Quiz!')
print('PLEASE READ THE RULES BEFORE STARTING THE QUIZ GAME!')
print('All answers must be in lowercase.')
print('There are 50 questions.')
print('Answers must be typed correctly.')
answer=input("Are you ready to play the Quiz ? (yes/no): ")
score=0
total_questions=50

if answer.lower()=='yes':
    
    answer=input('Question 1: What is my favorite color? ')
    if answer.lower()=='blue':
        score += 1
        print('woooooooooooooow, you guessed it right, Correct!')
    else:
        print('i know this might be a hard question but YOU ARE WRONG, Correct Answer is blue')
    

    answer=input('Question 2: Who said this line: So what do you guys want to talk about? ')
    if answer.lower()=='cody rhodes':
        score += 1
        print('WOOOOAAAH! Correct!')
    else:
        print('I know what I want to talk about....it is that YOU ARE WRONG, Correct Answer is cody rhodes')

    
    answer=input('Question 3: 2 + 2 is? ')
    if answer.lower()=='4':
        score += 1
        print('you are smart, was you in an AP math class or somethin? Correct!')
    else:
        print('oh my...YOU ARE WRONG, Correct Answer is 4')

    
    answer=input('Question 4: What wrestler is known by this line: Hustle, Loyalty, and Respect? ')
    if answer.lower()=='john cena':
        score += 1
        print('You cant see me because you are Correct!')
    else:
        print('you need an attitude adjustment because...YOU ARE WRONG, Correct Answer is john cena')


    answer=input('Question 5: What wrestler is known by this line: the MOST electrifying man in SPORTS entertainment HISTORY? ')
    if answer.lower()=='the rock':
        score += 1
        print('If you SMEEEEEEEEEEEEEEEEEEEEEEELL, what the rock is cooking! Correct!')
    else:
        print('IT DOESNT MATTER WHAT YOU PUT because...YOU ARE WRONG, Correct Answer is the rock')


    answer=input('Question 6: Who sings this song called, Alien Superstar? ')
    if answer.lower()=='beyonce':
        score += 1
        print('You are UNIQUE...Correct!')
    else:
        print('you aint unique enough, YOU ARE UNIQUELY WRONG, Correct Answer is beyonce')


    answer=input('Question 7: What wrestler is known by this line: You think you know me? ')
    if answer.lower()=='edge':
        score += 1
        print('you do know me...Correct!')
    else:
        print('SPEAR...YOU ARE WRONG, Correct Answer is edge')


    answer=input('Question 8: Who sings this song called, The Last Song? ')
    if answer.lower()=='rihanna':
        score += 1
        print('work work work work work work because you are Correct!')
    else:
        print('work work work work work work...because YOU ARE WRONG WRONG WRONG WRONG WRONG WRONG, Correct Answer is rihanna')


    answer=input('Question 9: what wrestler is known by this line: The Head of the Table? ')
    if answer.lower()=='roman reigns':
        score += 1
        print('Roman Reigns is proud of you...Correct!')
    else:
        print('Acknowledge this...YOU ARE WRONG, Correct Answer is roman reigns')


    answer=input('Question 10: What About Us? is sung by? ')
    if answer.lower()=='brandy':
        score += 1
        print('What about this? Correct!')
    else:
        print('What about this? YOU ARE WRONG, Correct Answer is brandy')

    answer=input('Question 11: Feedback is a song sung by? ')
    if answer.lower()=='janet jackson':
        score += 1
        print('my feedback to you is that you are...Correct!')
    else:
        print('my feedback to you is that...YOU ARE WRONG, Correct Answer is janet jackson')

    
    answer=input('Question 12: Whos video game character is known by this line: hey Niko! Lets go Bowling! ')
    if answer.lower()=='roman bellic':
        score += 1
        print('You scored a strike in the bowling game...Correct!')
    else:
        print('lets not go bowling because...YOU ARE WRONG, Correct Answer is roman bellic')
    

    answer=input('Question 13: What popular person is known by this line: WHERE IS THE LAMB SAUCE? ')
    if answer.lower()=='gordon ramsay':
        score += 1
        print('The scallops is cooked well....Correct!')
    else:
        print('GET OUT, THE CHICKEN IS RAW AND YOU ARE WRONG, Correct Answer is gordon ramsay')
    

    answer=input('Question 14: What wrestler is known by this line: Im AWESOME! ')
    if answer.lower()=='the miz':
        score += 1
        print('YOU ARE AWESOME, Correct!')
    else:
        print('you are not awesome enough because YOU ARE WRONG, Correct Answer is the miz')
    
    answer=input('Question 15: 3 times 3 is? ')
    if answer.lower()=='9':
        score += 1
        print('you muust have went to school for PhD because you are... Correct!')
    else:
        print('Brain Fart, YOU ARE WRONG, Correct Answer is 9')
    

    answer=input('Question 16: What year was AEW founded in? ')
    if answer.lower()=='2019':
        score += 1
        print('you deserve some wrestling gifts...Correct!')
    else:
        print('no..no...no..YOU ARE WRONG, Correct Answer is 2019')
    

    answer=input('Question 17: What is WWWE most popular show of each year? ')
    if answer.lower()=='wrestlemania':
        score += 1
        print('the winner of this match is...Correct!')
    else:
        print('wrestle this...YOU ARE WRONG, Correct Answer is wrestlemania')
    
    answer=input('Question 18: Who sung the popular song called Its a Wrap? ')
    if answer.lower()=='mariah carey':
        score += 1
        print('Its not a wrap for ya becase You Are Correct!')
    else:
        print('Mariah Carey dont know you...YOU ARE WRONG, Correct Answer is mariah carey')
    
    answer=input('Question 19: 4 + 4 is? ')
    if answer.lower()=='8':
        score += 1
        print('you are smart, Correct!')
    else:
        print('you need a math teacher because YOU ARE WRONG, Correct Answer is 8')
    
    answer=input('Question 20: What is the keyboard button when you are trying to remove a letter? ')
    if answer.lower()=='backspace':
        score += 1
        print('backspace is happy because YOU ARE Correct!')
    else:
        print('backspace would like to say some words to ya...YOU ARE WRONG, Correct Answer is backspace')
    
    answer=input('Question 21: what is the reload key button on the keyboard? ')
    if answer.lower()=='f5':
        score += 1
        print('Correct!')
    else:
        print('Come on now, YOU ARE WRONG, Correct Answer is f5')
    
    answer=input('Question 22: Energy is a song, released in 2008, sung by? ')
    if answer.lower()=='keri hilson':
        score += 1
        print(' I hope this response give you energy because.... you are correct!')
    else:
        print('cause you take away my energy because...YOU ARE WRONG, Correct Answer is keri hilson')
    
    answer=input('Question 23: What wrestler is known by this line: Whats Up?! ')
    if answer.lower()=='r-truth':
        score += 1
        print('You know whats happening...YOU ARE CORRECT!')
    else:
        print('jimmy is angry with you because...YOU ARE WRONG, Correct Answer is r-truth')
    
    answer=input('Question 24: What popular phone that first released in the year of 2007? ')
    if answer.lower()=='iphone':
        score += 1
        print('Hey Siri, Am I Correct? Yes, You are correct!')
    else:
        print('Siri is angry said that AI will take over the world and also said....YOU ARE WRONG, Correct Answer is iphone')
    
    answer=input('Question 25: Guess the song by the lyrics: Who am I gonna lean on when times get tough? Whos gon talk to me till the sun comes up? ')
    if answer.lower()=='we belong together':
        score += 1
        print('Mariah Carey know you well....Correct!')
    else:
        print('you should take a music class because YOU ARE WRONG! Correct Answer is we belong together')
    
    answer=input('Question 26: what is roman reigns primary finisher? ')
    if answer.lower()=='spear':
        score += 1
        print('The Tribal Chief is proud of ya...Correct!')
    else:
        print('you need to watch more professional wrestling...YOU ARE WRONG')
    
    answer=input('Question 27: Whos is the one who sing this song: Gimme More? ')
    if answer.lower()=='britney spears':
        score += 1
        print('Its Britney, You are correct!')
    else:
        print('I will give this one, YOU ARE WRONG....Correct answer is britney spears')
    
    answer=input('Question 28: Guess the song by the lyrics: why wont you lead me home? Cause im lost in this dream, I need you to hold me? ')
    if answer.lower()=='scared of lonely':
        score += 1
        print('You are so C O R R E C T!')
    else:
        print('Beyonce is so angry at you because You are soooooooooo WRONG, Correct Answer is scared of lonely')
    
    answer=input('Question 29: What company are the computer mouses in the room are from? ')
    if answer.lower()=='hp':
        score += 1
        print('HP is happy of ya...Correct!')
    else:
        print('HP is angry with ya and said computer mouses will take over the world....YOU ARE WRONG, Correct Answer is hp')
        
    answer=input('Question 30: What is 8 times 8 times 8? ')
    if answer.lower()=='512':
        score += 1
        print('You must have a Masters degree in Math! Correct!')
    else:
        print('Why bruh? You are W R O N G!')
    
    answer=input('Question 31: Dont Stop The Music, was released in 2007, sung by? ')
    if answer.lower()=='rihanna':
        score += 1
        print('Please dont stop the music, music, music, You are correct!')
    else:
        print('Stop the music....YOU ARE WRONG, Correct Answer is rihanna')
    
    answer=input('Question 32: 6 times 6 is? ')
    if answer.lower()=='36':
        score += 1
        print('PhD Student, Correct!')
    else:
        print('You must be super...WRONG, Correct Answer is 36')
        
    answer=input('Question 33: Jey Uso and Jimmy Uso are a tag team called? ')
    if answer.lower()=='the usos':
        score += 1
        print('DAY ONE-ISH, YEET, Correct!')
    else:
        print('The USOS finna superkick your head off....YOU ARE WRONG, Correct Answer is the usos')
    
    answer=input('Question 34: What wrestler is known by this line: YES! YES! YES! YES! YES! YES! YES! ')
    if answer.lower()=='daniel bryan':
        score += 1
        print('YES! YES! YES! YOU ARE Correct!')
    else:
        print('NO! NO! NO! YOU ARE WRONG, Correct Answer is daniel bryan')
    
    answer=input('Question 35: Whats 5 times 5? ')
    if answer.lower()=='25':
        score += 1
        print('Wow, i am so proud of ya, Correct!')
    else:
        print('you......you are........WRONG! Correct Answer is 25')
    
    answer=input('Question 36: What is The Rock primary signature move? ')
    if answer.lower()=='spinebuster':
        score += 1
        print('The Brahma Bull is proud of ya! Correct!')
    else:
        print('why? why are you sooo...WRONG! Correct Answer is spinebuster')
    
    answer=input('Question 37: Who is the original voice of Siri? ')
    if answer.lower()=='susan bennett':
        score += 1
        print('Siri is happy and will gift you Apple products, Correct!')
    else:
        print('Siri is furious and she tells you that robots and AI will take over the world, she will no longer be a service for ya iphone or even ANDROID...You are wrong! Correct Answer is susan bennett')
    
    answer=input('Question 38: Did Jey Uso superkicked Roman Reigns recently? yes or no? ')
    if answer.lower()=='yes':
        score += 1
        print('THE USOS!!! Correct!')
    else:
        print('THE USOS SUPERKICKED YOUR HEAD OFF!!! YEEET! WRONG! Correct Answer is yes')
    
    answer=input('Question 39: Who first defeated the streak in WWE? ')
    if answer.lower()=='brock lensar':
        score += 1
        print('Paul Heyman is proud of ya...Correct!')
    else:
        print('F5, WRONG! Correct Answer is brock lensar')
    
    answer=input('Question 40: Who is currently the World Heavyweight Championship in WWE? ')
    if answer.lower()=='seth rollins':
        score += 1
        print('WOOOOO, AHHHHH, OOOOOOOOOO, WOOOOOOOO, Correct!')
    else:
        print('you just got a curb stomp! WRONG, Correct Answer is seth rollins')
    
    answer=input('Question 41: This is a team in WWE. This tag team consist of Big E, Kofi Kingston, and Xavier Woods. This tag team is called? ')
    if answer.lower()=='the new day':
        score += 1
        print('ITS A NEW DAY, YES IT IS, Correct!')
    else:
        print('Shame...Shame...SHAME! Wrong! Correct Answer is the new day')
    
    answer=input('Question 42: Who is the newest member in The Bloodline in WWE? ')
    if answer.lower()=='solo sikoa':
        score += 1
        print('Paul Heyman is happy of ya...Correct!')
    else:
        print('You just got SAMOAN SPIKE by solo sikoa! WRONG, Correct Answer is solo sikoa')
    
    answer=input('Question 43: Beyonce released an album in 2011 called? ')
    if answer.lower()=='4':
        score += 1
        print('Love is on top for ya.....Correct!')
    else:
        print('0 + 0 equals WRONG.....Corect Answer is 4')
    
    answer=input('Question 44: What is Kevin Owens finisher move? Kevin Owens is a WWE wrestler. ')
    if answer.lower()=='stunner':
        score += 1
        print('STUNNER!!!!!!! YOU ARE CORRECT! WOO HOOO!')
    else:
        print('Kevin Owens has an angry problem and will yell at you because you got this question, WRONG! Correct Answer is stunner')
    
    answer=input('Question 45: Who is the main protagonist of GTA 4? ')
    if answer.lower()=='niko bellic':
        score += 1
        print('Niko Bellic is proud of ya..Correct!')
    else:
        print('HAD ENOUGH OF THIS...WRONG! Correct Answer is niko bellic')
    
    answer=input('Question 46: Who was Niko Bellic main friend in GTA 4? ')
    if answer.lower()=='little jacob':
        score += 1
        print('You must have played GTA 4...Correct!')
    else:
        print('YOU ARE SO WRONG....Correct Answer is little jacob')
    
    answer=input('Question 47: Who is Jey Uso twin? ')
    if answer.lower()=='jimmy uso':
        score += 1
        print('Its the USOS! Correct!')
    else:
        print('Jimmy Uso superkicked your head off..wrong! Correct Answer is jimmy uso')
    
    answer=input('Question 48: What WWE TV show takes place on Fridays? ')
    if answer.lower()=='smackdown':
        score += 1
        print('YOU ARE CORRECT!')
    else:
        print('you need to watch wrestling like WWE and AEW....WRONG! Correct Answer is smackdown')
    
    answer=input('Question 49: What WWE TV show takes place on Tuesdays? ')
    if answer.lower()=='nxt':
        score += 1
        print('you are correct!')
    else:
        print('WATCH WRESTLING...WRONG! Correct Answer is nxt')
    
    answer=input('Question 50: What show was before NXT? ')
    if answer.lower()=='fcw':
        score += 1
        print('You are smart! Correct!')
    else:
        print('Focus in class bruh...Wrong! Correct Answer is fcw')
    
    
    
        
        

print('Thank you for playing the Paul Quiz game, you attempted',score,"question correctly!")
totalpoints=(score/total_questions)*100
print('totalpoints obtained:',totalpoints)
print('Goodbye and also...So what do you guys want to talk about?')
