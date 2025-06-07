import os
from extract_title import extract_title
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown_content = file.read()
    
    with open(template_path, "r") as file:
        template_content = file.read()
    
    html_content = markdown_to_html_node(markdown_content).to_html()

    title = extract_title(markdown_content)

    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(full_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        source_entry_path = os.path.join(dir_path_content, entry)
        dest_entry_path = os.path.join(dest_dir_path, entry)
        
        if os.path.isfile(source_entry_path) and entry.endswith(".md"):
            relative_path = os.path.relpath(source_entry_path, dir_path_content)
            new_filename = os.path.splitext(relative_path)[0] + ".html"
            dest_path = os.path.join(dest_dir_path, new_filename)
            
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            generate_page(source_entry_path, template_path, dest_path)

        elif os.path.isdir(source_entry_path):
            generate_pages_recursive(source_entry_path, template_path, dest_entry_path)
