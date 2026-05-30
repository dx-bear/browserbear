



import asyncio
from browserBear.browsers import StealthBrowser


async def main():

    # Start new browser with new fingerprint and connect to it
    # The browser might take less than a second to warm up.
    # warm up process is very important to avoid anti-bot measures, as it mimics human behavior.
    b = await StealthBrowser.lunch_context()
    page = b.pages[0]
    # block resources to speed up the page load
    # We blocked the exact resources that are causing the most bot detection.
    await StealthBrowser.block_resources(page)

    # safly navigate to a page, without triggering anti-bot measures
    await StealthBrowser.safe_goto(page,"https://www.crunchbase.com/organization/medium")

    # wait a second, increase this if you want to see the page before solving the challenge
    await asyncio.sleep(5)

    # most of the time the challenge is solved by now, but if you want to be sure, you can use the expect_and_solve_challenge method.
    await StealthBrowser.expect_and_solve_challenge(page, wait_seconds=5, max_attempts=10)

    # get page content
    content = await page.content()
    print(content[:500])  # print first 500 characters of the page content
    

    # disconnect and close the browser
    await StealthBrowser.shutdown()

if __name__ == "__main__":
    asyncio.run(main())