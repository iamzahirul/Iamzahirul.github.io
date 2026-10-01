# iamzahirul.github.io — portfolio website

Static, dependency-free multi-page site for **Md. Zahirul Islam**. Works directly on GitHub Pages (no Jekyll build — `.nojekyll` is included).

## Pages
| File | Content |
|---|---|
| `index.html` | Home — hero, stats, services, partners, featured projects |
| `about.html` | Bio, skills, education, training & certifications |
| `experience.html` | Career timeline, responsibilities, sectors |
| `projects.html` | Featured projects + searchable list of 75 assignments |
| `publications.html` | Articles, manuscripts, evaluation reports, blog |
| `contact.html` | Contact details + mailto form |
| `404.html`, `sitemap.xml`, `robots.txt` | Housekeeping |

Assets live in `assets/` (CSS, JS, images). The project list is data-driven: edit `assets/js/projects-data.js` to add or change an assignment — no HTML edits needed.

## Deploy to GitHub Pages
1. In the `Iamzahirul.github.io` repository, delete the old Jekyll files (`_config.yml`, `index.md`, etc.).
2. Copy **everything in this folder** (including the hidden `.nojekyll`) into the repository root.
3. Commit and push to the `main` branch:
   ```bash
   git add -A
   git commit -m "New portfolio website"
   git push origin main
   ```
4. GitHub → Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
5. The site goes live at https://iamzahirul.github.io/ within a minute or two.

## Editing
- Text changes: edit the HTML files directly, **or** edit `build.py` and run `python3 build.py` to regenerate all pages from one place (recommended — header/footer stay consistent).
- Photo: replace `assets/img/zahirul.jpg` (3:4 portrait) and `assets/img/zahirul-square.jpg` (1:1, used for the About card and social previews).
- Colours and fonts: `assets/css/style.css` — the `:root` block holds the palette; dark mode is automatic and can be toggled from the header.
