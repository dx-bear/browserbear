import asyncio
from browserBear.browsers import StealthBrowser


async def main():

    # Launch a new browser context with one page
    b = await StealthBrowser.lunch_context()
    page = b.pages[0]

    # Safely navigate to a page, without triggering anti-bot measures
    await StealthBrowser.safe_goto(b, "https://example.com")

    # Wait a second, increase this if you want to see the page before solving the challenge
    await asyncio.sleep(5)

    # Save full screenshot of the page
    await page.screenshot(path="screenshot.png", full_page=True)

    # Close the browser context and free resources
    await StealthBrowser.shutdown(b)


if __name__ == "__main__":
    asyncio.run(main())