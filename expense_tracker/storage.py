import json
from pathlib import Path
from typing import List, Optional
from .models import Expense

def get_data_files() -> Path:
    root = Path(__file__).resolve().parent.parent
    path = root / 'storage' / 'expenses.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    return path

def load_expenses() -> List[Expense]:
    path = get_data_files()
    if not path.exists():
        return []
    with open(path, 'r', encoding='utf-8') as f:
        try:
            return [Expense.from_dict(item) for item in json.load(f)]
        except json.JSONDecodeError:
            return []
def save_expenses(expenses: List[Expense]) -> None:
    with open(get_data_files(), 'w', encoding='utf-8') as f:
        json.dump([e.to_dict() for e in expenses], f, indent=2)

def add_expense(expense: Expense) -> None:
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

def delete_expense(expense_id: str) -> bool:
    expenses = load_expenses()
    filtered = [e for e in expenses if e.id != expense_id]
    if len(filtered) == len(expenses):
        return False  # Not found
    save_expenses(filtered)
    return True