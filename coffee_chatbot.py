def coffee_bot():
  print('Welcome to the cafe!')

  size = get_size()
  drink_type = get_drink_type()
  print('Alright, that\'s a {} {}!'.format(size, drink_type))

  extra_options()

  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))

def extra_options():
    cup_choice()
    add_cookies()
    add_pastries()

def cup_choice():
    res = input('Would you like a plastic cup or did you bring your own reusable cup? \n[a] I\'ll need a cup. \n[b] Brought my own! \n> ')
    if res == 'a':
        print('Okay, no problem! We\'ll get you a plastic cup.')
    elif res == 'b':
        print('Great! We\'ll fill up your reusable cup.')
    else:
        print_message()
        return cup_choice()

def add_cookies():
    res = input('Would you like to add cookies to your order? \n[a] Yes, please! \n[b] No, thanks. \n> ')
    if res == 'a':
        print('Excellent choice! Adding cookies to your order.')
    elif res == 'b':
        print('Alright, no cookies for now.')
    else:
        print_message()
        return add_cookies()

def add_pastries():
    res = input('How about some pastries? \n[a] Yes, I\'d love some! \n[b] Not today. \n> ')
    if res == 'a':
        print('Delicious choice! Adding pastries to your order.')
    elif res == 'b':
        print('Understood, no pastries this time.')
    else:
        print_message()
        return add_pastries()

# Rest of your code...

  
def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")   

def get_size():
    res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")
    if res == "a":
        return "small"
    elif res == "b":
        return "medium"
    elif res == "c":
        return "large"
    else:
        print_message()
        return get_size()

def order_latte():
    res=input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ")
    if res=="a":
        return "latte"
    elif res=="b":
        return "non-fat latte"
    elif res=="c":
        return "soy latte"
    else:
        print_message()
        return order_latte()
    
def get_drink_type():
    res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ")
    if res == "a":
        return "brewed coffee"
    elif res == "b":
        return "mocha"
    elif res == "c":
        return order_latte()
    else:
        print_message()
        return get_drink_type()
    
coffee_bot()