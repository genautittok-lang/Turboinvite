from .start import register_start
from .callbacks import register_callbacks
from .withdraw import register_withdraw
from .admin import register_admin

def register_all(dp):
    register_start(dp)
    register_callbacks(dp)
    register_withdraw(dp)
    register_admin(dp)
