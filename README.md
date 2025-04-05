# 🏓 Ping Pong Game

Welcome to the **Ping Pong Game** repository! This project is a two-player Ping Pong game developed in Python using the Turtle graphics library. It's a fun way to understand game development concepts and the use of object-oriented programming in Python.

---

## 📂 Repository Structure

```
pin-pong/
│
├── main.py         # The main script that sets up the game environment and controls the game loop
├── bar.py          # Contains the Paddle class defining paddle properties and movements
├── ball.py         # Contains the Ball class defining ball properties and behaviors
└── scoreboard.py   # Contains the Scoreboard class to track and display scores
```

---

## 🎮 How to Play

- **Left Paddle**: Use **W** (up) and **S** (down) keys.
- **Right Paddle**: Use **Up** and **Down Arrow** keys.
- Try to hit the ball back and forth—if it passes your paddle, the other player scores a point.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Installation

```bash
git clone https://github.com/psyccho00/pin-pong.git
cd pin-pong
python main.py
```

---

## 🧩 Code Breakdown

### `main.py`

- Sets up the screen using `turtle.Screen()`.
- Initializes paddles, ball, and scoreboard.
- Listens for player inputs to move paddles.
- Runs a game loop:
  - Updates screen and ball position
  - Checks for wall and paddle collisions
  - Resets ball and updates score when a point is scored

### `bar.py`

- Contains the `Paddle` class.
- Each paddle is a white vertical rectangle that moves up and down.
- Methods: `go_up()` and `go_down()` with screen boundary checks.

```python
class Paddle(Turtle):
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
```

### `ball.py`

- Contains the `Ball` class.
- Moves in diagonal directions by default.
- Methods:
  - `move()` – advances ball
  - `bounce_y()` – inverts Y direction
  - `bounce_x()` – inverts X direction
  - `reset_position()` – centers ball and changes direction

```python
def bounce_x(self):
    self.x_move *= -1
```

### `scoreboard.py`

- Displays and updates the score on screen.
- Methods: `update_scoreboard()`, `l_point()`, `r_point()`

```python
class Scoreboard(Turtle):
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
```

---

## 🌟 Features

- Multiplayer controls
- Real-time score tracking
- Ball physics: bouncing off paddles and walls
- Endless loop gameplay

---

## 🖼️ Sample Output

```
Player controls paddles using keyboard.
Scores appear at the top of the screen.
Ball moves realistically, bounces off edges and paddles.
```

---

## 🛠️ Improvements to Consider

- Add sound effects
- Create a start menu or game over screen
- Add AI-controlled paddle
- Track high scores

---

## 👨‍💻 Author

Made by [@psyccho00](https://github.com/psyccho00)

If you liked this game, please ⭐ the repo!

---

Have fun playing Ping Pong in Python! 🕹️
