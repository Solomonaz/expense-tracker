from dataclasses import dataclass, field
from datetime import date, datetime
import uuid

SUPPORTED_CURRENCIES = ['USD', 'EUR']

@dataclass
class Expense:
    amount: float
    currency: str
    description: str
    date: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'currency': self.currency,
            'description': self.description,
            'date': self.date
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            amount=data['amount'],
            currency=data['currency'],
            description=data['description'],
            date=data['date']
        )