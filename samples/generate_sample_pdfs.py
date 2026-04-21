from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parent
SRC_DIR = ROOT / "cims"
OUT_DIR = ROOT / "pdfs"


def markdown_table_to_rows(lines):
    rows = []
    for line in lines:
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and not all(set(cell) <= {"-", ":"} for cell in cells):
            rows.append(cells)
    return rows


def add_table(story, lines, styles):
    rows = markdown_table_to_rows(lines)
    if not rows:
        return
    table = Table(rows, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f4e5f")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#c9d3d8")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f6f8f9")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 0.12 * inch))


def build_pdf(markdown_path):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="DealTitle", parent=styles["Title"], fontSize=18, leading=22, spaceAfter=14))
    styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"], fontSize=12, leading=15, spaceBefore=10))
    styles.add(ParagraphStyle(name="Body", parent=styles["BodyText"], fontSize=9.5, leading=13, spaceAfter=7))
    styles.add(ParagraphStyle(name="BulletText", parent=styles["BodyText"], fontSize=9.5, leading=13, leftIndent=14, firstLineIndent=-8))

    output_path = OUT_DIR / f"{markdown_path.stem}.pdf"
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        rightMargin=0.6 * inch,
        leftMargin=0.6 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        title=markdown_path.stem,
    )

    story = []
    lines = markdown_path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith("# "):
            story.append(Paragraph(line[2:], styles["DealTitle"]))
        elif line.startswith("## "):
            story.append(Paragraph(line[3:], styles["Section"]))
        elif line.startswith("- "):
            story.append(Paragraph(f"- {line[2:]}", styles["BulletText"]))
        elif line.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            add_table(story, table_lines, styles)
            continue
        else:
            story.append(Paragraph(line, styles["Body"]))
        i += 1

    doc.build(story)
    return output_path


def main():
    OUT_DIR.mkdir(exist_ok=True)
    for markdown_path in sorted(SRC_DIR.glob("*.md")):
        output_path = build_pdf(markdown_path)
        print(output_path)


if __name__ == "__main__":
    main()
