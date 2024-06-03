from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


limiter_instance = Limiter(
        get_remote_address,
        #default_limits=["200 per day", "50 per hour" ],
        default_limits=["5 per minute"],
        storage_uri="memory://" # use the Redis server running on localhost:6379 as the storage backend, storage backend is used to store the rate limit information
    )

def init_apdp(app):
    limiter_instance.init_app(app)
    return app