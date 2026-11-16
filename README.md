# 🐍 Python Mini Apps

A collection of simple and interactive Python terminal applications, built to practice programming fundamentals, algorithms, loops, functions, and user input handling.

This project brings together four small applications in one command-line interface (CLI), allowing users to select and run each application independently.

---

## ✨ Features

The project currently includes four interactive applications:

### 1. 🔎 Binary Search App

A simple implementation of the Binary Search algorithm.

- Accepts a list of integers and a target value.
- Sorts the list before searching.
- Uses Binary Search to find the target.
- Returns the target's index if found.
- Returns `-1` if the target does not exist.

### 2. 🔷 Shape Generator

Generate simple geometric shapes using the `*` character.

- Draws a rectangle.
- Draws a right-angled triangle.
- Accepts the shape size from the user.

### 3. 🔢 Collatz Conjecture

Explore the Collatz sequence by entering a positive integer.

The program follows these rules:

- If the number is even, divide it by 2.
- If the number is odd, multiply it by 3 and add 1.
- Repeat until the number reaches 1.

The complete sequence is displayed in the terminal.

### 4. 🎮 Hope Game

An interactive number game between the user and the computer.

- The user selects a positive integer.
- The computer starts the game.
- Players take turns counting upward.
- Multiples of the selected number must be replaced with `hope`.
- Incorrect answers end the game.
- Enter `-1` to exit the game.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed on your system.

Check your Python version:

```bash
python3 --version
```

### Installation

Clone the repository:

```bash
git clone <YOUR-REPOSITORY-URL>
```

Navigate to the project directory:

```bash
cd <PROJECT-DIRECTORY>
```

### Run the Application

Execute the following command:

```bash
python3 mini_apps.py
```

---

## 🖥️ Application Menu

When you run the program, the following menu appears:

```text
===================================
       PYTHON MINI APPS
===================================
[1] Binary Search App
[2] Shape Generator
[3] Collatz Conjecture
[4] Hope Game
[0] Exit
===================================
Select an app (0-4):
```

Select an application by entering its corresponding number.

After an application finishes, press `Enter` to return to the main menu.

---

## 📂 Project Structure

```text
python-mini-apps/
│
├── mini_apps.py
│
└── README.md
```

---

## 🛠️ Technologies Used

- **Python 3**
- Command Line Interface (CLI)
- Built-in Python functions and modules

No external libraries or dependencies are required.

---

## 🎯 Learning Objectives

This project was created to practice and strengthen fundamental programming concepts, including:

- Functions and code reusability
- Conditional statements (`if`, `elif`, `else`)
- Loops (`for`, `while`)
- Lists and list manipulation
- Sorting algorithms
- Binary Search
- Mathematical operators
- User input and output
- Exception handling (`try`, `except`)
- Program flow control (`break`, `return`)

---

## 📌 Future Improvements

Possible features and improvements for future versions:

- Add more algorithm-based applications.
- Improve the user interface with colors.
- Add more geometric shapes.
- Introduce difficulty levels to Hope Game.
- Add unit tests for individual functions.
- Improve input validation and error handling.

---

## 👨‍💻 Author

**Milad Afzali**

GitHub: [@MiladAfzali-DP](https://github.com/MiladAfzali-DP)

---

⭐ If you find this project interesting, consider giving it a star!
