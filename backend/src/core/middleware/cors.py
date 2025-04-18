from fastapi.middleware.cors import CORSMiddleware

def get_cors_middleware():
    return {
        "middleware_class": CORSMiddleware,
        "options": {
            "allow_origins": ["*"],
            "allow_methods": ["*"],
            "allow_headers": ["*"],
        },
    }
