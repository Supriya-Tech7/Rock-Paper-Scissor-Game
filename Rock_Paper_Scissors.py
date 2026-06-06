import random
from js import document
from pyodide.ffi import create_proxy

choices = {"rock": "✊", "paper": "✋", "scissors": "✌️"}
user_score = 0
computer_score = 0

def choose(event):
    global user_score, computer_score
    user_move = event.target.id
    computer_move = random.choice(list(choices.keys()))

    document.getElementById("user-choice").innerText = choices[user_move]
    document.getElementById("computer-choice").innerText = choices[computer_move]

    if user_move == computer_move:
        result = "It's a draw!"
    elif (user_move == "rock" and computer_move == "scissors") or \
         (user_move == "paper" and computer_move == "rock") or \
         (user_move == "scissors" and computer_move == "paper"):
        result = "You Win! 🎉"
        user_score += 1
    else:
        result = "Computer Wins! 😔"
        computer_score += 1

    document.getElementById("result").innerText = result
    document.getElementById("user-score").innerText = str(user_score)
    document.getElementById("computer-score").innerText = str(computer_score)

def reset_game(event=None):
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    document.getElementById("user-choice").innerText = "❔"
    document.getElementById("computer-choice").innerText = "❔"
    document.getElementById("result").innerText = "Start Playing!"
    document.getElementById("user-score").innerText = "0"
    document.getElementById("computer-score").innerText = "0"

# Attach Python event handlers to HTML buttons
for move in ["rock", "paper", "scissors"]:
    button = document.getElementById(move)
    button.addEventListener("click", create_proxy(choose))

reset_button = document.getElementById("reset-btn")
reset_button.addEventListener("click", create_proxy(reset_game))
