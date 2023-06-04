from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.zhipin.com/")
    
    _search = page.locator("#wrap > div.column-search-panel.search-panel-new > div > div.search-box > div.search-form > form > div.search-form-con > p > input")
    _search.click()
    _search.fill("前端开发工程师")
    _search.press("Enter")
    input('等待中...')

    # page.locator("#kw").click()
    # page.locator("#kw").fill("ai")
    # page.locator("#kw").press("Enter")
    # with page.expect_popup() as page1_info:
    #     page.get_by_role("link", name="ai-在线使用 - 国内版AI").click()
    # page1 = page1_info.value
    # page1.goto("https://www.gulingai.com/?s=baidu_bd2-wenzhang2&gnType=5&bd_vid=7120938849953622124")
    # page1.close()

    # # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
