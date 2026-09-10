# Lukas Xue — Personal Bio Page

A single-page personal bio site deployed on GitHub Pages at `https://lukas-xue.github.io`.

## Project Structure

```
.
├── index.html          # The entire site — HTML + inline CSS, no JS
└── img/
    ├── aws.png         # AWS logo (Google Favicon API, 128px)
    ├── maersk.png      # Maersk logo (Google Favicon API, 128px)
    ├── emory.gif       # Emory University shield (external source)
    ├── trine.jpg       # Trine University seal (Wikipedia)
    ├── nanollada.png   # nanoLLaDA project logo (from GitHub repo)
    ├── cert-claude-architect.png
    ├── cert-ai-dlc.png
    ├── cert-ai-foundational.png
    ├── cert-ai-practitioner.png
    ├── cert-ml-engineer.png
    ├── cert-ml-specialty.png
    └── cert-developer.png
```

No build tools, no frameworks, no JavaScript. Just static HTML + CSS.

## How the Page is Organized

The page has three sections:

1. **Header** — Name, tagline, links to GitHub / LinkedIn / Google Scholar
2. **Timeline** — Nested vertical timeline with company/school logos
3. **Certifications** — Horizontal badge grid from Credly

### Timeline Structure

The timeline uses a two-level nesting pattern:

- **Top-level items** (`.tl-item`) — Major career blocks (AWS, Emory, Oxford)
- **Nested children** (`.tl-child` inside `.tl-children`) — Individual roles, internships, or education within a parent

Publications and open source projects are inline lists (`.tl-list`) attached to the relevant timeline entry rather than standalone sections.

## Updating Content

### Add a new role under AWS

Add a new `.tl-child` div inside the AWS `.tl-children` block. Follow the existing pattern:

```html
<div class="tl-child">
  <div class="tl-child-logo"><img src="img/aws.png" alt="AWS"></div>
  <div class="tl-date">MMM YYYY – MMM YYYY</div>
  <div class="tl-title">LEVEL · Team Name</div>
  <div class="tl-org">AWS</div>
  <div class="tl-desc">Description of work.</div>
</div>
```

### Add a new publication

Find the `.tl-list` with label "Publications" (under the Emory entry) and add a `<li>`:

```html
<li>
  <a href="https://link-to-paper">Paper Title</a>
  <span class="meta">· Authors · Venue, Year</span>
</li>
```

### Add a new open source project

Find the `.tl-list` with label "Open Source" (under the CMO entry) and add a `<li>`:

```html
<li>
  <a href="https://github.com/...">Project Name</a> — Short description.
  <span class="meta"><img src="https://img.shields.io/github/stars/OWNER/REPO?style=social" alt="stars" style="height:1.6em;vertical-align:-0.3em;margin-left:0.3rem"></span>
</li>
```

The star count badge auto-updates via [shields.io](https://shields.io). No action needed.

### Add a new certification

1. Download the badge image from Credly and save to `img/cert-NAME.png`
2. Add a new `.cert` block in the Certifications section:

```html
<a class="cert" href="https://www.credly.com/badges/BADGE-ID">
  <img src="img/cert-NAME.png" alt="Cert Name">
  <div class="cert-name">Full Certification Name</div>
  <div class="cert-date">Mon YYYY</div>
</a>
```

**To get badge images programmatically**, Credly has an undocumented JSON API:

```bash
curl -sL "https://www.credly.com/users/renhao-xue/badges.json" | python3 -m json.tool
```

Each badge object contains:
- `badge_template.image_url` — direct PNG URL for the badge
- `badge_template.name` — certification name
- `issued_at_date` — date earned
- `id` — badge ID (for the Credly link: `https://www.credly.com/badges/{id}`)

## Images & Logos

### Where logos come from

| Image | Source | Notes |
|-------|--------|-------|
| `aws.png` | `google.com/s2/favicons?domain=aws.amazon.com&sz=128` | Works reliably |
| `maersk.png` | `google.com/s2/favicons?domain=maersk.com&sz=128` | Works reliably |
| `emory.gif` | `cpa.uw.edu.pl/wp-content/uploads/2023/06/fb-emory.gif` | External; keep local copy |
| `trine.jpg` | Wikipedia (Trine University Angola seal) | Extracted via mobile Wikipedia HTML |
| `nanollada.png` | `raw.githubusercontent.com/Lukas-Xue/nanoLLaDA/main/logo.png` | From the repo |
| `cert-*.png` | Credly `images.credly.com/images/{id}/image.png` | Via JSON API above |

### Adding a new company/school logo

1. Try Google Favicon API first: `https://www.google.com/s2/favicons?domain=DOMAIN&sz=128`
2. If that returns a tiny 16px image, try the company's press/brand page
3. For Wikipedia images: fetch the mobile page, grep for `upload.wikimedia.org` URLs, then `curl` the direct URL
4. Save to `img/` and reference as `img/filename.ext`

### Logo sizing

- Main timeline logos (`.tl-logo`): 40px circle, 36px image inside
- Emory uses `.tl-logo.padded` which shrinks the image to 30px for breathing room around the seal
- Child logos (`.tl-child-logo`): 30px circle, 26px image inside
- All use `object-fit: contain` so logos aren't cropped

## Dynamic Data

| Data | Auto-updates? | How |
|------|--------------|-----|
| GitHub stars (nanoLLaDA) | ✅ Yes | shields.io badge fetches live count |
| Citation counts | ❌ No | Google Scholar has no public API; omitted intentionally |
| Certification badges | ❌ No | Static images; re-download from Credly API if needed |

## Deployment

Push to a GitHub repo named `Lukas-Xue.github.io`. GitHub Pages serves from the root of the `main` branch automatically.

```bash
git init
git add index.html img/
git commit -m "feat: initial bio page"
git remote add origin git@github.com:Lukas-Xue/Lukas-Xue.github.io.git
git push -u origin main
```

The site will be live at `https://lukas-xue.github.io` within a few minutes.

## Local Preview

```bash
open index.html
# or
python3 -m http.server 8000  # then visit localhost:8000
```
