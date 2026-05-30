import asyncio
import time
from browserBear.browsers import StealthBrowser


async def main():

    story_text = """
        Late one evening, Omar was walking home through the narrow streets of the old city when the power suddenly went out. The shops became dark, and the usual noise of traffic faded into silence. As he continued walking, he noticed a small bookstore with a single candle glowing inside.

        Curious, he stepped in. An old man sat behind the counter reading a worn-out novel. Without looking up, the man said, "People only come here when they are searching for something."

        Omar smiled awkwardly and began looking through the dusty shelves. Most of the books were old and damaged, but one caught his attention. It had no title on the cover. He opened it and found handwritten notes instead of printed text. The pages described moments from his own life, including memories he had never shared with anyone.

        Startled, Omar quickly closed the book. The old man finally looked up and said softly, "Some stories find their owners."

        When the city lights returned a few minutes later, Omar left the bookstore carrying the strange book under his arm, unsure whether he had discovered magic or simply lost his mind.
    """

    # Launch a new browser context with one page
    b = await StealthBrowser.lunch_context()
    page = b.pages[0]

    # Safely navigate to a page, without triggering anti-bot measures
    await StealthBrowser.safe_goto(b, "https://ahrefs.com/writing-tools/ai-humanizer")

    # Wait a second
    await asyncio.sleep(4)

    # Fill the text area with some text
    await page.locator("textarea").first.fill(story_text)
    await asyncio.sleep(2)
    await page.get_by_role("button", name="Humanize Text").click()

    await asyncio.sleep(7)

    await StealthBrowser.expect_and_solve_challenge(page, wait_seconds=7, max_attempts=10)

    locator = page.locator("p:has-text('New version:')")
    await locator.wait_for()

    full_text = await locator.text_content()

    if full_text and "New version:" in full_text:
        humanized_text = full_text.split("New version:")[1].strip()
    else:
        humanized_text = full_text.strip() if full_text else "No text found."

    print("Humanized Text:")
    print(humanized_text)

    # Close the browser context and free resources
    await StealthBrowser.shutdown(b)


if __name__ == "__main__":
    asyncio.run(main())