# Task 1 — CLI Calculator App

**Internship:** Python Developer Internship — Elevate Labs  
**Task:** Build a Calculator CLI App  

---

## 📌 Objective
Create a command-line calculator that supports basic arithmetic operations — addition, subtraction, multiplication, and division — using Python functions, user input, and a loop-until-exit flow.

---

## 🛠️ Tools Used
- Python 3
- VS Code
- Terminal / Command Prompt

---

## 📁 Project Structure

```
calculator-task/
│
├── calculator.py       # Main Python script
├── README.md           # Project documentation
└── screenshots/
    └── output.png      # Sample terminal output
```

---

## ▶️ How to Run

1. Make sure Python is installed:
   ```
   python --version
   ```

2. Run the script:
   ```
   python calculator.py
   ```

3. Choose an operation (1–5) from the menu and follow the prompts.

---

## 💻 Sample Output

```
=============================================
         CLI CALCULATOR APP
=============================================
|  1. ADDITION        (+)           |
|  2. SUBTRACTION     (-)           |
|  3. MULTIPLICATION  (*)           |
|  4. DIVISION        (/)           |
|  5. EXIT                          |
=============================================

Enter your choice (1-5): 1
Enter first number: 10
Enter second number: 5
Result = 15.0

Enter your choice (1-5): 4
Enter first number: 10
Enter second number: 0
Result = Cannot divide by zero

Enter your choice (1-5): 5

Thank you for using Calculator!
```

---

## 🔑 Key Concepts Used
- **Functions** — separate function for each operation (`add`, `subtract`, `multiply`, `divide`)
- **Loops** — `while True` loop keeps the app running until the user exits
- **Conditionals** — `if/elif/else` to route user choices
- **CLI Interaction** — `input()` for user input, `print()` for output
- **Input Validation** — handles invalid menu choices and division by zero

---

## 📚 What I Learned
- How to structure a Python CLI application using functions
- How to use `while True` with a `break` exit condition
- How to handle edge cases like division by zero
- How to build a clean, user-friendly terminal interface