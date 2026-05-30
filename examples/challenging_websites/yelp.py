import asyncio
from browserBear.browsers import StealthBrowser


async def main():

    # Launch a new browser context with one page
    b = await StealthBrowser.lunch_context()
    page = b.pages[0]

    # Block resources to speed up the page load
    # We block the exact resources that cause the most bot detection
    await StealthBrowser.block_resources(page)

    # Safely navigate to a page, without triggering anti-bot measures
    await StealthBrowser.safe_goto(b, "https://www.yelp.com/search?find_desc=Plumbers&find_loc=San+Francisco%2C+CA")

    # Wait a second, increase this if you want to see the page before solving the challenge
    await asyncio.sleep(7)

    # Get page content
    content = await page.content()
    print(content[:500])  # print first 500 characters of the page content

    # Close the browser context and free resources
    await StealthBrowser.shutdown(b)


if __name__ == "__main__":
    asyncio.run(main())