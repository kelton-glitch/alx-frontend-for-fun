#!/bin/usr/python3
import sys
import os.path

def convert_markdown_to_html(markdown_file, output_file):
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Your code to convert Markdown to HTML goes here
    # Replace this comment with your actual implementation

    print(f"Markdown file '{markdown_file}' successfully converted to HTML and saved to '{output_file}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)
    sys.exit(0)
