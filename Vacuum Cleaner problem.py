class VacuumCleaner:
    def __init__(self):
        self.is_on = False
        self.position = (0, 0)
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print("Vacuum cleaner is now on.")
        else:
            print("Vacuum cleaner is already on.")
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print("Vacuum cleaner is now off.")
        else:
            print("Vacuum cleaner is already off.")
    def move(self, direction):
        if not self.is_on:
            print("Please turn on the vacuum cleaner first.")
            return
        movements = {
            'up': (0, 1),
            'down': (0, -1),
            'left': (-1, 0),
            'right': (1, 0)
        }
        if direction in movements:
            dx, dy = movements[direction]
            x, y = self.position
            new_x = x + dx
            new_y = y + dy
            self.position = (new_x, new_y)
            print(f"Moved {direction}. Current position: ({new_x}, {new_y})")
        else:
            print("Invalid direction. Please choose from 'up', 'down', 'left', 'right'.")
    def clean_floor(self):
        if not self.is_on:
            print("Please turn on the vacuum cleaner first.")
            return
        print("Vacuum cleaner is cleaning the floor.")
vacuum = VacuumCleaner()
while True:
    command = input("Enter command (turn on, turn off, move [up/down/left/right], clean, exit): ").lower()
    if command == 'turn on':
        vacuum.turn_on()
    elif command == 'turn off':
        vacuum.turn_off()
    elif command.startswith('move'):
        direction = command.split(' ', 1)[1]
        vacuum.move(direction)
    elif command == 'clean':
        vacuum.clean_floor()
    elif command == 'exit':
        print("Exiting program.")
        break
    else:
        print("Invalid command. Please try again.")
