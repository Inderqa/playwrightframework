# import time
#
# import openpyxl
# from pytest_playwright.pytest_playwright import context, browser
# import pytest
# from openpyxl import load_workbook
#
#
# @pytest.mark.usefixtures("start_browser_with_tracing")
# def test_basic_launch(start_browser_with_tracing):
#     page = start_browser_with_tracing
#     page.goto("https://rahulshettyacademy.com/loginpagePractise")
#     page.get_by_label("Username:").fill("rahulshettyacademy")
#     page.get_by_label("Password:").fill("learning")
#     page.get_by_role("combobox").select_option("teach")
#     page.get_by_role("checkbox",name="terms").click()
#     page.get_by_role("button",name="Sign In").click()
#     time.sleep(5)
#
# # def test_iframe(playwright):
# #     browser= playwright.chromium.launch(headless=False)
# #     context=browser.new_context()
# #     page=context.new_page()
# #     page.goto("https://letcode.in/frame")
# #     main_frame_scroll = page.locator("#firstFr").scroll_into_view_if_needed()
# #     main_frame = page.frame_locator("#firstFr")
# #     nested_frame = main_frame.frame_locator("//iframe[@src='innerframe']")
# #     import pdb
# #     pdb.set_trace()
# #     nested_frame.get_by_label("text").fill("test")
# #     nested_frame.locator("//input[@name='email']").fill("test")
#
# # def test_invalid_login_validate_error_message(page:Page):
# #     page.goto("https://rahulshettyacademy.com/loginpagePractise")
# #     page.get_by_label("Username:").fill("rahulshettyacademy")
# #     page.get_by_label("Password:").fill("learning2")
# #     page.get_by_role("combobox").select_option("teach")
# #     page.get_by_role("checkbox",name="terms").click()
# #     page.get_by_role("button",name="Sign In").click()
# #     expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
# #
# # def test_handle_child_window(playwright):
# #     browser = playwright.chromium.launch(headless=False,slow_mo=2000)
# #     context = browser.new_context()
# #     page = context.new_page()
# #     page.goto("https://rahulshettyacademy.com/loginpagePractise")
# #     with context.expect_page() as new_page_info:
# #         page.locator("//a[@class='blinkingText']").click()
# #     child_page = new_page_info.value
# #     child_page.wait_for_load_state()
# #     print("Child Window Title:", child_page.title())
# #     page.bring_to_front()
# #     print("Parent Window Title:", page.title())
# #     browser.close()
#
# # def test_handle_child(playwright):
# #     browser = playwright.chromium.launch(headless=False,slow_mo=2000)
# #     context = browser.new_context()
# #     page = context.new_page()
# #     page.goto("https://rahulshettyacademy.com/loginpagePractise")
# #     with context.expect_page() as new_page_info:
# #         page.locator("//a[@class='blinkingText']").click()
# #     new_page = new_page_info.value
# #     expect(new_page.locator("//h1[contains(text(),'Documents request')]")).to_contain_text("Documents request")
# #     new_page.close()
#
#
#
# #
# # def test_handle_dropdown(page:Page):
# #     page.goto("https://rahulshettyacademy.com/angularpractice/shop")
# #     phoneProduct = page.locator("app-card").filter(has_text='Nokia Edge')
# #     phoneProduct.get_by_role('button').click()
# #     expect(page.locator("//a[contains(normalize-space(text()), 'Checkout')]")).to_be_visible()
# #     page.locator("//a[contains(normalize-space(text()), 'Checkout')]").click()
# #     expect(page.locator("//a[contains(text(),'Nokia Edge')]")).to_be_visible()
# #     expect(page.locator("//td[contains(normalize-space(@class),'col-sm-8')]")).to_have_count(1)
# #
# #
# # # In following test have window is maximized,scroll into view until locator is visible is used
# # def test_UIChecks(playwright):
# #     browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
# #     context = browser.new_context(no_viewport=True)
# #     page = context.new_page()
# #     page.goto("https://rahulshettyacademy.com/AutomationPractice")
# #     expect(page.locator("//input[@value='Hide']")).to_be_visible()
# #     page.locator("//input[@value='Show']").click()
# #     page.locator("//input[@placeholder='Hide/Show Example']").scroll_into_view_if_needed()
# #     expect(page.locator("//input[@placeholder='Hide/Show Example']")).to_be_visible()
# #     page.locator("//input[@value='Hide']").click()
# #     expect(page.locator("//input[@placeholder='Hide/Show Example']")).to_be_hidden()
# #
# # def test_handle_alert(playwright):
# #     browser = playwright.chromium.launch(headless=False, args=["--start-maximized"],slow_mo=2000)
# #     context = browser.new_context(no_viewport=True)
# #     page = context.new_page()
# #     page.goto("https://rahulshettyacademy.com/AutomationPractice")
# #     page.on("dialog",lambda dialog:dialog.accept()) ## Accept the dialog or click okay on alert
# #     page.get_by_role("button",name="Confirm").click()
# #     page.on("dialog", lambda dialog: dialog.dismiss()) ##Click cancel on alert
# #     page.get_by_role("button", name="Confirm").click()
#
# # def test_handle__multiple_alert(playwright):
# #     browser = playwright.chromium.launch(headless=False, args=["--start-maximized"],slow_mo=2000)
# #     context = browser.new_context(no_viewport=True)
# #     page = context.new_page()
# #     page.goto("https://letcode.in/alert")
# #     page.on("dialog",lambda dialog:dialog.accept()) ## Accept the dialog or click okay on alert
# #     page.locator("#accept").click()
# #     page.on("dialog", lambda dialog: dialog.dismiss()) ##Click cancel on alert
# #     page.locator("#confirm").click()
# #
# #     def handle_prompt(dialog):
# #         print(f"Alert Text: {dialog.message}")
# #         dialog.accept("John Doe")
# #     page.on("dialog", handle_prompt)
# #     page.locator("#prompt").click()
# #
# # def test_frames(playwright):
# #     browser = playwright.chromium.launch(headless=False, args=["--start-maximized"],slow_mo=2000)
# #     context = browser.new_context(no_viewport=True)
# #     page = context.new_page()
# #     page.goto("https://rahulshettyacademy.com/AutomationPractice")
# #     page.locator("#courses-iframe").scroll_into_view_if_needed()
# #     pageFrame = page.frame_locator("#courses-iframe")
# #     pageFrame.get_by_role("link",name="All Access plan")
# #     expect(pageFrame.locator("body")).to_contain_text(" Learn Earn & Shine")
# #     page.locator("#mousehover").hover()
# #
# # def test_handle_dynamic_Web_elements(playwright):
# #     browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
# #     context = browser.new_context(no_viewport=True)
# #     page = context.new_page()
# #     page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# #     columns =  page.locator("//th[@role='columnheader']").all()
# #     for index, column in enumerate(columns):
# #         if column.inner_text() == "Price":
# #            Pricecol = index
# #     rice_row = page.locator("//tbody//tr").filter(has_text="Rice")
# #     expect(rice_row.locator("td").nth(Pricecol)).to_contain_text("37")
#
#
# # def test_nested_iframe_pracs(playwright):
# #     browser = playwright.chromium.launch(headless=False, args=["--start-maximized"],slow_mo=2000)
# #     context = browser.new_context(no_viewport=True)
# #     page = context.new_page()
# #     page.goto("https://letcode.in/frame")
# #     page.locator("//iframe[@id='firstFr']").scroll_into_view_if_needed()
# #     main_ifm = page.frame_locator("//iframe[@id='firstFr']")
# #     inner_ifm = main_ifm.frame_locator("//iframe[@src='innerFrame']")
# #     inner_ifm.locator("//input[@name='email']").fill("test12")
#
# # def test_drag_drop(playwright):
# #     browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=2000)
# #     context = browser.new_context(no_viewport=True)
# #     page = context.new_page()
# #     page.goto("https://letcode.in/draggable")
# #     source = page.locator("#sample-box")
# #     # source.drag_to(source, target_position={"x": 200, "y": 100})
# #     bounding_box = source.bounding_box()  # Get element's position
# #     # Move to the center of the draggable element
# #     page.mouse.move(bounding_box["x"] + bounding_box["width"] / 2, bounding_box["y"] + bounding_box["height"] / 2)
# #     page.mouse.down()  # Click and hold
# #     # Move the element to a new position (adjust offset as needed)
# #     page.mouse.move(bounding_box["x"] + 200, bounding_box["y"] + 100)
# #     # Release the mouse after dragging
# #     page.mouse.up()
#
# # def test_slider(playwright):
# #     browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=2000)
# #     context = browser.new_context(no_viewport=True)
# #     page = context.new_page()
# #     page.goto("https://letcode.in/slider")
# #     slider = page.locator("//input[@id='generate']")
# #     slider.fill("50")
#
# # def test_child_window(playwright):
# #     browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=2000)
# #     context = browser.new_context(no_viewport=True)
# #     page = context.new_page()
# #     page.goto("https://letcode.in/windows")
# #     with context.expect_page() as new_page_info:
# #         page.locator("#home").click()
# #     child_window = new_page_info.value
# #     expect(child_window.locator("//p[normalize-space(text())='Practice test automation!']")).to_be_visible()
# #     child_window.close()
# #     page.bring_to_front()
# #     expect(page.locator("//h1[contains(text(),'Windows')]")).to_be_visible()
#
#
# def test_Read_Excel_Data():
#     book = openpyxl.load_workbook("/Users/inderpreetsingh/Downloads/mysheet.xlsx")
#     sheet = book.active
#     test_data = []
#     for row in sheet.iter_rows(min_row=2, max_col=3, values_only=True):
#         test_data.append((int(row[0]), row[1], row[2]))
#     return test_data
# #
# # @pytest.mark.parametrize('id, name, email', test_Read_Excel_Data())
# # def test_user_data(id, name, email):
# #     assert isinstance(id, str)
# #     assert isinstance(name, int)
# #     assert '@' in email
#
#
#
# # def test_pracs(playwright):
# #     browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=2000)
# #     context = browser.new_context(no_viewport=True)
# #     page = context.new_page()
# #     # page.goto("https://rahulshettyacademy.com/angularpractice/shop")
# #     # cards = page.locator("//div[contains(@class,'card h-100')]").element_handles()
# #     # for card in cards:
# #     #     title_text = card.query_selector("//h4[@class='card-title']//a").text_content()
# #     #     if "Samsung Note 8" in title_text:
# #     #         card.query_selector("//button[contains(text(),'Add')]").click()
# #     #
# #     # checkout_text = page.locator("//a[@class='nav-link btn btn-primary']").text_content()
# #     # import pdb
# #     # pdb.set_trace()
# #     # assert "1" in checkout_text.strip()
# #     page.goto("https://rahulshettyacademy.com/AutomationPractice")
# #     # page.on("dialog", lambda dialog:dialog.accept())
# #     # page.get_by_role("button",name="Confirm").click()
# #     # time.sleep(5)
# #     page.locator("//legend[contains(text(),'iFrame Example')]").scroll_into_view_if_needed()
# #     main_fr = page.frame_locator("#courses-iframe")
# #     # page.get_by_role("link",name="lifetime-access")
# #     all_frm = "//li[@class='current' and .//a[contains(text(),'All Access plan')]]"
# #     # page.locator(all_frm).scroll_into_view_if_needed()
# #     # main_fr.frame_locator(all_frm)
# #     # page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
# #     main_fr.get_by_role("link",name="All Access plan").click()