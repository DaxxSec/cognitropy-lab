#!/usr/bin/env python3
"""
update-readme-stats.py
Updates the cognitropy-lab README.md with shields.io badges and a summary stats table.
Run from within the cloned repo directory.

Usage: python3 update-readme-stats.py <repo_dir> [workspace_count] [categories_covered] [streak_days]
"""

import sys
import os
import re
import datetime

def count_workspaces(repo_dir):
    """Count workspace directories (non-hidden, non-file entries)."""
    count = 0
    skip = {'.git', '.github', '__pycache__', 'node_modules'}
    non_workspace_files = {'README.md', 'LICENSE', 'WORKSPACE_SPEC.md', 'cognitropy.py',
                           'cognitropy-dashboard.html', 'cognitropy-server', '.gitignore',
                           'awesome-list-pr-drafts.md', '.workspace-template'}
    for entry in os.listdir(repo_dir):
        full = os.path.join(repo_dir, entry)
        if os.path.isdir(full) and entry not in skip and not entry.startswith('.') and entry not in non_workspace_files:
            # Check if it looks like a workspace (has CLAUDE.md or README.md)
            if os.path.exists(os.path.join(full, 'CLAUDE.md')) or os.path.exists(os.path.join(full, 'README.md')):
                count += 1
    return count


def get_unique_categories(repo_dir):
    """Scan workspace CLAUDE.md files for category hints."""
    categories = set()
    cat_keywords = {
        'clearance': 'Security & Intelligence', 'vetting': 'Security & Intelligence',
        'intelligence-': 'Security & Intelligence', 'insider-threat': 'Security & Intelligence',
        'cyber': 'Cyber & DFIR', 'dfir': 'Cyber & DFIR', 'forensic': 'Cyber & DFIR',
        'malware': 'Cyber & DFIR', 'security': 'Cyber & DFIR', 'phishing': 'Cyber & DFIR',
        'rf': 'RF/SDR/Signals', 'sdr': 'RF/SDR/Signals', 'signal': 'RF/SDR/Signals',
        'wireless': 'RF/SDR/Signals', 'antenna': 'RF/SDR/Signals', 'tpms': 'RF/SDR/Signals',
        'ble': 'RF/SDR/Signals', 'satellite-comm': 'RF/SDR/Signals',
        'engine': 'Automotive & Engine', 'ecu': 'Automotive & Engine', 'auto': 'Automotive & Engine',
        'driveline': 'Automotive & Engine', 'vehicle': 'Automotive & Engine',
        'firmware': 'Hardware & Embedded', 'embedded': 'Hardware & Embedded', 'pcb': 'Hardware & Embedded',
        'fpga': 'Hardware & Embedded', 'iot': 'Hardware & Embedded',
        'marine-bio': 'Life Sciences', 'ecology': 'Life Sciences', 'bio': 'Life Sciences',
        'volcano': 'Earth Sciences', 'seismo': 'Earth Sciences', 'glacier': 'Earth Sciences',
        'limnology': 'Earth Sciences',
        'aquaponics': 'Food & Agriculture', 'farm': 'Food & Agriculture',
        'space': 'Space & Aviation', 'rocket': 'Space & Aviation', 'eva': 'Space & Aviation',
        'weather': 'Environmental & Earth', 'invasive': 'Environmental & Earth',
        'wildland': 'Environmental & Earth',
        'curriculum': 'Education & Training', 'education': 'Education & Training',
        'training': 'Education & Training', 'learning': 'Education & Training',
        'emergency': 'Medical & Health', 'triage': 'Medical & Health',
        'medical': 'Medical & Health', 'health': 'Medical & Health',
        'hydraulic': 'Engineering & Technical', 'engineering': 'Engineering & Technical',
        'mechanic': 'Engineering & Technical', 'fluid': 'Engineering & Technical',
        'expo': 'Computing & Software', 'debugger': 'Computing & Software',
        'software': 'Computing & Software',
        'avalanche': 'Outdoor & Adventure', 'bushcraft': 'Outdoor & Adventure',
        'mountaineering': 'Outdoor & Adventure', 'foraging': 'Outdoor & Adventure',
        'accounting': 'Finance & Economics', 'fraud': 'Finance & Economics',
        'railway': 'Transportation & Logistics', 'dam-safety': 'Engineering & Technical',
    }
    skip = {'.git', '.github', '__pycache__', 'cognitropy-server', '.workspace-template'}
    for entry in os.listdir(repo_dir):
        full = os.path.join(repo_dir, entry)
        if os.path.isdir(full) and not entry.startswith('.') and entry not in skip:
            name_lower = entry.lower()
            for keyword, category in cat_keywords.items():
                if keyword in name_lower:
                    categories.add(category)
                    break
    return categories


def calculate_streak(repo_dir):
    """Calculate consecutive build days from git log."""
    try:
        import subprocess
        result = subprocess.run(
            ['git', 'log', '--format=%aI', '--all'],
            capture_output=True, text=True, cwd=repo_dir
        )
        if result.returncode != 0:
            return 1
        dates = set()
        for line in result.stdout.strip().split('\n'):
            if line:
                date_str = line[:10]
                try:
                    dates.add(datetime.date.fromisoformat(date_str))
                except ValueError:
                    pass
        if not dates:
            return 1
        today = datetime.date.today()
        streak = 0
        check_date = today
        while check_date in dates:
            streak += 1
            check_date -= datetime.timedelta(days=1)
        return max(streak, 1)
    except Exception:
        return 1


def update_readme(repo_dir):
    readme_path = os.path.join(repo_dir, 'README.md')
    if not os.path.exists(readme_path):
        print(f"[WARN] README.md not found at {readme_path}")
        return False

    with open(readme_path, 'r') as f:
        content = f.read()

    ws_count = count_workspaces(repo_dir)
    categories = get_unique_categories(repo_dir)
    cat_count = len(categories)
    streak = calculate_streak(repo_dir)
    today_str = datetime.date.today().strftime('%Y-%m-%d')
    project_start = datetime.date(2026, 3, 26)
    project_days = (datetime.date.today() - project_start).days + 1

    # Build badges section
    badges = (
        f'![Workspaces](https://img.shields.io/badge/workspaces-{ws_count}-8b5cf6?style=flat-square&logo=github) '
        f'![Categories](https://img.shields.io/badge/categories-{cat_count}-06b6d4?style=flat-square) '
        f'![Streak](https://img.shields.io/badge/streak-{streak}%20days-10b981?style=flat-square) '
        f'![Last Build](https://img.shields.io/badge/last%20build-{today_str}-3b82f6?style=flat-square) '
        f'![Project Day](https://img.shields.io/badge/project%20day-{project_days}-f59e0b?style=flat-square)'
    )

    # Build stats table
    stats_table = f"""| Metric | Value |
|--------|-------|
| Total Workspaces | **{ws_count}** |
| Categories Covered | **{cat_count}** |
| Build Streak | **{streak} days** |
| Project Day | **{project_days}** |
| Last Build | **{today_str}** |
| Categories | {', '.join(sorted(categories)) if categories else 'N/A'} |"""

    # Markers for the auto-generated section
    start_marker = '<!-- COGNITROPY-STATS-START -->'
    end_marker = '<!-- COGNITROPY-STATS-END -->'

    stats_block = f"""{start_marker}

{badges}

### Project Statistics

{stats_table}

{end_marker}"""

    if start_marker in content and end_marker in content:
        # Replace existing stats block
        pattern = re.compile(
            re.escape(start_marker) + r'.*?' + re.escape(end_marker),
            re.DOTALL
        )
        content = pattern.sub(stats_block, content)
    else:
        # Insert after the first heading (# line)
        lines = content.split('\n')
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('# '):
                insert_idx = i + 1
                # Skip any blank lines or subtitle immediately after heading
                while insert_idx < len(lines) and (lines[insert_idx].strip() == '' or lines[insert_idx].startswith('>')):
                    insert_idx += 1
                break
        lines.insert(insert_idx, '\n' + stats_block + '\n')
        content = '\n'.join(lines)

    with open(readme_path, 'w') as f:
        f.write(content)

    print(f"[OK] README updated: {ws_count} workspaces, {cat_count} categories, {streak}-day streak")
    return True


if __name__ == '__main__':
    repo_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    update_readme(repo_dir)
