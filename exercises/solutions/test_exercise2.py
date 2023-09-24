import httpx
import pytest
from exercise2 import app
from fastapi import status

BASE_URL = "http://testserver"

httpx.AsyncClient(app=app, base_url=BASE_URL)

# To run this test case both path files needs to be set up in the command
# locate yourself in the solutions folder `cd exercises/solutions`
# pytest --cov=exercise2.py test_exercise2.py


@pytest.mark.asyncio
async def test_root():
    async with httpx.AsyncClient(app=app, base_url=BASE_URL) as client:
        response = await client.get("/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"message": "healthy"}
