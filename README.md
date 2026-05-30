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

https://github.com/user-attachments/assets/9e55e843-bece-4b46-97a2-766925cdb9e7



### Turnstile demo
`example/cloudflare/turnstile_demo.py`

https://github.com/user-attachments/assets/60c6699c-f348-4df2-ae5d-7ab1e4bde3ee



### Ahrefs AI humanizer
Scrape humanized text from the Ahrefs AI Humanizer tool that converts AI-generated content into natural, human-like text.
`example/cloudflare/ahrefs_ai_humanizer.py`

https://github.com/user-attachments/assets/5e89e2f5-dbb3-4580-b08f-8bfd4bd0dff1




<<<<<<< HEAD

=======
>>>>>>> 2616bcb (Enhance BrowserBear functionality and examples)
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
    await StealthBrowser.safe_goto(page, "https://example.com")

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

<<<<<<< HEAD
BrowserBear is a minimal yet powerful library for undetectable web scraping and browser automation. Its main goal is to provide the essential tools you need for most websites while hiding the complex parts behind simple and clean methods.

Most stealth browsers and undetectable frameworks still trigger bot detection when making unsafe actions or using poorly configured proxies. BrowserBear provides abstracted methods that are carefully tuned to reduce detection and improve automation stability.

For example, BrowserBear automatically performs a browser **warm-up** when creating a new context. This step is very important for bypassing bot detection because many anti-bot systems monitor browser startup behavior, fingerprint consistency, and proxy handshakes.

🛡️ BrowserBear also includes safer navigation methods. The standard `goto()` method used in many automation libraries can be detectable on protected websites. Even popular stealth frameworks such as SeleniumBase may still trigger anti-bot systems in some cases.

Instead, BrowserBear provides a safer alternative called `safe_goto()`, designed to reduce suspicious browser behavior and avoid triggering protection systems.

⚡ The library focuses on:

-   Safer browser automation
-   Human-like browsing behavior
-   Better proxy handling
-   Reduced bot detection triggers
-   Simple and developer-friendly APIs

Below you will find the full documentation explaining all BrowserBear class methods and features.

----------
## 🧭 Import Browser
Right now, only `StealthBrowser` is available.

However, the roadmap includes adding more browser types, including a **Lite Browser** designed for ultra-fast scraping and lightweight automation.
=======
BrowserBear is a minimal yet powerful library for undetectable web scraping and browser automation. It exposes a single class — `StealthBrowser` — with a small, focused set of methods.
>>>>>>> 2616bcb (Enhance BrowserBear functionality and examples)

```python
from browserBear.browsers import StealthBrowser
```

<<<<<<< HEAD
----------

## 🚀 Create Browser

To create a new browser instance, BrowserBear provides the `connect()` method.

When called for the first time, it will:

-   Launch a new browser
-   Create an isolated browser context
-   Open a new page automatically

```python
page = await StealthBrowser.connect()

```

----------

## ⚙️ `connect()` Arguments

### 🧬 `fingerprint`

```python
fingerprint: str = "1"

```

Every browser instance can use a different fingerprint. This includes properties such as:

-   WebGL
-   Canvas
-   Audio
-   Browser characteristics
-   And more

BrowserBear heavily relies on a patched Chrome build powered by CloakBrowser.

For more information, check the CloakBrowser repository.

> ✨ **Feature Coming Soon** — Soon, BrowserBear will support changing fingerprints per browser context, giving you even more isolation and flexibility.

**Example:**

```python
await StealthBrowser.connect(fingerprint=1)  # Browser with fingerprint 1
await StealthBrowser.connect(fingerprint=2)  # Different browser with another fingerprint

```

The fingerprint also acts as a browser profile ID.

----------

### 🌍 `proxy`

```python
proxy: Any | None = None

```

You can configure a proxy when creating the browser first time, also you can create context with different proxy and timezone.

**Example proxy configuration:**

```python
proxyConfig = {
    "server": "ip:port",
    "username": "username",
    "password": "password"
}

```

**Example usage:**

```python
page = await StealthBrowser.connect(
    fingerprint=123,
    proxy=proxyConfig
)

```

----------

### 🕒 `timezone_id`

```python
timezone_id: Any | None = None

```

```python
'Europe/Berlin'

```

> ⚠️ It is very important to match your timezone with your proxy location. A misconfigured timezone can easily trigger bot detection systems.

----------

### 🌐 `locale`

```python
locale: Any | None = None

```

```python
'de-DE'

```

The locale should also match the proxy region for better consistency.

----------

### ✨ Upcoming `connect()` Features

BrowserBear will soon support:

-   Automatic locale detection
-   Automatic timezone configuration
-   Proxy-based context setup during warm-up

This helps create more realistic browser sessions automatically.

----------

## 🧩 Creating Isolated Contexts

You can also create isolated pages from an already running browser using different settings. Make sure to connect to the browser with the same fingerprint/id.

```python
page1 = await StealthBrowser.connect(
    fingerprint=123,
    proxy=proxyConfigUS
)

page2 = await StealthBrowser.connect(
    fingerprint=123,
    proxy=proxyConfigDE
)

```

> ⚡ **Important:** This creates a new isolated browser context, not a completely new browser process.

Each context is fully isolated while being much faster to create because the main browser is already running.

This allows BrowserBear to create new pages and contexts very quickly without reloading the full browser every time.

----------

## 📄 Page

A `page` created using `StealthBrowser.connect()` behaves exactly like a Playwright page. It includes all standard methods and properties from Playwright, so you can use the official Playwright documentation as a reference for full functionality.

### ⚠️ Differences from Playwright

BrowserBear extends the standard Playwright page with only two additional methods:

----------

#### 🛡️ `page.safe_goto()`

A safer navigation method designed to reduce bot detection risks.

```python
await page.safe_goto("http://example.com")

```

Unlike the standard `goto()`, this method is optimized to behave more naturally and avoid triggering anti-bot systems during navigation.

----------

#### 🧹 `page.clean()`

A fast and lightweight method to close both the page and its browser context in the background.

```python
await page.clean()

```

This is faster than manually closing each resource and helps ensure clean teardown of sessions.

----------

### ⏳ Page Load Handling

`safe_goto()` automatically waits for the page to load, but you can still use Playwright's built-in waiting strategies for more control.

**Example — Navigation + Load States:**

```python
await page.safe_goto("http://example.com")

# Wait for DOM to be fully loaded
await page.wait_for_load_state("domcontentloaded")

# Wait for all resources (images, stylesheets, etc.) to finish loading
await page.wait_for_load_state("load")

# Wait until network is idle (no requests for at least 500ms)
await page.wait_for_load_state("networkidle")

```

----------

### 🔗 Full Playwright Compatibility

All methods and properties available in Playwright's `page` object work seamlessly with the `StealthBrowser.connect()` page.

This means you can:

-   Use standard Playwright automation patterns
-   Mix BrowserBear methods with Playwright methods
-   Rely on existing Playwright knowledge without rewriting your logic

BrowserBear simply adds safer navigation and faster cleanup on top of the existing Playwright API.

----------

## 🚫 Blocking Resources

If you want to block network resources using Playwright, that is completely fine and fully supported. It will work as expected, and you can still use Playwright's native network control features.

However, some resources (like certain scripts, fonts, or media files) can trigger bot detection systems when loaded. For that reason, BrowserBear provides a safer and simpler alternative.

### 🛡️ `StealthBrowser.block_resources(page)`

This method automatically blocks common resource types that may increase bot detection risk while keeping the page functional.

```python
await StealthBrowser.block_resources(page)

```

**⚡ What it does:**

This method safely blocks or filters resources such as:

-   Images
-   Fonts
-   Certain media files
-   Other non-essential assets that may trigger detection systems

At the same time, it preserves important resources needed for normal page functionality and stability.

**🔧 Why use it?**

Using manual Playwright blocking rules gives you full control, but it can be complex and error-prone.

`block_resources()` is designed to:

-   Reduce bot detection risk
-   Simplify setup
-   Apply safe default rules automatically
-   Keep automation stable across different websites

**🧩 Playwright Flexibility:**

You are still free to use Playwright's native request interception and routing if you want full customization.

This means you can:

-   Define your own blocking rules
-   Allow or block specific domains
-   Fine-tune performance and privacy behavior

> 🧠 **Recommendation:** Use `StealthBrowser.block_resources(page)` for quick and safe setup. Use Playwright's native API when you need advanced or custom filtering logic.

BrowserBear gives you both simplicity and full control depending on your needs.

----------

## 🔓 Solving Cloudflare Challenges

In most cases, if you are using a high-quality proxy and the safe methods provided by BrowserBear, you will rarely encounter CAPTCHAs or anti-bot challenges.

However, some websites enforce a mandatory challenge for new visitors who do not have existing cookies for the target domain. In these cases, BrowserBear provides an automated method to detect and handle challenges safely.

### 🛡️ `StealthBrowser.expect_and_solve_challenge()`

This method automatically searches for and attempts to solve challenge boxes when they appear.

```python
await StealthBrowser.expect_and_solve_challenge(page, wait_seconds=5, max_attempts=10)

```

**⚙️ How it works:**

Unlike many stealth frameworks that aggressively try to interact with the page, this method is more controlled and safe:

-   It checks the page every few seconds
-   It only attempts interaction if a challenge is detected
-   If no challenge is found, it simply continues execution
-   It avoids unnecessary clicks or suspicious behavior

**📌 Parameters:**

`page`

—

The active browser page where the challenge may exist

`wait_seconds`

`5`

How long to wait between each check

`max_attempts`

`10`

Maximum number of attempts before stopping

**💡 Example usage:**

```python
page = await StealthBrowser.connect()

await page.safe_goto(url)

await asyncio.sleep(2)

await StealthBrowser.expect_and_solve_challenge(page)

```

> 🧠 **Key idea:** This method is designed to be passive when no challenge exists, active only when necessary, and safer than constant interaction or aggressive solving attempts. It helps maintain a more human-like browsing pattern while still handling forced anti-bot challenges when they appear.

----------

## 🛑 Shutdown the Browser

For better resource management, it is important to properly close the browser after you are done.

When you create multiple contexts or pages using BrowserBear, you should shut them down to free memory and system resources.

### 🧹 `StealthBrowser.shutdown_browser()`

You can close a specific browser instance using its fingerprint.

```python
await StealthBrowser.shutdown_browser(fingerprint: str)

```

**📌 Example:**

If you created a browser like this:

```python
page = await StealthBrowser.connect(fingerprint=55)

```

You can shut it down using:

```python
await StealthBrowser.shutdown_browser(55)

```

This will properly close all related contexts and resources tied to that fingerprint.

----------

### 💣 Shutdown All Browsers

You can also close every running browser instance at once.

```python
await StealthBrowser.shutdown_all()

```

This is useful when:

-   Ending a scraping session
-   Cleaning up multiple active contexts
-   Resetting the environment completely

----------
=======
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
    "server": "http://123.45.67.89:8080",
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
>>>>>>> 2616bcb (Enhance BrowserBear functionality and examples)

## 📚 More Features & Tutorials

More features and tutorials are coming soon.

You can learn more by checking the example folder in the repository:

```bash
clone the repo
run: example/<example_script.py>
<<<<<<< HEAD

```

----------
=======
```

---
>>>>>>> 2616bcb (Enhance BrowserBear functionality and examples)

## 🚀 Upcoming Features

-   🔄 Change fingerprint per context
-   ⚡ Lite Browser for ultra-fast scraping
-   🌐 HTTP-only scraping mode (no browser required)
<<<<<<< HEAD

----------
=======
-   🔒 Safe concurrency utilities for multi-session workflows
-   🌑 Built-in Shadow DOM helpers for modern web components

---
>>>>>>> 2616bcb (Enhance BrowserBear functionality and examples)

## ⭐ Support

If you find BrowserBear useful, consider giving the repository a star to support development and future updates.
<<<<<<< HEAD
---




=======

---

>>>>>>> 2616bcb (Enhance BrowserBear functionality and examples)
## 🤝 Contributing

We are not accepting direct code contributions at this time. If you find a bug or have a feature request, please submit an issue 🐛.

---

## 📜 License

This project is licensed under the [Apache 2.0 License](LICENSE) — see the LICENSE file for details.

---

<p align="center">
  Built with 🐻 by <a href="https://github.com/dx-bear">dx-bear</a>
</p>