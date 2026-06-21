# Custom Password Generator

A simple, interactive, and terminal-based Python script that generates random passwords based on user-defined lengths. This project demonstrates basic Python control flow, loop mechanics, data validation, and use of the built-in `string` and `random` libraries

---

## Features

* **Interactive Menu Loop:** Keeps running until the user explicitly chooses to exit (`2`).
* **Robust Character Pool:** Utilizes a highly secure and automated mix of uppercase letters, lowercase letters, digits, and special punctuation using Python's native `string` library.
* **Input Validation:** Gracefully handles incorrect menu selections without crashing the program, allowing the user to try again immediately.
* **Length Counter:** Displays both the generated password and its exact character length for easy confirmation.

---

## How It Works

1. The program starts an infinite `while True` loop and prompts the user with an options menu.
2. Selecting `1` requests a password length and enters a `for` loop to randomly choose characters from the master pool.
3. Selecting `2` triggers a `break` statement to cleanly close the program.
4. Any other input triggers a fallback message, looping back to the menu smoothly.

Output example:
<img width="633" height="105" alt="image" src="https://github.com/user-attachments/assets/ef666154-b71b-43aa-b34f-12bdbde4d2f2" />



---

## Requirements & Setup

### Prerequisites
Make sure you have [Python 3.x](https://www.python.org/) installed on your machine.

### How to Run the App
1. Open the file `random password generator.py` in your favorite Python IDE (like VS Code or Python IDLE).
2. Click the **Run** button (or press `F5` in IDLE) to start generating passwords!
