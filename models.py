from dataclasses import dataclass

@dataclass
class User:
    user_id: int
    username: str
    balance: float
    currency: str
    referrals_count: int
    level: str
    join_date: str
