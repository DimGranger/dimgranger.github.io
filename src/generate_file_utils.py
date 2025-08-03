import os

from block_utils import markdown_to_blocks
from markdown_utils import markdown_to_html_node


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for x in blocks:
        if len(x) > 2 and x[:2] == "# ":
            return x[2:].strip()
    raise Exception

def generate_file(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as md, open(template_path, "r") as template, open(dest_path, "w") as destination:
        md_string = md.read()
        html_string = markdown_to_html_node(md_string).to_html()
        title = extract_title(md_string)
        result = template.read().replace("{{ Title }}", title)
        result = result.replace("{{ Content }}", html_string)
        result = result.replace('href="/', f'href="{base_path}')
        result = result.replace('src="/', f'src="{base_path}')
        destination.write(result)

def generate_files_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    all_items = os.listdir(dir_path_content)

    for x in all_items:
        source_path = os.path.join(dir_path_content, x)
        destination_path = os.path.join(dest_dir_path, x)

        if os.path.isfile(source_path):
            write_path = destination_path[:-3] + ".html"
            generate_file(source_path, template_path, write_path, base_path)
        if os.path.isdir(source_path):
            os.mkdir(destination_path)
            generate_files_recursive(source_path, template_path, destination_path, base_path)


