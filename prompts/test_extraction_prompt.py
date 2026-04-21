import json
import os
import re
import sys
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = "gpt-4.1-mini"


def load_env(path):
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def extract_prompt_sections(prompt_path):
    text = prompt_path.read_text(encoding="utf-8")
    fences = re.findall(r"```text\n(.*?)```", text, re.DOTALL)
    if len(fences) < 2:
        raise RuntimeError("Expected extraction.md to contain system and user text fences.")
    return fences[0].strip(), fences[1].strip()


def extract_pdf_text(pdf_path):
    reader = PdfReader(str(pdf_path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def main():
    load_env(ROOT / ".env")
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is not set in .env")

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise SystemExit("Missing dependency: pip install openai pypdf") from exc

    sample = sys.argv[1] if len(sys.argv) > 1 else "northstar-field-services"
    pdf_path = ROOT / "samples" / "pdfs" / f"{sample}.pdf"
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")

    system_prompt, user_template = extract_prompt_sections(ROOT / "prompts" / "extraction.md")
    cim_text = extract_pdf_text(pdf_path)
    user_prompt = user_template.replace("{{CIM_TEXT}}", cim_text)

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=os.environ.get("OPENAI_MODEL", DEFAULT_MODEL),
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    output_text = response.output_text
    parsed = json.loads(output_text)

    out_dir = ROOT / "outputs" / "prompt-tests"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{sample}.json"
    out_path.write_text(json.dumps(parsed, indent=2), encoding="utf-8")
    print(out_path)
    print(parsed.get("deal", {}).get("company_name"))
    print(parsed.get("recommended_next_step"))
    print(parsed.get("scoring", {}).get("overall_fit_score"))


if __name__ == "__main__":
    main()
