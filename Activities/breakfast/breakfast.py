# Here is a function that displays the breakfast menu for the week
def breakfast():
    print("What is on the menu today?")
    # Ask user to enter day of week
    day = input('Enter current day of the week: ').capitalize()
    # dictionary of breakfast items
    Breakfast_menu = {
        'Monday': 'oatmeal',
        'Tuesday': 'eggs and bacon',
        'Wednesday':'smoothie',
        'Thursday':'french toast',
        'Friday': 'smoothie',
        'Saturday': 'pancakes',
        'Sunday': 'eggs and potatoes'
    }
    # search for day, based on input
    if day in Breakfast_menu.keys():
        # return the proper value
        result = Breakfast_menu[day]
        print(result)
    # otherwise, ask user to enter a different value
    else:
        print('Please enter valid day of the week (e.g. Monday)')
        breakfast()

# Call breakfast function: What should I eat for breakfast?
breakfast()  

def enjoy_breakfast():
    print("Do you like your breakfast option?")
    # ask user to input value
    answer = input('Please enter yes or no: ')
    if answer == 'yes':
        print('Yay! Glad to hear it!')
    elif answer == 'no':
        print('Sorry about that. Maybe we need a new menu')
    else:
        print('Please enter valid option (yes or no)')
        enjoy_breakfast()
    
# Call next function
enjoy_breakfast()