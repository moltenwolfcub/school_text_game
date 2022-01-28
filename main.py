import sys

class level_struct:
    """Level code for all levels"""

    def __init__(self, level_type, level_num, level_layout):
        self.level_layout = level_layout
        self.level_num = level_num
        self.level_type = level_type

        self.clear_space()
        print(f"{level_type.title()} {level_num}\n")

        self.move_words = ["move", "go"]

    def clear_space(self):
        for i in range(100):
            print("\n")

    def announce_room(self, room_name):
        print(f"You are currently in {room_name.title()}")

        dict_location = self.level_layout["rooms"][room_name]
        if dict_location:
            print("Your surrounding rooms are as follows:")
            for k, v in dict_location.items():
                print(f"  - To your {k.title()} is {v.title()}.")

            return ""
        else:
            print("You have somehow got stuck.\nexiting code...")
            return "stuck"
    
    def handle_input(self, command, current_room):
        command = command.lower().strip().split()

        if command[0] == "clear":
            self.clear_space()
            return ""


        elif command[0] in self.move_words:
            if len(command) == 1:
                print("You haven't told me where to move to, please add some more information")
            else:
                if command[1] in self.level_layout["rooms"][current_room].keys():
                    move_location = self.level_layout["rooms"][current_room][command[1]]
                    print(f"Moved {command[1]} to {move_location}\n")
                    return move_location
                else:
                    print(f"You can't move {command[1]}. There is no room there.")
                    return ""
        
        elif command[0] == "info":
            self.announce_room(current_room)


        else:
            print(f"Either you have a typo or you are typing an unknown input as I don't know how to {command}.")
            return ""
    
    def get_input(self) -> str:
        user_answer = input("\nWhat do you want to do?\n\t> ")
        return user_answer

class tutorial_1(level_struct):
    """first tutorial level"""

    def __init__(self):
        self.level_layout = {
            "goal": {
                "type": "enter",
                "rooms": [
                    "end"
                ]
            },
            "rooms": {
                "start": {
                    "south": "room_2"
                },
                "room_2": {
                    "north": "start",
                    "south": "end"
                },
                "end": {
                    "north": "room_2"
                }
            }
        }

        super().__init__("tutorial", 1, self.level_layout)

    def start(self):
        if not self.announce_room("start"):
            while True:
                output = self.handle_input(self.get_input(), "start")
                if output:
                    if output == "room_2":
                        self.room_2()
                    elif output == "end":
                        self.end()
    
    def room_2(self):
        if not self.announce_room("room_2"):
            while True:
                output = self.handle_input(self.get_input(), "room_2")
                if output:
                    if output == "start":
                        self.start()
                    elif output == "end":
                        self.end()

    def end(self):
        if not self.announce_room("end"):
            while True:
                output = self.handle_input(self.get_input(), "end")
                if output:
                    if output == "start":
                        self.start()
                    elif output == "room_2":
                        self.room_2()

if __name__ == "__main__":
    t1 = tutorial_1()
    t1.start()
