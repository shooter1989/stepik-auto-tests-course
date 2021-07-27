import pytest, math, time

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                    "https://stepik.org/lesson/236896/step/1",
                                    "https://stepik.org/lesson/236897/step/1",
                                    "https://stepik.org/lesson/236898/step/1",
                                    "https://stepik.org/lesson/236899/step/1",
                                    "https://stepik.org/lesson/236903/step/1",
                                    "https://stepik.org/lesson/236904/step/1",
                                    "https://stepik.org/lesson/236905/step/1"] )

class TestCheckLink():
    def test_link1(self, browser, links):
        browser.get(links)
        answer = math.log(int(time.time()))
        answer1 = browser.find_element_by_css_selector(".ember-text-area").send_keys(str(answer))
        button = browser.find_element_by_css_selector(".submit-submission").click()
        element_answer = browser.find_element_by_css_selector(".smart-hints__hint").text
        assert element_answer == "Correct!", 'No right text'

    # def test_link2(self, browser):
    #     browser.get(links[1])
    #     answer1 = browser.find_element_by_css_selector(".ember-text-area").send_keys(str(answer))
    #     button = browser.find_element_by_css_selector(".submit-submission").click()
    #     element_answer = browser.find_element_by_css_selector(".smart-hints__hint").text
    #     assert element_answer == "Correct!"
    # def test_link3(self, browser):
    #     browser.get(links[2])
    #     answer1 = browser.find_element_by_css_selector(".ember-text-area").send_keys(str(answer))
    #     button = browser.find_element_by_css_selector(".submit-submission").click()
    #     element_answer = browser.find_element_by_css_selector(".smart-hints__hint").text
    #     assert element_answer == "Correct!"
    # def test_link4(self, browser):
    #     browser.get(links[3])
    #     answer1 = browser.find_element_by_css_selector(".ember-text-area").send_keys(str(answer))
    #     button = browser.find_element_by_css_selector(".submit-submission").click()
    #     element_answer = browser.find_element_by_css_selector(".smart-hints__hint").text
    #     assert element_answer == "Correct!"
    # def test_link5(self, browser):
    #     browser.get(links[4])
    #     answer1 = browser.find_element_by_css_selector(".ember-text-area").send_keys(str(answer))
    #     button = browser.find_element_by_css_selector(".submit-submission").click()
    #     element_answer = browser.find_element_by_css_selector(".smart-hints__hint").text
    #     assert element_answer == "Correct!"
    # def test_link6(self, browser):
    #     browser.get(links[5])
    #     answer1 = browser.find_element_by_css_selector(".ember-text-area").send_keys(str(answer))
    #     button = browser.find_element_by_css_selector(".submit-submission").click()
    #     element_answer = browser.find_element_by_css_selector(".smart-hints__hint").text
    #     assert element_answer == "Correct!"
    # def test_link7(self, browser):
    #     browser.get(links[6])
    #     answer1 = browser.find_element_by_css_selector(".ember-text-area").send_keys(str(answer))
    #     button = browser.find_element_by_css_selector(".submit-submission").click()
    #     element_answer = browser.find_element_by_css_selector(".smart-hints__hint").text
    #     assert element_answer == "Correct!"
    # def test_link8(self, browser):
    #     browser.get(links[7])
    #     answer1 = browser.find_element_by_css_selector(".ember-text-area").send_keys(str(answer))
    #     button = browser.find_element_by_css_selector(".submit-submission").click()
    #     element_answer = browser.find_element_by_css_selector(".smart-hints__hint").text
    #     assert element_answer == "Correct!"
