import random


class Character:
    def __init__(self, properties={}):
        if not properties:
            print('properties is false')
        else:
            self.set_character_properties(properties)

    def set_character_properties(self, properties):
        self.name = properties['name']
        self.age = properties['age']
        self.gender = properties['gender']
        self.job = properties['job']
        self.hobbies = properties['hobbies']
        self.friends = properties['friends']
        self.family = properties['family']
        self.interests = properties['interests']
        self.behavior = properties['behavior']
        self.appearance = properties['appearance']
        self.personality = properties['personality']
        self.mood = properties['mood']
        self.live = properties['live']
        self.relationship = properties['relationship']


    def select(self, characters):
        print('Registered characters:\n')
        {print(f'{number + 1} - {character["name"]}')
         for number, character in enumerate(characters)}
        selected_number = input('\nSelect a character (default random): ')
        if not selected_number:
            print('has selected random')
            self.set_character_properties(random.choice(characters))
            return
        if not selected_number.isdigit():
            raise ValueError('Invalid input')
        print(f'has selected {selected_number}')
        selected_character = characters[int(selected_number) - 1]
        self.set_character_properties(selected_character)

    def get_description(self):
        print('get_description')
        print(self.name)
        return f"""
        {self.name} is a {self.age} years old {self.gender}, is a {self.job}, is {self.appearance}, 
        is always {self.mood} and treats all people {self.behavior}.
        Has a personality of {','.join(self.personality)},
        lives {self.live}, 
        currently {self.relationship}, 
        has interest in {', '.join(self.interests)},
        like to practice {', '.join(self.hobbies)} 
        and has {','.join(self.friends)} as friends.
        """
