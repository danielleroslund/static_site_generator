# 🌐 Static Site Generator

### Build static websites from Markdown using Python.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Pages](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-success?style=for-the-badge&logo=github)](https://danielleroslund.github.io/static_site_generator/)

A lightweight static site generator written in Python that converts Markdown files into a complete static website.

🌍 **Live Demo:** https://danielleroslund.github.io/static_site_generator/

---

## 📖 Overview

This project was built to better understand how static site generators work under the hood.

It reads Markdown files, converts them into HTML, applies a shared HTML template, copies static assets and generates a complete static website ready to be deployed with GitHub Pages.

Rather than relying on existing frameworks, I wanted to implement the complete generation pipeline myself and gain a deeper understanding of parsing, templating and static site generation.

---

## 📸 Preview

> *Add a screenshot of the generated website here.*

```md
![Preview](images/preview.png)
```

---

## ✨ Features

- 📝 Convert Markdown files into HTML
- 📄 Generate pages using a reusable HTML template
- 📂 Support nested directories through recursive page generation
- 📰 Automatically generate blog pages
- 🖼️ Copy static assets including CSS and images
- 🧪 Unit tested Markdown parser and HTML generation
- 🚀 Deploy the generated website using GitHub Pages

---

## 🛠️ Tech Stack

- Python
- HTML
- CSS
- Git
- GitHub Pages

---

## 📂 Project Structure

```text
.
├── content/          # Markdown content
├── docs/             # Generated website
├── src/              # Generator source code
├── static/           # CSS and images
├── template.html     # HTML template
├── build.sh          # Production build
├── main.sh           # Local development
└── test.sh           # Test suite
```

---

## ⚙️ How It Works

The generator follows a simple pipeline:

1. Read Markdown files from the `content` directory.
2. Parse Markdown into HTML.
3. Extract page titles.
4. Apply the shared HTML template.
5. Copy static assets.
6. Recursively generate the final website.
7. Output the generated site to the `docs` directory.

---

## 🌍 Example Output

The generated website includes:

- Home page
- Blog section
- Contact page
- Shared navigation
- Automatically generated HTML pages

You can view the generated site here:

**https://danielleroslund.github.io/static_site_generator/**

---

## 🚀 Getting Started

Clone the repository

```bash
git clone https://github.com/danielleroslund/static_site_generator.git
```

Navigate into the project

```bash
cd static_site_generator
```

Generate the website

```bash
./main.sh
```

Create a production build

```bash
./build.sh
```

Run the test suite

```bash
./test.sh
```

---

## 📚 What I Learned

This project helped me gain practical experience with:

- Markdown parsing
- HTML generation
- Recursive directory traversal
- Template-based page generation
- File system operations
- Unit testing
- Build automation with shell scripts
- Deploying static websites using GitHub Pages

---

## 🔮 Future Improvements

- YAML front matter
- Tags and categories
- Search functionality
- RSS feed generation
- Syntax highlighting
- Theme support
- Incremental builds

---

## 💡 Why I Built This

I enjoy understanding how software works beneath the surface.

Instead of relying on existing tools, I wanted to build a static site generator from scratch to better understand the technologies behind modern documentation sites and static website generators.

Projects like this help me strengthen my software engineering fundamentals while gaining a deeper understanding of the tools I use every day.
