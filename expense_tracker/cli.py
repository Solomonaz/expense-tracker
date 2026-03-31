#!/usr/bin/env python3
import click
from expense_tracker.models import SUPPORTED_CURRENCIES, Expense
from expense_tracker import storage

@click.group()
def cli():
    """Expense Tracker CLI"""
    
@cli.command()
def add():
    """Add a new expense"""
    while True:
        try:
            amount = float(input("Amount: ").strip())
            if amount > 0:
                break
            print("Amount must be positive.")
        except ValueError:
            print("Invalid amount. Please enter a number.")


    # Currency selection
    print("Select Currency:")
    for i, c in enumerate(SUPPORTED_CURRENCIES, 1):
        print(f"{i}. {c}")
    while True:
        choice = input(f"Enter number: (1-{len(SUPPORTED_CURRENCIES)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(SUPPORTED_CURRENCIES):
            currency = SUPPORTED_CURRENCIES[int(choice) - 1]
            break
        print("Invalid choice. Please try again.")
    
    # Description
    description = input("Description: ").strip()
    if not description:
        print("Description cannot be empty. Please try again.")
        return
    
    expense = Expense(amount = round(amount, 2), currency=currency, description=description)
    storage.add_expense(expense)
    print(f"Added [{expense.id}]:{expense.amount:.2f} {expense.currency} - {expense.description}")

@cli.command(name = 'list')
def list_expenses():
    """List all expenses"""
    expenses = storage.get_all_expenses()
    if not expenses:
        print("No expenses found.")
        return
    
    print(f"{'ID':<10} {'Date':<12} {'Amount':>10} {'Currency':<10} Description")
    print("-" * 60)
    for exp in expenses:
        print(f"{exp.id:<10} {exp.date:<12} {exp.amount:>10.2f} {exp.currency:<10} {exp.description}")
        print()

@cli.command()
@click.argument('expense_id')
def delete(expense_id):
    """Delete an expense by ID"""
    if storage.delete_expense(expense_id):
        print(f"Deleted expense with ID: {expense_id}")
    else:
        print(f"No expense found with ID: {expense_id}")


if __name__ == "__main__":
    cli()