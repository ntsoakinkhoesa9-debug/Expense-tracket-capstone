import flet as ft
import json, os

class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = float(amount)
        self.category = category
    def to_dict(self):
        return {"title": self.title, "amount": self.amount, "category": self.category}

FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(FILE) or os.stat(FILE).st_size == 0:
        return []
    try:
        with open(FILE, "r") as f:
            return [Expense(**d) for d in json.load(f)]
    except:
        return []

def save_expenses(exp_list):
    with open(FILE, "w") as f:
        json.dump([e.to_dict() for e in exp_list], f, indent=2)

def main(page: ft.Page):
    page.title = "Expense Tracker"
    page.theme = ft.Theme(color_scheme_seed="deepPurple")
    page.padding = 20
    expenses = load_expenses()
    title_input = ft.TextField(label="Title", expand=True)
    amount_input = ft.TextField(label="Amount (R)")
    category = ft.Dropdown(label="Category", value="Food", options=[ft.dropdown.Option("Food"), ft.dropdown.Option("Transport"), ft.dropdown.Option("Study"), ft.dropdown.Option("Other")])
    list_col = ft.Column()
    def refresh():
        list_col.controls.clear()
        for e in expenses:
            list_col.controls.append(ft.ListTile(title=ft.Text(f"{e.title} - R{e.amount}"), subtitle=ft.Text(e.category)))
        page.update()
    def add_click(e):
        if title_input.value and amount_input.value:
            expenses.append(Expense(title_input.value, amount_input.value, category.value))
            save_expenses(expenses)
            title_input.value = ""; amount_input.value = ""
            refresh()
    add_btn = ft.ElevatedButton("Add Expense", on_click=add_click, style=ft.ButtonStyle(bgcolor="deepPurple", color="white"), width=400, height=50)
    page.add(ft.Text("UJ Expense Tracker", size=24, weight="bold"), title_input, amount_input, category, add_btn, ft.Divider(), list_col)
    refresh()
ft.app(target=main)
