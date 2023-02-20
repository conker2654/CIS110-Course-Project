#Standard greetings to open the game with.
print('Greetings adventurer! Are you ready to discover a new world?')
print('First I will ask you some questions to help create your character.')
#starting point of restarting game after end.
##Restartadventure = 'y'
##while Restartadventure.lower() = 'y'
#Collecting variables from user
CharacterName = input('\nWhat name shall you be known by adventurer?: ')
while len(CharacterName) == 0:
    CharacterName = input('The world requires you to have a name for your adventure.: ')
if CharacterName.lower() == 'richter':
    print(f'\nYou unlocked a easter egg!')
    print(f'What is a man? A miserable little pile of secrets! But enough talk… Have at you!')
else:
    print(f'\n{CharacterName} is a fantastic name for this hero!')
ClassType = input('\nAre you a Warrior or a Mage?: ')
while ClassType.lower() not in ['warrior', 'mage']:
    ClassType = input('The only classes avaliable are Warrior and Mage. please choose one: ')
else:
    print(f'\nyour a {ClassType}? This shall be interesting.')
RaceType = input('\nWhat race are you Human?: ')
while len(RaceType) == 0:
    RaceType = input(f"Race cannot be blank. Please enter a valid race: ")
HairColor = input(f'\nWhat color is your hair?: ')
while len(HairColor) == 0:
    HairColor = input(f"Please enter a color for your hair.: ")
EyeColor = input(f'\nWhat color are your eyes?: ')
while len(HairColor) == 0:
    HairColor = input(f"Please enter a color for your eyes.: ")

#narrative start of the story
print('')
print('*' * 10)
print('*' * 10)
print('*' * 10)
print(f'\n*fading in from black*')
print(f'\nYou awake in a unfamilar place that is dark, damp, and cold.')
print(f'\nUnsure of how you arrived here you try to think about what happened.')
print(f'Unfortunately you cannot recall anything but your name: {CharacterName}')

#start of gameplay
#Decision 1
beginnerCave = input(f'\nIt is time to start your adventure. do you wish to leave the cave? (yes/no): ')
while beginnerCave.lower() not in ['yes', 'no']:
    beginnerCave = input(f'\n Please choose yes or no: ')
if beginnerCave == 'yes':
    print(f'\n{CharacterName} brings themself to their feet off the cold stone floor.')
    print(f'As {CharacterName} assesses their surroundings a light shines from a corner of the cave')
    print(f'[CharacterName} begins walking toward the light to emerge out in a dense forest')
else:
    print(f'\nStill dazed from awakening in this strange place {CharacterName} decides to rest for a bit')
    print(f'After resting, {CharacterName} feel rejuvinated and ready to take on the world.')
    print(f'With a refreshed mind {CharacterName} looks around the cave to spot a light in the corner.')
    print(f'{characterName} begins walking toward the light to emerge out in a dense forest')
