# 💰 Expense Tracker CLI

## About the Project

I built this Expense Tracker CLI using Python as a mini-project to practise my programming skills and learn how to manage data using file handling.

The idea behind this project is simple: keeping track of daily expenses can be difficult, so I wanted to build a small tool that makes it easier to record spending and see where the money goes.

The application runs in the terminal and stores expense records in a JSON file, so the data is still available when you run the program again.

## ✨ Features

- Add a new expense with its amount, category, and description.
- View all recorded expenses in one place.
- Check the total amount spent.
- Filter expenses by category, such as Food, Travel, or Shopping.
- Delete an expense using its ID.
- Save expense records in a JSON file for future use.
- Handle invalid inputs, such as incorrect amounts or expense IDs.

## 🛠️ Built With

- Python
- JSON for storing expense data
- Built-in Python modules: `json`, `datetime`, and `pathlib`

## 📁 Project Structure

```text
expense-tracker-cli/
├── main.py
├── expenses.json
└── README.md
```

## 🚀 How to Run the Project

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Open the project folder**

```bash
cd expense-tracker-cli
```

**3. Run the application**

```bash
python main.py
```

If you're using Windows, you can also run:

```bash
py main.py
```

Make sure Python is installed on your system before running the project.

## 💻 How to Use It

When you run the program, a menu appears in the terminal. You can choose an option to add, view, filter, or delete expenses.

For example, you can add an expense like this:

```text
Enter amount: ₹250
Enter category: Food
Enter description: Lunch

Expense added successfully!
```

The expense will be saved in `expenses.json`, so you won't lose your records when you close the program.

## 📚 What I Learned

While building this project, I got practical experience with:

- Writing functions to keep code organised.
- Working with Python lists and dictionaries.
- Reading and writing data using JSON.
- Handling errors and validating user input.
- Implementing basic CRUD operations.
- Calculating totals and filtering records.

## 🔮 What's Next?

I would like to improve this project by adding monthly expense reports, budget alerts, and the ability to update existing expenses. I also plan to explore SQLite and FastAPI to turn this small CLI application into a more complete backend project.

## 👨‍💻 Author

**Vaibhav Kumar Pal**

GitHub: [imVaibhavPal](https://github.com/imVaibhavPal)

---

This is one of my small projects as I continue learning Python and building practical applications. Feedback and suggestions are always welcome!
