def roll_call_dwarves(dwarves):
    index = 1
    for dwarf in dwarves:
        print(f"{index}. {dwarf}")
        index += 1
    
# roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])
    

def summon_captain_planet(planeteers):
    return [planet.capitalize() +"!" for planet in planeteers]
    # for planet in planeteers:
    #     print (planet.capitalize() + "!") 
    
# print(summon_captain_planet(["earth", "wind", "fire", "water", "heart"]))
        

def long_planeteer_calls(word_lists):
    for word in word_lists:
        if len(word) > 4:
            return True
    return False
   

# print(long_planeteer_calls(["puff", "go", "two"]))
# print(long_planeteer_calls(["two", "go", "industrious", "bop"]))


def find_the_cheese(cheese_list):
    cheese = ["cheddar","gouda","camembert"]
    for name in cheese_list:
        if name in cheese:
            return name
    
    

# print(find_the_cheese(["crackers", "gouda", "thyme"]))
# print(find_the_cheese(["tomato soup", "cheddar", "oyster crackers", "gouda"]))