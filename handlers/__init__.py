# handlers/__init__.py
from .start import router as start_router
from .referral import router as referral_router
from .earnings import router as earnings_router
from .withdraw import router as withdraw_router
from .promotion import router as promotion_router
from .stars import router as stars_router
from .admin import router as admin_router

def register_all(dp):
    """
    Реєструє всі роутери в Dispatcher
    """
    dp.include_router(start_router)
    dp.include_router(referral_router)
    dp.include_router(earnings_router)
    dp.include_router(withdraw_router)
    dp.include_router(promotion_router)
    dp.include_router(stars_router)
    dp.include_router(admin_router)
