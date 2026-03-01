def generate_tags(file, debug_output):
    if debug_output:
        print(f"Generating tags from {file}")
    tags = file["tags"]
    if debug_output:
        print(f"Tags:\n{tags}")
    all_tags = " · ".join(tag for tag in tags)
    if debug_output:
        print(f"all tags html:\n{all_tags}")
    return all_tags

def generate_body(file, debug_output):
    if debug_output:
        print(f"Generating body from {file}")
    content = file["content"]
    if debug_output:
        print(f"Content:\n{content}")

    all_section_html = ""
    for section_name, section_content in content.items():
        section_friendly_name = section_content["name"] if "name" in section_content else section_name
        section_html = f"""<div class="section" id="section-name-{section_name}">
<span class="section-label">{section_friendly_name}</span>        
<div class="section-row">
BOXES
</div>
</div>"""
        if debug_output:
            print(f"current section: {section_name}")
            print(f"section content: {section_content}")
        all_box_html = ""
        for box_name, box_content in section_content.items():
            if box_name in ["name"]:
                continue
            box_icon = box_content["icon"]
            box_icon_html = f"""<iconify-icon class="box-icon" icon="{box_icon}"></iconify-icon>"""
            box_title = box_content["title"]
            box_description = box_content["description"]
            box_category = box_content["category"] if "category" in box_content else "uncategorized"
            if debug_output:
                print(f"  box: {box_name}")
                print(f"  box content: {box_content}")
            box_html = f"""<div class="box category-{box_category}" id="box-name-{box_name}">
{box_icon_html}
<span class="box-title">{box_title}</span>
<span class="box-description">{box_description}</span>
</div>"""
            all_box_html += box_html
        if debug_output:
            print(f"all box html:\n{all_box_html}")
        section_html = section_html.replace("BOXES", all_box_html)
        if debug_output:
            print(f"section html:\n{section_html}")
        all_section_html += section_html
    if debug_output:
        print(f"all section html\n{all_section_html}")
    return all_section_html

def generate_category_css(content, debug_output):
    if debug_output:
        print(f"Generating category CSS from {content}")
    categories = content["categories"]
    all_category_css = ""
    for category_name, category_content in categories.items():
        if debug_output:
            print(f"current category: {category_name}")
            print(f"category content: {category_content}")
        category_color = category_content["color"]
        category_css = f""".category-{category_name} {{
background-color: color-mix(in srgb, var(--{category_color}) 15%, transparent);
border: 1px solid var(--{category_color});
}}"""
        all_category_css += category_css
    return all_category_css