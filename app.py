import zoo_management as manager


def menu():
    print('Welcome to the zoo simulator!')
    print('[R] Run the simulator')
    print('[Q] Quit program')


menu()
user_input = input()
if user_input != '':
    user_input = user_input.lower()

if user_input == 'r':
    day = 1
    running = True
    animals = manager.create_animals()

    while running:
        time = 8
        print(f'Day: {day}')
        print('Animals in the zoo: ')
        for animal in animals:
            print(f'{animal.name} the {animal.species}, energy {animal.energy}')

        print('\n\n')

        while time <= 20:

            print(f'~~~ {time}:00 ~~~')
            if time == 8:
                manager.feed_animals(animals)
                print(
                    'After the animals had breakfast the zoo open up for the visitors.')

            elif time == 20:
                manager.proceed(animals)
                print('All the visitors left the park.')
                manager.end_day(animals)

            elif time > 8 and time < 20:
                manager.proceed(animals)
                manager.visitor_watching(animals)
                manager.visitor_feeding(animals)

            time += 4
            print('\n')

        print('[N] next day \n[Q] quit')
        user_input = input()
        if user_input.lower() == 'q':
            running = False
        else:
            day += 1

elif user_input == 'q':
    pass
