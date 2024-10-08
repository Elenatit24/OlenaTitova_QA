import pytest
from modules.common.database import Database


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')
    assert user[0][0] == 'Maydan Nezalezhnosti 2'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)
    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)
    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)
    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1
    # Check struture of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


    # individual tasks


@pytest.mark.database
def test_add_user_stepan():
    db = Database()
    user = db.get_user_address_by_name('Stepan')
    assert user[0][0] == 'Stepana Bandery str, 2'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '2055'
    assert user[0][3] == 'Ukraine'

    
@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(5, 'сік', 'полуничний', 10)
    water_qnt = db.select_product_qnt_by_id(5)
    assert water_qnt[0][0] == 10


@pytest.mark.database
def test_change_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')
    assert user[0][0] == 'Shevchenko 34'
    assert user[0][1] == 'Lviv'
    assert user[0][2] == '2443'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_new_product_insert():
    db = Database()
    db.insert_product(6, 'Ostap', 'сік', 'яблуневий', 3)
    water_qnt = db.select_product_qnt_by_id(6)
    assert water_qnt[0][0] == 3
