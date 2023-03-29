#final code copy


import pyttsx3#text to speech
import datetime
import os
import numpy as np
import string
import random
import pandas as pd

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


NIRF_Overall = pd.read_csv("C:/Users/chris/Documents/New Horizon College of Engineering(AI&ML)/Second Year/Semester 3/10. 20AIL39A (Mini Project 1)/BRAINSTORM_FINAL/OverallRanking_2021.csv")
NIRF_University = pd.read_csv("C:/Users/chris/Documents/New Horizon College of Engineering(AI&ML)/Second Year/Semester 3/10. 20AIL39A (Mini Project 1)/BRAINSTORM_FINAL/UniversityRanking_2021.csv")
NIRF_Engg = pd.read_csv("C:/Users/chris/Documents/New Horizon College of Engineering(AI&ML)/Second Year/Semester 3/10. 20AIL39A (Mini Project 1)/BRAINSTORM_FINAL/EngineeringRanking_2021.csv")
NIRF_Medical = pd.read_csv("C:/Users/chris/Documents/New Horizon College of Engineering(AI&ML)/Second Year/Semester 3/10. 20AIL39A (Mini Project 1)/BRAINSTORM_FINAL/MedicalRanking_2021.csv")
NIRF_Management = pd.read_csv("C:/Users/chris/Documents/New Horizon College of Engineering(AI&ML)/Second Year/Semester 3/10. 20AIL39A (Mini Project 1)/BRAINSTORM_FINAL/ManagementRanking_2021.csv")
NIRF_Arch = pd.read_csv("C:/Users/chris/Documents/New Horizon College of Engineering(AI&ML)/Second Year/Semester 3/10. 20AIL39A (Mini Project 1)/BRAINSTORM_FINAL/ArchitectureRanking_2021.csv")


gr=0
sub = ""
optsub=""
stream=0
i=0
name=""

def wishName():
    print("\nBRAINSTORM:\nWhat is your name?")
    speak("What is your name?")
    name=input()
    wish_string="How may I help you "+name+"?"
    print(wish_string)
    speak(wish_string)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("\nBRAINSTORM: \nGood Morning! Brainstorm here, I'm here to assist you through your career selection procedure. Type bye to exit")
        speak("Good Morning! brainstorm here, I'm here to assist you through your career selection procedure")

    elif hour>=12 and hour<18:  
        print("\nBRAINSTORM: \nGood Afternoon! Brainstorm here, I'm here to assist you through your career selection procedure. Type bye to exit")
        speak("Good Afternoon! brainstorm here, I'm here to assist you through your career selection procedure") 

    else:
        print("\nBRAINSTORM: \nGood Evening! Brainstorm here, I'm here to assist you through your career selection procedure. Type bye to exit")
        speak("Good Evening! brainstorm here, I'm here to assist you through your career selection procedure")  

def grade():
    print("\nBRAINSTORM:\nEnter grade:\n10\n11\n12\n\nSTUDENT:")
    speak("enter grade")
    gr = int(input())
    return gr


def college(stream):
    pref=""
    print("\nBRAINSTORM:\n1.State preference\n2.No preference\n\nSTUDENT:")
    speak("select choice if you have a state preference")
    flag=int(input())
    if(flag==1):
        print("\nBRAINSTORM:\nEnter state of choice\n\nSTUDENT:")
        speak("enter your state of choice")
        pref=input()
        pref=pref.title()
    if(stream==1):
        if(flag==1):
            print(NIRF_Overall[NIRF_Overall['State']==pref])
            speak("best overall institutions in selected state are listed below")
        elif(flag==2):
            print(NIRF_Overall)
            speak("best overall institutions in india are listed below")
    elif(stream==2):
        if(flag==1):
            print(NIRF_University[NIRF_University['State']==pref])
            speak("best overall universities in selected state are listed below")
        elif(flag==2):
            print(NIRF_University)
            speak("best overall universities in india are listed below")
    elif(stream==3):
        if(flag==1):
            print(NIRF_Engg[NIRF_Engg['State']==pref])
            speak("best engineering colleges in selected state are listed below")
        elif(flag==2):
            print(NIRF_Engg)
            speak("best engineering colleges in india are listed below")
    elif(stream==4):
        if(flag==1):
            print(NIRF_Medical[NIRF_Medical['State']==pref])
            speak("best medical colleges in selected state are listed below")
        elif(flag==2):
            print(NIRF_Medical)
            speak("best medical colleges in india are listed below")
    elif(stream==5):
        if(flag==1):
            print(NIRF_Management[NIRF_Management['State']==pref])
            speak("best management colleges in selected state are listed below")
        elif(flag==2):
            print(NIRF_Management)
            speak("best management colleges in india are listed below")
    else:
        print("\nBrainstorm:\nEnter valid choice")
        speak("please enter valid choice")


def subjects(gr):
    
    if(gr==10):
        print("\nBRAINSTORM: \nSelect subject:\nMath\nEconomics\nPsychology\n\nSTUDENT:")
        speak("enter subject from given choice")
        sub = input()        

        if(sub=="math" or sub=="Math"):
            print("\nBRAINSTORM: \nGo ahead with science")
            speak("Go ahead with science")
            sub="science"
        elif(sub=="economics" or sub=="Economics"):
            print("\nBRAINSTORM: \nGo ahead with commerce")
            speak("Go ahead with commerce")
            sub="commerce"
        elif(sub=="psychology" or sub=="Psychology"):
            print("\nBRAINSTORM: \nGo ahead with arts")
            speak("Go ahead with arts")
            sub="arts"
        else:
            print("\nBRAINSTORM:\nEnter valid input")
            speak("Please enter valid input")
            return
        print("\nBRAINSTORM:\nDo you want further guidance for your selected subject?\nYes\nNo\n\nSTUDENT:")
        speak("Do you want further guidance for your selected subject?")
        c=input()
        if(c=="yes" or c=="Yes"):
            gr=11
            subjects(gr)
        elif(c=="No" or c=="no"):
            print("\nBRAINSTORM:\nPleasure helping you")
            speak("Pleasure helping you")
            return
        
    elif(gr==11):
        print("\nBRAINSTORM:\nSelect subject:\nScience\nCommerce\nArts\n\nSTUDENT:")
        speak("enter subject from given choice")
        sub = input()

        if(sub=="science" or sub=="Science"):
            print("\nBRAINSTORM: \nSelect optional subject:\nComputer\nBiology\nElectronics\n\nSTUDENT:")
            speak("select optional subject")
            optsub=input()
            if(optsub=="Biology" or optsub=="biology"):
                print("\nBRAINSTORM:\nGo ahead with PCMB")
                speak("go ahead with PCMB")
                stream=4
            elif(optsub=="Computer" or optsub=="computer"):
                print("\nBRAINSTORM:\nGo ahead with PCMC")
                speak("go ahead with PCMC")
                stream=3
            elif(optsub=="Electronics" or optsub=="electronic"):
                print("\nBRAINSTORM:\nGo ahead with PCME")
                speak("go ahead with PCME")
                stream=3
            else:
                print("\nBRAINSTORM:\nPlease enter valid input")
                speak("please enter valid input")

        elif(sub=="commerce" or sub=="Commerce"):
            print("\nBRAINSTORM: \nSelect optional subject:\nStatistics\nComputer\nHistory\n\nSTUDENT:")
            speak("select optional subject")
            optsub=input()
            if(optsub=="Statistics" or optsub=="statistics"):
                print("\nBRAINSTORM:\nGo ahead with SEBA")
                speak("go ahead with SEBA")
                stream=1
            elif(optsub=="Computer" or optsub=="computer"):
                print("\nBRAINSTORM:\nGo ahead with CEBA")
                speak("go ahead with CEBA")
                stream=1
            elif(optsub=="History" or optsub=="history"):
                print("\nBRAINSTORM:\nGo ahead with HEBA")
                speak("go ahead with HEBA")
                stream=1
            else:
                print("\nBRAINSTORM:\nPlease enter valid input")
                speak("please enter valid input")

        elif(sub=="arts" or sub=="Arts"):
            print("\nBRAINSTORM: \nSelect optional subject:\nHistory\nPolitical Science\nSociology\n\nSTUDENT:")
            speak("select optional subject")
            optsub=input()
            if(optsub=="History" or optsub=="history"):
                print("\nBRAINSTORM:\nGo ahead with HESP or HEPP")
                speak("go ahead with HESP or HEPP")
                stream=1
            elif(optsub=="Political Science" or optsub=="political science"):
                print("\nBRAINSTORM:\nGo ahead with HEPP or PPES")
                speak("go ahead with HEPP or PPES")
                stream=1
            elif(optsub=="Sociology" or optsub=="sociology"):
                print("\nBRAINSTORM:\nGo ahead with HESP or PPES")
                speak("go ahead with HESP or PPES")
                stream=1
            else:
                print("\nBRAINSTORM:\nPlease enter valid input")
                speak("please enter valid input")
        else:
            print("\nBRAINSTORM:\nEnter choice from given options only")
            speak("enter choice from given options only")
        print("\nBRAINSTORM:\nDo you want college reccomendations according to your chosen stream?\nYes\nNo\n\nSTUDENT:")
        speak("Do you want college reccomendations according to your chosen stream?")
        i=input()
        i=i.lower()
        if(i=="yes"):
            college(stream)
        else:
            return
        
    elif(gr==12):
        print("\nBRAINSTORM:\nDo you want college reccomendations?\nYes\nNo\n\nSTUDENT:")
        speak("Do you want college reccomendations?")
        i=input()
        i=i.lower()
        if(i=="yes"):
            print("\nBRAINSTORM:\nEnter Choice:\n1.Top overall\n2.Top universities\n3.Engineering\n4.Medical\n5.Management\n\nSTUDENT:")
            speak("enter your choice")
            stream=int(input())
            college(stream)
            

def chat():
    if __name__ == "__main__":
        wishMe()
        wishName()
        choice="hi"
        while(choice!="bye"):
            print("\nBRAINSTORM:\nEnter choice\n1.Subject Selection\n2.College Suggestion\n\nSTUDENT:")
            speak("enter your choice")
            ch=int(input())
            if(ch==1):
                gr = grade()
                subjects(gr)
            elif(ch==2):
                print("\nBRAINSTORM:\nEnter Choice:\n1.Top overall\n2.Top universities\n3.Engineering\n4.Medical\n5.Management\n\nSTUDENT:")
                speak("enter your choice")
                stream=int(input())
                college(stream)
            else:
                print("\nBRAINSTORM:\nEnter valid choice")
                speak("please enter valid choice")
            print("\nBRAINSTORM:\nType bye to leave or anything else to continue\n\nSTUDENT:")
            choice=input()
        print("\nBRAINSTORM:\nIt was a pleasure helping you.")
        speak("it was a pleasure helping you")

chat()