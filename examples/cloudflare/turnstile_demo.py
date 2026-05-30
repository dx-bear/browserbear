import asyncio
from browserBear.browsers import StealthBrowser


async def main():

    # Launch a new browser context with one page
    b = await StealthBrowser.lunch_context()
    page = b.pages[0]

    # Safely navigate to a page, without triggering anti-bot measures
    await StealthBrowser.safe_goto(b, "https://2captcha.com/demo/cloudflare-turnstile")

    # Wait a second
    await asyncio.sleep(5)

    await StealthBrowser.expect_and_solve_challenge(page, wait_seconds=5, max_attempts=10)

    # Save full screenshot of the page
    await page.screenshot(path="screenshot.png", full_page=True)

    # Close the browser context and free resources
    await StealthBrowser.shutdown(b)


if __name__ == "__main__":
    asyncio.run(main())