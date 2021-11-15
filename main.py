print('''
*******************************************************************************
             (\\  _                      ___
             .-"`"(\\                _.""`   `"-.
            /      ` `-._        _.-"            `\__
           6   6)        `-.__.-'                    `",
          /                                         `;-`
         /     ,                                     |
        ()    /  /`                                  |
         `---`"~``\                                  |
                   \                                 |
                    \            \      /           /
                    /`,   ,      |     |           /
                   /   "-.|      |     |         /'
                  /     / |     /,__   |       /`\
                                  
                 /    /'  |    /    `"'\      (   \

*******************************************************************************
''')
print("Welcome to Katmai.")
print("Your mission is to hug a bear.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

desc_1 = input("Left or Right?\n").lower()
if desc_1 == "left":
  print("You fell into a hole in ground. Game over!")
else:
  desc_2 = input("You are at Brooks Falls! Swim or wait?\n").lower()
  if desc_2 == "swim":
    print("Trouts got you! Game over!")
  else:
    desc_3 = input("A bunch of bears show up! Which bear should you try to hug? Otis, Holly or Scrawny?\n").lower()
    if desc_3 == 'otis':
      print("Otis is too focused for a hug. Game over.")
    elif desc_3 == 'holly':
      print("Holly is way to fat to hug. Game over.")
    elif desc_3 == 'scrawny':
      print('Scrawny hugs you so hard! You love it! You win!')
    else:
      print("This bear is not at the falls, try again later")

  