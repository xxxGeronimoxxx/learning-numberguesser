import random
print(" Hello, this Program will try to guess the Number you think of.")
print("even though you enter the number you think of, the Program will be 100% honesst.")
print("if the number the program thinks you picked is not the number you picked the programm is not going to lie.")
while True:
    while True:
        pickednum =(input("think of a Number in range 1-10, and enter it: "))

        try: pickednum = int(pickednum)
        except ValueError:
            print("Your input is not a number")
            break
    
        if pickednum <= 0 or 11 <= pickednum:
             print("Your input is not in range")
             break
        else:
            num_lines = sum(1 for line in open('numlist.txt'))
            rng = random.randint(0, num_lines)
            f=open('numlist.txt')
            lines = f.readlines()
            guess = lines[rng]
            print("I think: ", guess)
            pickednum = str(pickednum)
            with open('numberguessed.txt', 'a') as file:
                file.write(pickednum)
                file.write("\n")
                file.close()
            pickednum = int(pickednum)
            guess = int(guess)


            if guess == pickednum:
                print("Ha I was right!")
                with open("accuracy.txt", "a") as f:
                    f.write("right")
                    f.write("\n")
                    f.close
                guess = str(guess)
                pickednum = str(pickednum)
                with open('numlist.txt', 'a') as file:
                    file.write("\n")
                    file.write(guess)
                    file.write("\n")
                    file.write(pickednum)
                    file.close()

            else:
                print("I was wrong")
                with open("accuracy.txt", "a") as f:
                    f.write("wrong")
                    f.write("\n")
                    f.close
                guess = str(guess)
                pickednum = str(pickednum)
                fin = open( 'numlist.txt', "r" )
                data_list = fin.readlines()
                fin.close()
                del data_list[rng]
                fout = open("numlist.txt", "w")
                fout.writelines(data_list)
                fout.close()
                with open('numlist.txt', 'a') as file:
                    file.write("\n")
                    file.write(pickednum)
                    file.close()

                
                    
                

 


    


