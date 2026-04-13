# InstaMarathi — Design Spec

**Date:** 2026-04-13
**Repo:** `instamarathi/instamarathi.github.io`
**URL:** `https://instamarathi.github.io`

---

## Overview

A free, open Marathi website that teaches people how to build a business running Instagram pages for local businesses. The audience has no existing business or client base — they start from zero and learn to become Instagram content creators/managers for hire.

## Audience

- Marathi speakers, smartphone users, comfortable with Instagram as users
- No existing business — looking to start one
- Range from not-very-tech-savvy to moderately comfortable
- Located in Maharashtra — their clients are local businesses (dentists, salons, gyms, cafes, etc.)

## Language & SEO

- **Content language:** Marathi-English mix (Minglish) — Marathi script with English terms where natural ("content", "client", "post", "hook", etc.)
- **URL slugs:** English (e.g., `/playbooks/dentist/`, `/tools/canva/`)
- **HTML lang:** `mr`
- **Meta tags:** English `<title>`, `<meta description>`, `<meta keywords>` for search engine discoverability
- **Prompts/templates:** Written in English (since LLMs respond better to English prompts), with Marathi explanations

## Tech

- Static HTML hosted on GitHub Pages
- Mobile-first design (audience is primarily on phones)
- Minimal CSS — fast loading, no framework bloat
- No JavaScript frameworks required — vanilla HTML/CSS, progressive enhancement only

## Site Structure

```
instamarathi.github.io/
├── index.html                          # Homepage
├── shika/                              # Section 2: Learn the business
│   ├── business-kya-aahe.html          # What is this business
│   ├── approach-kasa-karaycha.html     # How to approach businesses
│   ├── trust-build-kara.html           # Building trust & responsibility
│   └── common-questions.html           # FAQ & real expectations
├── tools/                              # Section 3: Hands-on toolkit
│   ├── canva.html                      # Design with Canva
│   ├── ai-images.html                  # AI image generation (Gemini, Bing)
│   ├── ai-images-advanced.html         # Advanced prompting & consistency
│   ├── capcut.html                     # Video editing with CapCut
│   ├── voiceover.html                  # Audio & AI voice
│   ├── ai-content/                     # LLM for content (multi-page)
│   │   ├── research.html               # 3.6a Niche research
│   │   ├── content-calendar.html       # 3.6b Calendar creation
│   │   ├── script-carousel.html        # 3.6c Carousel scripts
│   │   ├── script-reel.html            # 3.6d Reel scripts
│   │   ├── captions-hashtags.html      # 3.6e Captions & hashtags
│   │   ├── validation.html             # 3.6f Content validation
│   │   └── iteration.html              # 3.6g Draft to final
│   ├── scheduling.html                 # Scheduling & management
│   └── zero-budget-toolkit.html        # Free toolkit summary
├── playbooks/                          # Section 4: Ready-made niche playbooks
│   ├── index.html                      # Playbook listing
│   ├── dentist/                        # Dental niche playbook
│   │   ├── index.html                  # Niche overview
│   │   ├── brand-voice.html            # Brand voice template
│   │   ├── content-pillars.html        # Content pillars
│   │   ├── calendar.html               # 30-day content calendar
│   │   ├── content-kits.html           # 10 ready-made content kits
│   │   ├── hashtags.html               # Hashtag strategy
│   │   └── pitch.html                  # Client pitch template
│   ├── parenting/                      # Parenting niche playbook (same structure)
│   └── [future niches]/                # gym, salon, cafe, etc.
├── diy/                                # Section 5: Build your own playbooks
│   ├── niche-research.html             # Research any business
│   ├── brand-voice.html                # Capture client's voice
│   ├── content-pillars.html            # Define themes
│   ├── content-calendar.html           # Plan the month
│   ├── content-kits.html               # Script to final output
│   └── packaging.html                  # Deliver to client
├── clients/                            # Section 6: Find and win clients
│   ├── kuthe-shodhayche.html           # Where to find clients
│   ├── pahila-contact.html             # How to approach
│   ├── pitch-and-pricing.html          # Close the deal
│   ├── pahila-client.html              # First 30 days
│   ├── grow-kara.html                  # Scale to 5 clients
│   └── common-problems.html            # What can go wrong
└── assets/
    └── css/
        └── style.css                   # Single stylesheet
```

---

## Section Details

### Section 1: Homepage

**File:** `index.html`

Value proposition in Marathi: "Instagram वरून business कसं चालवायचं शिका — दुसऱ्यांसाठी. मराठीत."

Clear navigation paths into all 5 sections. Brief description of each section. No signup, no gate — everything open.

---

### Section 2: शिका (Learn) — The Business of Instagram Management

Not an Instagram tutorial. A guide to understanding the business of managing Instagram for others.

#### 2.1 हा Business काय आहे? (`shika/business-kya-aahe.html`)
- What an Instagram manager actually does
- Different avenues:
  - Full page management (content + posting + engagement)
  - Content creation only (carousels, reels — client posts themselves)
  - Strategy/consulting (audit + plan, client executes)
  - Campaign-based work (launch, event, seasonal)
- Which type suits which kind of person

#### 2.2 Business ला कसं approach करायचं (`shika/approach-kasa-karaycha.html`)
- How to identify businesses that need Instagram help
- Cold approach vs warm introduction
- What to say and what NOT to say
- How to pitch with a sample/demo (using playbooks as proof)
- Common reactions and how to handle them
- Realistic success rates — "10 ला approach केलं तर 1-2 होतील"

#### 2.3 Trust कसं build करायचं (`shika/trust-build-kara.html`)
- Why this is a responsibility, not just a gig
- Handling brand voice — it's their voice, not yours
- Communication cadence — approval flows, what to check before posting
- What to do when something goes wrong
- Confidentiality — you'll see their numbers, DMs, business info
- Being reliable — deadlines, consistency, no ghosting

#### 2.4 Common Questions & Real Expectations (`shika/common-questions.html`)
- "किती पैसे मिळतात?" — realistic pricing at different levels
- "मला design येत नाही" — you don't need to, here are the tools
- "client ने नाही म्हटलं तर?" — it's normal, keep going
- "किती clients handle करता येतात?" — capacity planning
- "contract लागतं का?" — simple agreements, payment terms
- "results नाही आले तर?" — setting expectations, what you control vs don't

---

### Section 3: Tools — तुमची Toolkit (Hands-On)

**Philosophy:** Every tool page follows: explain -> demonstrate -> exercise -> next step. All exercises use free tools. Each page ends with "हे exercise केलं? मग पुढे जा ->"

#### 3.1 Design — Canva (`tools/canva.html`)
- Step-by-step: account -> first carousel
- Exercise: "या text चा 5-slide carousel बनवा" (exact text given)
- Nuances: templates, font sizing for mobile, brand colors
- Exercise 2: Same content, different template

#### 3.2 AI Images — Gemini & Bing (`tools/ai-images.html`)
- Deep dive on Gemini for image generation
- Step-by-step prompt improvement progression:
  - Level 1: "dentist clinic" -> generic result
  - Level 2: "a warm, modern dental clinic in India, natural lighting" -> better
  - Level 3: Add style, mood, composition -> professional
  - Level 4: Specific shot types for Instagram
- Exercise: "हा prompt टाका, result बघा, मग improved prompt टाका — फरक बघा"
- Prompt templates per niche (dental, gym, salon, cafe)
- Common prompting mistakes with before/after
- Bing Image Creator as alternative

#### 3.3 AI Images — Advanced (`tools/ai-images-advanced.html`)
- Consistency across posts
- Marathi/Hindi text in images — challenges and workarounds
- Creating series/themes with consistent style
- Exercise: "एका salon साठी 4 posts च्या images बनवा — consistent style"

#### 3.4 Video — CapCut (`tools/capcut.html`)
- Step-by-step: install -> first reel (images + text + music)
- Exercise: "Canva carousel ला 30-second reel मध्ये convert करा"
- Transitions, timing, text animation — one feature at a time
- Exercise 2: Add music, adjust volumes

#### 3.5 Audio — Voiceover & AI Voice (`tools/voiceover.html`)
- DIY recording tips, room setup, speaking pace
- Exercise: "हा script वाचा आणि record करा"
- ElevenLabs step-by-step, free tier
- Exercise: "तोच script AI voice ने बनवा — compare करा"
- When to use own voice vs AI voice vs no voice

#### 3.6 AI for Content — Script Writing & Validation (multi-page)

##### 3.6a Research (`tools/ai-content/research.html`)
- Using LLM to research unfamiliar niches
- Prompt: "I'm creating Instagram content for a [dentist] in [Pune]. Tell me: top 10 patient questions, common fears, differentiators."
- Exercise: swap niche, compare results
- Cross-checking research with real sources

##### 3.6b Content Calendar (`tools/ai-content/content-calendar.html`)
- Prompt progression: vague -> specific -> production-ready
- Exercise: "salon साठी 2-week content calendar"
- Output format: date, type, topic, hook, CTA

##### 3.6c Carousel Scripts (`tools/ai-content/script-carousel.html`)
- Full workflow: brief -> first draft -> refine -> final
- Step 1: Brand voice rules + audience + topic to LLM
- Step 2: Slide-by-slide script
- Step 3: Refine weak hooks, get alternatives
- Exercise: dental carousel "root canal भयंकर नाही"

##### 3.6d Reel Scripts (`tools/ai-content/script-reel.html`)
- Structure: hook (3 sec) -> problem -> solution -> CTA
- Templates for 30-sec, 60-sec, 90-sec formats
- Voiceover script vs text-on-screen — different prompts
- Exercise: gym reel "3 mistakes beginners make"

##### 3.6e Captions & Hashtags (`tools/ai-content/captions-hashtags.html`)
- Caption formula: hook line -> value -> CTA -> hashtags
- Generating niche-specific hashtag sets
- Exercise: caption + hashtags for previous carousel

##### 3.6f Validation (`tools/ai-content/validation.html`)
- LLM as quality checker — self-review prompts:
  - Hook strength check
  - Brand voice compliance check
  - Audience relatability check
  - Comparison validation (multiple versions)
  - Factual accuracy check (critical for dental/medical niches)
- Exercise: "3.6c चा carousel script या 4 validation prompts मधून pass करा"

##### 3.6g Iteration (`tools/ai-content/iteration.html`)
- Full loop: write -> validate -> fix -> validate again
- Real example walkthrough: dental carousel from first prompt to final
- Exercise: "bakery साठी complete carousel — research ते final validated script"
- Pre-client checklist: hook, voice, accuracy, CTA, visuals

#### 3.7 Scheduling & Managing (`tools/scheduling.html`)
- Meta Business Suite step-by-step
- Exercise: "एक post schedule करा"
- Multiple client management — folders, naming
- Google Sheets calendar template (provided)

#### 3.8 Zero Budget Toolkit (`tools/zero-budget-toolkit.html`)
- Complete free toolkit list
- "पहिले पैसे आले — कशात invest करायचं?" priority
- Checklist: "मी ready आहे"

---

### Section 4: Playbooks — Ready-Made Niche Playbooks

Each playbook is a complete, copy-and-execute content system for one niche.

**Standard playbook structure (every niche follows this):**

1. **Niche Overview** — business dynamics, client needs, their customer base
2. **Brand Voice Template** — tone, do's/don'ts, example phrases
3. **Content Pillars** — 6-8 recurring themes
4. **30-Day Content Calendar** — date, format, topic, hook
5. **10 Ready-Made Content Kits** — each containing:
   - Carousel/reel script (slide-by-slide or second-by-second)
   - Caption with CTA
   - Hashtag set
   - AI image prompts (for Gemini/Bing)
   - Visual style notes
6. **Hashtag Strategy** — niche-specific sets (big/medium/small/branded)
7. **Client Pitch Template** — niche-specific approach script

**Launch niches:**
- Dentist (adapt from existing `/private/tmp/dentist/` dental playbook)
- Parenting (adapt from existing parenting channel playbook)

**Phase 2 niches (add incrementally):**
- Gym / fitness trainer
- Beauty parlour / salon
- Restaurant / cafe
- Coaching classes (tuition)
- Home baker / tiffin service
- Real estate agent
- Wedding photographer
- Doctor (general / specialist)
- CA / accountant
- Lawyer
- Event planner
- Boutique / clothing store
- Nursery / plant shop
- Veterinarian

---

### Section 5: स्वतः बनवा (DIY) — Create Playbooks for Any Niche

Teaching the skill of building playbooks independently.

#### 5.1 Niche Research (`diy/niche-research.html`)
- Study any unfamiliar business
- 10 questions to ask in first meeting
- Online research: reviews, competitors, Quora, YouTube
- LLM-assisted research (connects to 3.6a)
- Exercise: "गल्लीतला एक business निवडा — 10 प्रश्नांची उत्तरं शोधा"

#### 5.2 Brand Voice (`diy/brand-voice.html`)
- Why every business sounds different
- 5 questions that define a brand voice
- Writing a voice doc from a 20-minute conversation
- Exercise: "research केलेल्या business चा brand voice doc लिहा"

#### 5.3 Content Pillars (`diy/content-pillars.html`)
- What they are and why they prevent blank-page panic
- Formula: 2 educational + 2 emotional + 2 behind-the-scenes + 1 promotional + 1 community
- Deriving pillars from research
- Exercise: "6-8 content pillars लिहा"

#### 5.4 Content Calendar (`diy/content-calendar.html`)
- Weekly rhythm: pillar-to-day mapping
- Format balancing: carousels, reels, stories
- LLM calendar generation from pillars
- Exercise: "30-day calendar बनवा"

#### 5.5 Content Kits (`diy/content-kits.html`)
- Full integration: tools (Section 3) + LLM workflow (3.6) + brand voice (5.2)
- Pick calendar slot -> write script -> create visuals -> validate -> package
- Exercise: "पहिले 3 content kits बनवा — start to finish"

#### 5.6 Packaging (`diy/packaging.html`)
- Folder structure per client
- Approval workflow: what to send, how to get sign-off
- Google Drive / Notion handoff templates
- Exercise: "3 content kits organize करा — जसं client ला पाठवाल तसं"

---

### Section 6: Clients मिळवा (Leads) — Find and Win Clients

#### 6.1 कुठे शोधायचे (`clients/kuthe-shodhayche.html`)
- Walk your street — every shop with no/dead Instagram
- Google Maps search — check their Instagram
- Instagram local hashtag search
- WhatsApp groups, business associations
- JustDial, Sulekha, IndiaMART listings
- Exercise: "20 businesses शोधा — list बनवा"

#### 6.2 पहिला Contact (`clients/pahila-contact.html`)
- Cold walk-in vs DM vs WhatsApp vs mutual introduction
- 30-second pitch script
- Free sample strategy — create 2-3 posts before approaching
- What NOT to do
- Handling rejection
- Exercise: "1 business साठी free sample बनवा"

#### 6.3 Pitch & Pricing (`clients/pitch-and-pricing.html`)
- What to show: sample posts + 1-page proposal
- Pricing models: per post, monthly package, revenue share
- Realistic pricing ranges
- First client discount — why it's okay
- Simple agreement template
- Exercise: "1-page proposal बनवा"

#### 6.4 पहिला Client (`clients/pahila-client.html`)
- Onboarding: what to collect (photos, logos, preferences, login)
- First week: audit, present calendar
- Communication rhythm: weekly updates, monthly reports
- 30-day success expectations

#### 6.5 Grow करा (`clients/grow-kara.html`)
- Portfolio building — every client = case study
- Referrals: when and how to ask
- Testimonials: get early, use in pitches
- Expanding services
- Capacity: how many clients solo, when to say no

#### 6.6 Common Problems (`clients/common-problems.html`)
- Client doesn't respond to approvals
- Constant change requests — setting boundaries
- Results not coming — honest conversation framework
- Client wants to stop — graceful exit
- You made a mistake — damage control

---

## Launch Plan

**Phase 1 (Launch):**
- Homepage
- Section 2: शिका (all 4 pages)
- Section 3: Tools (all pages including AI content sub-pages)
- Section 4: 2 playbooks (dental + parenting)
- Section 5: स्वतः बनवा (all 6 pages)
- Section 6: Clients मिळवा (all 6 pages)

**Phase 2 (Post-launch, incremental):**
- Add niche playbooks one at a time (gym, salon, cafe, etc.)
- Each new playbook follows the standard structure
- Priority order based on demand / local business density

## Content Source Mapping

| New section | Existing source | Adaptation needed |
|---|---|---|
| Tools / Canva, CapCut, voiceover | `instagram-tutorial-marathi.md` Bhag 5, 7, 10 | Reframe for client work, add exercises |
| Playbooks / Dentist | `/private/tmp/dentist/content/`, `brand/`, `calendar/`, `growth/` | Translate brand voice to Marathi explanation, restructure into web pages |
| Playbooks / Parenting | `parenting-channel-playbook.json`, `parenting-playbook-marathi.md` | Extract playbook structure, restructure for web |
| Tools / AI prompting | Dental playbook's B-roll prompts, image prompts | Use as examples in prompting exercises |

## Design Principles

1. **Exercises before theory** — every tools page has hands-on exercises using free tools
2. **Step-by-step prompting** — teach prompt nuances progressively, not all at once
3. **Free tools only for exercises** — paid tools mentioned but never required
4. **Every playbook is standalone** — usable immediately by someone with zero experience
5. **Mobile-first** — audience is on phones, design accordingly
6. **LLM workflow is core** — research -> write -> validate -> iterate is the fundamental skill
7. **Marathi content, English SEO** — content in Minglish, meta tags in English
