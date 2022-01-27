import sys

class level_struct:
    """Level code for all levels"""

    def __init__(self, level_type, level_num):
        self.clear_space()
        print(f"{level_type.title()} {level_num}\n")

    def clear_space(self):
        for i in range(100):
            print("\n")

    def announce_room(self, room_name, level_layout):
        print(f"You are currently in {room_name.title()}\n")

        dict_location = level_layout["rooms"][room_name]
        if dict_location:
            print("Your surrnounding rooms are as follows:")
            for k, v in dict_location.items():
                print(f"  - To your {k.title()} is {v.title()}.")

            return ""
        else:
            print("You have somehow got stuck.\nexiting code...")
            return "stuck"
    
    def handle_input(self, command):
        command = command.lower().strip().split()
        if command[0] == "clear":
            self.clear_space()
        else:
            print(f"Either you have a typo or you are typing an unknown input as I don't know how to {input}.")
    
    def get_input(self) -> str:
        user_answer = input("\t> ")
        return user_answer

class tutorial_1(level_struct):
    """first tutorial level"""

    def __init__(self):
        super().__init__("tutorial", 1)
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

    def start(self):
        if not self.announce_room("start", self.level_layout):   
            self.handle_input(self.get_input())
    
    def room_2(self):
        if not self.announce_room("room_2", self.level_layout):   
            self.handle_input(self.get_input())

    def end(self):
        if not self.announce_room("end", self.level_layout):   
            self.handle_input(self.get_input())

if __name__ == "__main__":
    t1 = tutorial_1()
    t1.start()
