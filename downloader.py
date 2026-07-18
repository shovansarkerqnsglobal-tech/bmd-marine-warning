from playwright.sync_api import sync_playwright
import os
from datetime import datetime

DOWNLOAD_DIR = "downloads"

def download_pdf():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
            "https://server8.bmd.gov.bd/bn/p/Marine-Warning",
            wait_until="networkidle",
            timeout=60000,
        )

        with page.expect_download() as download_info:
            page.get_by_role("button", name="Download").click()

        download = download_info.value

        today = datetime.now().strftime("%Y-%m-%d")

        filename = f"Marine_Warning_{today}.pdf"

        filepath = os.path.join(DOWNLOAD_DIR, filename)

        download.save_as(filepath)

        browser.close()

        return filepath


if _name_ == "_main_":
    print(download_pdf())
