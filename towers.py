class Tower:
    def __init__(self, name):
        self.name = name
        self.stack = []

    def push(self, disk):
        if self.stack and self.stack[-1] < disk:
            raise ValueError("Cannot place larger disk on a smaller disk.")
        self.stack.append(disk)

    def pop(self):
        if not self.stack:
            raise ValueError("Cannot remove disk from an empty tower.")
        return self.stack.pop()

    def __str__(self):
        return f"{self.name}: {self.stack}"

class TowersOfHanoi:
    def __init__(self, numDisks):
        self.numDisks = numDisks
        self.towers = {
            'A': Tower('A'),
            'B': Tower('B'),
            'C': Tower('C'),
        }
        for disk in range(numDisks, 0, -1):
            self.towers['A'].push(disk)

    def move(self, source, target):
        if not self.towers[source].stack:
            print(f"Invalid move: Tower {source} is empty.")
            return
        disk = self.towers[source].stack[-1]
        if self.towers[target].stack and self.towers[target].stack[-1] < disk:
            print(f"Invalid move: Cannot place larger disk {disk} on smaller disk {self.towers[target].stack[-1]}.")
            return
        self.towers[source].pop()
        self.towers[target].push(disk)
        print(f"Moved disk {disk} from {source} to {target}")

    def display(self):
        print("\nCurrent state:")
        maxHeight = self.numDisks
        towerRepr = {name: self.diskRepresentation(tower) for name, tower in self.towers.items()}
        for level in range(maxHeight, 0, -1):
            row = []
            towerName = ['A', 'B', 'C']
            for name in towerName:
                if level <= len(towerRepr[name]):
                    row.append(towerRepr[name][level - 1])
                else:
                    row.append(" " * (2 * self.numDisks - 1))
            print("  ".join(row))
        print(" A  " + " " * (2 * self.numDisks - 2) + "B  " + " " * (2 * self.numDisks - 2) + "C\n")

    def diskRepresentation(self, tower):
        representation = []
        for disk in tower.stack:
            padding = " " * (self.numDisks - disk)
            representation.append(padding + "*" * (2 * disk - 1) + padding)
        return representation

    def play(self):
        self.display()
        while len(self.towers['C'].stack) != self.numDisks:
            move_input = input("Enter your move (e.g., 'A C' to move from A to C): ").strip().upper()
            if move_input in ['Q', 'QUIT']:
                print("Game quit. Goodbye!")
                break
            try:
                source, target = move_input.split()
                if source not in self.towers or target not in self.towers:
                    raise ValueError("Invalid tower names. Use 'A', 'B', or 'C'.")
                self.move(source, target)
                self.display()
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Congratulations! You solved the puzzle!")



if __name__ == "__main__":
    numDisks = int(input("Enter the number of disks: "))
    game = TowersOfHanoi(numDisks)
    print("Start the game!")
    print("Instructions: Enter moves in the format 'A C' to move from tower A to tower C. Type 'Q' or 'QUIT' to exit.")
    game.play()





