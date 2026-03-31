#!/usr/bin/env python3
"""
regenerate-dashboard.py
Regenerates cognitropy-dashboard.html by importing the server's render_dashboard()
and writing the output to the static HTML file.

Usage: python3 regenerate-dashboard.py <output_path> [server_dir]

If server_dir is provided, it adds that to sys.path to import server.py.
Otherwise it looks for cognitropy-server/ relative to this script.
"""

import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 regenerate-dashboard.py <output_path> [server_dir]")
        sys.exit(1)

    output_path = sys.argv[1]

    # Determine server directory
    if len(sys.argv) >= 3:
        server_dir = sys.argv[2]
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        server_dir = os.path.join(script_dir, 'cognitropy-server')

    if not os.path.isdir(server_dir):
        print(f"[ERROR] Server directory not found: {server_dir}")
        sys.exit(1)

    # Add server dir to path and import
    sys.path.insert(0, server_dir)

    try:
        import server
        html = server.render_dashboard()

        with open(output_path, 'w') as f:
            f.write(html)

        print(f"[OK] Dashboard regenerated: {output_path} ({len(html):,} bytes)")
        return True

    except Exception as e:
        print(f"[ERROR] Failed to regenerate dashboard: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
