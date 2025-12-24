from weasyprint import HTML
from jinja2 import Template
import os
from typing import Optional, Dict


def render_pdf_from_template(
    first_name: str,
    last_name: str,
    template_file: str = "template/index.html",
    output_file: str = "Saint Benet Biscop Catholic Academy Bedlington.pdf",
    write_local: bool = False,
) -> Dict:
    """
    Render a PDF from a Jinja2 HTML template.

    Args:
        first_name: First name
        last_name: Last name
        template_file: Path to the HTML template
        output_file: Output PDF filename
        write_local: If True, write PDF to disk

    Returns:
        dict with file_name and data (bytes)
    """
    base_dir = os.path.abspath(os.path.dirname(template_file))

    # Load and render template
    with open(template_file, encoding="utf-8") as f:
        template = Template(f.read())

    html_content = template.render(
        first_name=first_name,
        last_name=last_name,
    )

    html = HTML(string=html_content, base_url=base_dir)

    if write_local:
        # Ensure output directory exists
        output_path = os.path.abspath(output_file)
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

        html.write_pdf(output_path)
        with open(output_path, "rb") as f:
            pdf_bytes = f.read()
    else:
        pdf_bytes = html.write_pdf()

    return {
        "file_name": os.path.basename(output_file),
        "data": pdf_bytes,
    }

if __name__ == "__main__":
    # Example usage
    result = render_pdf_from_template(
        first_name="John",
        last_name="Doe",
        write_local=True,
    )
    print(f"Generated PDF: {result['file_name']} ({len(result['data'])} bytes)")