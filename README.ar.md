<div dir="rtl">

# 🐻 BrowserBear

> مكتبة أتمتة المتصفح الخفية التي تتجاوز تقريبًا جميع أنظمة كشف الـ <bdi>bot</bdi>.

> [!WARNING]
> هذه المكتبة قيد التطوير المكثف. قد تتغير الـ <bdi>APIs</bdi> أو تتعطل أو تختفي دون إشعار مسبق. استخدمها بحذر!

---

## ✨ المميزات

| الميزة | الوصف |
|---------|-------------|
| 🌐 **Browser Automation** | تصفح وانقر واكتب واستخرج البيانات بأقل قدر من الكود |
| 🐍 **Pythonic API** | واجهة نظيفة وبديهية تبدو كـ <bdi>Python</bdi> الأصلية، لا <bdi>boilerplate</bdi> ممل |
| 🛡️ **Bypass Bot Detection** | تتحايل على أكثر أنظمة كشف الـ <bdi>bot</bdi> تطورًا بشكل تلقائي |
| ☁️ **Auto-Solve Cloudflare** | تعالج وتتجاوز تحديات <bdi>Cloudflare</bdi> تلقائيًا |
| 🔄 **Proxy Support** | دعم كامل للـ <bdi>proxy</bdi>، بما في ذلك <bdi>proxy</bdi> لكل صفحة لـ <bdi>multi-profile scraping</bdi> |
| 🎭 **Playwright-like Syntax** | صياغة مألوفة وقوية، مبنية على نسخة مُعدَّلة من <bdi>Patchright</bdi> |
| ⚡ **Safe Concurrency** | طرق <bdi>scraping</bdi> متزامنة آمنة بحيث لا تتداخل الـ <bdi>sessions</bdi> مع بعضها |
| 🌑 **Shadow DOM Access** | وصول كامل لعناصر الـ <bdi>Shadow DOM</bdi> لاستخراج البيانات من مكونات الويب الحديثة |
| 🚀 **المزيد من المميزات قادمة!** | قيد التطوير النشط مع إمكانيات جديدة في الطريق |

---

## 🎯 عرض توضيحي

---

### اختبار Pixelscan
`example/bot_detection/pixelscan.py`

https://github.com/user-attachments/assets/c9ef2920-1cd3-472d-8127-4822f8f7fb54




### عرض Turnstile
`example/cloudflare/turnstile_demo.py`

https://github.com/user-attachments/assets/0e38a64a-26ac-4113-bb88-49c11a4d6550




### Ahrefs AI humanizer
استخراج النص المُحوَّل من أداة <bdi>Ahrefs AI Humanizer</bdi> التي تحوّل المحتوى المُولَّد بالذكاء الاصطناعي إلى نص طبيعي يشبه كتابة الإنسان.
`example/cloudflare/ahrefs_ai_humanizer.py`

https://github.com/user-attachments/assets/493b8020-5ebc-4f0e-8128-613eed7f10b8


### 🤖 النقر التلقائي على التحديات
مثال يوضح كيف يكتشف <bdi>BrowserBear</bdi> وينقر تلقائيًا على مربعات الاختيار الخاصة بتحديات <bdi>Cloudflare</bdi>.
`example/cloudflare/ahrefs_ai_humanizer.py`

https://github.com/user-attachments/assets/2588b496-8cf8-40c1-9f7e-aca1b84c1e6e


---

## 📦 التثبيت

### 🚀 1 — باستخدام `uv` *(موصى به)*

```bash
uv init                  # 🏗️ ابدأ مشروعًا جديدًا
uv add browserBear       # 📥 أضف BrowserBear كـ dependency
```

### 🐌 2 — باستخدام `pip`

```bash
pip install browserBear
```

---

## 🚀 البداية السريعة

```python
import asyncio
from browserBear.browsers import StealthBrowser


async def main():
    # شغّل browser context جديد بصفحة واحدة
    b = await StealthBrowser.lunch_context()
    page = b.pages[0]

    # انتقل بأمان إلى الصفحة دون تشغيل إجراءات مكافحة الـ bot
    await StealthBrowser.safe_goto(b, "https://example.com")

    # انتظر ثانية
    await asyncio.sleep(1)

    # اطبع عنوان الصفحة (طريقة Playwright القياسية)
    title = await page.title()
    print(f"Page title: {title}")

    # أغلق الـ browser context وحرر الموارد
    await StealthBrowser.shutdown(b)


if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🧪 استكشف الأمثلة

هل تريد رؤية <bdi>BrowserBear</bdi> في العمل؟ انسخ الـ <bdi>repo</bdi> وشغّل الأمثلة:

```bash
# 📥 انسخ الـ repository
git clone https://github.com/dx-bear/browserbear.git
cd browserbear

# 📦 ثبّت الـ dependencies
uv sync

# ▶️ شغّل مثالًا
uv run examples/example_name.py
```

> [!TIP]
> تحقق من مجلد `examples/` للحصول على القائمة الكاملة للأمثلة المتاحة.

---

# 🐻 BrowserBear — التوثيق

<bdi>BrowserBear</bdi> هي مكتبة بسيطة وقوية لـ <bdi>web scraping</bdi> غير قابل للاكتشاف وأتمتة المتصفح. تعرض <bdi>class</bdi> واحدة فقط — `StealthBrowser` — مع مجموعة صغيرة ومحددة من الطرق.

```python
from browserBear.browsers import StealthBrowser
```

---

## 📋 نظرة عامة على الطرق

| الطريقة | النوع | الوصف |
|--------|------|-------------|
| `StealthBrowser.lunch_context()` | `async static` | شغّل <bdi>browser context</bdi> جديدًا مع صفحات |
| `StealthBrowser.safe_goto()` | `async classmethod` | انتقل بأمان إلى صفحة واحدة أو أكثر بشكل متزامن |
| `StealthBrowser.shutdown()` | `async classmethod` | أغلق <bdi>context</bdi> محدد أو جميع المتصفحات |
| `StealthBrowser.expect_and_solve_challenge()` | `async classmethod` | اكتشف وحل تحديات مكافحة الـ <bdi>bot</bdi> |
| `StealthBrowser.block_resources()` | `async classmethod` | احجب موارد الشبكة غير الضرورية |

---

## 🚀 `StealthBrowser.lunch_context()`

يشغّل <bdi>browser context</bdi> جديدًا بالـ <bdi>fingerprint</bdi> والإعداد المحدد. يُعيد `BrowserData` <bdi>dataclass</bdi> يحتوي على <bdi>instance</bdi> المتصفح والـ <bdi>context</bdi> وقائمة الصفحات.

```python
b = await StealthBrowser.lunch_context(
    fingerprint="1",
    pageCount=1,
    proxy=None,
    timezone_id=None,
    locale=None,
)
```

### المعاملات

| المعامل | النوع | القيمة الافتراضية | الوصف |
|-----------|------|---------|-------------|
| `fingerprint` | `str` | `"1"` | معرّف فريد لملف تعريف المتصفح والـ <bdi>fingerprint</bdi> كـ <bdi>(WebGL، Canvas، Audio،</bdi> إلخ.) |
| `pageCount` | `int` | `1` | عدد الصفحات التي يتم فتحها داخل الـ <bdi>context</bdi> |
| `proxy` | `dict \| None` | `None` | قاموس إعداد الـ <bdi>proxy</bdi> |
| `timezone_id` | `str \| None` | `None` | المنطقة الزمنية للـ <bdi>context</bdi> (مثلًا `"Europe/Berlin"`) — يجب أن تتطابق مع موقع الـ <bdi>proxy</bdi> |
| `locale` | `str \| None` | `None` | اللغة والمنطقة للـ <bdi>context</bdi> (مثلًا `"de-DE"`) — يجب أن تتطابق مع منطقة الـ <bdi>proxy</bdi> |

### القيمة المُعادة

<bdi>BrowserData dataclass</bdi> يحتوي على <bdi>instance</bdi> المتصفح والـ <bdi>context</bdi> والصفحات.

### أمثلة

**تشغيل أساسي — صفحة واحدة:**

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

**كيف يتحكم الـ <bdi>fingerprint</bdi> في عمليات المتصفح:**

كل قيمة <bdi>fingerprint</bdi> تُحدد عملية متصفح مستقلة. استدعاء `lunch_context()` بنفس الـ <bdi>fingerprint</bdi> يُعيد استخدام المتصفح الذي يعمل بالفعل ويفتح <bdi>context</bdi> معزولًا جديدًا بداخله — دون تشغيل عملية جديدة. أما <bdi>fingerprint</bdi> مختلف فيبدأ دائمًا عملية متصفح جديدة كليًا بهويتها الخاصة.

```python
# يشغّل عملية المتصفح #1
b1 = await StealthBrowser.lunch_context(fingerprint=1)

# يشغّل عملية متصفح منفصلة تمامًا #2
b2 = await StealthBrowser.lunch_context(fingerprint=2)

# يُعيد استخدام عملية المتصفح #1 — يفتح context معزولًا جديدًا بداخلها
b3 = await StealthBrowser.lunch_context(fingerprint=1)
```

**التشغيل مع <bdi>proxy</bdi> و<bdi>timezone</bdi> و<bdi>locale</bdi>:**

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

**<bdi>contexts</bdi> معزولة متعددة من نفس المتصفح:**

```python
# كلا الـ contexts يشتركان في نفس عملية المتصفح (fingerprint="99")
# لكنهما معزولان تمامًا عن بعضهما — proxies مختلفة، sessions مختلفة
b_us = await StealthBrowser.lunch_context(fingerprint="99", proxy=proxy_us)
b_de = await StealthBrowser.lunch_context(fingerprint="99", proxy=proxy_de)
```

> ⚠️ احرص دائمًا على مطابقة `timezone_id` و`locale` مع المنطقة الجغرافية للـ <bdi>proxy</bdi>. عدم التطابق إشارة شائعة لكشف الـ <bdi>bot</bdi>.

---

## 🌐 `StealthBrowser.safe_goto()`

ينتقل بأمان إلى جميع الصفحات داخل <bdi>BrowserData context</bdi> بشكل متزامن. إذا كان عدد الصفحات أكثر من عدد الـ <bdi>URLs</bdi>، يُعاد استخدام آخر <bdi>URL</bdi> لجميع الصفحات المتبقية. يتم التعامل مع أخطاء التنقل في الصفحات الفردية وعزلها حتى لا يوقف فشل واحد دفعة العمل بأكملها.

```python
await StealthBrowser.safe_goto(target, urls)
```

### المعاملات

| المعامل | النوع | القيمة الافتراضية | الوصف |
|-----------|------|---------|-------------|
| `target` | `BrowserData \| list[Page]` | — | كائن <bdi>browser data</bdi> أو قائمة صفحات للتنقل |
| `urls` | `str \| list[str]` | `"https://example.com"` | <bdi>URL</bdi> واحد أو قائمة <bdi>URLs</bdi> للتنقل إليها |

### القيمة المُعادة

`None`

### أمثلة

**التنقل إلى صفحة واحدة:**

```python
b = await StealthBrowser.lunch_context()
await StealthBrowser.safe_goto(b, "https://example.com")
```

**التنقل في جميع الصفحات إلى <bdi>URLs</bdi> مختلفة بشكل متزامن:**

```python
b = await StealthBrowser.lunch_context(pageCount=3)

# الصفحة 1 → Yelp، الصفحة 2 → ZoomInfo، الصفحة 3 → ZoomInfo (يُعاد استخدام آخر URL)
await StealthBrowser.safe_goto(b, ["https://yelp.com", "https://zoominfo.com"])
```

**التنقل في جميع الصفحات إلى نفس الـ <bdi>URL</bdi>:**

```python
b = await StealthBrowser.lunch_context(pageCount=5)
await StealthBrowser.safe_goto(b, "https://example.com")
```

**التنقل في صفحات محددة فقط — مرّر <bdi>slice</bdi> من الصفحات:**

يمكنك استهداف مجموعة فرعية من الصفحات بتمرير <bdi>slice</bdi> من `b.pages` بدلًا من الـ <bdi>context</bdi> الكامل. يتيح لك ذلك إرسال صفحات مختلفة إلى وجهات مختلفة بشكل مستقل.

```python
b = await StealthBrowser.lunch_context(pageCount=4)

# التنقل في أول صفحتين فقط بشكل متزامن
await StealthBrowser.safe_goto(b.pages[:2], [
    "https://example.com",
    "https://spyfu.com",
])

# التنقل في آخر صفحتين فقط بشكل متزامن
await StealthBrowser.safe_goto(b.pages[2:], [
    "https://ahrefs.com",
    "https://semrush.com",
])
```

**التنقل في صفحة واحدة محددة بالفهرس:**

```python
b = await StealthBrowser.lunch_context(pageCount=3)

# أرسل الصفحة 0 إلى موقع، والصفحة 2 إلى موقع آخر — بشكل مستقل
await StealthBrowser.safe_goto([b.pages[0]], "https://example.com")
await StealthBrowser.safe_goto([b.pages[2]], "https://spyfu.com")
```

---

## 🛑 `StealthBrowser.shutdown()`

يُنهي بأمان <bdi>browser context</bdi> محدد أو يُنفذ إغلاقًا شاملًا لجميع المتصفحات العاملة.

- **مع `target`** — يغلق الـ <bdi>context</bdi> المحدد. إذا لم تتبق <bdi>contexts</bdi> لذلك المتصفح، يتم إنهاء عملية المتصفح تلقائيًا.
- **بدون `target`** (`None`) — يغلق كل متصفح و<bdi>context</bdi> وصفحة، ويوقف <bdi>Playwright driver</bdi> كليًا.

```python
await StealthBrowser.shutdown(target=None)
```

### المعاملات

| المعامل | النوع | القيمة الافتراضية | الوصف |
|-----------|------|---------|-------------|
| `target` | `BrowserData \| None` | `None` | الـ <bdi>context</bdi> المحدد للإغلاق. مرّر `None` لإيقاف كل شيء. |

### القيمة المُعادة

`None`

### أمثلة

**إغلاق مستهدف — إغلاق <bdi>context</bdi> واحد:**

```python
b = await StealthBrowser.lunch_context(fingerprint="55")
# ... نفّذ العمل ...
await StealthBrowser.shutdown(b)
```

**إغلاق شامل — إغلاق جميع المتصفحات دفعة واحدة:**

```python
p = await StealthBrowser.lunch_context(fingerprint="1")
q = await StealthBrowser.lunch_context(fingerprint="2")
# ... نفّذ العمل ...
await StealthBrowser.shutdown()  # يغلق كل شيء
```

> 💡 يُفضَّل الإغلاق المستهدف خلال جلسات الـ <bdi>scraping</bdi> الطويلة لاستعادة الذاكرة تدريجيًا. استخدم الإغلاق الشامل فقط في نهاية السكريبت.

---

## 🛡️ `StealthBrowser.expect_and_solve_challenge()`

يكتشف ويحل تحديات مكافحة الـ <bdi>bot</bdi> (مثل <bdi>Cloudflare Turnstile</bdi>) التي تظهر على الصفحة. تتحقق الطريقة بشكل دوري ولا تتفاعل مع الصفحة إلا عند اكتشاف تحدٍّ فعليًا — مما يتجنب السلوك المثير للشك كالنقر المستمر أو الأتمتة العدوانية.

```python
await StealthBrowser.expect_and_solve_challenge(page, wait_seconds=5, max_attempts=10)
```

### المعاملات

| المعامل | النوع | القيمة الافتراضية | الوصف |
|-----------|------|---------|-------------|
| `page` | `Page` | — | كائن <bdi>Playwright Page</bdi> لمراقبته بحثًا عن التحديات |
| `wait_seconds` | `int` | `5` | ثوانٍ الانتظار بين كل فحص |
| `max_attempts` | `int` | `10` | الحد الأقصى لعدد محاولات الفحص قبل الاستسلام |

### القيمة المُعادة

`None`

### أمثلة

**الاستخدام الأساسي بعد التنقل:**

```python
import asyncio
from browserBear.browsers import StealthBrowser

async def main():
    b = await StealthBrowser.lunch_context()
    page = b.pages[0]

    await StealthBrowser.safe_goto(b, "https://protected-site.com")
    await asyncio.sleep(2)

    # انتظر حتى ~50 ثانية (10 محاولات × 5 ثوانٍ) لظهور تحدٍّ وحلّه
    await StealthBrowser.expect_and_solve_challenge(page)

    # استمر بشكل طبيعي بعد التعامل مع التحدي
    title = await page.title()
    print(f"Page title: {title}")

    await StealthBrowser.shutdown(b)

asyncio.run(main())
```

**توقيت مخصص — فحوصات أسرع ومحاولات أكثر:**

```python
await StealthBrowser.expect_and_solve_challenge(page, wait_seconds=2, max_attempts=20)
```

> 🧠 إذا لم يُعثر على تحدٍّ، تنتهي الطريقة بهدوء دون التفاعل مع الصفحة. آمنٌ استدعاؤها على أي صفحة بغض النظر عمّا إذا كان التحدي متوقعًا أم لا.

---

## 🚫 `StealthBrowser.block_resources()`

تحجب موارد الشبكة غير الضرورية — مثل الصور والخطوط وبعض الوسائط — لتقليل أوقات تحميل الصفحة وخفض خطر تشغيل أنظمة كشف الـ <bdi>bot</bdi>. يتم الحفاظ على الموارد المهمة اللازمة لوظائف الصفحة.

```python
await StealthBrowser.block_resources(page)
```

### المعاملات

| المعامل | النوع | الوصف |
|-----------|------|-------------|
| `page` | `Page` | كائن <bdi>Playwright Page</bdi> لتطبيق حجب الموارد عليه |

### القيمة المُعادة

`None`

### أمثلة

**حجب الموارد قبل التنقل:**

```python
from browserBear.browsers import StealthBrowser

async def main():
    b = await StealthBrowser.lunch_context()
    page = b.pages[0]

    # طبّق الحجب قبل التنقل لتحقيق أقصى تأثير
    await StealthBrowser.block_resources(page)
    await StealthBrowser.safe_goto(b, "https://example.com")

    content = await page.content()
    print(content)

    await StealthBrowser.shutdown(b)
```

**مع حل التحديات:**

```python
b = await StealthBrowser.lunch_context(fingerprint="77", proxy=proxy_config)
page = b.pages[0]

await StealthBrowser.block_resources(page)
await StealthBrowser.safe_goto(b, "https://protected-site.com")
await StealthBrowser.expect_and_solve_challenge(page)

# الصفحة الآن غير محجوبة والموارد مفلترة بالفعل
html = await page.inner_html("body")
```

> 🧠 استخدم `block_resources()` كإعداد افتراضي سريع وآمن. للفلترة المتقدمة (السماح أو الحجب لـ <bdi>domains</bdi> أو أنواع موارد محددة)، استخدم <bdi>Playwright API</bdi> الأصلي `page.route()` مباشرةً — كلا الأسلوبين متوافقان تمامًا.

---

## 📜 مثال كامل للسكريبت

سكريبت كامل شامل يجمع جميع طرق <bdi>BrowserBear</bdi> — <bdi>context</bdi> متعدد الصفحات، حجب الموارد، التنقل الآمن، حل التحديات، واستخراج البيانات من صفحات محددة.

```python
import asyncio
from browserBear.browsers import StealthBrowser


proxy_config = {
    "server": "123.45.67.89:8080",
    "username": "user",
    "password": "pass",
}


async def scrape(b, page, url: str) -> str:
    """استخرج البيانات من صفحة واحدة وأعد عنوانها."""
    await StealthBrowser.block_resources(page)
    await StealthBrowser.safe_goto([page], url)
    await StealthBrowser.expect_and_solve_challenge(page, wait_seconds=3, max_attempts=8)
    title = await page.title()
    return title


async def main():
    # شغّل متصفحًا بـ 4 صفحات وproxy ومنطقة زمنية ولغة متطابقة
    b = await StealthBrowser.lunch_context(
        fingerprint="10",
        pageCount=4,
        proxy=proxy_config,
        timezone_id="America/New_York",
        locale="en-US",
    )

    # أرسل أول صفحتين إلى URLs مختلفة بشكل متزامن
    await StealthBrowser.safe_goto(b.pages[:2], [
        "https://example.com",
        "https://spyfu.com",
    ])

    # أرسل آخر صفحتين إلى URLs مختلفة بشكل متزامن
    await StealthBrowser.safe_goto(b.pages[2:], [
        "https://ahrefs.com",
        "https://semrush.com",
    ])

    # استخرج البيانات من الصفحات الأربع بشكل متزامن
    results = await asyncio.gather(
        scrape(b, b.pages[0], "https://example.com"),
        scrape(b, b.pages[1], "https://spyfu.com"),
        scrape(b, b.pages[2], "https://ahrefs.com"),
        scrape(b, b.pages[3], "https://semrush.com"),
    )

    for title in results:
        print(f"Title: {title}")

    # أغلق هذا الـ context؛ تُغلق عملية المتصفح تلقائيًا
    # لأنه لا توجد contexts أخرى تستخدم fingerprint "10"
    await StealthBrowser.shutdown(b)

    # شغّل متصفحًا ثانيًا منفصلًا كليًا بـ fingerprint مختلف
    c = await StealthBrowser.lunch_context(fingerprint="20")
    page = c.pages[0]

    await StealthBrowser.block_resources(page)
    await StealthBrowser.safe_goto(c, "https://protected-site.com")
    await StealthBrowser.expect_and_solve_challenge(page)

    # استخدم Playwright API الأصلي لبقية العمل — توافق كامل
    await page.wait_for_load_state("networkidle")
    html = await page.inner_html("body")
    print(html[:500])

    # إغلاق شامل — يغلق كل شيء المتبقي
    await StealthBrowser.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
```

---

## 📚 المزيد من المميزات والشروحات

المزيد من المميزات والشروحات قادمة قريبًا.

يمكنك معرفة المزيد بمراجعة مجلد الأمثلة في الـ <bdi>repository</bdi>:

```bash
انسخ الـ repo
شغّل: example/<example_script.py>
```

---

## 🚀 المميزات القادمة

- 🔄 تغيير الـ <bdi>fingerprint</bdi> لكل <bdi>context</bdi>
- ⚡ <bdi>Lite Browser</bdi> للـ <bdi>scraping</bdi> فائق السرعة
- 🌐 وضع <bdi>HTTP-only</bdi> للـ <bdi>scraping</bdi> (دون الحاجة لمتصفح)
- 🔒 أدوات <bdi>concurrency</bdi> آمنة لسير عمل متعدد الـ <bdi>sessions</bdi>
- 🌑 مساعدات <bdi>Shadow DOM</bdi> مدمجة لمكونات الويب الحديثة

---

## ⭐ الدعم

إذا وجدت <bdi>BrowserBear</bdi> مفيدًا، فكّر في إعطاء الـ <bdi>repository</bdi> نجمة لدعم التطوير والتحديثات المستقبلية.

---

## 🤝 المساهمة

لا نقبل المساهمات البرمجية المباشرة في الوقت الحالي. إذا وجدت خطأً أو لديك طلب ميزة، يرجى تقديم <bdi>issue</bdi> 🐛.

---

## 📜 الرخصة

هذا المشروع مرخص بموجب [Apache 2.0 License](LICENSE) — راجع ملف <bdi>LICENSE</bdi> للتفاصيل.

---

<p align="center">
  مبني بـ 🐻 من قِبل <a href="https://github.com/dx-bear">dx-bear</a>
</p>

</div>