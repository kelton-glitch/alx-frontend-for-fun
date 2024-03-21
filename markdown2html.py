#/usr/bin/python3
import sys
import markdown


def convert_markdown_to_html(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            markdown_text = f.read()
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    html_text = markdown.markdown(markdown_text)

    with open(output_file, 'w') as f:
        f.write(html_text)

if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)

    sys.exit(0)
