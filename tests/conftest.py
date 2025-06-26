import os

import pytest
from requests import session


@pytest.fixture(scope="session")
def user_credentialss(request):
    return request.param

@pytest.fixture(scope="function")
def start_browser(playwright):
    browser=playwright.chromium.launch(headless=False,args=["--disable-notifications"])
    context=browser.new_context()
    page=context.new_page()
    yield page
    browser.close()


@pytest.fixture(scope="function")
def start_browser_with_tracing(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield page

    # Stop and save tracing
    context.tracing.stop(path="trace.zip")
    browser.close()


def start_browser_with_traching_with_video(playwright, request):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir="videos/")  # 🎥 enable video
    context.tracing.start(screenshots=True, snapshots=True, sources=True)  # 🧩 enable tracing
    page = context.new_page()

    yield page

    # Stop tracing
    context.tracing.stop(path=f"traces/{request.node.name}_trace.zip")

    video_path = page.video.path()
    print(f"\n📹 Video saved at: {video_path}")

    context.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page") or item.funcargs.get("start_browser")
        if page:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            file_path = os.path.join(screenshot_dir, f"{item.name}.png")
            page.screenshot(path=file_path, full_page=True)
            print(f"\n Test failed. Screenshot saved at: {file_path}")