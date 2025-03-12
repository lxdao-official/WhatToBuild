import os
import yaml
from datetime import datetime
import glob

def parse_idea_md(file_path):
    """Parse the idea markdown file and extract the metadata."""
    full_path = file_path if os.path.isabs(file_path) else os.path.join(os.getcwd(), file_path)
    relative_path = os.path.relpath(full_path, os.getcwd())
    
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            if '---' not in content:
                print(f"Error: No YAML frontmatter found in {file_path}")
                return None
                
            # Extract YAML part (between first two --- markers)
            parts = content.split('---', 2)
            if len(parts) < 3:
                print(f"Error: Invalid YAML frontmatter format in {file_path}")
                return None
                
            yaml_content = parts[1]
            
            # Parse YAML
            try:
                data = yaml.safe_load(yaml_content.strip())
                # Add file path to data
                data['file_path'] = relative_path
                return data
            except yaml.YAMLError as e:
                print(f"Error parsing YAML in {file_path}: {e}")
                return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def format_tags(tags):
    """Format tags as markdown code blocks."""
    if not tags:
        return ''
    return ', '.join([f'`{tag}`' for tag in tags])

def format_contributors(contributors):
    """Format contributors as GitHub links."""
    if not contributors:
        return ''
    
    result = []
    for c in contributors:
        github = c.get('github', '')
        if github:
            result.append(f'[{github}](https://github.com/{github})')
    
    return ', '.join(result)

def format_status(status):
    """Format status with appropriate emoji."""
    status_map = {
        'todo': '🔴',
        'analyzing': '🟡',
        'done': '🟢',
        # Fallbacks for old status names
        'ideation': '🔴',
        'in-progress': '🟡',
        'completed': '🟢'
    }
    
    if not status:
        return '🔴 todo'
    
    emoji = status_map.get(status.lower(), '🔴')
    return f'{emoji} {status}'

def generate_readme_content(ideas):
    """Generate the content for the README.md file."""
    # Start with the header
    content = [
        "# Idea List",
        "",
        "Welcome to the **Awesome Ideas Collection**! This is a place to share, discuss, and collaborate on innovative ideas in the Web3 space. Whether you have a groundbreaking DeFi concept, a novel DAO governance model, or a revolutionary NFT use case, we'd love to hear about it!",
        "",
        "This is a great idea.",
        "",
        "1. Fork this repository",
        "2. Copy the [template](template.md) to create your idea file in the `ideas/` folder with a descriptive name (e.g., `defi-lending-protocol.md`)",
        "3. Fill in all required fields in the template:",
        "   - `title`: A clear, descriptive name for your idea",
        "   - `description`: A concise explanation of what your idea does and why it matters",
        "   - `tags`: Relevant categories (e.g., ZK, DeFi, NFT, Wallet, DAO, Infra, Identity, Gaming, PublicGoods, Privacy, Security)",
        "   - `contributors`: Your GitHub username",
        "   - `status`: Current development stage (todo, analyzing, done)",
        "4. Add a detailed introduction including what, why, how, and related materials",
        "5. Submit a Pull Request",
        "6. After review and merge, your idea will be automatically added to this list",
        "",
        "## 🔍 Ideas List",
        "",
        "| Idea | Description | Tags | Contributors | Status |",
        "| ---- | ----------- | ---- | ------------ | ------ |"
    ]

    # Add each idea to the table
    for idea in ideas:
        title = f"[{idea.get('title', 'Untitled')}]({idea.get('file_path', '#')})"
        description = idea.get('description', 'No description provided')
        tags = format_tags(idea.get('tags', []))
        contributors = format_contributors(idea.get('contributors', []))
        status = format_status(idea.get('status', 'todo'))

        row = f"| {title} | {description} | {tags} | {contributors} | {status} |"
        content.append(row)

    # Add footer
    content.extend([
        "",
        "## 📊 Status Legend",
        "",
        "- 🔴 todo - Initial idea stage",
        "- 🟡 analyzing - Analysis in progress",
        "- 🟢 done - Ready to use",
        "",
        "---",
        "",
        f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
    ])

    return '\n'.join(content)

def scan_idea_files():
    """Scan the ideas directory for markdown files."""
    ideas_dir = os.path.join(os.getcwd(), 'ideas')
    if not os.path.exists(ideas_dir):
        print(f"Ideas directory not found: {ideas_dir}")
        return []
        
    return glob.glob(os.path.join(ideas_dir, '*.md'))

def generate_readme():
    """Generate the README.md from all idea files."""
    idea_files = scan_idea_files()
    print(f"Found {len(idea_files)} idea files")
    
    ideas = []
    for idea_file in idea_files:
        idea_data = parse_idea_md(idea_file)
        if idea_data:
            ideas.append(idea_data)
    
    # Sort ideas by title
    ideas.sort(key=lambda x: x.get('title', '').lower())
    
    # Generate and write README
    readme_content = generate_readme_content(ideas)
    readme_path = os.path.join(os.getcwd(), 'README.md')
    
    with open(readme_path, "w", encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"Updated README.md with {len(ideas)} ideas.")

if __name__ == '__main__':
    generate_readme()
