# 🎓 Classmate Tracker

A **simple Python + SQLite3** program for storing and analyzing information about your friends or classmates using a local database.

---

## 📋 Features

* Store information about each classmate:

  * Full name
  * Whether they left the state
  * Current occupation
  * Whether they attended college
  * Name of the college (if applicable)
* View, search, edit, or delete entries
* Calculate and display simple statistics

## 📟 Example Database Entry

```
|   ID | Name         | Out of State | Occupation | Went to University  | University Name                 |
|------|--------------|--------------|------------|---------------------|---------------------------------|
|    1 | Joshua Tang  | True         | student    | True                | University of California Irvine |
```

## 📊 Statistics

The program calculates:

* Total number of entries
* Number and percentage who left the state
* Number and percentage who attended college
* Top 3 most frequently attended colleges

## 🚀 Getting Started

1. Install dependencies:

   ```bash
   pip install tabulate
   ```
2. Run the program:

   ```bash
   python main.py
   ```
3. Available Commands:

   * `1` – Add a classmate
   * `2` – Remove a classmate
   * `3` – Edit a classmate
   * `4` – Search for a classmate
   * `5` – View all classmates
   * `6` – Calculate statistics
   * `7` – Quit program

## ✅ Requirements

* Python 3.7+
* [tabulate](https://pypi.org/project/tabulate/)

---
