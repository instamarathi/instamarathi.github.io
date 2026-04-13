# InstaMarathi Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a free, mobile-first Marathi website (`instamarathi.github.io`) that teaches people how to build a business running Instagram pages for local businesses.

**Architecture:** Static HTML site hosted on GitHub Pages. Single shared CSS stylesheet. No JavaScript frameworks. Each page follows a common HTML template with consistent navigation. Content written in Marathi-English mix, meta tags in English for SEO.

**Tech Stack:** HTML5, CSS3, GitHub Pages. Playbooks (dermatologist, gym) created fresh. Tool tutorials adapted from existing Instagram tutorial (`/private/tmp/dentist/instagram-tutorial-marathi.md`) and production guide (`/private/tmp/dentist/brand/production-guide.md`).

**Source repo:** `instamarathi/instamarathi.github.io` on GitHub (already created, user has write access).

---

## Task 1: Site Skeleton — CSS, HTML Template, Directory Structure

**Files:**
- Create: `assets/css/style.css`
- Create: `index.html`
- Create: all directories (`shika/`, `tools/`, `tools/ai-content/`, `playbooks/`, `playbooks/dermatologist/`, `playbooks/gym/`, `diy/`, `clients/`, `assets/css/`)

This task creates the mobile-first CSS and the homepage. All subsequent pages copy the HTML structure from `index.html`.

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p assets/css shika tools/ai-content playbooks/dermatologist playbooks/gym diy clients
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
        <li><a href="/sales/">Sales</a></li>
        <li><a href="/clients/kuthe-shodhayche.html">Clients</a></li>
      </ul>
    </div>
  </nav>

  <div class="container">
    <div class="hero">
      <h1>Instagram वरून Business चालवायचं शिका — दुसऱ्यांसाठी</h1>
      <p class="subtitle">Local businesses साठी Instagram manage करा. पैसे कमवा. सगळं मराठीत शिका.</p>
      <p class="subtitle" style="font-size:0.95rem;">₹50,000 च्या 8-day social marketing course मधलं सगळ्यात important — मराठीत, free.</p>
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

      <a href="/sales/" class="card">
        <h3>Sales शिका — ₹50,000 च्या Course मधलं</h3>
        <p>Sales mindset, book summaries मराठीत. Rejection handle करणं, trust build करणं, deal close करणं.</p>
      </a>

      <a href="/clients/kuthe-shodhayche.html" class="card">
        <h3>Clients मिळवा — Business कसं वाढवायचं</h3>
        <p>Clients कुठे शोधायचे, call strategy, meeting tips, proposal format, pricing, growth.</p>
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

## Task 6: Section 4 — Dermatologist Playbook

**Files:**
- Create: `playbooks/index.html`
- Create: `playbooks/dermatologist/index.html`
- Create: `playbooks/dermatologist/brand-voice.html`
- Create: `playbooks/dermatologist/content-pillars.html`
- Create: `playbooks/dermatologist/calendar.html`
- Create: `playbooks/dermatologist/content-kits.html`
- Create: `playbooks/dermatologist/hashtags.html`
- Create: `playbooks/dermatologist/pitch.html`

**Source material:** Created fresh — dermatology is a visual-heavy, high-demand niche. Use existing dental playbook structure as a template for format/layout, but all content is new.

- [ ] **Step 1: Create `playbooks/index.html`**

Playbook listing page. Shows available playbooks as cards. Currently 2: Dermatologist and Gym.

Content:
- Heading: "Ready-Made Playbooks"
- Explanation: "प्रत्येक playbook एक complete content system आहे. Copy करा, client साठी customize करा, deliver करा."
- Card for each playbook: name, one-line description, number of content kits included
- Future niches listed as "लवकरच येत आहे" (coming soon) — dentist, salon, cafe, etc.

- [ ] **Step 2: Create `playbooks/dermatologist/index.html`**

Dermatologist niche overview.

Content:
- Dermatologist niche म्हणजे काय — skin care clinic Instagram page कशासाठी
- Why this niche is powerful: skin is visual, before/after content performs extremely well, everyone has skin concerns
- Target audience: patients (18-45), urban India, skin concerns (acne, pigmentation, aging, hair loss), looking for trusted info before booking
- Why dermatologists need Instagram: patients Google/Instagram skin issues before visiting, visual proof builds trust, local discovery
- What this playbook contains: links to all sub-pages
- Quick start: "हे 7 pages वाचा, client ला approach करा, content deliver करा"

- [ ] **Step 3: Create `playbooks/dermatologist/brand-voice.html`**

Content:
- Handle suggestions: `@Dr[Name].Skin`, `@[City].SkinClinic`, `@SkinFactsBy[Name]`, `@Dr[Name].Derm`, `@[Name]SkinCare`
- Bio template: `[Who you are] + [What followers learn] + [CTA]`
  - Example: "Dr. Priya Sharma | Dermatologist, Pune\nSkin science — simple मध्ये\nDM for appointment 📩"
- Tone: science-backed but approachable. Confident but not salesy. Educational, busting myths.
- What we are: Clear, Scientific, Reassuring, Practical, Visual
- What we are NOT: Fear-mongering ("your skin is damaged!"), product-pushing, judgmental about skin conditions, making medical claims in content
- Do's and Don'ts table:
  - Do: "Acne होणं normal आहे — हे का होतं ते समजून घ्या"
  - Don't: "तुमची skin खराब आहे — लगेच treatment घ्या!"
- Example phrases: good vs bad versions
- `.warning` box: "Medical content sensitive आहे. Client (dermatologist) ने प्रत्येक post approve करणं mandatory आहे. चुकीची medical माहिती = serious problem."

- [ ] **Step 4: Create `playbooks/dermatologist/content-pillars.html`**

Content — 8 pillars:
1. **Skin Science Simplified** — how skin works, why problems happen (acne, pigmentation, dryness). Educational carousels.
2. **Myth Busting** — "lemon लावलं तर glow येतो" = myth. High engagement, shareable.
3. **Treatment Explainers** — what happens in a chemical peel, laser, microneedling. Demystify procedures.
4. **Before/After** — real patient transformations (with consent). Most powerful content type for this niche.
5. **Skincare Routine** — morning/night routines, product recommendations by skin type. Practical, save-worthy.
6. **Seasonal Skin Care** — monsoon fungal infections, winter dryness, summer sunscreen. Timely content.
7. **Behind the Scenes** — clinic tour, equipment, team, day-in-the-life of a dermatologist.
8. **Quick Tips** — 15-30 second actionable advice. "Sunscreen reapply कधी करायचं?" format.

Each pillar: description, 3 example topics, recommended format, posting frequency.

- [ ] **Step 5: Create `playbooks/dermatologist/calendar.html`**

30-day content calendar.

Content:
- Table: Day | Topic | Format | Content Pillar | Hook
- Week 1 (Launch): Start with myth-busting + skin science (high engagement, shareable)
  - Mon: "Face wash दिवसातून 5 वेळा = चांगली skin?" (Carousel, Myth Busting)
  - Wed: "तुमचा Skin Type कोणता?" (Carousel, Skin Science)
  - Fri: "Sunscreen — कधी, किती, कोणतं?" (Reel, Quick Tips)
- Week 2: Treatment explainers + before/after
- Week 3: Skincare routines + seasonal
- Week 4: Mix of all pillars + first behind-the-scenes
- Posting time: 8-10 PM (after work, scrolling time)
- Daily stories: polls ("तुम्ही sunscreen लावता का?"), skin type quizzes, Q&A

- [ ] **Step 6: Create `playbooks/dermatologist/content-kits.html`**

10 ready-made content kits:

1. **"Face Wash दिवसातून 5 वेळा?"** — Myth busting carousel. Hook: "जितकं जास्त wash, तितकी चांगली skin — खरं का?" Slides debunk over-washing, explain skin barrier.
2. **"तुमचा Skin Type कोणता?"** — Educational carousel. 4 skin types explained with simple test. Save-worthy.
3. **"Sunscreen चं खरं सत्य"** — Reel script. 60-sec explainer: SPF meaning, how much to apply, reapplication.
4. **"Acne का होतं?"** — Science simplified carousel. Hormones, diet, stress — what actually causes acne.
5. **"Chemical Peel म्हणजे काय?"** — Treatment explainer carousel. Step-by-step what happens, pain level, results timeline.
6. **"DIY Face Pack — Safe का Risky?"** — Myth busting carousel. Which home remedies work, which are dangerous.
7. **"Pigmentation कमी करायचं?"** — Educational carousel. Types of pigmentation, what works, what doesn't, realistic timeline.
8. **"Morning Skincare Routine — 5 Minutes"** — Reel script. Quick routine: cleanser → serum → moisturizer → sunscreen.
9. **"Hair Loss — कधी tension घ्यायची?"** — Educational carousel. Normal vs concerning hair fall, when to see a dermatologist.
10. **"Laser Treatment — भयंकर नाही"** — Treatment explainer. What happens, pain level, recovery, results.

Each kit contains:
- Topic, hook, emotion target
- Carousel script (slide-by-slide) OR reel script (second-by-second)
- Caption with CTA
- Hashtag set
- AI image prompt for Gemini (skin care visuals — clean, clinical but warm, Indian setting)
- Visual style note (clean whites, soft blues, clinical-but-approachable aesthetic)
- "हा post का काम करतो" — strategy explanation in Marathi

- [ ] **Step 7: Create `playbooks/dermatologist/hashtags.html`**

Content:
- Primary hashtags: `#SkinCareTips #DermatologistExplains #SkinScience #HealthySkin`
- Rotating sets (3 sets, rotate weekly):
  - Set A: `#AcneTreatment #SkinCareRoutine #GlowingSkin #DermTips #IndianSkinCare`
  - Set B: `#PigmentationTreatment #SunscreenDaily #SkinMyths #ClearSkin #SkinHealth`
  - Set C: `#HairLoss #AntiAging #ChemicalPeel #SkinCareFacts #BeautyScience`
- Local hashtags: `#PuneDermatologist #MumbaiSkinClinic #[City]SkinCare`
- Size mix: 1 large (1M+) + 3 medium (100K-1M) + 3 small (10K-100K) + 1 branded
- "Same hashtags सलग दोन posts वर लावू नका" rule

- [ ] **Step 8: Create `playbooks/dermatologist/pitch.html`**

Content (Marathi):
- How to find dermatologists: Google Maps "dermatologist near me" / "skin clinic", check Instagram
- Signs they need help: no Instagram, or posting stock photos, or inconsistent posting
- The pitch: "नमस्कार Doctor, मी [नाव]. मी dermatologists साठी Instagram content बनवतो. मी तुमच्या clinic साठी 2 sample posts बनवले — बघाल का? Patients आजकाल Instagram वर clinic search करतात."
- What to show: 2 sample posts (myth-busting + treatment explainer) + 30-day calendar
- Why dermatologists say yes: patients DO search Instagram before booking, competitors are already there
- Pricing: ₹8,000-20,000/month (dermatologists have higher budgets than many local businesses)
- Common objections:
  - "Medical content sensitive आहे" → "म्हणूनच प्रत्येक post तुम्ही approve कराल"
  - "माझ्याकडे patients येतात already" → "Instagram वर patients trust build होतो — ते directly book करतात"
- Simple agreement template with medical content approval clause

- [ ] **Step 9: Verify and commit**

```bash
git add playbooks/
git commit -m "feat: add playbook section — listing page + complete dermatologist playbook (7 pages)"
```

---

## Task 7: Section 4 — Gym / Fitness Playbook

**Files:**
- Create: `playbooks/gym/index.html`
- Create: `playbooks/gym/brand-voice.html`
- Create: `playbooks/gym/content-pillars.html`
- Create: `playbooks/gym/calendar.html`
- Create: `playbooks/gym/content-kits.html`
- Create: `playbooks/gym/hashtags.html`
- Create: `playbooks/gym/pitch.html`

**Source material:** Created fresh — fitness is aspirational, transformation-driven content. High engagement niche.

- [ ] **Step 1: Create `playbooks/gym/index.html`**

Gym/fitness niche overview.

Content:
- Gym/fitness niche म्हणजे काय — gym, personal trainer, fitness studio चं Instagram
- Why this niche is powerful: transformation content is king, reels perform extremely well, aspirational + educational mix
- Target audience: gym-goers (18-40), beginners scared of gym, people who want to start but don't know how
- Why gyms need Instagram: local discovery, member retention, trainer credibility, competition is high
- What this playbook contains: links to sub-pages
- Quick start: "हे 7 pages वाचा, client ला approach करा, content deliver करा"

- [ ] **Step 2: Create `playbooks/gym/brand-voice.html`**

Content:
- Handle suggestions: `@[GymName].Fitness`, `@[City]FitHub`, `@Coach[Name]`, `@[Name].Fitness`, `@Train.With.[Name]`
- Bio template:
  - Example: "FitZone Gym | Pune\nNo judgement. Just results.\nFree trial class — DM करा 💪"
- Tone: Motivational but NOT toxic-positive. Inclusive — beginners welcome. Science-backed, not bro-science.
- What we are: Energetic, Encouraging, Practical, Inclusive, Real
- What we are NOT: Shaming ("तुम्ही lazy आहात"), unrealistic ("6 weeks मध्ये six-pack"), supplement-pushing, only-for-advanced
- Do's and Don'ts table:
  - Do: "तुम्ही gym ला आलात — हे सगळ्यात कठीण step होतं. Respect."
  - Don't: "Summer body बनवायचं असेल तर आत्ताच सुरू करा — otherwise too late!"
- Key rule: "Progress, not perfection. प्रत्येकाचा journey different आहे."

- [ ] **Step 3: Create `playbooks/gym/content-pillars.html`**

Content — 8 pillars:
1. **Beginner Guides** — "Gym चा पहिला दिवस — काय करायचं?" Reduce intimidation.
2. **Exercise Form** — correct technique for common exercises. Safety-first. Reel-perfect content.
3. **Myth Busting** — "Weights उचलले तर bulky होतो" = myth. High engagement.
4. **Transformation Stories** — member before/after (with consent). Most powerful content type.
5. **Nutrition Basics** — simple diet tips, protein sources, meal prep. Save-worthy.
6. **Workout Plans** — "chest day", "leg day", full-body routines. Practical, bookmarkable.
7. **Behind the Scenes** — gym atmosphere, trainer life, member community, events.
8. **Motivation** — "Monday motivation", progress celebration, consistency reminders. Use sparingly (~15%).

Each pillar: description, 3 example topics, recommended format, posting frequency.

- [ ] **Step 4: Create `playbooks/gym/calendar.html`**

30-day content calendar.

Content:
- Table: Day | Topic | Format | Content Pillar | Hook
- Week 1 (Launch): Start with beginner content + myth busting (widest appeal)
  - Mon: "Gym चा पहिला दिवस — 5 गोष्टी" (Carousel, Beginner Guide)
  - Wed: "Weights उचलले तर bulky होतो — खरं का?" (Reel, Myth Busting)
  - Fri: "Protein किती लागतं — simple math" (Carousel, Nutrition)
- Week 2: Exercise form + workout plans (practical value)
- Week 3: Transformation stories + behind the scenes (social proof)
- Week 4: Mix of all pillars + nutrition deep dive
- Posting time: 6-8 AM (morning gym crowd) and 6-8 PM (evening crowd)
- Daily stories: workout polls, "आज काय train केलं?", member spotlights

- [ ] **Step 5: Create `playbooks/gym/content-kits.html`**

10 ready-made content kits:

1. **"Gym चा पहिला दिवस — 5 गोष्टी कोणी सांगत नाही"** — Beginner carousel. Hook: "पहिल्या दिवशी हे माहीत असतं तर बरं झालं असतं." Slides: what to wear, what to bring, which machines to start with, how long to stay, it's okay to feel lost.
2. **"Weights उचलले तर bulky होतो — खरं का?"** — Myth busting reel (60-sec). Science-backed explanation: why it doesn't work that way, especially for women.
3. **"Squat — बरोबर कसं करायचं"** — Exercise form reel (30-sec). Side-view, key form points highlighted with text overlay.
4. **"Protein किती लागतं? — Simple Math"** — Nutrition carousel. Body weight × 1.6-2.2g formula. Indian protein sources with quantities.
5. **"3 Months — Real Transformation"** — Before/after carousel. Member story, what they did, consistency message. (Template — client fills in real member photos)
6. **"Home Exercise — Gym नाही तरी चालेल"** — 5 bodyweight exercises carousel. For days you can't go to gym.
7. **"Chest Day Complete Workout"** — Workout plan carousel. Exercise name, sets × reps, rest time. Save-worthy.
8. **"काय खायचं — Gym आधी आणि नंतर"** — Nutrition reel (60-sec). Pre-workout and post-workout meals, Indian food options.
9. **"Running vs Gym — काय चांगलं?"** — Myth busting carousel. Answer: both, depends on goals. Comparison table.
10. **"1 Month Challenge — Daily 30 Minutes"** — Engagement carousel. 30-day workout plan, each day listed. "Save करा आणि start करा."

Each kit contains:
- Topic, hook, emotion target
- Carousel script (slide-by-slide) OR reel script (second-by-second)
- Caption with CTA
- Hashtag set
- AI image prompt for Gemini (gym visuals — energetic, clean gym, Indian setting, diverse body types)
- Visual style note (high contrast, dark/bold backgrounds for workout content, bright for nutrition)
- "हा post का काम करतो" — strategy explanation in Marathi

- [ ] **Step 6: Create `playbooks/gym/hashtags.html`**

Content:
- Primary hashtags: `#GymTips #FitnessIndia #WorkoutMotivation #FitLife`
- Rotating sets (3 sets):
  - Set A: `#GymBeginner #FitnessJourney #StrengthTraining #GymLife #HealthyLiving`
  - Set B: `#WorkoutPlan #NutritionTips #ProteinDiet #FitnessTips #BodyTransformation`
  - Set C: `#HomeWorkout #WeightLoss #MuscleBuilding #FitnessMotivation #IndianFitness`
- Local hashtags: `#PuneGym #MumbaiFitness #[City]Gym`
- Size mix: 1 large + 3 medium + 3 small + 1 branded

- [ ] **Step 7: Create `playbooks/gym/pitch.html`**

Content (Marathi):
- How to find gyms: Google Maps "gym near me", walk past gyms in your area, check their Instagram
- Signs they need help: only posting member selfies, no educational content, inconsistent, <500 followers
- The pitch: "नमस्कार, मी [नाव]. मी gyms आणि trainers साठी Instagram content बनवतो. तुमच्या gym साठी 2 sample posts बनवले — बघाल का? नवीन members attract करायला Instagram खूप powerful आहे."
- What to show: 2 sample posts (beginner guide + myth busting) + 30-day calendar
- Why gyms say yes: competition for members is fierce, Instagram helps with local discovery and trust
- Pricing: ₹5,000-15,000/month (gyms have marketing budgets, especially chains/franchises)
- Common objections:
  - "आमचे members आधीच येतात" → "नवीन members कुठून येतात? Instagram वरून search करतात."
  - "आम्ही स्वतः post करतो" → "तुमचा वेळ training ला द्या, content creation मी handle करतो"
- Simple agreement template

- [ ] **Step 8: Verify and commit**

```bash
git add playbooks/gym/
git commit -m "feat: add gym/fitness playbook — 7 pages with content kits and strategy"
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

## Task 9: Section 6 — Sales शिका (Books & Mindset)

**Files:**
- Create: `sales/index.html`
- Create: `sales/you-can-sell.html`
- Create: `sales/jeet-aapki.html`
- Create: `sales/lets-build-a-company.html`
- Create: `sales/sell-like-crazy.html`
- Create: `sales/the-opportunity.html`

**Credibility framing:** Every page opens with or references: "मी ₹50,000 चा 8-day social marketing course केला. त्यातले main lessons मी मराठीत लिहिले — free." This isn't the entire course — it's the most important takeaways, especially from the books recommended in that course.

- [ ] **Step 1: Create directory**

```bash
mkdir -p sales
```

- [ ] **Step 2: Create `sales/index.html`**

Content:
- Opening: "मी ₹50,000 चा 8-day social marketing course केला. तिथे सगळ्यात important lesson हा होता: हा business technical नाही — हा sales चा business आहे. Tools कोणीही शिकू शकतं. पण client मिळवणं, trust build करणं, deal close करणं — हे शिकायला लागतं."
- Why sales matters: "तुम्ही Canva master असाल, reels perfect बनवाल — पण client नसेल तर कोणाला दाखवणार?"
- "या course मध्ये या 5 books चे references आले. मी त्या वाचल्या. प्रत्येक book चे main points मी मराठीत लिहिले. तुम्हाला ₹50,000 खर्च करायची गरज नाही."
- 5 book cards with one-line description each:
  1. You Can Sell — "Sales म्हणजे मदत करणं, push करणं नाही"
  2. Jeet Aapki — "Confidence आणि attitude — sales च्या आधी"
  3. Let's Build a Company — "Brand कसं build करायचं — Tata कडून शिका"
  4. Sell Like Crazy — "Digital service कसं विकायचं — step by step"
  5. The Opportunity — "प्रत्येक business without Instagram = तुमची opportunity"
- Reading order recommendation: Jeet Aapki first (mindset) → You Can Sell (sales basics) → Sell Like Crazy (digital selling) → The Opportunity (positioning) → Let's Build a Company (long-term brand thinking)
- Nav: prev = diy/packaging, next = sales/jeet-aapki

- [ ] **Step 3: Create `sales/jeet-aapki.html`**

Content — "Jeet Aapki (You Can Win)" by Shiv Khera:
- Book overview: "हे sales चं book नाही — हे attitude चं book आहे. पण sales करायच्या आधी attitude बरोबर लागतो."
- 10 key points in Marathi, each with Instagram business context:
  1. **Winners vs Losers:** Winners find solutions, losers find excuses. "Client ने नाही म्हटलं = excuse शोधायचं नाही, पुढच्या client कडे जायचं."
  2. **Attitude is everything:** तुमचा attitude तुमचं काम ठरवतो. "मला sales नाही जमत" हा attitude बदला → "मला अजून शिकायला लागेल."
  3. **Goal setting:** लिहून ठेवा — "3 months मध्ये 3 clients." Written goals = accountability.
  4. **Self-confidence:** "तुम्ही value देताय — तुम्ही भीक नाही मागत. Client ला Instagram लागतं, तुमच्याकडे skill आहे."
  5. **Handling failure:** "10 calls = 8 rejections + 2 meetings. हे normal आहे. Rejection = failure नाही."
  6. **Persistence:** "बहुतेक लोक 2-3 rejections नंतर सोडतात. यशस्वी लोक 10 rejections नंतर पण continue करतात."
  7. **First impression:** "तुम्ही कसं दिसता, कसं बोलता, वेळेवर येता का — हे सगळं trust build करतं."
  8. **Continuous learning:** "हे book वाचलंत — पुढचं वाचा. शिकणं कधी थांबवू नका."
  9. **Integrity:** "जे करू शकता तेच promise करा. Over-promise + under-deliver = client गेला."
  10. **Action over planning:** "Perfect plan ची वाट बघू नका. आज एक call करा. सुरुवात करा."
- "तुमच्या business साठी 3 takeaways":
  - Rejection personal नाही — business decision आहे
  - Written goals ठेवा — monthly review करा
  - आज एक action करा — एक call, एक sample post, एक pitch
- Nav: prev = sales/index, next = sales/you-can-sell

- [ ] **Step 4: Create `sales/you-can-sell.html`**

Content — "You Can Sell" by Shiv Khera:
- Book overview: "Sales म्हणजे pushing नाही — sales म्हणजे helping. तुम्ही client ला solve करताय त्यांचं problem."
- 10 key points in Marathi with Instagram business context:
  1. **Selling = Helping:** "तुम्ही dentist ला Instagram वर patients आणून देताय. हे helping आहे, selling नाही."
  2. **Know your product:** "तुमचं product = content creation skill + playbook. हे तुम्हाला पूर्ण माहीत हवं."
  3. **Know your customer:** "Dentist ला काय हवं? Patients. Gym ला काय हवं? Members. त्यांच्या language मध्ये बोला."
  4. **Ask questions, don't pitch:** "Client ला विचारा — 'तुमचे customers कसे येतात?' — मग solution सांगा."
  5. **Handle objections gracefully:** "नाही' म्हणजे 'आत्ता नाही' किंवा 'मला अजून माहिती हवी.' प्रत्येक objection = opportunity."
  6. **Follow up:** "80% sales follow-up मध्ये होतात, पहिल्या meeting मध्ये नाही. Follow up करा — 3 दिवस, 1 आठवडा, 1 महिना."
  7. **Build trust first:** "Free sample दिलात = trust build झालं. Trust = sale."
  8. **Listen more, talk less:** "Client 70% बोलायला हवा, तुम्ही 30%. त्यांचं problem ऐका, मग solution सांगा."
  9. **Close with confidence:** "Proposal पाठवल्यावर विचारा — 'पुढच्या week पासून सुरू करू?' Silence is okay."
  10. **After-sale relationship:** "Sale झाली = relationship सुरू. Monthly reports, communication, reliability — हे retention आहे."
- "तुमच्या business साठी 3 takeaways":
  - Free sample = best sales tool
  - Follow-up discipline = difference between 1 client and 5 clients
  - Sales = solving problems, not convincing people
- Nav: prev = sales/jeet-aapki, next = sales/sell-like-crazy

- [ ] **Step 5: Create `sales/sell-like-crazy.html`**

Content — "Sell Like Crazy" by Sabri Suby:
- Book overview: "Digital service कसं विकायचं — यासाठी सगळ्यात practical book. तुम्ही exactly हेच करताय — digital service sell करताय local businesses ला."
- 10 key points in Marathi with Instagram business context:
  1. **Dream buyer:** "तुमचा ideal client कोण आहे? Dentist? Gym? Salon? एक niche निवडा — सगळ्यांना sell करू नका."
  2. **The Godfather Strategy:** "एक offer बनवा जो refuse करणं कठीण आहे. 'Free मध्ये 3 posts बनवतो — आवडले तरच पुढे' = Godfather offer."
  3. **Lead magnet:** "तुमचा free sample = तुमचा lead magnet. हे दाखवतं 'मी काय करू शकतो.'"
  4. **High-value content:** "तुमची website (InstaMarathi) = तुमचं proof. 'मी हे शिकलो, मी हे करू शकतो.'"
  5. **Follow-up sequences:** "पहिला contact → sample → proposal → follow-up → follow-up → close. System बनवा."
  6. **Irresistible offer:** "₹5,000/month for 12 professional posts + calendar + hashtags = client ला स्वतः करण्यापेक्षा स्वस्त"
  7. **Scarcity (ethical):** "मी 5 पेक्षा जास्त clients घेत नाही — quality maintain करायला." (हे खरं असायला हवं)"
  8. **Testimonials:** "पहिल्या client चा screenshot = तुमचं strongest sales tool. लगेच मागा."
  9. **Track and measure:** "किती calls → किती meetings → किती sales. Numbers track करा."
  10. **Speed wins:** "Client ने interest दाखवला? 24 तासांत proposal पाठवा. Slow = lost."
- "तुमच्या business साठी 3 takeaways":
  - Godfather offer: free sample that proves your value
  - System बनवा: contact → sample → proposal → follow-up
  - Speed: interest → proposal within 24 hours
- Nav: prev = sales/you-can-sell, next = sales/the-opportunity

- [ ] **Step 6: Create `sales/the-opportunity.html`**

Content — "The Opportunity" by Eben Pagan:
- Book overview: "Opportunity कशी शोधायची आणि कशी पकडायची — service business perspective मधून."
- 10 key points in Marathi with Instagram business context:
  1. **Opportunity is everywhere:** "तुमच्या गल्लीत 50 दुकानं आहेत. 40 चं Instagram नाही. = 40 opportunities."
  2. **Solve real problems:** "Business owner ला customers हवेत. तुम्ही Instagram वरून customers आणता. = Real problem, real solution."
  3. **Position yourself as expert:** "तुम्ही playbook वाचलंय, tools शिकलंय, practice केलंय. = तुम्ही expert आहात — या niche मध्ये."
  4. **Value-based selling:** "₹10,000/month expensive नाही — जर त्यातून 5 new patients/customers आले."
  5. **Start small, prove, expand:** "एक client, एक niche. Prove करा. मग expand करा."
  6. **The gap:** "Business owner ला Instagram चालवायला वेळ नाही. तुम्ही तो gap fill करताय."
  7. **First-mover advantage:** "तुमच्या area मध्ये अजून कोणी हे करत नाही. = First mover."
  8. **Service > Product:** "तुम्ही product विकत नाही — service देताय. Service = relationship."
  9. **Create your own opportunity:** "Client नाही? Sample बनवा, दाखवा. Opportunity create करा."
  10. **Long-term thinking:** "पहिला client = ₹5,000. दोन वर्षांनी 5 clients = ₹50,000/month. Long game खेळा."
- "तुमच्या business साठी 3 takeaways":
  - Walk your street — opportunities are physical, not theoretical
  - Value frame: cost vs what client gets in return
  - Long game: build reputation, not quick money
- Nav: prev = sales/sell-like-crazy, next = sales/lets-build-a-company

- [ ] **Step 7: Create `sales/lets-build-a-company.html`**

Content — "Let's Build a Company" by Harish Bhat:
- Book overview: "Tata group कसं build झालं — brand, trust, long-term thinking. तुम्ही freelancer नाही — तुम्ही brand build करताय."
- 10 key points in Marathi with Instagram business context:
  1. **Trust is the brand:** "Tata म्हटलं की trust. तुमचं नाव म्हटलं की quality — हे build करा."
  2. **Customer obsession:** "Client चं Instagram तुमच्या स्वतःच्या पेक्षा important आहे. त्यांचा success = तुमचा success."
  3. **Consistency over brilliance:** "एक brilliant post पेक्षा 30 consistent posts जास्त powerful आहेत."
  4. **Long-term relationships:** "एक client 2 वर्षं ठेवणं > 10 clients 1 महिन्यात गमावणं."
  5. **Quality never compromised:** "Deadline miss करा, पण quality कमी करू नका."
  6. **Innovation:** "नवीन formats, नवीन tools शिका. Stagnant होऊ नका."
  7. **Give back:** "Community ला शिकवा, knowledge share करा. = More trust, more referrals."
  8. **Ethics in business:** "Client चे DMs वाचता, numbers बघता — confidentiality ठेवा. Always."
  9. **Build systems:** "प्रत्येक वेळी scratch पासून करू नका. Templates, processes, checklists बनवा."
  10. **Think like a company:** "तुम्ही एकटे असाल तरी — brand name ठेवा, professional invoice द्या, agreement बनवा."
- "तुमच्या business साठी 3 takeaways":
  - Brand = trust. Trust = repeat clients + referrals
  - Systems save time: templates, checklists, processes
  - Think long-term: 2-year plan, not 2-week plan
- Nav: prev = sales/the-opportunity, next = clients/kuthe-shodhayche

- [ ] **Step 8: Verify and commit**

```bash
git add sales/
git commit -m "feat: add sales section — 6 pages with book summaries and sales mindset"
```

---

## Task 10: Section 7 — Clients मिळवा (Leads)

**Files:**
- Create: `clients/kuthe-shodhayche.html`
- Create: `clients/pahila-contact.html`
- Create: `clients/call-strategy.html`
- Create: `clients/meeting-tips.html`
- Create: `clients/proposal-format.html`
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

- [ ] **Step 3: Create `clients/call-strategy.html`**

Content — Phone/video call strategy for client acquisition:
- Before the call:
  - Research the business: check their Instagram, website, Google reviews
  - Prepare 2-3 specific observations: "तुमची Google rating 4.5 आहे पण Instagram वर फक्त 200 followers — हे match होत नाही"
  - Have your sample posts ready to share (WhatsApp/email during call)
- The call structure (step-by-step script in Marathi):
  1. Introduction (30 sec): "नमस्कार, मी [नाव]. मी local businesses साठी Instagram content बनवतो."
  2. Observation (30 sec): share one specific thing you noticed about their business/online presence
  3. Value (1 min): explain what Instagram can do for their specific business — use examples from playbooks
  4. Offer (30 sec): "मी तुमच्यासाठी 2 free sample posts बनवतो — बघता? कोणतीही commitment नाही."
  5. Next step (15 sec): schedule a meeting or send samples on WhatsApp
- What to say vs what NOT to say (table):
  - Say: "तुमचे patients/customers Instagram वर search करतात" / Don't say: "तुमचं Instagram खूप वाईट आहे"
  - Say: "मी handle करतो, तुमचा वेळ वाचतो" / Don't say: "हे खूप सोपं आहे"
- Handling objections on phone:
  - "आम्हाला interest नाही" → "ठीक आहे. मी तरी 2 sample posts पाठवतो WhatsApp वर — बघा, आवडले तर सांगा."
  - "किती खर्च?" → "आधी sample बघा, मग बोलू — commitment नाही."
  - "वेळ नाही आत्ता" → "कधी convenient आहे? 5 मिनिटं पुरतील."
- Follow-up strategy: कधी follow up करायचं, किती वेळा, WhatsApp vs call
- Exercise: "तुमच्या list मधल्या 3 businesses ला call करा. Script follow करा. काय reaction आली ते लिहा."

- [ ] **Step 4: Create `clients/meeting-tips.html`**

Content — In-person/video meeting tips:
- Before the meeting:
  - Dress professionally (business casual — neat, clean)
  - Carry: phone with sample posts, printed 1-page proposal (optional but impressive), visiting card
  - Arrive 5 min early. Never be late — trust starts here.
- During the meeting — 7 rules:
  1. **Listen first:** पहिले 5 minutes — त्यांच्या business बद्दल विचारा. "तुमचे customers कसे येतात? कोणत्या challenges आहेत?"
  2. **Don't oversell:** "मी तुम्हाला 10,000 followers देतो" — हे कधीच बोलू नका
  3. **Show, don't tell:** Sample posts दाखवा — phone वर carousel swipe करा, reel दाखवा
  4. **Speak their language:** "ROI", "engagement rate" नाही — "नवीन customers येतील", "लोकांना तुमचं clinic माहीत होईल"
  5. **Be honest about timeline:** "Instagram चे results 2-3 months ला दिसतात. Overnight magic नाही."
  6. **Ask questions:** "तुम्हाला कोणत्या type चे patients/customers हवे आहेत?" — हे तुम्हाला content strategy ठरवायला मदत करतं
  7. **End with clear next step:** "मी तुम्हाला proposal पाठवतो. बघा, आवडलं तर पुढच्या week पासून सुरू करू."
- Body language tips:
  - Eye contact ठेवा
  - Phone silent/flip ठेवा (तुम्हीच social media manage करणार — तुम्ही phone बघत बसलात तर impression खराब)
  - Notepad ठेवा — त्यांचे points लिहा (shows you care)
- After the meeting:
  - Same day: WhatsApp/email — "धन्यवाद भेटीसाठी. मी proposal पाठवतो."
  - Within 24 hours: Send proposal
  - After 3 days: Gentle follow-up if no response
- `.warning` box: "पहिली meeting = first impression. तुम्ही professional आहात हे दाखवा. वेळेवर या, तयारी करून या, listen करा."
- Exercise: "Mirror समोर practice करा — 2-minute introduction + sample दाखवणं. Record करा, बघा, improve करा."

- [ ] **Step 5: Create `clients/proposal-format.html`**

Content — Professional proposal format:
- Why a proposal matters: "WhatsApp वर 'मी posts बनवतो, 5000 रुपये' — हे amateur वाटतं. एक proper proposal = तुम्ही serious आहात."
- 1-page proposal template (Marathi + English, ready to copy):
  - **Header:** तुमचं नाव/brand, client चं business name, date
  - **Section 1: तुम्हाला काय मिळेल (What You Get)**
    - X posts per month (carousel + reel mix)
    - Content calendar (monthly)
    - Hashtag strategy
    - Caption writing
    - [Optional] Story content
    - [Optional] Engagement management (reply to comments)
  - **Section 2: कसं काम होईल (How It Works)**
    - Week 1: Research + brand voice + calendar approval
    - Week 2 onwards: Content batch → approval → posting
    - Communication: weekly WhatsApp update
    - Approval: 48-hour window before posting
  - **Section 3: Investment**
    - Package A: Content creation only — ₹X/month
    - Package B: Content creation + posting + basic engagement — ₹Y/month
    - Payment: monthly, advance, UPI/bank transfer
  - **Section 4: Terms**
    - Minimum commitment: 1 month (first month = trial)
    - Content ownership: client's
    - Revisions: 2 per post included
    - Cancellation: 15-day notice
- Google Docs template link (create and share a public template)
- Canva proposal template alternative (more visual, impressive for creative clients)
- Tips:
  - Print it if meeting in person — physical document = professional
  - Customize for each client — don't send generic proposals
  - Include 1-2 sample posts in the proposal or as attachment
- Exercise: "Proposal template copy करा. तुमच्या sample business साठी fill करा. PDF बनवा."
- Nav links updated to include these 3 new pages in the flow

- [ ] **Step 6: Create `clients/pitch-and-pricing.html`**

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

- [ ] **Step 7: Create `clients/pahila-client.html`**

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

- [ ] **Step 8: Create `clients/grow-kara.html`**

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

- [ ] **Step 9: Create `clients/common-problems.html`**

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

- [ ] **Step 10: Verify and commit**

```bash
git add clients/
git commit -m "feat: add clients section — 9 pages on finding and managing clients"
```

---

## Task 11: Push to GitHub & Enable GitHub Pages

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
Task 1 (skeleton)      ← everything depends on this
Task 2 (शिका)         ← independent after Task 1
Task 3 (tools 1-5)    ← independent after Task 1
Task 4 (AI content)    ← independent after Task 1
Task 5 (scheduling)    ← independent after Task 1
Task 6 (dermatologist) ← independent after Task 1, benefits from Task 3-4 being done (cross-references)
Task 7 (gym)           ← independent after Task 1, benefits from Task 3-4 being done
Task 8 (DIY)           ← references tools section, better done after Tasks 3-4
Task 9 (sales)         ← independent after Task 1
Task 10 (clients)      ← benefits from Task 9 (sales mindset before tactics)
Task 11 (deploy)       ← after all other tasks
```

**Parallelizable:** Tasks 2, 3, 4, 5, 9 can all run in parallel after Task 1.
Tasks 6, 7 can run in parallel after Task 1 (ideally after 3-4).
Task 8 after Tasks 3-4.
Task 10 benefits from Task 9 being done first.
Task 11 last.
