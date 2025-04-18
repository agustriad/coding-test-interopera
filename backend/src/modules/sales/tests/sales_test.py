import pytest
from unittest.mock import MagicMock
from src.modules.sales.application.services.sales import SalesService
from src.modules.sales.domain.repositories.sales_repository import SalesRepository
from src.modules.sales.domain.entities.sales_entity import SalesEntity

def test_get_list_sales():
    mock_repo = MagicMock(SalesRepository)
    mock_sales = [
        SalesEntity(id="1", name="Aleeya", total_sales=2000),
        SalesEntity(id="2", name="Rayya", total_sales=3000)
    ]
    mock_repo.get_list_sales.return_value = mock_sales

    sales_service = SalesService(mock_repo)
    result = sales_service.get_list_sales()

    assert len(result) == 2
    assert result[0].name == "Aleeya"
    assert result[1].total_sales == 3000

def test_get_detail_sales():
    mock_repo = MagicMock(SalesRepository)
    sales_detail = SalesEntity(id="1", name="Aleeya", total_sales=2000)
    mock_repo.get_detail_sales.return_value = sales_detail

    sales_service = SalesService(mock_repo)
    result = sales_service.get_detail_sales("1")

    assert result.name == "Aleeya"
    assert result.total_sales == 2000

def test_get_top_sales():
    mock_repo = MagicMock(SalesRepository)
    top_sales = [
        SalesEntity(id="2", name="Aleeya", total_sales=3000),
        SalesEntity(id="3", name="Rayya", total_sales=2500)
    ]
    mock_repo.get_top_sales.return_value = top_sales

    sales_service = SalesService(mock_repo)
    result = sales_service.get_top_sales()

    assert len(result) == 2
    assert result[0].name == "Aleeya"
    assert result[0].total_sales == 3000
