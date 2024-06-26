import allure
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.uitesting.qa_practice.selenium.input_password_page import PasswordInputPage
from pages.uitesting.qa_practice.selenium.simple_text_input_page import SimpleTextInputPage
from pages.uitesting.qa_practice.selenium.input_email_page import EmailInputPage
from pages.uitesting.qa_practice.selenium.simple_button_page import SimpleButtonPage
from pages.uitesting.qa_practice.selenium.looks_like_a_button import LooksLikeAButtonPage
from pages.uitesting.qa_practice.selenium.displayed_button_page import DisplayedButtonPage
from pages.uitesting.qa_practice.selenium.single_checkbox_page import SingleCheckboxPage
from pages.uitesting.qa_practice.selenium.mult_checkboxes_page import MultCheckboxes
from pages.uitesting.qa_practice.selenium.single_select_page import SingleSelectPage
from pages.uitesting.qa_practice.selenium.mult_select_page import MultSelectPage
from pages.uitesting.qa_practice.selenium.new_tab_link_page import NewTabLinkPage
from pages.uitesting.qa_practice.selenium.text_areas_page import TextAreasPage
from pages.uitesting.qa_practice.selenium.confirm_alert_page import ConfirmAlertPage
from pages.uitesting.qa_practice.selenium.drag_and_drop_boxes_page import DragAndDropBoxesPage
from pages.uitesting.qa_practice.selenium.drag_and_drop_images_page import DragAndDropImagePage
from pages.uitesting.qa_practice.selenium.iframe_popup_page import IframePopUp
from pages.uitesting.qa_practice.selenium.pop_up_modal_page import PopUpModalPage
from pages.uitesting.uitestingplayground.progress_bar_page import ProgressBarPage


@pytest.mark.selenium
def test_simple_text_input_page(start_selenium_driver):

    simple_text_input_page = SimpleTextInputPage(start_selenium_driver, text="qwerty-2")

    simple_text_input_page.open()

    simple_text_input_page.paste_text_to_input()

    result_text = simple_text_input_page.result_text

    assert result_text == simple_text_input_page.text


@pytest.mark.selenium
def test_email_input_page(start_selenium_driver):
    simple_text_input_page = EmailInputPage(start_selenium_driver, email="qyaywq@gmail.com")

    simple_text_input_page.open()

    simple_text_input_page.paste_text_to_input()

    result_text = simple_text_input_page.result_text

    assert result_text == simple_text_input_page.email


@pytest.mark.selenium
def test_password_input_page(start_selenium_driver):
    password_input_page = PasswordInputPage(start_selenium_driver, password="Qwerty-2")

    password_input_page.open()

    password_input_page.paste_text_to_input()

    result_text = password_input_page.result_text

    assert result_text == password_input_page.password


@pytest.mark.selenium
def test_simple_button_is_displayed(start_selenium_driver):
    simple_button = SimpleButtonPage(start_selenium_driver)

    simple_button.open()

    assert simple_button.button_is_displayed


@pytest.mark.selenium
def test_simple_button(start_selenium_driver):
    result = "Submitted"

    simple_button = SimpleButtonPage(start_selenium_driver)

    simple_button.open()

    button = simple_button.button

    with allure.step('Click "Submit" button'):
        button.click()

    assert result == simple_button.result_text


@pytest.mark.selenium
def test_like_a_button_is_displayed(start_selenium_driver):
    simple_button = LooksLikeAButtonPage(start_selenium_driver)

    simple_button.open()

    assert simple_button.button_is_displayed


@pytest.mark.selenium
def test_like_a_button(start_selenium_driver):
    result = "Submitted"

    simple_button = LooksLikeAButtonPage(start_selenium_driver)

    simple_button.open()

    button = simple_button.button

    with allure.step('Click "Submit" button'):
        button.click()

    assert result == simple_button.result_text


@pytest.mark.selenium
def test_disabled_button_page(start_selenium_driver):
    result = "Submitted"

    disabled_button = DisplayedButtonPage(start_selenium_driver)

    disabled_button.open()

    disabled_button.change_drop_down_list_to_enable()

    button = disabled_button.button

    with allure.step('Click the button'):
        button.click()

    result_text = disabled_button.result_text

    assert result_text == result


@pytest.mark.selenium
def test_single_checkbox(start_selenium_driver):
    result = 'select me or not'

    single_chechbox = SingleCheckboxPage(start_selenium_driver)

    single_chechbox.open()

    single_chechbox.checkbox_click()

    single_chechbox.button_click()

    result_text = single_chechbox.result_text()

    assert result == result_text


@pytest.mark.selenium
def test_mult_checkboxes(start_selenium_driver):
    result = 'one, two, three'

    mult_checkboxes = MultCheckboxes(start_selenium_driver)

    mult_checkboxes.open()

    mult_checkboxes.click_all_checkboxes()

    mult_checkboxes.click_button()

    assert mult_checkboxes.result_text == result


# tests with parametrization
@pytest.mark.parametrize(
    'marker',
    [
        'Python',
        'Ruby',
        'JavaScript',
        'Java',
        'C#',
    ]
)
@pytest.mark.selenium
def test_single_select(start_selenium_driver, marker):
    single_input = SingleSelectPage(start_selenium_driver, marker)

    single_input.open()

    single_input.change_drop_down_list_to_marker_value()

    single_input.click_button()

    assert single_input.result_text == marker


def generate_pairs():
    you_want_to_go_list = ['Sea', 'Mountains', 'Old town', 'Ocean', 'Restaurant']
    you_want_to_get_there_list = ['Car', 'Bus', 'Train', 'Air']
    when_you_want_to_go_list = ['Today', 'Tomorrow', 'Next week']

    pair_list = []

    for you_want in you_want_to_go_list:
        for get_there in you_want_to_get_there_list:
            for when_you_want in when_you_want_to_go_list:
                pair_list.append(pytest.param((you_want, get_there, when_you_want),
                                              id='{}, {}, {}'.format(you_want, get_there, when_you_want)))

    return pair_list


# pairwise testing
@pytest.mark.parametrize(
    "pairs",
    generate_pairs()[:5]  # reduced to 5 tests
)
@pytest.mark.selenium
def test_mult_select(start_selenium_driver, pairs):
    marker_1, marker_2, marker_3 = pairs
    mult_select = MultSelectPage(start_selenium_driver, marker_1, marker_2, marker_3)

    mult_select.open()

    mult_select.change_drop_down_list_to_marker_values()

    mult_select.click_button()

    result_text = mult_select.result_text

    assert "to go by {} to the {} {}".format(marker_2, marker_1, marker_3).lower() == result_text


@pytest.mark.selenium
def test_new_tab_link_page(start_selenium_driver):
    result = 'I am a new page in a new tab'

    new_tab_link_page = NewTabLinkPage(start_selenium_driver)

    new_tab_link_page.open()

    new_tab_link_page.click_link()

    new_tab_link_page.switch_page()

    result_text = new_tab_link_page.result_text

    assert result_text == result


@pytest.mark.selenium
def test_text_areas(start_selenium_driver):
    text_areas_page = TextAreasPage(start_selenium_driver, ["Q", "W", "E"])

    text_areas_page.open()

    text_areas_page.write_messages_to_chapters()

    text_areas_page.scroll_to()

    text_areas_page.click_button()

    result_text = text_areas_page.result_text

    assert result_text == "{}\n{}\n{}".format(
        text_areas_page.value1.capitalize(),
        text_areas_page.value2.capitalize(),
        text_areas_page.value3.capitalize())


@pytest.mark.selenium
def test_confirm_alert(start_selenium_driver):
    confirm_alert_page = ConfirmAlertPage(start_selenium_driver)

    confirm_alert_page.open()

    confirm_alert_page.click_button()

    confirm_alert_page.confirm_alert()

    result_text = confirm_alert_page.result_text

    assert result_text == 'Ok'


@pytest.mark.selenium
def test_dismiss_alert(start_selenium_driver):
    confirm_alert_page = ConfirmAlertPage(start_selenium_driver)

    confirm_alert_page.open()

    confirm_alert_page.click_button()

    confirm_alert_page.dismiss_alert()

    result_text = confirm_alert_page.result_text

    assert result_text == 'Cancel'


@pytest.mark.selenium
def test_drag_and_drop_boxes(start_selenium_driver):
    result = 'Dropped!'

    drag_and_drop_boxes_page = DragAndDropBoxesPage(start_selenium_driver)

    drag_and_drop_boxes_page.open()

    drag_and_drop_boxes_page.drag_and_drop()

    result_text = drag_and_drop_boxes_page.result_text

    assert result_text == result


@pytest.mark.selenium
def test_drag_and_drop_image(start_selenium_driver):
    result = 'Dropped!'

    drag_and_drop_boxes_page = DragAndDropImagePage(start_selenium_driver)

    drag_and_drop_boxes_page.open()

    drag_and_drop_boxes_page.drag_and_drop()

    result_text = drag_and_drop_boxes_page.result_text

    assert result_text == result


@pytest.mark.selenium
def test_iframe_pop_up(start_selenium_driver):
    result = 'Correct!'
    iframe_pop_up_page = IframePopUp(start_selenium_driver)

    iframe_pop_up_page.open()

    iframe_pop_up_page.click_launch_popup()

    iframe_pop_up_page.switch_to_pop_up_frame()

    iframe_text_element = WebDriverWait(iframe_pop_up_page.get_browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'p[id="text-to-copy"]'))
    )

    coppied_text = iframe_pop_up_page.copy_text()

    iframe_pop_up_page.switch_to_default()

    iframe_pop_up_page.click_check_button()

    iframe_pop_up_page.paste_text_to_input(coppied_text)

    iframe_pop_up_page.click_submit_button()

    result_text = iframe_pop_up_page.result_text

    assert result_text == result


@pytest.mark.selenium
def test_pop_up_modal_page(start_selenium_driver):
    result = 'select me or not'

    pop_up_modal_page = PopUpModalPage(start_selenium_driver)

    pop_up_modal_page.open()

    pop_up_modal_page.click_launch_pop_up()

    pop_up_modal_page.click_checkbox()

    pop_up_modal_page.click_send_button()

    result_text = pop_up_modal_page.result_text

    assert result == result_text


@pytest.mark.selenium
def test_progress_bar(start_selenium_driver):
    progressBar = ProgressBarPage(start_selenium_driver)

    progressBar.open()

    progressBar.click_start()

    progressBar.wait_for_progress_bar_75()

    progressBar.click_stop()

    result_text = progressBar.result_text

    assert result_text <= 2

