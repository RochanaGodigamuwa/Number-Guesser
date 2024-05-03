import random

list=[1,2,3,4,5,6]
guess_list=(random.sample(list,k=4))
guess=0
print(guess_list)
Score=0
Attempt=1
Start=int(input("To start the game enter 1:"))
if Start==1:
            Name=str(input("Enter your name please: "))
            print(" "*25,"Hi",Name,"Welcome to Gamelet\n")
            print("Number to Guess - X X X X"," "*5,"Colour Mapping: 1-White 2-Blue 3-Red 4-Yellow 5-Green 6-Purple\n")
            while Attempt<=8:
                        print("Attempt No :",Attempt,"\t")
                        Num_1=int(input("Enter your first Number :"))       #Inputs of player
                        Num_2=int(input("Enter your second Number :"))
                        Num_3=int(input("Enter your third Number :"))
                        Num_4=int(input("Enter your fourth Number :"))
                        if Num_1>6 or Num_2>6 or Num_3>6 or Num_4>6:
                            Attempt+=1
                            print("Please enter numbers between 1 to 6 in your guess,'NOTICE':This attempt will be COUNTED\n")
                            continue

                        if Num_1==0 and Num_2==0 and Num_3==0 and Num_4==0: #Existing  Function
                            print("You Existed the Game")
                            break
                        My_list=[Num_1,Num_2,Num_3,Num_4]
                        print(My_list,"\t")
                        if My_list==guess_list:
                            if Attempt==1:
                                Score=100
                            elif Attempt==2:
                                Score=80
                            elif Attempt==3:
                                Score=60
                            elif Attempt==4:
                                Score=40
                            elif Attempt==5:
                                Score=30
                            elif Attempt==6:
                                Score=20
                            elif Attempt==7:
                                Score=10
                            elif Attempt==8:
                                Score=0
                            print("Congratulation!!!!  You have won the game....\n")
                            print("You have scored ",Score ,"points.\n\n")
                            Choice=str(input("Do you want to play another game(Yes/No)?"))
                            Choice.lower()
                            if Choice=="yes":
                                Attempt=1
                                continue
                            else:
                                break

                        j=0                                #Program Main
                        for i in My_list:
                            if My_list[j]==guess_list[j]:
                                  result='1'
                            elif My_list[j] in guess_list:
                                  result='0'
                            else:
                                  result='.'
                            print(result,end=' ')
                            j=j+1
                        print()    
                        Attempt+=1
            if Choice=="no":
                print("Thank you for playing this game by chandupa")
            elif Attempt>8:
                print("Your ATTEMPTS are over you could not guess the numbers correctly")
            else:
                print("You entered something other than 'No' when asked if u want to play again we are gonna take it as no but")
else:
        print("You ended the game")
        
