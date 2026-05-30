import asyncio
from browserBear.browsers import StealthBrowser


async def main():

    
    # Start new browser with new fingerprint and connect to it
    # The browser might take less than a second to warm up.
    # warm up process is very important to avoid anti-bot measures, as it mimics human behavior.
    b = await StealthBrowser.lunch_context()
    page = b.pages[0]

    # safly navigate to a page, without triggering anti-bot measures
    await StealthBrowser.safe_goto(page, urls="https://pixelscan.net/bot-check")

    # wait a second
    await asyncio.sleep(5)

    
    # save full screenshot of the page
    await page.screenshot(path="screenshot.png", full_page=True)

    # disconnect and close the browser
    await StealthBrowser.shutdown()

if __name__ == "__main__":
    asyncio.run(main())