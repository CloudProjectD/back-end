# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.schemas.users import User  # noqa
from app.models.schemas.posts import Post  # noqa
from app.models.schemas.markets import Market  # noqa
from app.models.schemas.likes import Like  # noqa
