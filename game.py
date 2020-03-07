import random
total_points = 100
points_to_deduct=5
number_to_predict= random.randint(1,100)

print('Hello\nWelcome to How Smart are You\nThis is a simple game which asks you to predict a number in a range\nand each time you make a mistake, you get a hint whether\nyou are close or far and 5 points is deducted from your total points.\nYou have 100 points\nLets Begin')
 
predicted = input('Enter any number between 1 and 100:')

while int(predicted) != int(number_to_predict):
    total_points -= points_to_deduct
    if total_points==0:
        print('Damn Nigga You Lost')
        break
    if predicted !=0:
        if int(predicted) in range((number_to_predict-5),(number_to_predict+5)):
            print('Wow, You are very close, Try again')
            predicted = input('Enter any number between 1 and 100:')
        else :
            print('Please Try again')
            predicted = input('Enter any number between 1 and 100:')

if int(total_points) in range(85,100):
    print('congratulations, You did soo well, What a Geek!!')
elif int(total_points) in range(70,84):
    print('Damn, You are Good, Better luck next time')
elif int(total_points) in range(50,69):
    print('Not bad, You learn before coming here next time!')
elif int(total_points)>50:
    print('Do not come here again !!')

print('Your total Points : '+str(total_points))

