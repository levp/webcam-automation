import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="session")
def driver() -> WebDriver:
    video_file = "/home/levi/Downloads/video.y4m"

    options = webdriver.Options()
    options.add_argument("--use-fake-device-for-media-stream")
    options.add_argument(f"--use-file-for-fake-video-capture={video_file}")

    driver = WebDriver(options=options)

    yield driver
