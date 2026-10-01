#!/usr/bin/env python3
"""Static builder for iamzahirul.github.io — writes the HTML pages from shared chrome."""
import json, html, pathlib

ROOT = pathlib.Path(__file__).parent
SITE = "https://iamzahirul.github.io/"
NAME = "Md. Zahirul Islam"
EMAIL = "zahirul.islam@arced.foundation"
INTL_EMAIL = "zahirul.islam@arced-international.com"
GMAIL = "zahirul.islam.spa@gmail.com"
GSITE = "https://sites.google.com/view/zahirul97"
ORCID = "https://orcid.org/0000-0002-7167-178X"
PHONE = "+880 1688 831919"
PHONE_RAW = "+8801688831919"
TAGLINE = "Research & Evaluation • Project Management • Data Analytics • Monitoring & Learning"
LINKEDIN = "https://www.linkedin.com/in/zahirul-islam-dhaka/"
GITHUB = "https://github.com/zahirul-islam-dhaka"
X = "https://x.com/raselnet97"
FACEBOOK = "https://www.facebook.com/zahirulislam07"

NAV = [("index.html", "Home"), ("about.html", "About"), ("experience.html", "Experience"),
       ("projects.html", "Projects"), ("publications.html", "Publications"), ("contact.html", "Contact")]

ICONS = {
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.72v20.56C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.72V1.72C24 .77 23.2 0 22.22 0z"/></svg>',
 "github": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5A12 12 0 0 0 0 12.6c0 5.35 3.44 9.88 8.2 11.48.6.11.82-.26.82-.58v-2.1c-3.34.73-4.04-1.6-4.04-1.6-.55-1.4-1.33-1.78-1.33-1.78-1.09-.75.08-.74.08-.74 1.2.09 1.84 1.26 1.84 1.26 1.07 1.86 2.8 1.32 3.49 1.01.11-.79.42-1.32.76-1.63-2.67-.31-5.47-1.36-5.47-6.06 0-1.34.47-2.43 1.24-3.29-.12-.31-.54-1.56.12-3.25 0 0 1-.33 3.3 1.25a11.3 11.3 0 0 1 6 0c2.3-1.58 3.3-1.25 3.3-1.25.66 1.69.24 2.94.12 3.25.77.86 1.24 1.95 1.24 3.29 0 4.71-2.8 5.74-5.48 6.05.43.38.81 1.12.81 2.26v3.35c0 .32.22.7.83.58A12.02 12.02 0 0 0 24 12.6 12 12 0 0 0 12 .5z"/></svg>',
 "x": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.24 2H21.5l-7.5 8.57L22.8 22h-6.9l-5.4-7.06L4.3 22H1.04l8.02-9.17L.6 2h7.07l4.88 6.45L18.24 2zm-1.14 18h1.8L7.04 3.9H5.1L17.1 20z"/></svg>',
 "facebook": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.09 10.13 24v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.8-4.7 4.54-4.7 1.31 0 2.68.24 2.68.24v2.97h-1.51c-1.49 0-1.95.93-1.95 1.88v2.26h3.32l-.53 3.49h-2.79V24C19.61 23.09 24 18.1 24 12.07z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s7-6.1 7-12a7 7 0 1 0-14 0c0 5.9 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "download": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12M7 10l5 5 5-5M5 21h14"/></svg>',
 "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>',
 "clipboard": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V2h6v2M9 11h6M9 15h4"/></svg>',
 "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3 9 5-9 5-9-5 9-5z"/><path d="m3 13 9 5 9-5M3 18l9 5 9-5"/></svg>',
 "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M21.5 20a6.5 6.5 0 0 0-4.5-6.2"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5l-8-3z"/><path d="m9 12 2 2 4-4"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8.1 9.7a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.8 2z"/></svg>',
 "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>',
}

def head(title, desc, path):
    full = f"{title} · Zahirul Islam" if path != "index.html" else title
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="author" content="{NAME}">
<link rel="canonical" href="{SITE}{'' if path=='index.html' else path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(full)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{SITE}{'' if path=='index.html' else path}">
<meta property="og:image" content="{SITE}assets/img/zahirul-square.jpg">
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@raselnet97">
<meta name="theme-color" content="#0f2a44">
<link rel="icon" type="image/png" sizes="64x64" href="assets/img/icon-64.png">
<link rel="apple-touch-icon" href="assets/img/icon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script>try{{var t=localStorage.getItem('theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
</head>
<body>
<header class="site-header">
  <nav class="wrap nav" aria-label="Main">
    <a class="brand" href="index.html"><span class="brand-mark">ZI</span><span>Zahirul Islam</span></a>
    <ul class="nav-links" id="navLinks">
      {''.join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV)}
    </ul>
    <div class="nav-actions">
      <button class="icon-btn" id="themeToggle" type="button" aria-label="Toggle colour theme"></button>
      <button class="icon-btn menu-btn" id="menuBtn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    </div>
  </nav>
</header>
<main id="main">
"""

def foot(extra_js=""):
    return f"""</main>
<footer class="site-footer">
  <div class="wrap affil">
    <div class="affil-orgs">
      <a href="https://arced-international.com" target="_blank" rel="noopener"><strong>ARCED International</strong><span>{INTL_EMAIL}</span><span>arced-international.com</span></a>
      <span class="diamond" aria-hidden="true">◆</span>
      <a href="https://arced.foundation" target="_blank" rel="noopener"><strong>ARCED Foundation</strong><span>{EMAIL}</span><span>arced.foundation</span></a>
    </div>
    <div class="affil-me">
      <div class="affil-name">Zahirul Islam</div>
      <div class="affil-title">Senior Project Associate</div>
      <div class="affil-tag">{TAGLINE}</div>
      <div class="affil-tag"><a href="tel:{PHONE_RAW}">{PHONE}</a> · Dhaka, Bangladesh</div>
      <div class="affil-links">
        <a href="{GSITE}" target="_blank" rel="noopener">Google Site</a>{'<span>|</span><a href="'+ORCID+'" target="_blank" rel="noopener">ORCID</a>' if ORCID else ''}<span>|</span><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a><span>|</span><a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a>
      </div>
    </div>
  </div>
  <div class="wrap">
    <div>© <span id="year">2026</span> {NAME} · Dhaka, Bangladesh</div>
    <div class="social" aria-label="Social links">
      <a href="mailto:{EMAIL}" aria-label="Email">{ICONS['mail']}</a>
      <a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{ICONS['linkedin']}</a>
      <a href="{GITHUB}" target="_blank" rel="noopener" aria-label="GitHub">{ICONS['github']}</a>
      <a href="{X}" target="_blank" rel="noopener" aria-label="X (Twitter)">{ICONS['x']}</a>
      <a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook">{ICONS['facebook']}</a>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
{extra_js}
</body>
</html>
"""

def write(path, title, desc, body, extra_js=""):
    (ROOT / path).write_text(head(title, desc, path) + body + foot(extra_js), encoding="utf-8")
    print("wrote", path)

# ---------------------------------------------------------------- content
PROJECTS = json.loads((ROOT / "assets/js/_projects.json").read_text(encoding="utf-8"))
for p in PROJECTS:
    if p["period"] == "2024 – 2025":
        p["period"] = "Recent"

FEATURED = [
 ("Demand for Clean Air in the Workplace", "UC San Diego · Nov 2025 – Mar 2026",
  "Randomized field study in ready-made garment factories linking workplace air quality to worker productivity — calibrated PM2.5 monitors, smart-plug systems, attendance and productivity data, worker surveys.",
  ["RCT", "Sensor data", "SurveyCTO"], "layers"),
 ("Brick Kiln Tracker — 43 districts", "National University of Singapore · 2023 – present",
  "Technology-enabled randomized study to improve monitoring and enforcement of brick-kiln pollution: tracker and dashboard across 43 districts, workshops with Department of Environment officials, longitudinal follow-ups.",
  ["Dashboard", "GIS", "Government liaison"], "globe"),
 ("Impact Assessment of CDSP IV", "IFPRI & IFAD · Nov 2024 – Feb 2025",
  "Coastal char livelihoods impact assessment in Noakhali — Survey Solutions and SurveyCTO templates, listing/pilot/main surveys in Companiganj, Hatiya and Subarnachar, cleaned datasets to the PIs.",
  ["Survey Solutions", "Stata", "Impact evaluation"], "chart"),
 ("Skill for Growth — Human Capital & Labor-Market Frictions", "University of Minnesota · Apr 2024 – Feb 2025",
  "Large-scale study of manufacturing firms, managers and employees in Dhaka, Gazipur and Narayanganj: questionnaire development and testing, enumerator training, daily high-frequency checks.",
  ["Firm survey", "HFCs", "Training"], "users"),
 ("EZ-Bike Battery Market — Audit & Exit Surveys", "Stanford, Georgetown, ADB & PEDL · 2024 – 2025",
  "Mixed-methods audit study of dealer price, information and reputation trade-offs in the electric three-wheeler battery market, with an incentivized consumer-preference survey.",
  ["Audit study", "Circular economy", "SPSS"], "clipboard"),
 ("Household Air Filter Project", "UC San Diego · Dec 2022 – Mar 2025",
  "Randomized evaluation of air purifiers on health outcomes and willingness-to-pay in Pallabi and Mirpur — 40-household pilot, 1,000-household scale-up and a 2,500-household follow-on survey.",
  ["RCT", "Air-quality monitoring", "Power BI"], "shield"),
 ("Father Engagement in Humanitarian Play Labs", "New York University & LEGO Foundation · 2022 – 2023",
  "Impact evaluation of a father-engagement model for early childhood development in Rohingya camps and host communities — surveys with 1,000 fathers and 1,000 mothers of children aged 0–24 months.",
  ["Humanitarian", "ECD", "Panel survey"], "users"),
 ("Garments Whistleblowing Escrow — Endline", "Columbia, Princeton & Ben-Gurion · 2022 – present",
  "Endline surveys with 6,700 apparel workers across Dhaka, Savar, Narayanganj, Comilla and Chittagong to evaluate a whistleblowing escrow mechanism for worker protection.",
  ["Worker survey", "Multi-round", "Quality assurance"], "shield"),
 ("Shaping Student Mindsets for Climate Action", "World Bank · Mar – May 2024",
  "Student assessments and teacher interviews in 140 schools — 8,400 students and 560 teachers — covering tool translation, survey coordination, quality control and analysis.",
  ["Learning assessment", "Translation", "Analysis"], "chart"),
]

def feature_cards(items):
    out = []
    for title, meta, desc, tags, icon in items:
        out.append(f"""<article class="card feature reveal">
  <div class="card-icon">{ICONS[icon]}</div>
  <h3>{html.escape(title)}</h3>
  <div class="meta"><span>{html.escape(meta)}</span></div>
  <p>{html.escape(desc)}</p>
  <div class="foot">{''.join(f'<span class="chip">{html.escape(t)}</span>' for t in tags)}</div>
</article>""")
    return "\n".join(out)

CLIENTS = ["World Bank", "UC San Diego", "Stanford University", "Georgetown University", "IFPRI & IFAD", "New York University", "Columbia Business School", "Princeton University", "International Growth Centre", "ILO", "USAID", "IFRC", "Oxfam", "Save the Children",
           "Innovations for Poverty Action", "National University of Singapore", "MIT", "Yale University", "University of York",
           "Plan International", "Swisscontact", "ActionAid", "Action Against Hunger", "GAIN", "BRAC University", "Sesame Workshop", "Dalberg", "University of Bremen", "University of Minnesota"]

# ---------------------------------------------------------------- index
index_body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">ARCED International ◆ ARCED Foundation · Dhaka, Bangladesh</span>
      <h1>Turning field data into <span class="accent">evidence that decides.</span></h1>
      <p class="lede">I'm Zahirul Islam, Senior Project Associate at ARCED Foundation and part of the ARCED International team. For 13+ years I have designed, run and analysed surveys, impact evaluations and randomized controlled trials — 100+ projects for universities, UN agencies, governments and NGOs.</p>
      <div class="hero-tags">
        <span class="chip accent">Impact evaluation &amp; RCTs</span>
        <span class="chip">Stata · R · Python · SPSS</span>
        <span class="chip">SurveyCTO · ODK · KoBo</span>
        <span class="chip">Power BI · Tableau</span>
        <span class="chip">GIS</span>
      </div>
      <div class="hero-actions">
        <a class="btn btn-primary" href="projects.html">Explore projects {ICONS['arrow']}</a>
        <a class="btn btn-ghost" href="contact.html">Get in touch</a>
      </div>
    </div>
    <div class="portrait reveal">
      <img src="assets/img/zahirul.jpg" alt="Portrait of Md. Zahirul Islam" width="900" height="1200" fetchpriority="high">
      <div class="portrait-badge"><strong>13+ yrs</strong>research &amp; data practice</div>
    </div>
  </div>
</section>

<section class="section tight">
  <div class="wrap stats reveal">
    <div class="stat"><b>100+</b><span>research projects managed</span></div>
    <div class="stat"><b>8,400</b><span>students assessed in a single World Bank study</span></div>
    <div class="stat"><b>6,700</b><span>garment workers surveyed for one endline</span></div>
    <div class="stat"><b>30+</b><span>international partners served</span></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">What I do</span><h2>From questionnaire to dashboard</h2></div>
      <p>I cover the whole evidence pipeline — so findings reach clients clean, on time and defensible.</p>
    </div>
    <div class="grid grid-3">
      <article class="card reveal"><div class="card-icon">{ICONS['clipboard']}</div><h3>Study design &amp; instruments</h3><p>Sampling strategies, questionnaire development and translation, protocols and manuals, IRB and ethics compliance.</p></article>
      <article class="card reveal"><div class="card-icon">{ICONS['users']}</div><h3>Field &amp; team management</h3><p>Enumerator training, field supervision, back-checks and audio audits, daily reporting to PIs and clients — on CATI and in-person surveys.</p></article>
      <article class="card reveal"><div class="card-icon">{ICONS['layers']}</div><h3>Digital data systems</h3><p>SurveyCTO, ODK and KoBo form programming with built-in quality checks; data pipelines, cleaning and documentation in Stata, R and Python.</p></article>
      <article class="card reveal"><div class="card-icon">{ICONS['chart']}</div><h3>Analysis &amp; visualisation</h3><p>Descriptive and inferential analysis, rubric-based evaluation scoring, Power BI / Tableau / Looker Studio dashboards and GIS mapping.</p></article>
      <article class="card reveal"><div class="card-icon">{ICONS['shield']}</div><h3>M&amp;E systems &amp; evaluation</h3><p>Monitoring frameworks, indicator design and OECD-DAC evaluations for development programmes — from inception to final report.</p></article>
      <article class="card reveal"><div class="card-icon">{ICONS['globe']}</div><h3>Reporting &amp; proposals</h3><p>Evaluation reports, technical proposals and budgets for institutional tenders, plus web, graphics and document design.</p></article>
    </div>
  </div>
</section>

<section class="section band">
  <div class="wrap">
    <span class="eyebrow">Trusted by</span>
    <h2>Partners and clients</h2>
    <p class="muted" style="max-width:60ch">Research collaborations and consultancies delivered through ARCED Foundation and ARCED International since 2013.</p>
    <div class="logo-wall">{''.join(f'<span>{html.escape(c)}</span>' for c in CLIENTS)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Selected work</span><h2>Featured projects</h2></div>
      <a class="btn btn-ghost" href="projects.html">All {len(PROJECTS)} projects {ICONS['arrow']}</a>
    </div>
    <div class="grid grid-3">{feature_cards(FEATURED[:6])}</div>
  </div>
</section>

<section class="section tight">
  <div class="wrap grid grid-2">
    <article class="card reveal">
      <span class="eyebrow">Latest learning</span>
      <h3>Reproducible Research Fundamentals</h3>
      <p>Completed the World Bank course on reproducible research and BIGD's crash course on research communications (2025), alongside a series on data science, analytics, Power BI and machine-learning basics with Cambridge International Qualifications.</p>
      <div class="foot"><a href="about.html#training">See all training →</a></div>
    </article>
    <article class="card reveal">
      <span class="eyebrow">Writing</span>
      <h3>Publications &amp; reports</h3>
      <p>Peer-reviewed articles on economic growth in developing countries and on COVID-19 lockdowns and tobacco use; a preprint on urban mental health in Dhaka; study and evaluation reports for IFRC, USAID and others.</p>
      <div class="foot"><a href="publications.html">Browse publications →</a></div>
    </article>
  </div>
</section>

<section class="section">
  <div class="wrap center">
    <h2>Working on a survey, evaluation or data system?</h2>
    <p class="lede" style="margin-inline:auto">I'm open to research collaborations, evaluation assignments and data-management consultancies in Bangladesh and, through ARCED International, across East Africa.</p>
    <div class="hero-actions" style="justify-content:center;margin-top:20px">
      <a class="btn btn-primary" href="mailto:{EMAIL}">{ICONS['mail']} Email me</a>
      <a class="btn btn-ghost" href="{LINKEDIN}" target="_blank" rel="noopener">{ICONS['linkedin']} LinkedIn</a>
    </div>
  </div>
</section>
"""
write("index.html", "Zahirul Islam — Data Analyst & Research Specialist, Dhaka",
      "Official portfolio of Md. Zahirul Islam — Senior Project Associate at ARCED Foundation. 12+ years of survey research, impact evaluation and data analysis across 100+ projects in Bangladesh.",
      index_body)

# ---------------------------------------------------------------- about
SKILLS = [
 ("Statistics & analysis", ["Stata", "R", "SPSS", "Python (pandas, NumPy)", "Excel (advanced)", "Regression & ML basics"]),
 ("Data collection platforms", ["SurveyCTO", "ODK", "KoBoToolbox", "Survey Solutions", "CSPro", "SurveyMonkey", "Zoho Survey", "Microsoft Access"]),
 ("Dashboards & visualisation", ["Power BI", "Tableau", "Looker Studio", "Google Sites", "Excel dashboards"]),
 ("GIS & mapping", ["ArcGIS", "QGIS", "Google Earth"]),
 ("Research methods", ["RCTs & impact evaluation", "Baseline / midline / endline", "Tracer studies", "Audit & lab-in-the-field studies", "CATI phone surveys", "Qualitative (FGD, KII, IDI)", "High-frequency checks & back-checks", "OECD-DAC criteria"]),
 ("Project & M&E management", ["Work planning & Gantt", "Budgeting & rate cards", "Field team supervision", "Data quality assurance", "IRB / ethics compliance", "Technical proposal writing"]),
 ("Web, design & productivity", ["HTML5 / CSS3", "WordPress", "GitHub", "Photoshop", "Illustrator", "Figma", "InDesign", "Canva", "Video editing", "Microsoft 365", "Windows / Linux / macOS"]),
]
EDU = [
 ("2018 – 2019", "Professional Master of Development Studies (PMDS)", "Jagannath University, Dhaka"),
 ("2010 – 2012", "Master of Business Administration (MBA), Human Resource Management", "Atish Dipankar University of Science & Technology, Dhaka"),
 ("2005 – 2009", "Bachelor of Arts (BA)", "Pangsha Government College, National University of Bangladesh"),
]
TRAINING = [
 ("2025", "Reproducible Research Fundamentals", "The World Bank Group — Institute for Economic Development / DIME Analytics"),
 ("2025", "Crash Course on Effective Research Communications", "BRAC Institute of Governance and Development (BIGD), BRAC University"),
 ("2025", "WEkEO for Atmosphere Monitoring (workshop)", "Copernicus & Mercator Ocean International"),
 ("2025", "Data science & analytics series — Basics of Data Science; Descriptive Analytics; Data Cleaning; Univariate, Bivariate & Multivariate Analysis; NumPy; Microsoft Power BI; Regression Algorithms in Machine Learning; Agents & Environments in AI; Essentials of MS Excel – Formulas; Basics of Cyber Law", "UniAthena in partnership with Cambridge International Qualifications, UK (blockchain-verified certificates)"),
 ("—", "Human Subjects Research — Social-Behavioral-Educational (SBE) Foundations", "CITI Program"),
 ("2020", "Data Ethics, AI and Responsible Innovation", "The University of Edinburgh"),
 ("2019", "Research Ethics", "The Global Health Network"),
 ("2019", "Professional Communication and Etiquette", "Training with Rushdina"),
 ("2018", "Protecting Human Research Participants", "NIH Office of Extramural Research"),
 ("2016", "Professional Project Management (35-hour PMP preparation)", "Project Management Solutions Bangladesh"),
]
def rows(items):
    return "\n".join(f'<div class="row reveal"><div class="when">{html.escape(w)}</div><div><h3>{html.escape(t)}</h3><p>{html.escape(o)}</p></div></div>' for w,t,o in items)

about_body = f"""
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">About</span>
  <h1>Research is only useful when the data can be trusted.</h1>
  <p class="lede">That belief has shaped more than a decade of work at the intersection of field research, data systems and evaluation.</p>
</div></section>

<section class="section tight"><div class="wrap hero-grid" style="align-items:start">
  <div>
    <p>I am Md. Zahirul Islam, a Senior Project Associate at <strong>ARCED Foundation</strong> (Aureolin Research, Consultancy &amp; Expertise Development) in Dhaka, where I have worked since 2013. Over that time I have managed more than 100 research assignments — baseline, midline and endline assessments, impact evaluations, randomized controlled trials, tracer studies and large-scale listing surveys — for partners including the World Bank, Oxfam, Stanford, Georgetown, UC San Diego, IFPRI, ILO, USAID and Innovations for Poverty Action.</p>
    <p>My work usually begins before the first interview: contributing to research design and sampling, building the instruments, programming them in SurveyCTO or ODK with quality checks baked in, and training the teams who will use them. In the field I run the supervision, back-check and audio-audit routines that keep data honest, and report daily to principal investigators and clients. Afterwards I clean, document and analyse the data in Stata, R or Python, build the dashboards, and help write the report.</p>
    <p>Since 2026 I also work with <strong>ARCED International</strong>, the group's international consulting arm, as Survey Design &amp; Field Quality Assurance Specialist on evaluation and research bids in Kenya and East Africa — questionnaire programming, enumerator screening and training, high-frequency checks, back-checking and audio audits, consent registers and evidence ledgers. Before joining ARCED in 2013 I spent five years at Chowdhury Group as Senior Research Officer (R&amp;D), which is where my habit of building systems for other people to use began.</p>
    <p>I hold a Professional Master's in Development Studies from Jagannath University and an MBA in Human Resource Management. Outside work I build websites, tinker with data tools, and run a small mobile-accessories ecommerce business.</p>
  </div>
  <aside class="card">
    <img src="assets/img/zahirul-square.jpg" alt="" width="600" height="600" style="border-radius:12px;aspect-ratio:1;object-fit:cover">
    <h3 style="margin-top:6px">{NAME}</h3>
    <p>Senior Project Associate<br>ARCED International ◆ ARCED Foundation<br>Dhaka, Bangladesh</p>
    <p class="muted" style="font-size:.85rem">{TAGLINE}</p>
    <div class="meta"><span>{ICONS['pin']} Bangladesh (nationwide fieldwork)</span></div>
    <div class="foot">
      <span class="chip">English — fluent</span><span class="chip">Bangla — native</span><a class="chip" href="{ORCID}" target="_blank" rel="noopener">ORCID 0000-0002-7167-178X</a>
    </div>
    <div class="foot">
      <a class="btn btn-primary" href="contact.html">Contact</a>
      <a class="btn btn-ghost" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
    </div>
  </aside>
</div></section>

<section class="section" id="skills"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Toolkit</span><h2>Skills</h2></div><p>Tools I use week to week, grouped by the part of the pipeline they serve.</p></div>
  <div class="grid grid-3">
    {''.join(f'<div class="skill-group reveal"><h3>{html.escape(g)}</h3><div class="chips">{"".join(f"<span class=chip>{html.escape(s)}</span>" for s in ss)}</div></div>' for g,ss in SKILLS)}
  </div>
</div></section>

<section class="section tight" id="education"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Education</span><h2>Academic background</h2></div></div>
  <div class="rows">{rows(EDU)}</div>
</div></section>

<section class="section" id="training"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Continuous learning</span><h2>Training &amp; certifications</h2></div><p>Research ethics, reproducibility and data-science coursework that backs the practice.</p></div>
  <div class="rows">{rows(TRAINING)}</div>
</div></section>
"""
write("about.html", "About", "Background, skills, education and certifications of Md. Zahirul Islam — survey research, data analysis and evaluation specialist in Dhaka.", about_body)

# ---------------------------------------------------------------- experience
exp_body = f"""
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Experience</span>
  <h1>Thirteen years in the field and at the keyboard.</h1>
  <p class="lede">A career path through research operations, data systems and evaluation — with the roles I have held along the way.</p>
</div></section>

<section class="section tight"><div class="wrap hero-grid" style="align-items:start">
  <div class="timeline">
    <div class="tl-item reveal">
      <div class="when">2026 – present</div>
      <h3>Survey Design &amp; Field Quality Assurance Specialist</h3>
      <div class="org">ARCED International · Nairobi / Dhaka</div>
      <p>Technical team member on ARCED International's evaluation and research bids in Kenya and East Africa — ActionAid LRP evaluations, Christian Aid energy-access evaluation, IUCN CREATES baseline, MEDA climate-smart agriculture assessment and others. Owns questionnaire design and programming, enumerator screening and training, high-frequency checks, back-checking and audio audits, consent registers and evidence ledgers, and data cleaning and documentation.</p>
    </div>
    <div class="tl-item reveal">
      <div class="when">Jan 2023 – present</div>
      <h3>Senior Project Associate</h3>
      <div class="org">ARCED Foundation (Aureolin Research, Consultancy &amp; Expertise Development) · Dhaka</div>
      <p>Research Associate on university-led field experiments and evaluations — UC San Diego, Stanford, Georgetown, NYU, Columbia, Princeton, Minnesota, IFPRI/IFAD, NUS and the World Bank — from instrument design through field operations to clean, documented datasets.</p>
      <ul>
        <li>Clean-air and air-filter RCTs in garment factories and households (UC San Diego), with sensor, productivity and health data streams.</li>
        <li>Brick-kiln tracker and dashboard across 43 districts with the Department of Environment (NUS, 2023–present).</li>
        <li>CDSP IV impact assessment in coastal Noakhali (IFPRI/IFAD); Skill for Growth firm survey in Dhaka, Gazipur and Narayanganj (Minnesota).</li>
        <li>World Bank education studies: formative assessment impact evaluation, learning-loss assessment, teacher and student phone surveys, climate-action mindsets in 140 schools.</li>
        <li>Prepares technical and financial proposals, budgets and project archives; coordinates IRB submissions and data-security protocols; mentors junior staff.</li>
      </ul>
    </div>
    <div class="tl-item reveal">
      <div class="when">Jan 2020 – Dec 2022</div>
      <h3>Project Associate</h3>
      <div class="org">ARCED Foundation · Dhaka</div>
      <p>Study Coordinator and Field Manager on COVID-era research: World Bank remote-learning RCT and teacher surveys, REACH to TEACH virtual teacher training, GAIN price tracing, University of York internet-user study, IFRC market-based livelihoods assessment in Teknaf, Sesame Workshop early-learning baseline, USAID/MTaPS programme evaluation.</p>
    </div>
    <div class="tl-item reveal">
      <div class="when">May 2017 – Dec 2020</div>
      <h3>Project Assistant</h3>
      <div class="org">ARCED Foundation · Dhaka</div>
      <p>Survey and study coordination for tracer studies (ILO B-SEP across 47 districts, Swisscontact B-SkillFUL), baselines and evaluations for Oxfam, Plan International, BDRCS, Islamic Relief, Save the Children and Action Against Hunger; SurveyCTO programming, translation, audio checks and field reporting.</p>
    </div>
    <div class="tl-item reveal">
      <div class="when">May 2013 – Apr 2017</div>
      <h3>Junior Project Assistant</h3>
      <div class="org">ARCED Foundation · Dhaka</div>
      <p>Field supervision, data entry systems and analysis support on studies for IPA, MIT, BIGD/UCL, University of Warwick, SANEM, HELVETAS, Swisscontact and Terre des Hommes — the foundation years in data digitisation and field quality control.</p>
    </div>
    <div class="tl-item reveal">
      <div class="when">Aug 2008 – Apr 2013</div>
      <h3>Senior Research Officer (R&amp;D)</h3>
      <div class="org">Chowdhury Group</div>
      <p>Research and development support for the group's businesses — the start of a long habit of building systems other people can rely on.</p>
    </div>
  </div>
  <aside>
    <div class="card reveal">
      <span class="eyebrow">Responsibilities in brief</span>
      <div class="chips" style="display:flex;flex-wrap:wrap;gap:6px">
        {''.join(f'<span class="chip">{s}</span>' for s in ["Project management","Research design","Sampling","Instrument development","SurveyCTO programming","Field supervision","Back-checks & audio audits","Data cleaning","Statistical analysis","Dashboards","Report writing","Proposal writing","Budgeting","IRB & ethics","Team leadership","Client liaison"])}
      </div>
    </div>
    <div class="card reveal" style="margin-top:16px">
      <span class="eyebrow">Sectors</span>
      <div class="chips" style="display:flex;flex-wrap:wrap;gap:6px">
        {''.join(f'<span class="chip teal">{s}</span>' for s in ["Education & skills","Public health & nutrition","Climate resilience & agriculture","Gender & child protection","Labour markets & enterprise","Governance & public services","Humanitarian (Rohingya response)"])}
      </div>
    </div>
    <div class="card reveal" style="margin-top:16px">
      <span class="eyebrow">Geography</span>
      <p>Fieldwork in all eight divisions of Bangladesh, from the Chittagong Hill Tracts and Cox's Bazar camps to the northern chars and the southern coast. With ARCED International, now contributing to evaluations in Kenya, Tanzania, Malawi and Somalia.</p>
    </div>
  </aside>
</div></section>

<section class="section band"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Track record</span><h2>By the numbers</h2></div></div>
  <div class="stats">
    <div class="stat" style="background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.12)"><b style="color:#ffd38a">{len(PROJECTS)}</b><span style="color:#c9d4e2">assignments listed on this site</span></div>
    <div class="stat" style="background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.12)"><b style="color:#ffd38a">2013</b><span style="color:#c9d4e2">first assignment at ARCED</span></div>
    <div class="stat" style="background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.12)"><b style="color:#ffd38a">6,700</b><span style="color:#c9d4e2">garment workers in one endline survey</span></div>
    <div class="stat" style="background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.12)"><b style="color:#ffd38a">5</b><span style="color:#c9d4e2">countries in current bid portfolio</span></div>
  </div>
  <p style="margin-top:22px"><a href="projects.html">Browse the full project list →</a></p>
</div></section>
"""
write("experience.html", "Experience", "Professional experience of Md. Zahirul Islam — Senior Project Associate at ARCED Foundation, evaluation and data-systems roles since 2013.", exp_body)

# ---------------------------------------------------------------- projects
sectors = sorted({p["sector"] for p in PROJECTS})
years = sorted({p["year"] for p in PROJECTS if p["year"]}, reverse=True)
proj_body = f"""
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Projects</span>
  <h1>{len(PROJECTS)} assignments, 2013 to today.</h1>
  <p class="lede">Surveys, evaluations and data systems delivered with ARCED Foundation and ARCED International, as listed in my current CV. Search by topic, client or place, or filter by sector and year.</p>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Highlights</span><h2>Featured</h2></div></div>
  <div class="grid grid-3">{feature_cards(FEATURED)}</div>
</div></section>

<section class="section" id="all"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Complete list</span><h2>All projects</h2></div></div>
  <div class="toolbar">
    <input type="search" id="q" placeholder="Search title, client or location…" aria-label="Search projects">
    <select id="sector" aria-label="Filter by sector"><option value="">All sectors</option>{''.join(f'<option>{html.escape(s)}</option>' for s in sectors)}</select>
    <select id="yr" aria-label="Filter by year"><option value="">All years</option>{''.join(f'<option>{y}</option>' for y in years)}</select>
  </div>
  <div class="count" id="count"></div>
  <div class="plist" id="plist"></div>
</div></section>
"""
proj_js = """<script src="assets/js/projects-data.js"></script>
<script>
(function(){
  var q=document.getElementById('q'),sec=document.getElementById('sector'),yr=document.getElementById("yr"),list=document.getElementById('plist'),count=document.getElementById('count');
  function esc(s){return String(s||'').replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  function render(){
    var t=(q.value||'').toLowerCase().trim(),s=sec.value,y=yr.value,n=0,out=[];
    window.PROJECTS.forEach(function(p){
      if(s&&p.sector!==s)return; if(y&&String(p.year)!==y)return;
      if(t&&!(p.title+' '+p.client+' '+p.location+' '+p.role+' '+(p.summary||'')).toLowerCase().includes(t))return;
      n++;
      out.push('<article class="pitem"><div class="year">'+(p.year||'')+'<small>'+esc(p.period)+'</small></div><div><h4>'+esc(p.title)+'</h4>'+(p.summary?'<p class="psum">'+esc(p.summary)+'</p>':'')+'<div class="meta">'+(p.client?'<span><b>Client:</b> '+esc(p.client)+'</span>':'')+(p.role?'<span><b>Role:</b> '+esc(p.role)+'</span>':'')+(p.location?'<span><b>Location:</b> '+esc(p.location)+'</span>':'')+'</div></div><span class="chip">'+esc(p.sector)+'</span></article>');
    });
    list.innerHTML=out.length?out.join(''):'<div class="empty">No projects match that filter.</div>';
    count.textContent='Showing '+n+' of '+window.PROJECTS.length+' projects';
  }
  [q,sec,yr].forEach(function(el){el.addEventListener('input',render);});
  render();
})();
</script>"""
write("projects.html", "Projects", f"Full list of {len(PROJECTS)} research, survey and evaluation projects delivered by Md. Zahirul Islam since 2013 — searchable by sector, client and year.", proj_body, proj_js)

# ---------------------------------------------------------------- publications
PUBS = [
 ("Journal article", "Determinant on Economic Growth in Developing Country: A Special Case Regarding Turkey and Bangladesh",
  "Bazaluk, O., Kader, S. A., Zayed, N. M., Islam, Md. Zahirul, et al.",
  "Journal of the Knowledge Economy (Springer), 2024.",
  [("DOI", "https://doi.org/10.1007/s13132-024-01989-8")]),
 ("Journal article", "COVID-19 lockdowns and tobacco use among private university students in Dhaka, Bangladesh",
  "Ishaq, M., Islam, Md. E., Rahman, H., Rahman, & Islam, Md. Z.",
  "Global Journal for Research Analysis, Vol. 11, Issue 2, February 2022. Print ISSN 2277-8160. DOI 10.36106/gjra",
  [("Journal", "https://www.worldwidejournals.com/global-journal-for-research-analysis-GJRA/")]),
 ("Preprint", "An examination of residents' mental health in particular Dhaka City neighborhoods in the context of civic health and environmental well-being",
  "Gomes, R., & Islam, M.",
  "Research Square preprint, 2024.",
  [("DOI", "https://doi.org/10.21203/rs.3.rs-4333520/v1")]),
 ("Study report", "Building Sustainable Futures: Integrative Strategies for Disaster Resilience and Economic Empowerment in Cox's Bazar",
  "Islam, Md. Z., Chowdhury, R., & Alam, Md. M.",
  "Quantitative baseline of 908 Rohingya and host-community participants on disaster preparedness and livelihoods. ARCED Foundation with GUK, 2024.",
  []),
]
REPORTS = [
 ("2025", "Situation Analysis of Healthcare Waste Management in Bangladesh's Health Facilities", "USAID MTaPS Program — 41 health facilities; Study Coordinator"),
 ("2023", "End-line Evaluation of the Integrated Flood Resilience Programme, Phase 2", "International Federation of Red Cross and Red Crescent Societies — Data Analyst"),
 ("2022", "Baseline Study of USAID's Promoting Education for Early Learners Activity", "Sesame Workshop Bangladesh — KIIs with 107 teachers and headteachers, 844-parent phone survey"),
 ("2021", "A Market-based Livelihoods Assessment, Teknaf, Cox's Bazar", "British Red Cross / IFRC"),
 ("2021", "Program Evaluation: MTaPS-facilitated COVID-19 Response in Bangladesh", "USAID MTaPS Program"),
 ("2020", "Start Fund Bangladesh Midterm Evaluation — survey component", "Action Against Hunger"),
 ("2018 – 2019", "B-SEP and B-SkillFUL tracer studies", "ILO Bangladesh (47 districts); Swisscontact"),
]
pub_body = f"""
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Publications</span>
  <h1>Articles, reports and work in progress.</h1>
  <p class="lede">Peer-reviewed articles, a preprint, study reports and the evaluation reports I have contributed to as analyst, coordinator or author.</p>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Research writing</span><h2>Articles &amp; manuscripts</h2></div></div>
  <div class="rows">
  {''.join(f'''<article class="pub reveal"><span class="type">{html.escape(t)}</span><h3>{html.escape(ti)}</h3><div class="authors">{html.escape(a)}</div><div class="venue">{html.escape(v)}</div>{('<div class="links">'+''.join(f'<a href="{u}" target="_blank" rel="noopener">{html.escape(l)} ↗</a>' for l,u in links)+'</div>') if links else ''}</article>''' for t,ti,a,v,links in PUBS)}
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Grey literature</span><h2>Selected evaluation &amp; study reports</h2></div><p>Client reports are shared on request where the commissioning organisation permits.</p></div>
  <div class="rows">{rows(REPORTS)}</div>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Blog</span><h2>Field notes</h2></div></div>
  <div class="rows">
    <article class="pub reveal"><span class="type">Guest post</span><h3>Studying the Ready-Made Garments (RMG) sector in Bangladesh with ARCED Foundation</h3><div class="venue">SurveyCTO blog — on running factory-level surveys with digital data collection.</div><div class="links"><a href="https://www.surveycto.com/blog/" target="_blank" rel="noopener">SurveyCTO blog ↗</a></div></article>
  </div>
</div></section>
"""
write("publications.html", "Publications", "Journal articles, preprints, study reports and manuscripts by Md. Zahirul Islam on economic growth, public health, adolescent development and disaster resilience in Bangladesh.", pub_body)

# ---------------------------------------------------------------- contact
contact_body = f"""
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Contact</span>
  <h1>Let's talk about your data.</h1>
  <p class="lede">For research collaborations, evaluation assignments, data-system builds or speaking requests — email is the fastest way to reach me. Use the ARCED International address for Africa and international work, the ARCED Foundation address for Bangladesh.</p>
</div></section>

<section class="section tight"><div class="wrap contact-grid">
  <div>
    <ul class="contact-list">
      <li><span class="ic">{ICONS['mail']}</span><div><small>ARCED International</small><a href="mailto:{INTL_EMAIL}">{INTL_EMAIL}</a> · <a href="https://arced-international.com" target="_blank" rel="noopener">arced-international.com</a></div></li>
      <li><span class="ic">{ICONS['mail']}</span><div><small>ARCED Foundation</small><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://arced.foundation" target="_blank" rel="noopener">arced.foundation</a></div></li>
      <li><span class="ic">{ICONS['mail']}</span><div><small>Personal email</small><a href="mailto:{GMAIL}">{GMAIL}</a></div></li>
      <li><span class="ic">{ICONS['globe']}</span><div><small>Google Site</small><a href="{GSITE}" target="_blank" rel="noopener">sites.google.com/view/zahirul97</a></div></li>
      <li><span class="ic">{ICONS['linkedin']}</span><div><small>LinkedIn</small><a href="{LINKEDIN}" target="_blank" rel="noopener">linkedin.com/in/zahirul-islam-dhaka</a></div></li>
      <li><span class="ic">{ICONS['github']}</span><div><small>GitHub</small><a href="{GITHUB}" target="_blank" rel="noopener">github.com/zahirul-islam-dhaka</a></div></li>
      <li><span class="ic">{ICONS['x']}</span><div><small>X (Twitter)</small><a href="{X}" target="_blank" rel="noopener">@raselnet97</a></div></li>
      <li><span class="ic">{ICONS['facebook']}</span><div><small>Facebook</small><a href="{FACEBOOK}" target="_blank" rel="noopener">facebook.com/zahirulislam07</a></div></li>
      {'<li><span class="ic">'+ICONS['globe']+'</span><div><small>ORCID</small><a href="'+ORCID+'" target="_blank" rel="noopener">'+ORCID.replace('https://','')+'</a></div></li>' if ORCID else ''}
      <li><span class="ic">{ICONS['phone']}</span><div><small>Phone / WhatsApp</small><a href="tel:{PHONE_RAW}">{PHONE}</a></div></li>
      <li><span class="ic">{ICONS['pin']}</span><div><small>Location</small>Dhaka, Bangladesh (GMT+6)</div></li>
    </ul>
  </div>
  <div class="card">
    <h3>Send a message</h3>
    <p class="muted" style="font-size:.9rem">This form opens your email app with the message pre-filled — nothing is stored on this site.</p>
    <form class="form" id="contactForm">
      <label>Your name<input type="text" name="name" required autocomplete="name"></label>
      <label>Your email<input type="email" name="email" required autocomplete="email"></label>
      <label>Subject<input type="text" name="subject" required></label>
      <label>Message<textarea name="message" required></textarea></label>
      <button class="btn btn-primary" type="submit">Compose email {ICONS['arrow']}</button>
    </form>
  </div>
</div></section>
"""
contact_js = f"""<script>
document.getElementById('contactForm').addEventListener('submit',function(e){{
  e.preventDefault();var f=e.target;
  var body='Name: '+f.name.value+'\\nEmail: '+f.email.value+'\\n\\n'+f.message.value;
  location.href='mailto:{EMAIL}?subject='+encodeURIComponent(f.subject.value)+'&body='+encodeURIComponent(body);
}});
</script>"""
write("contact.html", "Contact", "Contact Md. Zahirul Islam — data analyst and research specialist in Dhaka, Bangladesh.", contact_body, contact_js)

# ---------------------------------------------------------------- 404, sitemap, robots, nojekyll
write("404.html", "Page not found", "Page not found.", """
<section class="section center"><div class="wrap">
  <span class="eyebrow">404</span><h1>That page has gone to the field.</h1>
  <p class="lede" style="margin-inline:auto">The link you followed doesn't exist here. Try the home page or the project list.</p>
  <div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" href="index.html">Home</a><a class="btn btn-ghost" href="projects.html">Projects</a></div>
</div></section>""")
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
  "".join(f"  <url><loc>{SITE}{'' if h=='index.html' else h}</loc></url>\n" for h,_ in NAV) + "</urlset>\n")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
(ROOT / ".nojekyll").write_text("")
print("done")
