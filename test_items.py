def test_open_page_with_language(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # Простой assert на наличие кнопки "Добавить в корзину" (текст зависит от языка)
    assert browser.find_element("css selector", ".btn-add-to-basket"), "Add to basket button not found"
