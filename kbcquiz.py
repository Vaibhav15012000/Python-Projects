
                                    # Simple KBC Quiz for Entertainment Purpose

import winsound
import time
import pygame
pygame.mixer.init()
pygame.mixer.music.load('Kbc Ringtone Download.mp3')
pygame.mixer.music.play()
print("\n\n")
print("NAMASTE DEVIO AUR SAJJANO . APKA BAHUT BAHUT BHAUT SWAGAT HAI ISS KHEL M JISKA NAME H KAUN BANEGA CROREPATI")
time.sleep(5) 
print("             $ $ $ $ $    ' (: WELCOME TO KAUN BANEGA CROREPATI (: '    $ $ $ $ $ " )
time.sleep(6)
print("HELLO CANDIDATES , HERE WE ARE PRESENTING A SIMPLE KBC GAME DEVELOPED BY STUDENTS OF SAGE UNIVERSITY (INSTITUTE OF ADVANCE COMPUTING 1ST YEAR.  )")
print("THIS IS NOT A PIRATED QUIZ . THIS IS PURELY OWNED BY VAIBHAV DUBEY . ALL RIGHTS RESERVED . TM , & COPYRIGHT  © 2019 BY NIDHI ARORA \n\n")
time.sleep(17)

print("PLEASE ENTER THE REQUIRED DETAILs")

def personal_details():
    NAME = input(" ENTER YOUR NAME:\n")
    AGE =  int(input("ENTER YOUR AGE:\n"))
    SEX =  input("ENTER YOUR SEX(MALE/FEMALE):\n")
    CITY=  input(" ENTER YOUR HOMETOWN:\n")
    print("\n")
    return NAME,AGE,SEX,CITY

PD=personal_details()
print("|||||||||||||||||||||||[THANKYOU]||||||||||||||||||||||||||||||\n")
time.sleep(4)
 
winsound.Beep(1000,500)
print("RULES OF THE GAME ARE AS FOLLOWS:\n")
print("1.There will be a total of 10 questions.\n")
print("2.Difficulty will be raised after every question.\n")
print("3.Every question holds 10 points for correct answer and -5 for incorrect answer.\n")
print("4.After each question your scored will be shown.\n")
print("5.You will get 10 seconds to perform each question.\n")
print("6.You cannot leave the game in between.\n\n")
time.sleep(7)

print("CHALIYE SHURU KARTE HAI ISS KHEL KO . LETS PLAY KAUN BANEGA CROREPATI\n\n")
time.sleep(5)
SCORE=0


def Questions():
    print("|||||||||||||AAPKA PEHLA SAWAL YEH RAHA AAPKI COMPUTER SCREEN PAR||||||||||||||\n\n")
    time.sleep(1)
    pygame.mixer.music.load('Kbc.mp3')
    pygame.mixer.music.play()
    time.sleep(2)
    print("Q-1 : WHO IS THE CEO OF AMAZON ONLiNE SHOPPING WEBSITE ?\n")
    time.sleep(3)
    print("AND HERE ARE THE OPTIONS:\n")
    print("1.JACK MAA                         2.BILL GATES\n3.STEVE JOBS                       4.JEFF BEZOS\n")
    time.sleep(2)
    ANSWER=int(input("ENTER YOUR CHOICE: "))
    time.sleep(1)
    if ANSWER == 4:
        global SCORE
        SCORE+=10
        print("|||||||HURRAY ( : ( : YOUR ANSWER IS CORRECT|||||||||\n ")
        time.sleep(2)
        print("CONGRATS !! YOUR POINTS ARE:", SCORE)
        print("\n")
    else:
         print("SORRY!! ) : ): YOU ARE WRONG!!\n")
         SCORE-=5
         time.sleep(2)
         print("OHHHH YOU SCORE IS;", SCORE)
         time.sleep(5)
         print("\n")
         
    
    print("|||||||||YEH RAHA AGLA SAWAL APKI COMPUTER SCREEN PAR||||||||\n\n")
    pygame.mixer.music.load('Kbc.mp3')
    pygame.mixer.music.play()
    time.sleep(1)
    print("Q-2 : WHICH ARTICLE ENSURES SPECIAL STATUS TO JAMMU AND KASHMIR ?\n")
    time.sleep(3)
    print("AND HERE ARE THE OPTIONS:\n")
    print("1.ARTICLE 372                         2.ARTICLE 35(A)\n3.ARTILCE 347                         4.ARTICLE 370\n")
    time.sleep(7)     
    ANSWER=int(input(" ENTER YOUR CHOICE: "))
    time.sleep(1)
    if ANSWER == 4:
        SCORE+=10
        print("|||||||HURRAY ( : ( : YOUR ANSWER IS CORRECT|||||||||\n ")
        time.sleep(2)
        print("CONGRATS !! YOUR POINTS ARE:", SCORE)
        print("\n")
    else:
         print("SORRY!! ) : ): YOU ARE WRONG!!\n")
         SCORE-=5
         time.sleep(2)
         print("OHHHH YOU SCORE IS;", SCORE)
         time.sleep(5)
         
         
    print("|||||||||YEH RAHA AGLA SAWAL APKI COMPUTER SCREEN PAR||||||||\n\n") 
    pygame.mixer.music.load('Kbc.mp3')
    pygame.mixer.music.play()
    time.sleep(1)
    print("Q-3 : WHICH OF THE FOLLOWING IS NOT A PYTHON LIBRARY ?\n")
    time.sleep(3)
    print("AND HERE ARE THE OPTIONS:\n")
    print("1.NUMPHY                         2.SWIFT\n3.PANDA                         4.MAPTLOLIB\n")
    time.sleep(7)
    ANSWER=int(input("ENTER YOUR CHOICE: "))
    time.sleep(1)
    if ANSWER == 2:
        SCORE+=10
        print("|||||||HURRAY ( : ( : YOUR ANSWER IS CORRECT|||||||||\n ")
        time.sleep(2)
        print("CONGRATS !! YOUR POINTS ARE:", SCORE)
        print("\n")     
    else:
         print("SORRY!! ) : ): YOU ARE WRONG!!\n")
         SCORE-=5
         time.sleep(2)
         print("OHHHH YOU SCORE IS;", SCORE)
         time.sleep(5)
         
    
    print("|||||||||YEH RAHA AGLA SAWAL APKI COMPUTER SCREEN PAR||||||||\n\n") 
    pygame.mixer.music.load('Kbc.mp3')
    pygame.mixer.music.play() 
    time.sleep(1)
    print("Q-4 : LUCKNOW PACT WAS SIGNED BETWEEN INDIAN NATIONAL CONGRESS AND WHOM IN 1961 ?\n")
    time.sleep(3)
    print("AND HERE ARE THE OPTIONS:\n")
    print("1.MUSLIM LEAGUE                         2.LORD IRWIN\n3.WARREN HASTINGS                         4.GHADAR PARTY\n")
    time.sleep(7)
    ANSWER=int(input(" ENTER YOUR CHOICE: "))
    time.sleep(1)
    if ANSWER == 1:
        SCORE+=10
        print("|||||||HURRAY ( : ( : YOUR ANSWER IS CORRECT|||||||||\n ")
        time.sleep(2)
        print("CONGRATS !! YOUR POINTS ARE:", SCORE)
        print("\n")
    else:
         print("SORRY!! ) : ): YOU ARE WRONG!!\n")
         SCORE-=5
         time.sleep(2)
         print("OHHHH YOU SCORE IS;", SCORE)
         time.sleep(5)
              
    print("|||||||||YEH RAHA AGLA SAWAL APKI COMPUTER SCREEN PAR||||||||\n\n") 
    pygame.mixer.music.load('Kbc.mp3')
    pygame.mixer.music.play() 
    time.sleep(1)
    print("Q-5 : WHICH WAS THE DATE ON WHICH ARTICLE 370 WAS PASSED IN LOK SABHA?\n")
    time.sleep(3)
    print("AND HERE ARE THE OPTIONS:\n")
    print("1.5 AUGUST 2019                         2.3 SEPTEMBER 2019(A)\n3.6 AUGUST 2019                         4.8 AUGUST 2019\n")
    time.sleep(7)
    ANSWER=int(input(" ENTER YOUR CHOICE: "))
    time.sleep(1)
    if ANSWER == 3:
        SCORE+=10
        print("|||||||HURRAY ( : ( : YOUR ANSWER IS CORRECT|||||||||\n ")
        time.sleep(2)
        print("CONGRATS !! YOUR POINTS ARE:", SCORE)
        print("\n") 
    else:
         print("SORRY!! ) : ): YOU ARE WRONG!!\n")
         SCORE-=5
         time.sleep(2)
         print("OHHHH YOU SCORE IS;", SCORE)
         time.sleep(5)
             
    print("|||||||||YEH RAHA AGLA SAWAL APKI COMPUTER SCREEN PAR||||||||\n\n") 
    pygame.mixer.music.load('Kbc.mp3')
    pygame.mixer.music.play() 
    time.sleep(1)
    print("Q-6 : WHO IS THE FIRST WOMAN PARA ATHLETE TO WIN A GOLD MEDAL IN RIO PARA OLMPICS ?\n")
    time.sleep(3)
    print("AND HERE ARE THE OPTIONS:\n")
    print("1.PV SINDHU                         2.DIPA MALIK\n3.DIPA KARMAKAR                         4.JYOTI DAS JOSHI\n")
    time.sleep(7)
    ANSWER=int(input(" ENTER YOUR CHOICE: "))
    time.sleep(1)
    if ANSWER == 2:
        SCORE+=10
        print("|||||||HURRAY ( : ( : YOUR ANSWER IS CORRECT|||||||||\n ")
        time.sleep(2)
        print("CONGRATS !! YOUR POINTS ARE:", SCORE)
        print("\n") 
    else:
         print("SORRY!! ) : ): YOU ARE WRONG!!\n")
         SCORE-=5
         time.sleep(2)
         print("OHHHH YOU SCORE IS;", SCORE)
         time.sleep(5)
         
         
    print("|||||||||YEH RAHA AGLA SAWAL APKI COMPUTER SCREEN PAR||||||||\n\n") 
    pygame.mixer.music.load('Kbc.mp3')
    pygame.mixer.music.play() 
    time.sleep(1)
    print("Q-7 : WHAT IS THE NAME OF FIRST CANDIDATE TO BE A CROREPATI IN KBC 2019 ?\n")
    time.sleep(3)
    print("AND HERE ARE THE OPTIONS:\n")
    print("1.VAIBHAV DUBEY                         2.PRAVEEN TAMBE\n3.JUNAID KHAN                         4.BABITA TADE\n")
    time.sleep(7)
    ANSWER=int(input(" ENTER YOUR CHOICE: "))
    time.sleep(1)
    if ANSWER == 4:
        SCORE+=10
        print("|||||||HURRAY ( : ( : YOUR ANSWER IS CORRECT|||||||||\n ")
        time.sleep(2)
        print("CONGRATS !! YOUR POINTS ARE:", SCORE)
        print("\n") 
    else:
         print("SORRY!! ) : ): YOU ARE WRONG!!\n")
         SCORE-=5
         time.sleep(2)
         print("OHHHH YOU SCORE IS;", SCORE)
         time.sleep(5)
              
         
    print("|||||||||YEH RAHA AGLA SAWAL APKI COMPUTER SCREEN PAR||||||||\n\n") 
    pygame.mixer.music.load('Kbc.mp3')
    pygame.mixer.music.play()
    time.sleep(1)
    print("Q-8 : WHAT IS THE NAME OF EQUIPMENT MADE BY FRENCH SCIENTIST FOR PARALISED PATIENTS ?\n")
    time.sleep(3)
    print("AND HERE ARE THE OPTIONS:\n")
    print("1.ENDOSKELETON                         2.EXOSKELETON\n3.PARAROBOT                         4.THEEBOLT\n")
    time.sleep(7)
    ANSWER=int(input(" ENTER YOUR CHOICE: "))
    time.sleep(1)
    if ANSWER == 2:
        SCORE+=10
        print("|||||||HURRAY ( : ( : YOUR ANSWER IS CORRECT|||||||||\n ")
        time.sleep(2)
        print("CONGRATS !! YOUR POINTS ARE:", SCORE)
        print("\n") 
    else:
         print("SORRY!! ) : ): YOU ARE WRONG!!\n")
         SCORE-=5
         time.sleep(2)
         print("OHHHH YOU SCORE IS;", SCORE)
         time.sleep(5)     
    
    
    print("|||||||||YEH RAHA AGLA SAWAL APKI COMPUTER SCREEN PAR||||||||\n\n") 
    time.sleep(4)
    print("Q-8 : WHAT IS NAME OF FIRST SIKH OFFICER GOT MURDERED IN HUGSTON , USA ?\n")
    time.sleep(3)
    print("AND HERE ARE THE OPTIONS:\n")
    print("1.VIKRAM BATRA                         2.GURDEEP SINGH\n3.SANDEEP SINGH                         4.GURJINDER SINGH\n")
    time.sleep(7)
    ANSWER=int(input(" ENTER YOUR CHOICE: "))
    time.sleep(1)
    if ANSWER == 3:
        SCORE+=10
        print("|||||||HURRAY ( : ( : YOUR ANSWER IS CORRECT|||||||||\n ")
        time.sleep(2)
        print("CONGRATS !! YOUR POINTS ARE:", SCORE)
        print("\n") 
    else:
         print("SORRY!! ) : ): YOU ARE WRONG!!\n")
         SCORE-=5
         time.sleep(2)
         print("OHHHH YOU SCORE IS;", SCORE)
         time.sleep(5)
    
    
    print("|||||||||YEH RAHA AGLA SAWAL APKI COMPUTER SCREEN PAR||||||||\n\n") 
    pygame.mixer.music.load('Kbc.mp3')
    pygame.mixer.music.play() 
    time.sleep(1)
    print("Q-9 : WHAT IS NAME OF LATEST SUBMARINE INVOLVED IN INDIAN NAVY IN YEAR 2019?\n")
    time.sleep(3)
    print("AND HERE ARE THE OPTIONS:\n")
    print("1.INS KALVARI                         2.INS KHANDERI\n3.INS CHITRA                         4.INS VIKRAM\n")
    time.sleep(7)
    ANSWER=int(input(" ENTER YOUR CHOICE: "))
    time.sleep(1)
    if ANSWER == 2 :
        SCORE+=10
        print("|||||||HURRAY ( : ( : YOUR ANSWER IS CORRECT|||||||||\n ")
        time.sleep(2)
        print("CONGRATS !! YOUR POINTS ARE:", SCORE)
        print("\n") 
    else:
         print("SORRY!! ) : ): YOU ARE WRONG!!\n")
         SCORE-=5
         time.sleep(2)
         print("OHHHH YOU SCORE IS;", SCORE)
         time.sleep(5)
    
    
    print("|||||||||YEH RAHA AGLA SAWAL APKI COMPUTER SCREEN PAR||||||||\n\n") 
    pygame.mixer.music.load('Kbc.mp3')
    pygame.mixer.music.play() 
    time.sleep(1)
    print("Q-10 : WHAT IS NAME OF FIRST A.I CHIP DEVELOPED BY INTEL ?\n")
    time.sleep(3)
    print("AND HERE ARE THE OPTIONS:\n")
    print("1.TIGERHILL                         2.SPRINGHILL\n3.BLACKSHIP                         4.FLAGSHIP\n")
    time.sleep(7)
    ANSWER=int(input(" ENTER YOUR CHOICE: "))
    time.sleep(1)
    if ANSWER == 2:
        SCORE+=10
        print("|||||||HURRAY ( : ( : YOUR ANSWER IS CORRECT|||||||||\n ")
        time.sleep(2)
        print("CONGRATS !! YOUR POINTS ARE:", SCORE)
        print("\n") 
    else:
         print("SORRY!! ) : ): YOU ARE WRONG!!\n")
         SCORE-=5
         time.sleep(2)
         print("OHHHH YOU SCORE IS;", SCORE)
         print("\n")
         time.sleep(5)
         
    print("THANKYOU FOR PLAYING WITH US. YOUR SCORE IS : ", SCORE )
    
Questions()


 


  






        