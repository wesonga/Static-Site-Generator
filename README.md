# Static-Site-Generator

A lightweight and customizable static site generator built from scratch. Designed for simplicity and flexibility, this tool transforms plain text and templates into fast, modern, and fully static websites — no frameworks, no unnecessary bloat.

## 📐 Architecture

Before diving into the code, here's a high-level overview of how this static site generator works.

### Flow of Data

1. **Markdown files** live in the `/content` directory. A `template.html` file is used for layout.
2. The static site generator (Python code in `/src/`) reads the Markdown and template files.
3. It **converts Markdown into HTML**, applies the template, and writes output to the `/public` directory.
4. A **Python HTTP server** serves files from `/public` to `http://localhost:8888`.
5. You open the browser and view the final site.

---

### System Diagram

![Architecture Diagram](./image.png) <!-- Adjust the path if necessary -->

---

### ⚙️ How the Static Site Generator (SSG) Works

Most of the action happens in the `/src/` directory. Here's a breakdown of the core steps:

1. **Clear the `/public` directory** to ensure a clean build.
2. **Copy static assets** (CSS, images, etc.) from `/static` to `/public`.
3. For each Markdown file in `/content`:
   - Read content and split it into logical blocks (e.g., paragraphs, headings, lists).
   - Convert Markdown blocks into a tree of `HTMLNode` objects.
     - For inline elements like bold text, links, etc.:
       ```
       Markdown -> TextNode -> HTMLNode
       ```
   - Combine all block nodes under a single parent `HTMLNode`.
   - Recursively call `.to_html()` on the root `HTMLNode` to generate the final HTML string.
   - Inject the generated content into `template.html`.
   - Write the final HTML file into `/public`.

---

### 🚀 Quick Run

To generate the static site and serve it locally:

```bash
# Generate the site
python3 src/main.py

# Serve the site locally
python3 -m http.server 8888
```

Then open http://localhost:8888 in your browser to view the site.

### 📂 Project Structure

```
project-root/
│
├── content/          # Markdown files
├── static/           # Static assets (images, CSS)
├── public/           # Output directory (generated site)
├── src/              # Static site generator code (Python)
└── template.html     # HTML template for all pages
```