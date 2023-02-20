import random

#Standard greetings to open the game with.
print('Greetings adventurer! Are you ready to discover a new world?')
print('First I will ask you some questions to help create your character.')
#starting point of restarting game after end.
Restartadventure = 'yes'
while Restartadventure.lower() == 'yes':
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
        print(f'{CharacterName} begins walking toward the light to emerge out in a dense forest')
    else:
        print(f'\nStill dazed from awakening in this strange place {CharacterName} decides to rest for a bit')
        print(f'After resting, {CharacterName} feel rejuvinated and ready to take on the world.')
        print(f'With a refreshed mind {CharacterName} looks around the cave to spot a light in the corner.')
        print(f'{CharacterName} begins walking toward the light to emerge out in a dense forest')

    #gameplay loop using a random number loop to see if story will loop or continue
    Forestloop = 0
    while Forestloop == 0:
        Forestpathway = input(f'\nWhile walking in the forest {CharacterName} comes across a fork in the road.\nWhich direction do you go? left or right?: ')
        while Forestpathway.lower() not in ['left','right']:
            Forestpathway = input(f'Please choose left or right: ')
        Forestloop = random.randint(0,1)
        if Forestloop == 0:
            print(f'\n{CharacterName} walks around aimlessly not sure of which direction is the closest town.')
        elif Forestloop == 1:
            print(f'\n{CharacterName} follows the path until they can see the local village in the distance.')

    #Decision 2 fighting a monster
    print(f'\nWhile walking along the path to the town a orc jumps out of the bushes to ambush {CharacterName}.')
    print(f'The orc glances at {CharacterName} and begins to laugh')
    print(f'The orc speaks out saying: \"looks like a puny {RaceType} human with ridiculous {HairColor} hair!\"')
    print(f'With no other choice but to fight you decide to slay the orc.')
    print(f'After the long hard fight you are tired but upon inspection of the orc\'s corpse you find a prompt.')
    Monsterfight = input(f'\nDo you wish to use your unique skill *Devour*?\n(Using Devour will consme the corpse along with any items but you will gain the skills of the creature.) Yes or no?: ')
    while Monsterfight.lower() not in ['yes', 'no']:
        Monsterfight = input(f'\n Please choose yes or no: ')
    if Monsterfight == 'yes':
        print(f'\n{CharacterName} uses *Devour* on the orc\'s corpse.')
        print(f'The corpse liquifies into a puddle of grey goo')
        print(f'A sudden rush of air surrounds {CharacterName} and a new prompt appears!')
        print(f'YOU HAVE AQUIRED A NEW SKILL: *Cleave*')
        print(f'After the battle {CharacterName} decides to head to town to rest at the inn.')
    else:
        print(f'\nDeclining to use *Devour* {CharacterName} loots the body to find a few items.')
        print(f'Congratulations you have aquired a *HIDE TUNIC*(damaged) and 5x*ORC TEETH*')
        print(f'After the battle {CharacterName} decides to head to town to rest at the inn.')

    #Final Decision
    print(f'\nAfter walking to town and finding the inn {CharacterName} Decides to talk to the innkeeper.')
    print(f'Innkeeper: \"Why what lovely {EyeColor} eyes you have! What can I get for you?')
    Innsavepoint = input(f'\n Do you decide to stay at the inn and rest or leave and continue on your journey?\n(stay or leave?): ')
    while Innsavepoint.lower() not in ['stay', 'leave']:
        Innsavepoint = input(f'Please choose stay or leave: ')
    if Innsavepoint == 'stay':
        print(f'\n{CharacterName} decided to stay the night at the inn safe from danger.')
    else:
        print(f'\n{CharacterName} decided to continue on with the journey and brave the dangerous forest.')

    #endings - First ending is Secret Ending
    if beginnerCave == 'yes' and Monsterfight == 'yes' and Innsavepoint == 'stay' and CharacterName.lower() == 'richter':
        print(f'\n*****SECRET ENDING UNLOCKED*****')
        print(f'Richter sits all alone at the tavern bar and mumbles: What a horrible night to have a curse.')
    elif beginnerCave == 'yes' and Monsterfight == 'yes' and Innsavepoint == 'stay':
        print(f'\nAfter a long journey in a new world {CharacterName} has decided to stay in the safety of the inn.')
        print(f'After enjoying a hearty stew to feed their hunger {CharacterName} retires to their room.')
        print(f'{CharacterName} decided to review their new skill and plan how to utilize it.')
        print(f'{CharacterName} awakes in the morning ready to start a new journey!')   
    elif beginnerCave == 'no' and Monsterfight == 'no' and Innsavepoint == 'leave':
        print(f'\nWeary from the travel and fight {CharacterName} decides to not stay at the inn.')
        print(f'Without even eating a meal to sate their hunger {CharacterName} Leaves in a hurry.')
        print(f'{CharacterName} wonders throughout the night hungry and tired never to be seen again.')
    else:
        print(f'{CharacterName} seeks out new way to improve from the townsfolk and continues on with their journey.')
        print(f' it is not know what ever became of {CharacterName}.')

    #Loop back to beginning
    print('*' * 20)
    print('*' * 20)
    print('*' * 20)
    print(f'Thank you for playing!')

    Restartadventure = input("Do you wish to restart? Yes or no: ")
    while Restartadventure.lower() not in ['yes', 'no']:
        Restartadventure = input('Please enter Yes or No: ')