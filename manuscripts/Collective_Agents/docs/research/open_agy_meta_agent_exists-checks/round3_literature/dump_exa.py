"""Condense the Exa agent_run JSON result into plain text for reading.

Usage: python -I dump_exa.py <input_json> <output_txt>
Reads only; uses the standard library json module.
"""
import json
import sys


def main() -> None:
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    out = []
    out.append(f"status={data.get('status')} stopReason={data.get('stopReason')}")
    out.append(f"cost={data.get('costDollars')}")
    output = data.get("output", {}) or {}
    structured = output.get("structured", {}) or {}
    synth = structured.get("synthesis", {}) or {}
    out.append("=== SYNTHESIS ===")
    for key in ("topic_i", "topic_ii", "topic_iii", "topic_iv"):
        out.append(f"--- {key}\n{synth.get(key, '')}")
    out.append("=== NOT FOUND ===")
    for item in structured.get("not_found", []) or []:
        out.append(f"* {item}")
    out.append("=== SOURCES ===")
    for i, s in enumerate(structured.get("sources", []) or [], 1):
        out.append(
            f"[{i}] topic={s.get('topic')} | verified={s.get('verified_from_full_text')}\n"
            f"  citation: {s.get('citation')}\n"
            f"  doi: {s.get('doi')} | arxiv: {s.get('arxiv')} | url: {s.get('full_text_url')}\n"
            f"  locator: {s.get('locator')}\n"
            f"  statement: {s.get('statement')}\n"
            f"  bearing: {s.get('bearing')}"
        )
    text = output.get("text", "") or ""
    out.append("=== TEXT (first 6000 chars) ===")
    out.append(text[:6000])
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print(f"wrote {dst}; sources={len(structured.get('sources', []) or [])}; text_len={len(text)}")


if __name__ == "__main__":
    main()
