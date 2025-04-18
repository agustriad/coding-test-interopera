# src\modules\sales\interfaces\api\sales_router.py

from fastapi import APIRouter
from src.core.exceptions import InternalServerErrorException, NotFoundException, BadRequestException
from typing import List

from src.modules.sales.domain.entities.sales_entity import SalesEntity
from src.modules.sales.application.dto.response_dto import ResponseDto
from src.modules.sales.infrastructure.repositories.sales_repo_impl import SalesRepoImpl
from src.modules.sales.application.services.sales import SalesService
from src.modules.sales.interfaces.controller.sales_controller import SalesController


# inject repo, service, controller
repository = SalesRepoImpl(data_path="public/dummyData.json")
sales_service = SalesService(repository=repository)
sales_controller = SalesController(service=sales_service)

sales_router = APIRouter()

@sales_router.get("/", response_model=ResponseDto)
async def get_list_sales_rep():
    try:
        sales = await sales_controller.get_sales_list()
        return { "data": sales, "message": "Success", "error":None }
    except FileNotFoundError as e:
        raise NotFoundException(str(e))
    except Exception as e:
        raise InternalServerErrorException("Something went wrong while getting sales data")
    
@sales_router.get("/top")
async def get_top_sales_rep():
    try:
        sales = await sales_controller.get_top_sales()
        return { "data": sales, "message": "Success", "error":None }
    except FileNotFoundError as e:
        raise NotFoundException(str(e))
    except Exception as e:
        print(str(e))
        raise InternalServerErrorException("Something went wrong while getting sales data")
    
@sales_router.get("/detail/{sales_id}")
async def get_sales_rep_by_id(sales_id: str):
    try:
        sales = await sales_controller.get_sales_detail(int(sales_id))
        return { "data": sales, "message": "Success", "error":None }
    except ValueError as e:
        raise BadRequestException("ID must be integer")
    except FileNotFoundError as e:
        raise NotFoundException(str(e))
    except Exception as e:
        raise InternalServerErrorException("Something went wrong while getting sales data")