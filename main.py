import asyncio
from browserBear.browsers import StealthBrowser


async def main():

    # Start new browser with new fingerprint and connect to it
    # The browser might take less than a second to warm up.
    # warm up process is very important to avoid anti-bot measures, as it mimics human behavior.
    page = await StealthBrowser.connect()

    # safly navigate to a page, without triggering anti-bot measures
    await page.safe_goto("https://example.com")

    # wait a second
    await asyncio.sleep(1)

    # print page title
    title = await page.title()
    print(f"Page title: {title}")

    # safly clean page in the background
    await page.clean()

    # disconnect and close the browser
    await StealthBrowser.shutdown_all()

if __name__ == "__main__":
    asyncio.run(main())