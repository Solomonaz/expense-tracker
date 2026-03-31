from setuptools import setup, find_packages
setup(
    name='Expense-tracker-cli',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'click>8.0',
    ],
    entry_points={
        'console_scripts': [
            'expense-tracker=expense_tracker.cli:cli',
        ],
    },
)