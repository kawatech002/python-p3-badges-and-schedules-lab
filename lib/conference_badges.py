def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    badges = []
    for name in names:
      badges.append(f"Hello, my name is {name}.")
    return badges

def assign_rooms(names):
    
    rooms = []
    i = 0

    while i < len(names):
        for name in names:
            rooms.append(f"Hello, {name}! You'll be assigned to room {i+1}!")
            i += 1
    return rooms

def printer(names):
   
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)


(printer(["Arel", "Carol", "charles", "esther", "wanjiku"]))
    