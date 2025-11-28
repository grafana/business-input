#!/usr/bin/env python3
"""
Script to fix frontmatter in documentation markdown files.

This script:
- Makes all tags lowercase
- Replaces "tags" with "keywords"
- Removes quotation marks from "title" and "description" fields
- Adds "cloud" to the list of product labels
- Puts frontmatter in the order: title, menuTitle, description, keywords, labels, weight
- Removes anything that's not in the allowed fields
- Ensures a blank line between frontmatter and H1 heading
"""

import re
from pathlib import Path
try:
    import yaml
except ImportError:
    print("PyYAML not found. Installing...")
    import subprocess
    subprocess.check_call(['pip3', 'install', 'pyyaml'])
    import yaml


def parse_frontmatter(content):
    """
    Parse frontmatter from markdown content.
    Returns (frontmatter_dict, body)
    """
    # Match frontmatter between --- delimiters
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not match:
        return None, content
    
    frontmatter_text = match.group(1)
    body = match.group(2)
    
    try:
        # Parse YAML frontmatter
        frontmatter = yaml.safe_load(frontmatter_text)
        if frontmatter is None:
            frontmatter = {}
    except yaml.YAMLError as e:
        print(f"  ⚠ YAML parsing error: {e}")
        return None, content
    
    return frontmatter, body


def fix_frontmatter(frontmatter):
    """
    Fix frontmatter according to requirements:
    - Convert tags to keywords (lowercase)
    - Remove quotes from title and description (handled by YAML)
    - Add "cloud" to products
    - Keep only allowed fields
    """
    fixed = {}
    
    # Handle title
    if 'title' in frontmatter:
        fixed['title'] = str(frontmatter['title'])
    
    # Handle menuTitle (if present)
    if 'menuTitle' in frontmatter:
        fixed['menuTitle'] = str(frontmatter['menuTitle'])
    
    # Handle description
    if 'description' in frontmatter:
        fixed['description'] = str(frontmatter['description'])
    
    # Handle tags -> keywords (lowercase)
    if 'tags' in frontmatter:
        tags = frontmatter['tags']
        if isinstance(tags, list):
            # Convert all tags to lowercase
            keywords = [str(tag).lower() for tag in tags]
        else:
            keywords = [str(tags).lower()]
        fixed['keywords'] = keywords
    elif 'keywords' in frontmatter:
        # Already has keywords, just lowercase them
        keywords = frontmatter['keywords']
        if isinstance(keywords, list):
            fixed['keywords'] = [str(kw).lower() for kw in keywords]
        else:
            fixed['keywords'] = [str(keywords).lower()]
    
    # Handle labels - add cloud to products
    if 'labels' in frontmatter:
        labels = frontmatter['labels']
        if isinstance(labels, dict) and 'products' in labels:
            products = labels['products']
            if isinstance(products, list):
                products = [str(p) for p in products]
                # Add cloud if not present
                if 'cloud' not in products:
                    products.append('cloud')
                # Sort for consistency
                products.sort()
                fixed['labels'] = {'products': products}
            else:
                fixed['labels'] = {'products': [str(products), 'cloud']}
        else:
            # Create labels structure with cloud
            fixed['labels'] = {'products': ['cloud']}
    else:
        # No labels, create with cloud
        fixed['labels'] = {'products': ['cloud']}
    
    # Handle weight
    if 'weight' in frontmatter:
        fixed['weight'] = frontmatter['weight']
    
    return fixed


def format_frontmatter(frontmatter):
    """
    Format frontmatter in the correct order with proper YAML syntax.
    Order: title, menuTitle, description, keywords, labels, weight
    """
    lines = ['---']
    
    # Order of fields
    field_order = ['title', 'menuTitle', 'description', 'keywords', 'labels', 'weight']
    
    for field in field_order:
        if field not in frontmatter:
            continue
        
        value = frontmatter[field]
        
        if field in ['title', 'description', 'menuTitle']:
            # Simple string fields (no quotes)
            lines.append(f"{field}: {value}")
        elif field == 'keywords':
            # List field
            lines.append(f"{field}:")
            for item in value:
                lines.append(f"  - {item}")
        elif field == 'labels':
            # Nested dictionary
            lines.append(f"{field}:")
            if isinstance(value, dict):
                for key, val in value.items():
                    lines.append(f"  {key}:")
                    if isinstance(val, list):
                        for item in val:
                            lines.append(f"    - {item}")
                    else:
                        lines.append(f"    - {val}")
        elif field == 'weight':
            # Number field
            lines.append(f"{field}: {value}")
    
    lines.append('---')
    return '\n'.join(lines)


def ensure_blank_line_after_frontmatter(body):
    """
    Ensure there's exactly one blank line between frontmatter and H1 heading.
    """
    # Remove leading whitespace
    body = body.lstrip('\n')
    
    # Ensure one blank line before content
    if body:
        body = '\n\n' + body
    
    return body


def process_file(filepath):
    """
    Process a single markdown file to fix its frontmatter.
    """
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse frontmatter
    frontmatter, body = parse_frontmatter(content)
    
    if frontmatter is None:
        print(f"  ⚠ No frontmatter found, skipping")
        return False
    
    # Fix frontmatter
    fixed_frontmatter = fix_frontmatter(frontmatter)
    
    # Format frontmatter
    new_frontmatter = format_frontmatter(fixed_frontmatter)
    
    # Ensure blank line after frontmatter
    body = ensure_blank_line_after_frontmatter(body)
    
    # Combine
    new_content = new_frontmatter + body
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Updated")
    return True


def main():
    """
    Main function to process all markdown files in the sources folder.
    """
    # Get the script directory
    script_dir = Path(__file__).parent
    sources_dir = script_dir / 'docs' / 'sources'
    
    if not sources_dir.exists():
        print(f"Error: Sources directory not found at {sources_dir}")
        return
    
    # Find all markdown files
    md_files = list(sources_dir.rglob('*.md'))
    
    print(f"Found {len(md_files)} markdown files to process\n")
    
    processed = 0
    for md_file in sorted(md_files):
        if process_file(md_file):
            processed += 1
    
    print(f"\n✓ Successfully processed {processed}/{len(md_files)} files")


if __name__ == '__main__':
    main()
