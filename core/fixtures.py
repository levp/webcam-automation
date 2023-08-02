from os import path

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

VIDEO_FILE = "./assets/video.y4m"


@pytest.fixture(scope="session")
def driver() -> WebDriver:
    video_file_path = path.abspath(VIDEO_FILE)
    if not path.exists(video_file_path):
        raise FileNotFoundError(
            f"Video file for mocking webcam not found: {video_file_path}"
        )

    options = webdriver.Options()
    options.add_argument("--use-fake-device-for-media-stream")
    options.add_argument(f"--use-file-for-fake-video-capture={video_file_path}")

    driver = WebDriver(options=options)

    yield driver
