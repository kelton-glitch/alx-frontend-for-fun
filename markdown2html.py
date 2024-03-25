#!/bin/usr/python3
import sys
import os.path


def convert_markdown_to_html(markdown_file, output_file):
    """
    Convert Markdown file to HTML.

    Args:
        markdown_file (str): Path to the Markdown file.
        output_file (str): Path to the output HTML file.

    Raises:
        FileNotFoundError: If the Markdown file does not exist.
    """
    if not os.path.exists(markdown_file):
        raise FileNotFoundError(f"Missing {markdown_file}")

    # Your code to convert Markdown to HTML goes here
    # Replace this comment with your actual implementation

    print(f"Markdown file '{markdown_file}' successfully converted to HTML and saved to '{output_file}'")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        convert_markdown_to_html(markdown_file, output_file)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    sys.exit(0)
