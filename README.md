# 🐻 BrowserBear

> Stealth browser automation library that bypasses nearly all bot detection systems.

> [!WARNING]
> This library is under heavy development. APIs may change, break, or disappear without notice. Use with caution!

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🌐 **Browser Automation** | Navigate, click, type, and scrape with minimal code |
| 🐍 **Pythonic API** | Clean, intuitive interface that feels like Python, not boilerplate |
| 🛡️ **Bypass Bot Detection** | Evades the most sophisticated bot detection systems out of the box |
| ☁️ **Auto-Solve Cloudflare** | Automatically handles and bypasses Cloudflare challenges |
| 🔄 **Proxy Support** | Full proxy integration, including proxy-per-page for multi-profile scraping |
| 🎭 **Playwright-like Syntax** | Familiar and powerful syntax, built with a patched version of Patchright |
| ⚡ **Safe Concurrency** | Concurrent-ready scraping methods so sessions never interfere with each other |
| 🌑 **Shadow DOM Access** | Full access to shadow DOM elements for scraping modern web components |
| 🚀 **More features coming soon!** | Actively under development with new capabilities on the way |

---


## 🎯 Showcase

---

### Pixelscan Test
`example/bot_detection/pixelscan.py`

https://github.com/user-attachments/assets/c9ef2920-1cd3-472d-8127-4822f8f7fb54




### Turnstile demo
`example/cloudflare/turnstile_demo.py`

https://github.com/user-attachments/assets/0e38a64a-26ac-4113-bb88-49c11a4d6550




### Ahrefs AI humanizer
Scrape humanized text from the Ahrefs AI Humanizer tool that converts AI-generated content into natural, human-like text.
`example/cloudflare/ahrefs_ai_humanizer.py`

https://github.com/user-attachments/assets/493b8020-5ebc-4f0e-8128-613eed7f10b8


### 🤖 Automatic Challenge Clicking
Example showing how BrowserBear automatically detects and clicks Cloudflare challenge checkboxes.
`example/cloudflare/ahrefs_ai_humanizer.py`

https://github.com/user-attachments/assets/2588b496-8cf8-40c1-9f7e-aca1b84c1e6e


---

## 📦 Installation

### 🚀 1 — Using `uv` *(recommended)*

```bash
uv init                  # 🏗️ Start a new project
uv add browserBear       # 📥 Add BrowserBear as a dependency
```

### 🐌 2 — Using `pip`

```bash
pip install browserBear
```

---

## 🚀 Quick Start

```python
import asyncio
from browserBear.browsers import StealthBrowser


async def main():
    # Launch a new browser context with one page
    b = await StealthBrowser.lunch_context()
    page = b.pages[0]

    # Safely navigate to a page, without triggering anti-bot measures
    await StealthBrowser.safe_goto(b, "https://example.com")

    # Wait a second
    await asyncio.sleep(1)

    # Print page title (standard Playwright method)
    title = await page.title()
    print(f"Page title: {title}")

    # Close the browser context and free resources
    await StealthBrowser.shutdown(b)


if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🧪 Explore the Examples

Want to see BrowserBear in action? Clone the repo and run the examples:

```bash
# 📥 Clone the repository
git clone https://github.com/dx-bear/browserbear.git
cd browserbear

# 📦 Install dependencies
uv sync

# ▶️ Run an example
uv run examples/example_name.py
```

> [!TIP]
> Check the `examples/` directory for a full list of available examples.

---

# 🐻 BrowserBear — Documentation

BrowserBear is a minimal yet powerful library for undetectable web scraping and browser automation. It exposes a single class — `StealthBrowser` — with a small, focused set of methods.

```python
from browserBear.browsers import StealthBrowser
```

---

## 📋 Method Overview

| Method | Type | Description |
|--------|------|-------------|
| `StealthBrowser.lunch_context()` | `async static` | Launch a new browser context with pages |
| `StealthBrowser.safe_goto()` | `async classmethod` | Safely navigate one or more pages concurrently |
| `StealthBrowser.shutdown()` | `async classmethod` | Close a specific context or all browsers |
| `StealthBrowser.expect_and_solve_challenge()` | `async classmethod` | Detect and solve anti-bot challenges |
| `StealthBrowser.block_resources()` | `async classmethod` | Block unnecessary network resources |

---

## 🚀 `StealthBrowser.lunch_context()`

Launches a new browser context with the specified fingerprint and configuration. Returns a `BrowserData` dataclass containing the browser instance, context, and list of pages.

```python
b = await StealthBrowser.lunch_context(
    fingerprint="1",
    pageCount=1,
    proxy=None,
    timezone_id=None,
    locale=None,
)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `fingerprint` | `str` | `"1"` | Unique identifier for the browser profile and fingerprint (WebGL, Canvas, Audio, etc.) |
| `pageCount` | `int` | `1` | Number of pages to open inside the context |
| `proxy` | `dict \| None` | `None` | Proxy configuration dictionary |
| `timezone_id` | `str \| None` | `None` | Timezone for the context (e.g. `"Europe/Berlin"`) — must match proxy location |
| `locale` | `str \| None` | `None` | Locale for the context (e.g. `"de-DE"`) — should match proxy region |

### Returns

A `BrowserData` dataclass with the browser instance, context, and pages.

### Examples

**Basic launch — single page:**

```python
import asyncio
from browserBear.browsers import StealthBrowser

async def main():
    b = await StealthBrowser.lunch_context()
    page = b.pages[0]
    print("Browser ready!")
    await StealthBrowser.shutdown(b)

asyncio.run(main())
```

**How fingerprint controls browser processes:**

Each fingerprint value maps to a distinct browser process. Calling `lunch_context()` with the same fingerprint reuses the already-running browser and opens a new isolated context inside it — no new process is launched. A different fingerprint always starts a brand-new browser process with its own identity.

```python
# Launches browser process #1
b1 = await StealthBrowser.lunch_context(fingerprint=1)

# Launches a completely separate browser process #2
b2 = await StealthBrowser.lunch_context(fingerprint=2)

# Reuses browser process #1 — opens a new isolated context inside it
b3 = await StealthBrowser.lunch_context(fingerprint=1)
```

**Launch with proxy, timezone, and locale:**

```python
proxy_config = {
    "server": "123.45.67.89:8080",
    "username": "user",
    "password": "pass"
}

b = await StealthBrowser.lunch_context(
    fingerprint="42",
    pageCount=2,
    proxy=proxy_config,
    timezone_id="Europe/Berlin",
    locale="de-DE"
)
```

**Multiple isolated contexts from the same browser:**

```python
# Both contexts share the same underlying browser process (fingerprint="99")
# but are fully isolated from each other — different proxies, different sessions
b_us = await StealthBrowser.lunch_context(fingerprint="99", proxy=proxy_us)
b_de = await StealthBrowser.lunch_context(fingerprint="99", proxy=proxy_de)
```

> ⚠️ Always match `timezone_id` and `locale` to your proxy's geographic region. A mismatch is a common bot detection signal.

---

## 🌐 `StealthBrowser.safe_goto()`

Safely navigates all pages inside a `BrowserData` context concurrently. If there are more pages than URLs, the last URL is reused for all remaining pages. Navigation errors on individual pages are caught and isolated so that one failure does not halt the entire batch.

```python
await StealthBrowser.safe_goto(target, urls)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `target` | `BrowserData \| list[Page]` | — | The browser data object (or list of pages) to navigate |
| `urls` | `str \| list[str]` | `"https://example.com"` | A single URL or list of URLs to navigate to |

### Returns

`None`

### Examples

**Navigate a single page:**

```python
b = await StealthBrowser.lunch_context()
await StealthBrowser.safe_goto(b, "https://example.com")
```

**Navigate all pages to different URLs concurrently:**

```python
b = await StealthBrowser.lunch_context(pageCount=3)

# Page 1 → Yelp, Page 2 → ZoomInfo, Page 3 → ZoomInfo (last URL reused)
await StealthBrowser.safe_goto(b, ["https://yelp.com", "https://zoominfo.com"])
```

**Navigate all pages to the same URL:**

```python
b = await StealthBrowser.lunch_context(pageCount=5)
await StealthBrowser.safe_goto(b, "https://example.com")
```

**Navigate only specific pages — pass a page slice:**

You can target a subset of pages by passing a slice of `b.pages` instead of the full context. This lets you send different pages to different destinations independently.

```python
b = await StealthBrowser.lunch_context(pageCount=4)

# Navigate only the first two pages concurrently
await StealthBrowser.safe_goto(b.pages[:2], [
    "https://example.com",
    "https://spyfu.com",
])

# Navigate only the last two pages concurrently
await StealthBrowser.safe_goto(b.pages[2:], [
    "https://ahrefs.com",
    "https://semrush.com",
])
```

**Navigate a single specific page by index:**

```python
b = await StealthBrowser.lunch_context(pageCount=3)

# Send only page 0 to one site, page 2 to another — independently
await StealthBrowser.safe_goto([b.pages[0]], "https://example.com")
await StealthBrowser.safe_goto([b.pages[2]], "https://spyfu.com")
```

---

## 🛑 `StealthBrowser.shutdown()`

Safely terminates a specific browser context or performs a complete global teardown of all running browsers.

- **With `target`** — closes the specific context. If no contexts remain for that browser, the browser process is also terminated automatically.
- **Without `target`** (`None`) — closes every browser, context, and page, and stops the Playwright driver entirely.

```python
await StealthBrowser.shutdown(target=None)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `target` | `BrowserData \| None` | `None` | The specific context to close. Pass `None` to shut down everything. |

### Returns

`None`

### Examples

**Targeted shutdown — close one context:**

```python
b = await StealthBrowser.lunch_context(fingerprint="55")
# ... do work ...
await StealthBrowser.shutdown(b)
```

**Global shutdown — close all browsers at once:**

```python
p = await StealthBrowser.lunch_context(fingerprint="1")
q = await StealthBrowser.lunch_context(fingerprint="2")
# ... do work ...
await StealthBrowser.shutdown()  # closes everything
```

> 💡 Prefer targeted shutdown during long scraping sessions to reclaim memory incrementally. Use global shutdown only at the very end of your script.

---

## 🛡️ `StealthBrowser.expect_and_solve_challenge()`

Detects and solves anti-bot challenges (such as Cloudflare Turnstile) that appear on a page. The method checks periodically and only interacts with the page when a challenge is actually detected — avoiding the suspicious behavior of constant clicking or aggressive automation.

```python
await StealthBrowser.expect_and_solve_challenge(page, wait_seconds=5, max_attempts=10)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | `Page` | — | The Playwright `Page` object to monitor for challenges |
| `wait_seconds` | `int` | `5` | Seconds to wait between each check |
| `max_attempts` | `int` | `10` | Maximum number of check attempts before giving up |

### Returns

`None`

### Examples

**Basic usage after navigation:**

```python
import asyncio
from browserBear.browsers import StealthBrowser

async def main():
    b = await StealthBrowser.lunch_context()
    page = b.pages[0]

    await StealthBrowser.safe_goto(b, "https://protected-site.com")
    await asyncio.sleep(2)

    # Wait up to ~50 seconds (10 attempts × 5s) for a challenge to appear and solve it
    await StealthBrowser.expect_and_solve_challenge(page)

    # Continue normally after the challenge is handled
    title = await page.title()
    print(f"Page title: {title}")

    await StealthBrowser.shutdown(b)

asyncio.run(main())
```

**Custom timing — faster checks, more attempts:**

```python
await StealthBrowser.expect_and_solve_challenge(page, wait_seconds=2, max_attempts=20)
```

> 🧠 If no challenge is found, the method exits quietly without interacting with the page. It is safe to call on any page regardless of whether a challenge is expected.

---

## 🚫 `StealthBrowser.block_resources()`

Blocks unnecessary network resources — such as images, fonts, and certain media files — to reduce page load times and lower the risk of triggering bot detection systems. Important resources required for page functionality are preserved.

```python
await StealthBrowser.block_resources(page)
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `page` | `Page` | The Playwright `Page` object to apply resource blocking to |

### Returns

`None`

### Examples

**Block resources before navigation:**

```python
from browserBear.browsers import StealthBrowser

async def main():
    b = await StealthBrowser.lunch_context()
    page = b.pages[0]

    # Apply blocking before navigating for maximum effect
    await StealthBrowser.block_resources(page)
    await StealthBrowser.safe_goto(b, "https://example.com")

    content = await page.content()
    print(content)

    await StealthBrowser.shutdown(b)
```

**Combined with challenge solving:**

```python
b = await StealthBrowser.lunch_context(fingerprint="77", proxy=proxy_config)
page = b.pages[0]

await StealthBrowser.block_resources(page)
await StealthBrowser.safe_goto(b, "https://protected-site.com")
await StealthBrowser.expect_and_solve_challenge(page)

# Page is now unblocked and resources are already filtered
html = await page.inner_html("body")
```

> 🧠 Use `block_resources()` as a quick, safe default. For advanced filtering (allow/block specific domains or resource types), use Playwright's native `page.route()` API directly — both approaches are fully compatible.

---

## 📜 Full Script Example

A complete end-to-end script combining all BrowserBear methods — multi-page context, resource blocking, safe navigation, challenge solving, and targeted page scraping.

```python
import asyncio
from browserBear.browsers import StealthBrowser


proxy_config = {
    "server": "123.45.67.89:8080",
    "username": "user",
    "password": "pass",
}


async def scrape(b, page, url: str) -> str:
    """Scrape a single page and return the page title."""
    await StealthBrowser.block_resources(page)
    await StealthBrowser.safe_goto([page], url)
    await StealthBrowser.expect_and_solve_challenge(page, wait_seconds=3, max_attempts=8)
    title = await page.title()
    return title


async def main():
    # Launch a browser with 4 pages, a proxy, and matching timezone/locale
    b = await StealthBrowser.lunch_context(
        fingerprint="10",
        pageCount=4,
        proxy=proxy_config,
        timezone_id="America/New_York",
        locale="en-US",
    )

    # Send the first two pages to different URLs concurrently
    await StealthBrowser.safe_goto(b.pages[:2], [
        "https://example.com",
        "https://spyfu.com",
    ])

    # Send the last two pages to different URLs concurrently
    await StealthBrowser.safe_goto(b.pages[2:], [
        "https://ahrefs.com",
        "https://semrush.com",
    ])

    # Scrape all four pages concurrently
    results = await asyncio.gather(
        scrape(b, b.pages[0], "https://example.com"),
        scrape(b, b.pages[1], "https://spyfu.com"),
        scrape(b, b.pages[2], "https://ahrefs.com"),
        scrape(b, b.pages[3], "https://semrush.com"),
    )

    for title in results:
        print(f"Title: {title}")

    # Shut down this context; the browser process closes automatically
    # because no other contexts are using fingerprint "10"
    await StealthBrowser.shutdown(b)

    # Launch a second, completely separate browser with a different fingerprint
    c = await StealthBrowser.lunch_context(fingerprint="20")
    page = c.pages[0]

    await StealthBrowser.block_resources(page)
    await StealthBrowser.safe_goto(c, "https://protected-site.com")
    await StealthBrowser.expect_and_solve_challenge(page)

    # Use Playwright's native API for the rest — full compatibility
    await page.wait_for_load_state("networkidle")
    html = await page.inner_html("body")
    print(html[:500])

    # Global shutdown — closes everything remaining
    await StealthBrowser.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
```

---

## 📚 More Features & Tutorials

More features and tutorials are coming soon.

You can learn more by checking the example folder in the repository:

```bash
clone the repo
run: example/<example_script.py>
```

---

## 🚀 Upcoming Features

-   🔄 Change fingerprint per context
-   ⚡ Lite Browser for ultra-fast scraping
-   🌐 HTTP-only scraping mode (no browser required)
-   🔒 Safe concurrency utilities for multi-session workflows
-   🌑 Built-in Shadow DOM helpers for modern web components

---

## ⭐ Support

If you find BrowserBear useful, consider giving the repository a star to support development and future updates.

---

## 🤝 Contributing

We are not accepting direct code contributions at this time. If you find a bug or have a feature request, please submit an issue 🐛.

---

## 📜 License

This project is licensed under the [Apache 2.0 License](LICENSE) — see the LICENSE file for details.

---

<p align="center">
  Built with 🐻 by <a href="https://github.com/dx-bear">dx-bear</a>
</p>
