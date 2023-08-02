from selenium.webdriver.chrome.webdriver import WebDriver


def test_webcam_site(driver: WebDriver) -> None:
    driver.get("http://localhost:3000")
    assert driver.title == "Webcam"
