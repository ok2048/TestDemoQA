import pytest
from pages.text_box import TextBoxPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker


def test_textbox_page_positive():
    '''Позитивный сценарий заполнения полей Full Name, Email, Current Address, Permanent Address,
    нажатия кнопки Submit и проверки заполнения результирующих полей'''
    page = TextBoxPage(webdriver.Chrome())

    # Генерируем случайные данные для заполнения и заполняем соответствующие поля
    fakedata = Faker('ru_RU')
    myfullname = fakedata.name()
    myemail = fakedata.ascii_free_email()
    mycurraddress = fakedata.address()
    mypermaddress = fakedata.address()

    page.enter_fullname(myfullname)
    page.enter_email(myemail)
    page.enter_curraddress(mycurraddress)
    page.enter_permaddress(mypermaddress)

    # Нажимаем кнопку и проверяем результат
    page.btn_click()

    result_fullname = page.driver.find_element(By.ID, 'name')
    result_email = page.driver.find_element(By.ID, 'email')
    result_curraddress = page.driver.find_element(By.CSS_SELECTOR, 'p#currentAddress.mb-1')
    result_permaddress = page.driver.find_element(By.CSS_SELECTOR, 'p#permanentAddress.mb-1')

    # знак != или == будет зависеть от того, верные или неверные данные мы вводим
    assert result_fullname.text == 'Name:' + myfullname, 'Incorrect Fullname'
    assert result_email.text == 'Email:' + myemail, 'Incorrect Email'
    assert result_curraddress.text == 'Current Address :' + mycurraddress, 'Incorrect Current Address'
    assert result_permaddress.text == 'Permananet Address :' + mypermaddress, 'Incorrect Permanent Address'
