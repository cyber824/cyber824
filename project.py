import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.resizable(False, False)

        
        self.canvas = tk.Canvas(master, width=600, height=400, bg="black")
        self.canvas.pack()

        
        self.snake = [[100, 100], [90, 100], [80, 100]]  #
        
        self.food = [self.random_food()]                 
        self.direction = "Right"                        
        self.running = True                              
        self.score = 0

        
        
        self.score_label = tk.Label(master, text=f"Score: {self.score}", font=("consolas", 20), bg="black", fg="white")
        self.score_label.pack()

        
        
        self.master.bind("<KeyPress>", self.change_direction)

        
        
        self.update_game()

    def random_food(self):
        """Generates random food coordinates within the canvas bounds."""
        x = random.randint(0, 59) * 10
        y = random.randint(0, 39) * 10
        return [x, y]

    def update_game(self):
        """Updates game at regular intervals."""
        if self.running:
            self.move_snake()
            self.check_collisions()
            self.update_canvas()
            self.master.after(100, self.update_game)  
            
    def move_snake(self):
        """Moves the snake in the current direction."""
        head = self.snake[0].copy()

        if self.direction == "Left":
            head[0] -= 10
        elif self.direction == "Right":
            head[0] += 10
        elif self.direction == "Up":
            head[1] -= 10
        elif self.direction == "Down":
            head[1] += 10

        self.snake.insert(0, head)

        
        
        if head == self.food[0]:
            self.food[0] = self.random_food()  
            
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.snake.pop()  
            

    def check_collisions(self):
        """Checks if the snake collides with walls or itself."""
        head = self.snake[0]



        if head[0] < 0 or head[0] >= 600 or head[1] < 0 or head[1] >= 400:
            self.game_over()
        
        
        
        if head in self.snake[1:]:
            self.game_over()

    def change_direction(self, event):
        """Changes snake direction based on user input."""
        key = event.keysym
        if key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"
        elif key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"

    def update_canvas(self):
        """Updates the canvas with new snake and food positions."""
        self.canvas.delete("all")

        
        
        self.canvas.create_rectangle(self.food[0][0], self.food[0][1], self.food[0][0] + 10, self.food[0][1] + 10, fill="red")

        
        
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green")

    def game_over(self):
        """Ends the game and shows game over message."""
        self.running = False
        self.canvas.create_text(300, 200, text="GAME OVER", fill="white", font=("consolas", 40))
        self.canvas.create_text(300, 250, text=f"Final Score: {self.score}", fill="white", font=("consolas", 20))



if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
