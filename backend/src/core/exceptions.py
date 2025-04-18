from fastapi import HTTPException

class NotFoundException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=404, detail=detail)

class BadRequestException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class UnauthorizedException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=401, detail=detail)

class ForbiddenException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=403, detail=detail)

class ConflictException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=409, detail=detail)

class InternalServerErrorException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)