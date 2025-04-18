from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import json

class ResponseInterceptor(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)


            if response.status_code == 200:
                content = await response.body()
                data = json.loads(content.decode("utf-8")) if content else None
                formatted_response = {
                    "data": data,
                    "message": "Success",
                    "error": None
                }
                return Response(
                    content=json.dumps(formatted_response),
                    status_code=response.status_code,
                    headers=response.headers,
                    media_type="application/json"
                )

            return response

        except Exception as e:
            error_response = {
                "data": None,
                "message": "An error occurred",
                "error": str(e)
            }
            return Response(
                content=json.dumps(error_response),
                status_code=500,
                media_type="application/json"
            )