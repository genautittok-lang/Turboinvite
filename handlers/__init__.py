from .start import register_start
from .referral import register_referral
from .earnings import register_earnings
from .withdraw import register_withdraw
from .promotion import register_promotion
from .stars import register_stars
from .admin import register_admin

def register_all(dp):
    register_start(dp)
    register_referral(dp)
    register_earnings(dp)
    register_withdraw(dp)
    register_promotion(dp)
    register_stars(dp)
    register_admin(dp)
