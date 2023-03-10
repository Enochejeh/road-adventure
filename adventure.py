name = input("what is your name: ")
print("welcome" , name, "to this great adventure")

answer = input("you are on a dirt road, it has come to an end and you can go left or right. which way will you lie to go? ").lower()

if answer == "left":
    answer = input("you come to a end of a river, you can walk around it or swim across? type walk to walk around it and swim to swim across it: ")
    if answer == "swim":
        print("you swam across and were eaten by crocodile.")

    elif answer == "walk":
        print("you will get to meet bridge in front of you.")

    else:
        print("not valid option! you lose.")
elif answer == "right":
    answer = input("you will see a hotel motel ahead, will you logde or pass. type lodge to logde or paas to pass: ")
    if answer == "logde":
        print("have a plesant night rest")
    

    if answer == "pass":
        print("have a long journey ahead")
        


else:
    print("not correct option! you lose.")
print("thnakyou for play" , name)    