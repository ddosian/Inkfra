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
        section_html = f"""<div class="section" id="section-name-{section_name}">
BOXES
</div>"""
        if debug_output:
            print(f"current section: {section_name}")
            print(f"section content: {section_content}")
        all_box_html = ""
        for box_name, box_content in section_content.items():
            box_title = box_content["title"]
            box_description = box_content["description"]
            if debug_output:
                print(f"  box: {box_name}")
                print(f"  box content: {box_content}")
            box_html = f"""<div class="box" id="box-name-{box_name}">
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