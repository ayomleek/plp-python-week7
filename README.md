# Shopping List Manager – Python Week 7

This project practises Python lists: creating them, changing them, checking
membership with `in`, and looping through them to summarise their contents.

## Files

- `list_warmup.py` – Demonstrates list indexing, `.append()`, `.remove()` and `len()` using a list of fruits.
- `shopping_list.py` – An interactive menu program (add / remove / show / done) that manages a shopping list without crashing.
- `list_report.py` – Loops through a fixed list to print a numbered list, count names longer than 4 letters, and find the longest name.
- `screenshots/` – Screenshots of each program running.

## Why check `in` before calling `.remove()`?

Calling `.remove()` on an item that is not in the list raises a `ValueError`
and crashes the program. Checking with `in` first lets the program handle a
missing item gracefully by printing a friendly message instead. This makes the
program more reliable and user-friendly, since users often mistype or forget
what is on their list.