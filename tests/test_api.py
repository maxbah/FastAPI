import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.students.schemas import StudentAdd, StudentInfoUpdate


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(base_url="http://test",
                           transport=ASGITransport(app=app)) as ac:
        yield ac


@pytest.fixture
def update_stud_info():
    return {
        "last_name": "Gordan",
        "phone_number": "+12345678",
        "address": "stringstri",
        "major_id": 1
    }


@pytest.fixture
def add_test_student():
    test_stud_data = {
        "phone_number": "+222222",
        "first_name": "2Mickhail",
        "last_name": "2Gordan",
        "date_of_birth": "2002-03-13",
        "email": "2jordan@example.com",
        "address": "2stringstri",
        "enrollment_year": 2022,
        "major_id": 3,
        "course": 2,
        "special_notes": "2string"
    }
    return test_stud_data


@pytest.mark.asyncio
async def test_home_page(async_client: AsyncClient()):
        resp = await async_client.get("/")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) != 0
        assert data == {'message': 'Привет всем!'}


@pytest.mark.asyncio
async def test_stud_get_all_students(async_client: AsyncClient):
        resp = await async_client.get(f"/students/")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) != 0
        assert data[0]['phone_number'] == '+98712334647'


@pytest.mark.asyncio
async def test_stud_add_student(async_client: AsyncClient, add_test_student: StudentAdd):
        resp = await async_client.post("/students/add/", json=add_test_student)
        assert resp.status_code == 200


@pytest.mark.asyncio
async def test_stud_get_one_student_by_id(async_client: AsyncClient):
        resp = await async_client.get("/students/{id}?student_id=4")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) != 0


@pytest.mark.asyncio
async def test_stud_get_one_student_by_filter(async_client: AsyncClient):
    resp = await async_client.get("/students/by_filter?student_id=2&course=3&major_id=1&enrollment_year=2018")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) != 0


@pytest.mark.asyncio
async def test_stud_update_student_major_id(async_client: AsyncClient, update_stud_info: StudentInfoUpdate):
    resp = await async_client.put("/students/update_student_info/", json=update_stud_info)
    assert resp.status_code == 200
    assert resp.json().get('message') == "Данные студента Gordan успешно обновлены"

@pytest.mark.asyncio
async def test_stud_del_student_by_id(async_client: AsyncClient):
    resp = await async_client.delete("/students/dell/13")
    assert resp.status_code == 200
    assert resp.json().get('message') == "Студент с айди 13 успешно удален"
