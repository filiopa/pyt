# This is my first code file!
# Inform yourself about comments!
#print('You know, if you press cntrl+Κ, cntrl+C when choosing multiple strings, the become comments!\n If you press cntrl+K, cntrl+U they UN-become comments!')

# Let's check the date! 
import datetime
current_date = str(datetime.date.today())
print('The date today is (yyyy-mm-dd) : ' + current_date)
currentDate = datetime.date.today()
print(currentDate.strftime('In other words, the date today is %A %d of %B in the year of %Y... What a surprise!'))

# Get user's birthday!
birthday = input('What is your birthday? (mm dd yyyy): ')
Birthday = datetime.datetime.strptime(birthday, '%m %d %Y').date()

# Calculate user's number of years and days being alive!
days_alive = (currentDate - Birthday).days
years_alive = days_alive // 365
print(f'You have been alive for about {years_alive} years ({days_alive} days)!')

# Get to know each other, bro!
name = input('\nYo bro, I am the great wizard of Oz! \n And you? whats your name? : ')
print('Hello ' + name + ', nice to meet you!')
common_names = ['John', 'Mike', 'Anna', 'Emma', 'Chris', 'David', \
    'Mary', 'Tom', 'Bob', 'Katy', 'George', 'Ben']

# Check if the name is typical or a number!
if name in common_names:
    print('That is a quite typical name!') 
if name == '1':
    print('This is a number, bro. Are you called like a number?')
if name == 'bro':
    print('MY BROOOOOO!!!')

# Calculate the volume of something!   
height = int(input(name + ', give me a height in meters, please : '))
width = int(input('Great! Now, give me width in meters : '))
depth = int(input('Give me depth in meters : '))
volume = str(height * width * depth)
v0lume = int(height * width * depth)
print('(I think this is '+ volume +')')
print('Your volume is ' + volume + ' m^3 ! ')
material = input('So, we have %.2f' % v0lume + ' squared meters, but of what? ')
print('Alright then! We have ' + volume + ' m^3 of ' + material + '!')
if material == 'shit':
    print('Disgusting!')