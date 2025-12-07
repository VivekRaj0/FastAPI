from .utils import *
from routers.users import get_current_user,get_db
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'darkshadow'
    assert response.json()['email'] == 'darkshadow@email.com'
    assert response.json()['first_name'] == 'Dark'
    assert response.json()['last_name'] == 'Shadow'
    assert response.json()['is_active'] == True
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '1234567890'

def test_change_password_success(test_user):
    response = client.put('/user/password', json={"password":"testpassword", "new_password":"newpassword"})
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid_current_password(test_user):
    response = client.put('/user/password', json={"password":"wrongpassword", "new_password":"newpassword"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Error! on Password Change."}

def test_change_phone_number_success(test_user):
    response = client.put('/user/phonenumber/1237799007')
    assert response.status_code == status.HTTP_204_NO_CONTENT