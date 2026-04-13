# InstaMarathi Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a free, mobile-first Marathi website (`instamarathi.github.io`) that teaches people how to build a business running Instagram pages for local businesses.

**Architecture:** Static HTML site hosted on GitHub Pages. Single shared CSS stylesheet. No JavaScript frameworks. Each page follows a common HTML template with consistent navigation. Content written in Marathi-English mix, meta tags in English for SEO.

**Tech Stack:** HTML5, CSS3, GitHub Pages. Source content adapted from existing dental playbook (`/private/tmp/dentist/`) and parenting playbook (`/private/tmp/dentist/parenting-channel-playbook.json`, `/private/tmp/dentist/instagram-tutorial-marathi.md`).

**Source repo:** `instamarathi/instamarathi.github.io` on GitHub (already created, user has write access).

---

## Task 1: Site Skeleton — CSS, HTML Template, Directory Structure

**Files:**
- Create: `assets/css/style.css`
- Create: `index.html`
- Create: all directories (`shika/`, `tools/`, `tools/ai-content/`, `playbooks/`, `playbooks/dentist/`, `playbooks/parenting/`, `diy/`, `clients/`, `assets/css/`)

This task creates the mobile-first CSS and the homepage. All subsequent pages copy the HTML structure from `index.html`.

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p assets/css shika tools/ai-content playbooks/dentist playbooks/parenting diy clients
```

- [ ] **Step 2: Create `assets/css/style.css`**

Mobile-first, minimal CSS. Warm color palette inspired by the parenting playbook (earthy tones). Clean typography — system fonts with Noto Sans Devanagari for Marathi text.

```css
/* InstaMarathi — Mobile-first stylesheet */

@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap');

/* Reset */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* Base */
:root {
  --color-bg: #FDF8F3;
  --color-text: #2C2420;
  --color-text-light: #5C4F47;
  --color-accent: #D4915E;
  --color-accent-dark: #B87A4A;
  --color-green: #7B9E87;
  --color-gold: #C4A265;
  --color-surface: #FFFFFF;
  --color-border: #E8DDD4;
  --color-code-bg: #F5EDE3;
  --font-marathi: 'Noto Sans Devanagari', sans-serif;
  --font-english: 'Inter', sans-serif;
  --max-width: 720px;
  --spacing: 1.5rem;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-marathi);
  background: var(--color-bg);
  color: var(--color-text);
  line-height: 1.8;
  -webkit-font-smoothing: antialiased;
}

/* Typography */
h1, h2, h3, h4 {
  font-weight: 700;
  line-height: 1.3;
  margin-bottom: 0.75rem;
}

h1 { font-size: 1.75rem; }
h2 { font-size: 1.4rem; margin-top: 2rem; }
h3 { font-size: 1.15rem; margin-top: 1.5rem; }

p { margin-bottom: 1rem; }

a {
  color: var(--color-accent-dark);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 2px;
}

a:hover {
  color: var(--color-accent);
}

/* Layout */
.container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 1rem var(--spacing);
}

/* Navigation */
nav {
  background: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
  padding: 0.75rem var(--spacing);
  position: sticky;
  top: 0;
  z-index: 100;
}

nav .nav-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.5rem;
}

nav .logo {
  font-family: var(--font-english);
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--color-text);
  text-decoration: none;
}

nav .logo span {
  color: var(--color-accent);
}

nav .nav-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem;
  list-style: none;
}

nav .nav-links a {
  display: inline-block;
  padding: 0.3rem 0.6rem;
  font-size: 0.85rem;
  color: var(--color-text-light);
  text-decoration: none;
  border-radius: 4px;
}

nav .nav-links a:hover,
nav .nav-links a.active {
  background: var(--color-code-bg);
  color: var(--color-text);
}

/* Hero (homepage) */
.hero {
  text-align: center;
  padding: 3rem 0 2rem;
}

.hero h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.hero .subtitle {
  font-size: 1.1rem;
  color: var(--color-text-light);
  margin-bottom: 2rem;
}

/* Section cards (homepage) */
.section-cards {
  display: grid;
  gap: 1rem;
  margin: 2rem 0;
}

.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  padding: 1.25rem;
  text-decoration: none;
  color: var(--color-text);
  transition: border-color 0.2s;
}

.card:hover {
  border-color: var(--color-accent);
}

.card h3 {
  margin-top: 0;
  margin-bottom: 0.5rem;
}

.card p {
  color: var(--color-text-light);
  font-size: 0.95rem;
  margin-bottom: 0;
}

/* Content pages */
.page-header {
  padding: 2rem 0 1rem;
  border-bottom: 1px solid var(--color-border);
  margin-bottom: 2rem;
}

.page-header .breadcrumb {
  font-size: 0.85rem;
  color: var(--color-text-light);
  margin-bottom: 0.5rem;
}

.page-header .breadcrumb a {
  color: var(--color-text-light);
}

/* Exercise boxes */
.exercise {
  background: #EFF6F1;
  border-left: 4px solid var(--color-green);
  padding: 1rem 1.25rem;
  margin: 1.5rem 0;
  border-radius: 0 6px 6px 0;
}

.exercise h4 {
  color: var(--color-green);
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 0.95rem;
}

/* Prompt blocks */
.prompt-block {
  background: var(--color-code-bg);
  border: 1px solid var(--color-border);
  padding: 1rem 1.25rem;
  margin: 1rem 0;
  border-radius: 6px;
  font-family: var(--font-english);
  font-size: 0.9rem;
  line-height: 1.6;
  white-space: pre-wrap;
  word-break: break-word;
}

.prompt-block .label {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-text-light);
  margin-bottom: 0.5rem;
  display: block;
}

/* Tip / Warning boxes */
.tip {
  background: #FFF8EB;
  border-left: 4px solid var(--color-gold);
  padding: 1rem 1.25rem;
  margin: 1.5rem 0;
  border-radius: 0 6px 6px 0;
}

.warning {
  background: #FFF0F0;
  border-left: 4px solid #C45B5B;
  padding: 1rem 1.25rem;
  margin: 1.5rem 0;
  border-radius: 0 6px 6px 0;
}

/* Tables */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  font-size: 0.9rem;
}

th, td {
  padding: 0.6rem 0.75rem;
  text-align: left;
  border-bottom: 1px solid var(--color-border);
}

th {
  background: var(--color-code-bg);
  font-weight: 600;
}

/* Lists */
ul, ol {
  margin: 1rem 0;
  padding-left: 1.5rem;
}

li {
  margin-bottom: 0.5rem;
}

/* Next page navigation */
.page-nav {
  display: flex;
  justify-content: space-between;
  margin-top: 3rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--color-border);
  gap: 1rem;
}

.page-nav a {
  display: block;
  padding: 0.75rem 1rem;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 6px;
  text-decoration: none;
  font-size: 0.9rem;
  flex: 1;
}

.page-nav a:hover {
  border-color: var(--color-accent);
}

.page-nav .next {
  text-align: right;
}

/* Footer */
footer {
  margin-top: 3rem;
  padding: 1.5rem var(--spacing);
  text-align: center;
  font-size: 0.85rem;
  color: var(--color-text-light);
  border-top: 1px solid var(--color-border);
}

/* Desktop */
@media (min-width: 768px) {
  html { font-size: 17px; }
  h1 { font-size: 2rem; }
  .hero h1 { font-size: 2.5rem; }
  .section-cards { grid-template-columns: 1fr 1fr; }
}
```

- [ ] **Step 3: Create `index.html` (homepage)**

This is the template all other pages follow. The homepage has the hero section + section cards.

```html
<!DOCTYPE html>
<html lang="mr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>InstaMarathi — Instagram Business Guide in Marathi</title>
  <meta name="description" content="Learn how to build a business running Instagram pages for local businesses. Free guide in Marathi.">
  <meta name="keywords" content="instagram marketing marathi, instagram business guide, social media manager marathi, instagram content creator">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <nav>
    <div class="nav-inner">
      <a href="/" class="logo">Insta<span>Marathi</span></a>
      <ul class="nav-links">
        <li><a href="/shika/business-kya-aahe.html">शिका</a></li>
        <li><a href="/tools/canva.html">Tools</a></li>
        <li><a href="/playbooks/">Playbooks</a></li>
        <li><a href="/diy/niche-research.html">स्वतः बनवा</a></li>
        <li><a href="/clients/kuthe-shodhayche.html">Clients</a></li>
      </ul>
    </div>
  </nav>

  <div class="container">
    <div class="hero">
      <h1>Instagram वरून Business चालवायचं शिका — दुसऱ्यांसाठी</h1>
      <p class="subtitle">Local businesses साठी Instagram manage करा. पैसे कमवा. सगळं मराठीत शिका.</p>
    </div>

    <div class="section-cards">
      <a href="/shika/business-kya-aahe.html" class="card">
        <h3>शिका — हा Business काय आहे?</h3>
        <p>Instagram management म्हणजे काय, कसं approach करायचं, trust कसं build करायचं, realistic expectations.</p>
      </a>

      <a href="/tools/canva.html" class="card">
        <h3>Tools — तुमची Toolkit</h3>
        <p>Canva, AI images, CapCut, voiceover, ChatGPT/Claude — hands-on exercises सहित सगळे tools शिका.</p>
      </a>

      <a href="/playbooks/" class="card">
        <h3>Playbooks — Ready-Made Content Plans</h3>
        <p>Dentist, parenting आणि इतर niches साठी तयार playbooks. Copy करा, customize करा, deliver करा.</p>
      </a>

      <a href="/diy/niche-research.html" class="card">
        <h3>स्वतः बनवा — कोणत्याही Business साठी</h3>
        <p>कोणत्याही niche साठी स्वतःचा playbook बनवायला शिका — research ते delivery.</p>
      </a>

      <a href="/clients/kuthe-shodhayche.html" class="card">
        <h3>Clients मिळवा — Business कसं वाढवायचं</h3>
        <p>Clients कुठे शोधायचे, pitch कसं करायचं, pricing, पहिले 30 दिवस, growth.</p>
      </a>
    </div>
  </div>

  <footer>
    <p>InstaMarathi — मराठीत Instagram Business शिका. सगळं free, सगळं open.</p>
  </footer>
</body>
</html>
```

- [ ] **Step 4: Verify locally**

```bash
cd /private/tmp/instamarathi && python3 -m http.server 8000
```

Open `http://localhost:8000` in browser. Verify:
- Page loads, fonts render (Marathi + English)
- Navigation bar is sticky and wraps on mobile
- Cards display in grid
- Responsive: test at 375px and 768px+ widths

- [ ] **Step 5: Commit**

```bash
git add assets/css/style.css index.html
git commit -m "feat: add site skeleton — CSS, homepage, directory structure"
```

---

## Task 2: Section 2 — शिका (Learn the Business)

**Files:**
- Create: `shika/business-kya-aahe.html`
- Create: `shika/approach-kasa-karaycha.html`
- Create: `shika/trust-build-kara.html`
- Create: `shika/common-questions.html`

All pages follow the HTML template from `index.html` — same `<nav>`, same `<footer>`, content in `<div class="container">` with a `.page-header` (breadcrumb + title).

- [ ] **Step 1: Create `shika/business-kya-aahe.html`**

Content covers:
- What an Instagram manager actually does (in Marathi)
- 4 avenues: full page management, content creation only, strategy/consulting, campaign-based
- For each avenue: काय करायचं, कोणासाठी योग्य, किती वेळ लागतो, potential earnings
- Table comparing the 4 types
- "तुमच्यासाठी कोणता type?" — simple decision framework

Page structure:
```html
<!-- Same <head> and <nav> as index.html, update <title> and meta -->
<title>हा Business काय आहे? — InstaMarathi</title>
<meta name="description" content="What is Instagram management as a business? Learn the different types of Instagram services you can offer to local businesses.">

<!-- Content -->
<div class="container">
  <div class="page-header">
    <div class="breadcrumb"><a href="/">Home</a> / <a href="/shika/business-kya-aahe.html">शिका</a></div>
    <h1>हा Business काय आहे?</h1>
    <p>Instagram management — दुसऱ्यांचं Instagram चालवून पैसे कमवणं</p>
  </div>

  <!-- Full Marathi-English content here covering all 4 avenues -->
  <!-- Comparison table -->
  <!-- Decision framework -->

  <div class="page-nav">
    <div></div>
    <a href="/shika/approach-kasa-karaycha.html" class="next">पुढे: Business ला कसं approach करायचं →</a>
  </div>
</div>
```

Write the full Marathi-English content for this page covering all points from spec section 2.1.

- [ ] **Step 2: Create `shika/approach-kasa-karaycha.html`**

Content covers:
- How to identify businesses that need Instagram help (signs: no page, dead page, bad content)
- Cold approach vs warm introduction — pros/cons table
- What to say: 30-second pitch script in Marathi
- What NOT to say: common mistakes
- How to pitch with a sample/demo
- Common reactions and how to handle each
- Realistic success rates: "10 ला approach केलं तर 1-2 होतील"
- Nav: prev = business-kya-aahe, next = trust-build-kara

Write full Marathi-English content covering all points from spec section 2.2.

- [ ] **Step 3: Create `shika/trust-build-kara.html`**

Content covers:
- Why this is a responsibility, not just a gig
- Brand voice: it's their voice, not yours — examples of how to adapt
- Communication cadence: daily/weekly check-ins, approval flow before posting
- What to do when something goes wrong (wrong post, negative comment, client unhappy)
- Confidentiality: you'll see their DMs, business numbers, customer info
- Being reliable: deadlines, consistency, never ghost a client
- Nav: prev = approach, next = common-questions

Write full Marathi-English content covering all points from spec section 2.3.

- [ ] **Step 4: Create `shika/common-questions.html`**

Content covers (FAQ format — each question as an h2, answer below):
- "किती पैसे मिळतात?" — pricing tiers: beginner (2-5K/month per client), intermediate (5-15K), experienced (15K+)
- "मला design येत नाही" — you don't need to, Canva + AI tools do the work (link to tools section)
- "client ने नाही म्हटलं तर?" — it's normal, numbers game, keep going
- "किती clients handle करता येतात?" — solo: 3-5 clients comfortably, more = quality drops
- "contract लागतं का?" — yes, even simple WhatsApp agreement helps, template provided
- "results नाही आले तर?" — what you control (content quality, consistency) vs what you don't (algorithm, market)
- Nav: prev = trust-build-kara, next = tools/canva (start tools section)

Write full Marathi-English content covering all points from spec section 2.4.

- [ ] **Step 5: Verify locally**

Open all 4 pages in browser. Check:
- Navigation works, breadcrumbs correct
- Page-nav prev/next links work
- Content renders well on mobile width (375px)
- Marathi text readable, line-height comfortable

- [ ] **Step 6: Commit**

```bash
git add shika/
git commit -m "feat: add शिका section — 4 pages on Instagram management business"
```

---

## Task 3: Section 3.1–3.5 — Tools (Design, Images, Video, Audio)

**Files:**
- Create: `tools/canva.html`
- Create: `tools/ai-images.html`
- Create: `tools/ai-images-advanced.html`
- Create: `tools/capcut.html`
- Create: `tools/voiceover.html`

**Source material to adapt:**
- `/private/tmp/dentist/instagram-tutorial-marathi.md` — Bhag 5 (Canva), Bhag 7 (CapCut/video/voiceover), Bhag 10 (tools list)
- `/private/tmp/dentist/brand/production-guide.md` — voiceover recording tips, Higgsfield prompting guide

- [ ] **Step 1: Create `tools/canva.html`**

Content (hands-on, exercise-driven):
- Canva म्हणजे काय — one paragraph intro
- Step-by-step: sign up → search "Instagram Carousel" → pick template
- Walkthrough: building a 5-slide carousel for a dentist client
  - Slide 1: Hook text, dark background, large font
  - Slide 2-3: Content slides, lighter background
  - Slide 4: CTA slide
  - Slide 5: Branding slide with handle
- Nuances: font sizing for mobile (minimum 24pt), brand colors, template consistency
- Exercise 1 (`.exercise` box): "हा text वापरून 5-slide carousel बनवा: [exact text given for a dental tip]"
- Exercise 2: "तोच content — वेगळा template वापरून बनवा. फरक बघा."
- Free vs Pro: what you get free is enough to start
- Tips: download as PNG, select all pages
- Adapt content from instagram-tutorial-marathi.md Bhag 5, reframed for client work
- Nav: prev = common-questions (shika section), next = ai-images

- [ ] **Step 2: Create `tools/ai-images.html`**

Content (deep dive on prompting, step-by-step):
- AI images म्हणजे काय — one paragraph, no jargon
- Gemini (Google) — how to access (free, browser-based)
- Step-by-step prompt improvement progression:
  - Level 1: Bad prompt — `"dentist clinic"` → explain why result is generic
  - Level 2: Better — `"A warm, modern dental clinic in Pune, India. Natural lighting, clean white walls, a friendly dentist talking to a patient. Photorealistic."` → explain what changed
  - Level 3: Good — add style/mood/composition: `"...Shot from the patient's perspective. Warm afternoon light. Soft focus on background. The dentist is smiling and explaining something with a dental model. Indian setting, modern but not sterile."` → explain each addition
  - Level 4: Instagram-specific — `"...Square format (1:1 ratio). Leave space in the top-right for text overlay. Warm color grading."` → explain why format matters
- Each level shown as a `.prompt-block` with a `.label` ("Level 1: Basic Prompt")
- Exercise 1: "Level 1 चा prompt Gemini मध्ये टाका. Result बघा. मग Level 4 चा prompt टाका. फरक बघा."
- Prompt templates per niche (each in a `.prompt-block`):
  - Dental: clinic, procedure, patient smile
  - Gym: workout, equipment, transformation
  - Salon: styling, products, interior
  - Cafe: food, ambiance, latte art
- Common prompting mistakes (table: mistake → why it fails → fix)
- Bing Image Creator as free alternative — how to access, same exercises
- Exercise 2: "तुमच्या आवडीच्या niche साठी 3 different images generate करा — Level 4 prompts वापरून"
- Nav: prev = canva, next = ai-images-advanced

- [ ] **Step 3: Create `tools/ai-images-advanced.html`**

Content:
- Consistency problem: 4 posts that look like they belong to the same brand
- Technique: style anchoring — include the same style descriptors in every prompt
- Example: "warm earthy tones, soft natural light, Indian setting, clean minimal composition" as a consistent suffix
- Marathi/Hindi text in AI images — current limitations, workaround (generate image + add text in Canva)
- Creating a series: "Week 1 Dental Tips" — 4 images with same visual style
  - Show 4 prompts that share a style block but vary in subject
- Exercise: "एका salon साठी 4 Instagram posts च्या images बनवा — सगळे consistent style मध्ये. Style block same ठेवा, subject बदला."
- Nav: prev = ai-images, next = capcut

- [ ] **Step 4: Create `tools/capcut.html`**

Content (adapt from instagram-tutorial-marathi.md Bhag 7 + production-guide.md):
- CapCut म्हणजे काय — free video editor, phone वर
- Step-by-step: download → new project → add images → set duration → add text → add music → export
- Each step with clear description of what to tap/select
- Duration: 5-8 seconds per image for a 30-sec reel
- Text animation: how to add text that appears on each slide
- Transitions: simple cuts vs fancy transitions (simple is better)
- Music: CapCut free library, search "gentle" or "acoustic"
- Volume: music should be 20-30% volume if there's voiceover
- Exercise 1: "Canva मध्ये बनवलेल्या carousel च्या images ला 30-second reel मध्ये convert करा"
- Exercise 2: "Background music add करा. Volume adjust करा. Export करा."
- Export settings: 1080p, high quality
- Nav: prev = ai-images-advanced, next = voiceover

- [ ] **Step 5: Create `tools/voiceover.html`**

Content (adapt from production-guide.md voiceover section):
- DIY voiceover — तुमच्या phone वर record करा
- Environment: शांत room, fan/AC बंद, closet trick (कपड्यांच्या closet मध्ये echo कमी)
- Recording tips: हळू बोला, हसून बोला, 10-15 second segments
- Exercise 1: "हा script वाचा आणि record करा:" — 30-second voiceover script given (dental tip about brushing)
- AI Voice — ElevenLabs:
  - Step-by-step: sign up → select voice → paste text → generate
  - Free tier: 10 min/month (enough for 5-10 reels)
  - Murf.ai as alternative (Indian voices)
- Exercise 2: "Exercise 1 चाच script ElevenLabs मध्ये टाका. AI voice ने बनवा. तुमच्या voice शी compare करा."
- Decision guide: when to use own voice vs AI vs no voice
  - Own voice: more authentic, clients prefer it
  - AI voice: consistent quality, faster, good for scale
  - No voice: text-on-screen reels work well too
- Nav: prev = capcut, next = ai-content/research

- [ ] **Step 6: Verify locally**

Open all 5 pages. Check:
- Exercise boxes render with green left border
- Prompt blocks render with code-style background
- Navigation chain works: canva → ai-images → ai-images-advanced → capcut → voiceover
- Content readable on mobile

- [ ] **Step 7: Commit**

```bash
git add tools/canva.html tools/ai-images.html tools/ai-images-advanced.html tools/capcut.html tools/voiceover.html
git commit -m "feat: add tools section — Canva, AI images, CapCut, voiceover pages"
```

---

## Task 4: Section 3.6 — AI Content (Script Writing & Validation)

**Files:**
- Create: `tools/ai-content/research.html`
- Create: `tools/ai-content/content-calendar.html`
- Create: `tools/ai-content/script-carousel.html`
- Create: `tools/ai-content/script-reel.html`
- Create: `tools/ai-content/captions-hashtags.html`
- Create: `tools/ai-content/validation.html`
- Create: `tools/ai-content/iteration.html`

This is the meatiest section. Each page builds on the previous. Prompts are in English (inside `.prompt-block`), explanations in Marathi.

- [ ] **Step 1: Create `tools/ai-content/research.html`**

Content:
- नवीन niche कसं research करायचं — LLM वापरून
- Step-by-step prompt progression:
  - Basic: `"Tell me about the dental industry"` → too vague, explain why
  - Better: `"I'm creating Instagram content for a dentist in Pune, India. Tell me: What are the top 10 questions patients commonly ask before visiting? What are their biggest fears? What makes someone choose one dentist over another?"` → targeted, specific
  - Best: add context about the Instagram format: `"...I need to create carousel posts and short reels. For each question, suggest an emotional hook that would stop someone from scrolling."` → production-ready output
- Each prompt in a `.prompt-block` with before/after explanation in Marathi
- How to validate research: Google reviews वाचा, actual business owner ला विचारा, Quora/YouTube check करा
- Exercise: "हा prompt टाका, पण 'dentist' ऐवजी 'gym trainer' टाका. Result compare करा. कोणते insights same आहेत? कोणते different?"
- Nav: prev = voiceover, next = content-calendar

- [ ] **Step 2: Create `tools/ai-content/content-calendar.html`**

Content:
- Content calendar म्हणजे काय — date, format, topic, hook चं plan
- Prompt progression:
  - Vague: `"Create a content calendar for a salon"` → output is generic
  - Specific: `"Create a 2-week Instagram content calendar for a women's beauty salon in Nashik, India. The salon specializes in bridal makeup and hair treatments. Target audience: women 22-35, getting married in the next 6 months. Format the calendar as a table with columns: Day, Format (carousel/reel/story), Topic, Hook (first line that stops scrolling), CTA. Post 3 times per week (Mon, Wed, Fri)."` → usable output
- Show the expected output format as a table
- Exercise: "Salon ऐवजी तुमच्या आवडीचा niche टाका. 2-week calendar generate करा. Table format मध्ये आला का check करा."
- Nav: prev = research, next = script-carousel

- [ ] **Step 3: Create `tools/ai-content/script-carousel.html`**

Content:
- Carousel script workflow: brief → first draft → refine → final
- Step 1 prompt — give context: `"You are writing an Instagram carousel for a dental clinic page. Brand voice: friendly, reassuring, educational. Not preachy. The audience is adults 25-45 in urban India who are nervous about dental procedures. Topic: 'Root canals are not scary.' Write a 5-slide carousel script. For each slide, give: the exact text to display (keep it short — max 2 sentences per slide), and a note about the visual/background."` (`.prompt-block`)
- Show a sample output
- Step 2 prompt — refine: `"The hook on slide 1 is weak. Give me 5 alternative hooks for slide 1 that would stop someone from scrolling. Each should be under 10 words and create curiosity or challenge an assumption."` (`.prompt-block`)
- Step 3 prompt — polish: `"Rewrite the carousel with hook #3. Make slide 4 more emotionally reassuring — the reader should feel 'oh, that's not bad at all.' Keep the CTA on slide 5 warm, not pushy."` (`.prompt-block`)
- Exercise: "या exact prompts वापरून dental carousel script बनवा. प्रत्येक step नंतर output वाचा — काय बदललं ते लक्षात घ्या."
- Nav: prev = content-calendar, next = script-reel

- [ ] **Step 4: Create `tools/ai-content/script-reel.html`**

Content:
- Reel structure: hook (first 3 seconds) → problem → solution → CTA
- Different from carousel: time-based, not slide-based
- Prompt templates for 3 formats:
  - 30-second reel: `"Write a 30-second Instagram reel script for a gym trainer's page. Topic: '3 mistakes beginners make in the gym.' Format: Hook (0-3 sec) — one shocking statement. Problem 1 (3-10 sec). Problem 2 (10-18 sec). Problem 3 (18-25 sec). CTA (25-30 sec). For each section, write: the voiceover text (conversational Hindi-English), and a one-line visual description."` (`.prompt-block`)
  - 60-second reel: similar structure, more depth per point
  - 90-second reel: story format, more emotional
- Voiceover script vs text-on-screen: different prompt approaches
  - Voiceover: conversational, complete sentences
  - Text-on-screen: punchy, short phrases, each 2-3 seconds
- Exercise: "Gym niche साठी 30-second reel script बनवा. मग तोच topic 60-second format मध्ये expand करा."
- Nav: prev = script-carousel, next = captions-hashtags

- [ ] **Step 5: Create `tools/ai-content/captions-hashtags.html`**

Content:
- Caption formula: hook line → value/story → CTA → hashtags
- Prompt: `"Write an Instagram caption for this carousel: [paste carousel topic]. Caption structure: Line 1: Hook (make them stop scrolling). Lines 2-5: Expand with 3-4 value points using → arrows. Last line: CTA (warm, not pushy — ask them to share with someone who needs this). Keep it under 150 words. Tone: friendly, conversational, Hindi-English mix."` (`.prompt-block`)
- Hashtag generation prompt: `"Generate 8 Instagram hashtags for a dental education post about root canals in India. Mix: 1 large (1M+ posts), 3 medium (100K-1M posts), 3 small (10K-100K posts), 1 branded. Format as a single line separated by spaces."` (`.prompt-block`)
- Tips: rotate hashtags across posts, don't copy same set every time
- Exercise: "तुमच्या carousel script साठी caption + hashtags generate करा. Hook line strong आहे का check करा."
- Nav: prev = script-reel, next = validation

- [ ] **Step 6: Create `tools/ai-content/validation.html`**

Content:
- LLM हा तुमचा writer पण आहे आणि editor पण
- 5 validation prompts (each in a `.prompt-block`):
  1. Hook strength: `"Review this carousel script. Rate the hook (slide 1) on a scale of 1-5 for: (a) Would it stop someone from scrolling? (b) Does it create curiosity? (c) Is it specific enough? Give a rating and one sentence explaining each score. If any score is below 4, suggest an improved version."`
  2. Brand voice: `"Here are the brand voice rules for this page: [paste rules]. Review this script against these rules. Point out any line that breaks a rule. Suggest a fix for each violation."`
  3. Audience check: `"The target audience is [describe audience]. Read this script from their perspective. What would feel relatable? What would feel off or preachy? Be specific — quote the exact lines."`
  4. Comparison: `"Here are 3 versions of slide 1. Which is the strongest hook? Rank them 1-3 and explain your reasoning in one sentence each."`
  5. Factual accuracy: `"Is this content medically/factually accurate? Flag anything a [dentist] would correct. This is critical — we're posting on a professional's behalf."`
- `.warning` box: "Factual validation खूप important आहे. तुम्ही एका professional च्या नावाने post करताय. चुकीची माहिती = client चं reputation damage."
- Exercise: "तुम्ही script-carousel page वर बनवलेला script — या 5 validation prompts मधून pass करा. किती changes लागले?"
- Nav: prev = captions-hashtags, next = iteration

- [ ] **Step 7: Create `tools/ai-content/iteration.html`**

Content:
- Full loop: write → validate → fix → validate again → done
- Real example walkthrough: dental carousel "root canal भयंकर नाही"
  - Show: first prompt → first output → validation feedback → revised prompt → revised output → final validation → approved
  - Each stage clearly labeled
- Pre-client checklist (table format):
  - Hook: scroll थांबवेल का?
  - Brand voice: client च्या tone शी match होतं का?
  - Factual accuracy: सगळं बरोबर आहे का?
  - CTA: natural वाटतं का, pushy नाही ना?
  - Visuals: image/video notes clear आहेत का?
- Exercise: "एका bakery साठी complete carousel बनवा — research (3.6a) ते final validated script. सगळे steps follow करा. हा exercise सगळ्यात important आहे."
- `.tip` box: "हा exercise पूर्ण करा. ही तुमची first 'real' deliverable आहे. हे तुम्ही client ला दाखवू शकता."
- Nav: prev = validation, next = scheduling

- [ ] **Step 8: Verify locally**

Open all 7 pages. Check:
- Prompt blocks render clearly with English text
- Exercise boxes distinct from prompt blocks
- Warning box renders with red left border
- Navigation chain: research → calendar → carousel → reel → captions → validation → iteration
- Breadcrumbs show: Home / Tools / AI Content / [page name]

- [ ] **Step 9: Commit**

```bash
git add tools/ai-content/
git commit -m "feat: add AI content section — 7 pages on LLM script writing and validation"
```

---

## Task 5: Section 3.7–3.8 — Scheduling & Zero Budget Toolkit

**Files:**
- Create: `tools/scheduling.html`
- Create: `tools/zero-budget-toolkit.html`

- [ ] **Step 1: Create `tools/scheduling.html`**

Content:
- Meta Business Suite — free scheduling tool by Meta
- Step-by-step: link Instagram to Facebook page → go to business.facebook.com → create post → schedule
- Google Sheets content calendar template:
  - Columns: Date | Format | Topic | Hook | Status (Draft/Approved/Posted) | Link
  - Show example rows filled in
  - "हा template copy करा: [link to a public Google Sheet template]"
- Managing multiple clients:
  - Folder structure: Client Name / Month / Content Type
  - Naming: `[ClientName]-[Date]-[Type]-[Topic].png`
  - Separate browser profiles or Instagram's account switching
- Exercise: "तुमचा एक post Meta Business Suite मध्ये schedule करा — उद्या सकाळी 10 ला"
- Later/Buffer mentioned as paid alternatives for scaling
- Nav: prev = iteration, next = zero-budget-toolkit

- [ ] **Step 2: Create `tools/zero-budget-toolkit.html`**

Content:
- "Zero Budget" Toolkit — सगळं free:
  - Design: Canva (free tier)
  - AI Images: Gemini (free), Bing Image Creator (free)
  - Video: CapCut (free)
  - Audio: Phone Voice Memos (free), ElevenLabs (10 min/month free)
  - Content Writing: ChatGPT (free tier), Gemini (free), Claude (free tier)
  - Scheduling: Meta Business Suite (free)
  - Calendar: Google Sheets (free)
  - Link in Bio: Linktr.ee (free)
- "पहिले पैसे आले — कशात invest करायचं?" priority list:
  1. Canva Pro (₹500/month) — more templates, brand kit
  2. Good mic (₹1500 one-time) — better voiceover quality
  3. ElevenLabs paid (if using AI voice heavily)
- Checklist: "मी ready आहे" — all tools set up:
  - [ ] Canva account
  - [ ] Gemini access
  - [ ] CapCut installed
  - [ ] Voice recording tested
  - [ ] ChatGPT/Claude/Gemini for writing
  - [ ] Meta Business Suite linked
  - [ ] Google Sheets calendar template copied
- Nav: prev = scheduling, next = playbooks/ (playbook section)

- [ ] **Step 3: Verify and commit**

```bash
git add tools/scheduling.html tools/zero-budget-toolkit.html
git commit -m "feat: add scheduling and zero-budget toolkit pages"
```

---

## Task 6: Section 4 — Dentist Playbook

**Files:**
- Create: `playbooks/index.html`
- Create: `playbooks/dentist/index.html`
- Create: `playbooks/dentist/brand-voice.html`
- Create: `playbooks/dentist/content-pillars.html`
- Create: `playbooks/dentist/calendar.html`
- Create: `playbooks/dentist/content-kits.html`
- Create: `playbooks/dentist/hashtags.html`
- Create: `playbooks/dentist/pitch.html`

**Source material:**
- `/private/tmp/dentist/brand/brand-identity.md` — brand voice, handle templates, bio templates
- `/private/tmp/dentist/content/preventive-care/*.md` — content kits (5 posts)
- `/private/tmp/dentist/content/treatment-demystified/*.md` — content kits (5 posts)
- `/private/tmp/dentist/calendar/content-calendar.md` — 90-day calendar (adapt first 30 days)
- `/private/tmp/dentist/growth/growth-playbook.md` — hashtag strategy, engagement tactics
- `/private/tmp/dentist/brand/hashtag-strategy.md` — hashtag sets

- [ ] **Step 1: Create `playbooks/index.html`**

Playbook listing page. Shows available playbooks as cards. Currently 2: Dentist and Parenting.

Content:
- Heading: "Ready-Made Playbooks"
- Explanation: "प्रत्येक playbook एक complete content system आहे. Copy करा, client साठी customize करा, deliver करा."
- Card for each playbook: name, one-line description, number of content kits included
- Future niches listed as "लवकरच येत आहे" (coming soon) — gym, salon, cafe, etc.

- [ ] **Step 2: Create `playbooks/dentist/index.html`**

Dental niche overview. Adapt from `/private/tmp/dentist/brand/brand-identity.md` and README.

Content:
- Dentist niche म्हणजे काय — dental Instagram page कशासाठी
- Target audience: patients (25-55), local area, scared of dentist, looking for trusted info
- Why dentists need Instagram: trust building, patient education, local discovery
- What this playbook contains: links to all sub-pages (brand voice, pillars, calendar, kits, hashtags, pitch)
- Quick start: "हे 7 pages वाचा, client ला approach करा, content deliver करा"

- [ ] **Step 3: Create `playbooks/dentist/brand-voice.html`**

Adapt from `/private/tmp/dentist/brand/brand-identity.md`.

Content (translated/adapted to Marathi explanation):
- Handle suggestions: `@Dr[Name].Dentist`, `@[City].Dental.Tips`, etc.
- Bio template: `[Who you are] + [What followers get] + [CTA]`
- Tone: friendly, reassuring, educational. NOT preachy or scary.
- Do's and Don'ts table
- Example phrases: good vs bad versions
- "हे client ला दाखवा आणि customize करा — त्यांचं नाव, शहर, specialty टाका"

- [ ] **Step 4: Create `playbooks/dentist/content-pillars.html`**

Content:
- 2 content series from existing source: Preventive Care, Treatment Demystified
- Expand to 6-8 pillars:
  1. Preventive Care (brushing, flossing, diet)
  2. Treatment Demystified (root canal, filling, extraction)
  3. Patient Stories / Testimonials
  4. Behind the Scenes (clinic, equipment, team)
  5. Myth Busting (common dental myths)
  6. Quick Tips (30-second actionable advice)
  7. Seasonal (Diwali sweets and teeth, summer hydration)
  8. Community (local health events, dental camps)
- Each pillar: description, example topics, posting frequency suggestion

- [ ] **Step 5: Create `playbooks/dentist/calendar.html`**

Adapt first 30 days from `/private/tmp/dentist/calendar/content-calendar.md`.

Content:
- 30-day calendar as a table: Day | Content Kit | Format | Content Pillar
- Week 1: Launch week — 3 posts (Mon/Wed/Fri)
- Week 2-4: Building rhythm
- Notes on timing: best posting times for Indian audience
- "हा calendar client ला दाखवा — approval घ्या — मग execute करा"

- [ ] **Step 6: Create `playbooks/dentist/content-kits.html`**

Adapt 10 content kits from `/private/tmp/dentist/content/`.

Each kit contains:
- Topic and hook
- Carousel script (slide-by-slide) OR reel script (second-by-second)
- Caption with CTA
- Hashtag set
- AI image prompt (Gemini-ready, in `.prompt-block`)
- Visual style note

Adapt all 10 kits:
1. Why Brushing Twice Matters (from `preventive-care/01`)
2. Flossing Truth (from `preventive-care/02`)
3. What Happens at a Cleaning (from `preventive-care/03`)
4. Diet and Teeth (from `preventive-care/04`)
5. Mouthwash — Do You Need It? (from `preventive-care/05`)
6. Root Canal Not Scary (from `treatment-demystified/01`)
7. What is a Filling (from `treatment-demystified/02`)
8. Wisdom Teeth Extraction (from `treatment-demystified/03`)
9. Dental Implants Explained (from `treatment-demystified/04`)
10. Crowns and Bridges (from `treatment-demystified/05`)

For each kit, add a Marathi explanation of the content strategy: "हा post का काम करतो" — why the hook works, what emotion it targets.

- [ ] **Step 7: Create `playbooks/dentist/hashtags.html`**

Adapt from `/private/tmp/dentist/brand/hashtag-strategy.md` and `growth/growth-playbook.md`.

Content:
- Primary hashtags (always use): `#DentalTips #OralHealth #DentistExplains`
- Rotating sets (3 different sets, rotate weekly)
- Size mix: 1 large + 3 medium + 3 small + 1 branded per post
- "Same hashtags सलग दोन posts वर लावू नका" rule
- Local hashtags: how to add city-specific tags (`#PuneDentist`, `#MumbaiDentalCare`)

- [ ] **Step 8: Create `playbooks/dentist/pitch.html`**

Content (Marathi):
- How to find dentists who need Instagram: Google Maps "dentist near me", check their online presence
- The pitch script (Marathi): "नमस्कार, मी [तुमचं नाव]. मी dentists साठी Instagram content बनवतो. मी तुमच्यासाठी 2 sample posts बनवले — बघाल का?"
- What to show: 2 sample posts from the content kits + the 30-day calendar
- Pricing suggestion for dental niche: ₹5,000-15,000/month depending on scope
- Common objections from dentists and how to handle them
- Simple agreement template for dental clients

- [ ] **Step 9: Verify and commit**

```bash
git add playbooks/
git commit -m "feat: add playbook section — listing page + complete dentist playbook (7 pages)"
```

---

## Task 7: Section 4 — Parenting Playbook

**Files:**
- Create: `playbooks/parenting/index.html`
- Create: `playbooks/parenting/brand-voice.html`
- Create: `playbooks/parenting/content-pillars.html`
- Create: `playbooks/parenting/calendar.html`
- Create: `playbooks/parenting/content-kits.html`
- Create: `playbooks/parenting/hashtags.html`
- Create: `playbooks/parenting/pitch.html`

**Source material:**
- `/private/tmp/dentist/parenting-channel-playbook.json` — complete channel blueprint (brand voice, tone, content pillars, visual style, hashtag strategy, carousel structure)
- `/private/tmp/dentist/instagram-tutorial-marathi.md` — carousel examples, content samples
- `/private/tmp/dentist/parenting-playbook-marathi.md` — full Marathi parenting content

- [ ] **Step 1: Create `playbooks/parenting/index.html`**

Parenting niche overview.

Content:
- Parenting Instagram page म्हणजे काय — emotional support, community building
- Target audience: working parents (25-40), nuclear family, metro cities, Hindi-Marathi speaking
- Why parenting pages work on Instagram: high engagement, very shareable content
- What this playbook contains: links to sub-pages
- Note: "हा playbook 'Ghar Ka Classroom' style channel साठी आहे — honest, warm, non-judgmental parenting content"

- [ ] **Step 2: Create `playbooks/parenting/brand-voice.html`**

Adapt from `parenting-channel-playbook.json` → `channel.tone`.

Content:
- Voice: "Like a friend who's 2 years ahead" — translated/explained in Marathi
- What we are: Warm, Reassuring, Honest, Gentle, Specific
- What we are NOT: Preachy, Guilt-inducing, Judgmental, Toxic-positive
- Rules (from JSON, explained in Marathi):
  - "Validate the struggle BEFORE offering reassurance"
  - "Never frame parenting as countdown or loss"
  - "Specificity > generality"
- Tone balance: ~65% warm, ~15% gut-punch, ~15% proud tears, ~5% funny
- Handle suggestions: `@ghar.ka.classroom`, `@pune.parents`, `@real.mumbai.parents`
- Bio template example

- [ ] **Step 3: Create `playbooks/parenting/content-pillars.html`**

Adapt from `parenting-channel-playbook.json` → content pillars.

Content (9 pillars):
1. बाळ मोठं होणं — milestones, development
2. Office vs घर — working parent guilt, balance
3. Couple life — relationship after kids
4. Nuclear family challenges — no village, doing it alone
5. School / education — homework, tiffin, school runs
6. Real talk — honest confessions, imperfect moments
7. Self-care — parent's identity beyond parenting
8. Festival / seasonal — Indian festivals with kids
9. Community — "you're not alone" solidarity posts

Each pillar: description, 3 example topics, recommended format (carousel/reel/story)

- [ ] **Step 4: Create `playbooks/parenting/calendar.html`**

30-day content calendar.

Content:
- Table: Day | Topic | Format | Content Pillar | Hook
- 3 posts per week (Mon/Wed/Fri) + daily stories
- Week 1: Launch with strongest emotional content
- Week 2-4: Rotate through pillars
- Posting time: 9 PM - 11 PM (when parents are scrolling after kids sleep)

- [ ] **Step 5: Create `playbooks/parenting/content-kits.html`**

10 ready-made content kits. Build from `parenting-channel-playbook.json` carousel structure and examples from `instagram-tutorial-marathi.md`.

Each kit:
- Topic, hook, emotion target
- Carousel script (5-6 slides): Hook → Struggle → Validate → Reframe → CTA
- Caption with CTA
- Hashtag set
- AI image prompt (warm, earthy, Indian home setting)
- Visual style note

Example kits:
1. "पहिला दिवस, कोणी Manual नाही" — new parent overwhelm
2. "रात्री 3 वाजता YouTube search" — sleepless nights
3. "Office मधून guilt call" — working parent guilt
4. "तुम्ही enough आहात" — reassurance
5. "Weekend म्हणजे laundry" — real life
6. "बाळाने पहिलं word बोललं — आणि ते 'no' होतं" — funny/proud
7. "Tiffin wars" — school lunch stress
8. "Video call वर आजी-आजोबा" — nuclear family emotions
9. "तुमचं बाळ argue करतंय — proud moment" — reframe
10. "Screen time guilt" — honest conversation

- [ ] **Step 6: Create `playbooks/parenting/hashtags.html`**

Adapt from `parenting-channel-playbook.json` → `engagement_strategy.hashtags`.

Content:
- Primary: `#GharKaClassroom #WorkingParents #NuclearFamily #ParentingIndia`
- Rotating sets (3 sets)
- Local tags: `#MumbaiMom #PuneParents #BangaloreParenting`
- Size mix strategy

- [ ] **Step 7: Create `playbooks/parenting/pitch.html`**

Content:
- This is different from dental — parenting pages are often personal brands, not business pages
- Who is the "client": a parent who wants to build a following but doesn't have time to create content
- How to find them: parenting WhatsApp groups, mommy bloggers who post irregularly
- Pitch: "तुमच्याकडे stories आहेत, मी त्या Instagram content मध्ये convert करतो"
- Pricing: lower than business clients (₹3,000-8,000/month) but high volume potential
- Alternative model: build the page yourself, monetize through brand collaborations later

- [ ] **Step 8: Verify and commit**

```bash
git add playbooks/parenting/
git commit -m "feat: add parenting playbook — 7 pages with content kits and strategy"
```

---

## Task 8: Section 5 — स्वतः बनवा (DIY)

**Files:**
- Create: `diy/niche-research.html`
- Create: `diy/brand-voice.html`
- Create: `diy/content-pillars.html`
- Create: `diy/content-calendar.html`
- Create: `diy/content-kits.html`
- Create: `diy/packaging.html`

- [ ] **Step 1: Create `diy/niche-research.html`**

Content:
- कोणत्याही business चं Instagram playbook बनवायला — पहिला step: research
- Two research methods:
  1. Talk to the owner — 10 questions to ask:
     - तुमचे customers कोण आहेत?
     - लोक तुम्हाला कसं शोधतात?
     - तुमच्या business चं सगळ्यात मोठं challenge काय आहे?
     - Competitors कोण आहेत?
     - तुमचं USP काय आहे?
     - (5 more questions — all in Marathi)
  2. Online research: Google reviews, competitor Instagram pages, Quora, YouTube
- LLM-assisted research (link to tools/ai-content/research.html): "या prompt ने सुरुवात करा"
- Exercise: "तुमच्या गल्लीतला एक business निवडा. या 10 प्रश्नांची उत्तरं शोधा — विचारून किंवा online. एका page वर लिहा."
- Nav: prev = zero-budget-toolkit, next = diy/brand-voice

- [ ] **Step 2: Create `diy/brand-voice.html`**

Content:
- प्रत्येक business चा आवाज वेगळा आहे — salon ≠ lawyer ≠ cafe
- 5 questions that define brand voice:
  1. तुमचे customers तुम्हाला काय म्हणतात? (formal "sir" vs casual "bhai")
  2. तुमच्या business चा mood काय आहे? (fun/serious/warm/professional)
  3. कोणते शब्द तुम्ही नेहमी वापरता?
  4. कोणते शब्द तुम्ही कधीच वापरणार नाही?
  5. तुमच्या best customer ला describe करा — त्यांच्याशी कसं बोलता?
- How to write a brand voice doc from a 20-minute conversation
- Template: a simple brand voice doc structure (tone, do/don't, example phrases)
- Exercise: "5.1 मध्ये research केलेल्या business चा brand voice doc लिहा. 1 page, 5 sections."

- [ ] **Step 3: Create `diy/content-pillars.html`**

Content:
- Content pillars म्हणजे काय — "काय post करू?" हा प्रश्न कायमचा संपतो
- Formula: 2 educational + 2 emotional + 2 behind-the-scenes + 1 promotional + 1 community
- How to derive pillars from research: map customer questions to educational, map customer emotions to emotional, etc.
- Example: bakery pillars — recipes (edu), customer celebrations (emotional), kitchen BTS, special offers (promo), baking community
- Exercise: "तुमच्या research + brand voice वरून 6-8 content pillars लिहा. प्रत्येकाचं 1-line description आणि 3 example topics."

- [ ] **Step 4: Create `diy/content-calendar.html`**

Content:
- Weekly rhythm: which pillar on which day
- Format balancing: carousels (2/week), reels (1/week), stories (daily)
- Using LLM to generate from pillars (link to tools/ai-content/content-calendar.html)
- Template: table format with columns
- Exercise: "तुमच्या pillars वरून 30-day content calendar बनवा. LLM वापरा, पण final judgment तुमचं."

- [ ] **Step 5: Create `diy/content-kits.html`**

Content:
- Putting it all together: pick calendar slot → write script (tools/ai-content) → create visuals (tools/canva, tools/ai-images) → validate (tools/ai-content/validation) → done
- Step-by-step walkthrough for one content kit
- This page is mostly cross-references to tools section, with the glue logic
- Exercise: "तुमच्या calendar मधले पहिले 3 content kits बनवा — start to finish. Research ते validated script."
- `.tip` box: "हे 3 kits तुमचा portfolio आहे. Client ला हेच दाखवा."

- [ ] **Step 6: Create `diy/packaging.html`**

Content:
- Folder structure per client:
  ```
  [Client Name]/
  ├── Brand Voice.pdf
  ├── Content Calendar.xlsx
  ├── Month 1/
  │   ├── Week 1/
  │   │   ├── Post-1-Carousel/
  │   │   │   ├── slides/ (PNG files)
  │   │   │   ├── caption.txt
  │   │   │   └── hashtags.txt
  ```
- Approval workflow: content kit → WhatsApp/email to client → approval → post
- Google Drive setup: shared folder with client
- Notion alternative for more organized clients
- Exercise: "तुमचे 3 content kits या folder structure मध्ये organize करा — जसं client ला पाठवाल तसं."
- Nav: prev = content-kits, next = clients/kuthe-shodhayche

- [ ] **Step 7: Verify and commit**

```bash
git add diy/
git commit -m "feat: add DIY section — 6 pages on creating playbooks for any niche"
```

---

## Task 9: Section 6 — Clients मिळवा (Leads)

**Files:**
- Create: `clients/kuthe-shodhayche.html`
- Create: `clients/pahila-contact.html`
- Create: `clients/pitch-and-pricing.html`
- Create: `clients/pahila-client.html`
- Create: `clients/grow-kara.html`
- Create: `clients/common-problems.html`

- [ ] **Step 1: Create `clients/kuthe-shodhayche.html`**

Content:
- 6 ways to find potential clients:
  1. Walk your street: दुकानं बघा — कोणाचं Instagram नाही? कोणाचं dead आहे?
  2. Google Maps: "dentist near me" search करा, त्यांचं Instagram check करा
  3. Instagram search: local hashtags (#PuneFood, #NagpurSalon) — pages with <500 followers, bad content
  4. JustDial/Sulekha: businesses that advertise but have no Instagram
  5. WhatsApp groups: local business groups, chamber of commerce
  6. Friends and family: "कोणाला माहीत आहे का जे business चालवतात?"
- Each method: how to do it, what to look for, pros/cons
- Exercise: "तुमच्या area मध्ये 20 businesses शोधा ज्यांना Instagram help लागू शकते. List बनवा: Name | Type | Instagram Status (no page / dead / active but bad)"

- [ ] **Step 2: Create `clients/pahila-contact.html`**

Content:
- 4 approach methods compared (table): Walk-in | DM | WhatsApp | Mutual intro — success rate, effort, best for
- The 30-second pitch (Marathi):
  - "नमस्कार, मी [नाव]. मी local businesses साठी Instagram content बनवतो. मी तुमच्यासाठी 2 sample posts बनवले — बघता का? Free आहे, कोणतीही commitment नाही."
- Free sample strategy: playbook मधून 2-3 posts बनवा BEFORE approaching
- What NOT to do:
  - "तुमचं Instagram खूप वाईट आहे" — never criticize
  - Followers चं promise करू नका
  - Desperate वाटू नका
- Handling "नको": "ठीक आहे, हे माझं card/number आहे. कधी वाटलं तर सांगा." — move on
- Exercise: "तुमच्या list मधल्या 1 business साठी free sample बनवा — playbook वापरून 2 posts बनवा"

- [ ] **Step 3: Create `clients/pitch-and-pricing.html`**

Content:
- What to show in a pitch meeting:
  1. Sample posts (2-3, already created)
  2. 1-page proposal: what you'll do, how often, what they need to provide
  3. 30-day calendar preview
- Pricing models (table):
  - Per post: ₹500-1,500 per post (beginner friendly, low commitment)
  - Monthly package: ₹5,000-15,000/month (12-16 posts + stories)
  - Revenue share: advanced, rare — only with trust
- "पहिला client स्वस्तात करा — हे ठीक आहे":
  - First client = portfolio + testimonial + learning
  - ₹2,000-3,000 for first month is fine
  - Free pilot (1 week) to prove value
- Simple agreement template (Marathi + English):
  - Scope: किती posts, कोणत्या format
  - Timeline: content कधी deliver, approval कधी
  - Payment: किती, कधी, कसं (UPI/cash)
  - Ownership: content कोणाचं (client चं)
- Exercise: "1-page proposal बनवा तुमच्या sample business साठी"

- [ ] **Step 4: Create `clients/pahila-client.html`**

Content:
- Onboarding checklist — client कडून काय collect करायचं:
  - Business photos (clinic, shop, products, team)
  - Logo (high quality)
  - Brand preferences (colors, fonts if any)
  - Instagram login credentials (secure sharing method)
  - Approval process: WhatsApp group? Email?
- First week plan:
  - Day 1-2: Account audit/setup (professional account, bio, highlights)
  - Day 3-4: Present 30-day content calendar for approval
  - Day 5-7: Create and post first 2-3 posts
- Communication rhythm:
  - Weekly: content batch for approval (WhatsApp message with images + captions)
  - Monthly: simple report — posts made, reach, engagement, saves
- What success looks like at 30 days:
  - NOT: "10,000 followers"
  - YES: consistent posting, professional look, first engagement from real people, client is happy with quality

- [ ] **Step 5: Create `clients/grow-kara.html`**

Content:
- 1 client ते 5 clients — growth path
- Portfolio building: every client = screenshot + results + testimonial
- Referrals: 30 दिवसांनंतर विचारा — "तुमच्या ओळखीत कोणाला Instagram help लागेल का?"
- Testimonials: WhatsApp screenshot (with permission) is powerful proof
- Expanding services:
  - Start: content creation only
  - Add: posting + scheduling
  - Add: engagement management (reply to comments/DMs)
  - Add: paid ads management (Meta ads)
- Capacity planning:
  - 1-2 clients: learning phase, spend more time per client
  - 3-4 clients: comfortable, systemized
  - 5+: need to template more, or hire help
  - "Quality कमी करू नका. 3 happy clients > 6 struggling clients"

- [ ] **Step 6: Create `clients/common-problems.html`**

Content (each problem as h2):
- "Client approval ला reply करत नाही":
  - Gentle reminder after 24 hours
  - Set expectations upfront: "48 तासांत approval नाही तर schedule shift होईल"
- "Client सारखे changes मागतो":
  - Agreement मध्ये revision limit ठेवा (2 revisions per post)
  - "तुमचं vision समजून घ्यायचं आहे" — listen first, then set boundary
- "Results येत नाहीत":
  - Honest conversation: "Instagram growth takes 3-6 months"
  - Show what you CAN control: quality, consistency, engagement
  - Show metrics that ARE improving (reach, saves) even if followers aren't
- "Client थांबवायचं म्हणतोय":
  - "ठीक आहे" — graceful exit
  - Ask for testimonial
  - Ask what could have been better — learn from it
  - Don't burn bridges
- "मी चूक केली" (wrong post, typo, wrong account):
  - Delete immediately if possible
  - Tell the client — don't hide it
  - Apologize, fix, add a safeguard (checklist before posting)
  - `.tip` box: "Posting checklist बनवा — प्रत्येक post पूर्वी check करा: account बरोबर आहे? Caption proofread? Hashtags correct? Approval मिळालं?"

- [ ] **Step 7: Verify and commit**

```bash
git add clients/
git commit -m "feat: add clients section — 6 pages on finding and managing clients"
```

---

## Task 10: Push to GitHub & Enable GitHub Pages

**Files:**
- No new files — push existing repo to `instamarathi/instamarathi.github.io`

- [ ] **Step 1: Add remote and push**

```bash
cd /private/tmp/instamarathi
git remote add origin https://github.com/instamarathi/instamarathi.github.io.git
git branch -M main
git push -u origin main
```

- [ ] **Step 2: Enable GitHub Pages**

```bash
gh api repos/instamarathi/instamarathi.github.io/pages -X POST -f build_type=legacy -f source='{"branch":"main","path":"/"}'
```

If Pages is already auto-enabled (due to repo name), verify:

```bash
gh api repos/instamarathi/instamarathi.github.io/pages
```

Expected: `"status": "built"` and `"html_url": "https://instamarathi.github.io"`

- [ ] **Step 3: Verify live site**

Open `https://instamarathi.github.io` in browser. Verify:
- Homepage loads
- Navigation works — all section links resolve
- All pages render correctly
- Mobile responsive

- [ ] **Step 4: Commit any fixes**

If any links or paths need fixing after going live, fix and push.

```bash
git add -A && git commit -m "fix: path corrections for GitHub Pages" && git push
```

---

## Task Dependencies

```
Task 1 (skeleton) ← everything depends on this
Task 2 (शिका)     ← independent after Task 1
Task 3 (tools 1-5) ← independent after Task 1
Task 4 (AI content) ← independent after Task 1
Task 5 (scheduling) ← independent after Task 1
Task 6 (dentist)    ← independent after Task 1, benefits from Task 3-4 being done (cross-references)
Task 7 (parenting)  ← independent after Task 1, benefits from Task 3-4 being done
Task 8 (DIY)        ← references tools section, better done after Tasks 3-4
Task 9 (clients)    ← independent after Task 1
Task 10 (deploy)    ← after all other tasks
```

**Parallelizable:** Tasks 2, 3, 4, 5, 9 can all run in parallel after Task 1.
Tasks 6, 7 can run in parallel after Task 1 (ideally after 3-4).
Task 8 after Tasks 3-4.
Task 10 last.
