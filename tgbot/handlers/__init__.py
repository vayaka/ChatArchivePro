"""Import all routers and add them to routers_list."""
from .admin import admin_router
from .user import user_router
from .groups import groups

routers_list = [
    groups,
    admin_router,
    user_router,
]

__all__ = [
    "routers_list",
]
