class Character:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def move(self, direction):
        if direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
    def display_location(self):
        print(f"{self.name} is at ({self.x}, {self.y}).")
player = Character("Player", 0, 0)

while True:
    player.display_location()
    move_direction = input("Enter a Direction (up/down/left/right/quit):").lower()

    if move_direction == "quit":
        break
    elif move_direction in ["up", "down", "left", "right"]:
        player.move(move_direction)
    else:
        print("Invalid input. Please Enter A Valid Direction")