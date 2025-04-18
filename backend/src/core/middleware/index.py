from src.core.middleware.logger import LoggingMiddleware
from src.core.middleware.cors import get_cors_middleware
from src.core.middleware.interceptors import ResponseInterceptor

middlewares = [
    {
        "middleware_class": LoggingMiddleware,
        "options": {},
    },
    get_cors_middleware(),
    # {
    #     "middleware_class": ResponseInterceptor,
    #     "options": {},
    # }
]
