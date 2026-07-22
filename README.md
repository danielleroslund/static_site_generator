# 🌐 Static Site Generator

### A static site generator built from scratch in Python.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Pages](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-success?style=for-the-badge&logo=github)](https://danielleroslund.github.io/static_site_generator/)
[![View Live Demo](https://img.shields.io/badge/🚀-View%20Live%20Demo-success?style=for-the-badge)](https://danielleroslund.github.io/static_site_generator/)

A static site generator written in Python that converts Markdown files into a complete static website.

🌍 **Live Demo:**  
https://danielleroslund.github.io/static_site_generator/

---

## 📖 Overview

This project was built to better understand how static site generators work behind the scenes.

It reads Markdown files, converts them into HTML, applies a shared HTML template, copies static assets and generates a complete static website ready to be deployed with GitHub Pages.

Rather than relying on existing frameworks, I wanted to implement the entire generation pipeline myself while gaining a deeper understanding of parsing, templating, recursive page generation and static website architecture.

---

## 📸 Preview

Click the image below to view the live demo.

[![Static Site Generator Preview](images/preview.png)](https://danielleroslund.github.io/static_site_generator/)

---

## ✨ Features

- 📝 Convert Markdown files into HTML
- 📄 Generate pages using a reusable HTML template
- 📂 Support nested directories through recursive page generation
- 📰 Automatically generate pages from Markdown content
- 🖼️ Copy static assets including CSS and images
- 🧪 Comprehensive unit tests covering the Markdown parser and HTML generation pipeline
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
├── template.html     # Shared HTML template
├── build.sh          # Production build
├── main.sh           # Local development
└── test.sh           # Test suite
```

---

## 🏗️ Architecture

The generator follows a straightforward pipeline that transforms Markdown content into a complete static website.

```text
                content/
                    │
                    ▼
          Read Markdown Files
                    │
                    ▼
         Parse Markdown Blocks
                    │
                    ▼
          Generate HTML Nodes
                    │
                    ▼
        Extract Page Metadata
                    │
                    ▼
        Apply HTML Template
                    │
                    ▼
        Copy Static Assets
                    │
                    ▼
          Generate Website
              (docs/)
                    │
                    ▼
          Deploy with GitHub Pages
```

Each stage has a single responsibility, making the generator easy to understand, test and extend.

---

## ⚙️ How It Works

The build process follows these steps:

1. Read Markdown files from the `content` directory.
2. Parse the Markdown into structured HTML nodes.
3. Extract page titles and metadata.
4. Apply the shared HTML template.
5. Copy static assets such as CSS and images.
6. Recursively generate HTML pages inside the `docs` directory.
7. Deploy the generated website using GitHub Pages.

---

## 🌍 Example Output

The generated website includes:

- Home page
- Blog pages
- Contact page
- Shared navigation
- Automatically generated HTML pages

You can explore the finished website here:

👉 https://danielleroslund.github.io/static_site_generator/

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/danielleroslund/static_site_generator.git
```

Navigate into the project:

```bash
cd static_site_generator
```

Generate the website:

```bash
./main.sh
```

Create a production build:

```bash
./build.sh
```

Run the test suite:

```bash
./test.sh
```

---

## 📚 What I Learned

Building this project gave me hands-on experience with:

- Parsing Markdown into structured data
- HTML generation
- Recursive directory traversal
- Template-based page generation
- File system operations
- Unit testing
- Build automation with shell scripts
- Deploying static websites with GitHub Pages

---

## 🔮 Future Improvements

Some ideas I'd like to explore in the future:

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

Projects like this help me strengthen my software engineering fundamentals while deepening my understanding of the tools I use every day.

---

## 👋 Thanks for Visiting

Thanks for taking the time to check out this project!

If you found it interesting, feel free to explore my other repositories or connect with me on LinkedIn.

[![GitHub](https://img.shields.io/badge/GitHub-danielleroslund-181717?style=for-the-badge&logo=github)](https://github.com/danielleroslund)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Danielle%20Roslund-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/danielle-roslund/)
