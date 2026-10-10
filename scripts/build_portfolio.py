#!/usr/bin/env python3
"""Build Siddhartha Gupta's four-page internship portfolio from repo assets.

Requires reportlab, Pillow, pypdf and PyMuPDF. Optional --render writes QA PNGs.
Content is grounded in the four project pages and the L'SPACE overview/PDR.
Rover content distinguishes the mechanical design from planned simulation work.
"""

from __future__ import annotations

import argparse
import io
import json
from pathlib import Path
import shutil

from PIL import Image, ImageChops
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "public/assets"
OUT = ROOT / "output/pdf/siddhartha-gupta-engineering-portfolio.pdf"
PUBLIC = ASSETS / OUT.name
QA = ROOT / "tmp/pdfs"
W, H = 612, 792
M, CONTENT = 38, 536
GUTTER = 16
COL = (CONTENT - GUTTER) / 2
RIGHT = M + COL + GUTTER
FIGURE_TOP, FIGURE_H, CAPTION_TOP = 166, 206, 380
MAIN_FIGURE_W, SIDE_FIGURE_W = 326, 194
SIDE_FIGURE_X = M + MAIN_FIGURE_W + GUTTER
METRIC_TOP, METRIC_H = 408, 60
SUMMARY_BOTTOM = 710
INK = colors.HexColor("#182630")
MUTED = colors.HexColor("#52616a")
BLUE = colors.HexColor("#245d78")
ORANGE = colors.HexColor("#b15c35")
PAPER = colors.HexColor("#f7f6f2")
LINE = colors.HexColor("#d5dedf")
TINT = colors.HexColor("#eaf0f1")
WHITE = colors.white


def register_fonts():
    font_dir = Path("/System/Library/Fonts/Supplemental")
    fonts = {
        "Body": "Arial.ttf",
        "Body-Italic": "Arial Italic.ttf", "Display": "Georgia.ttf",
    }
    if all((font_dir / file).exists() for file in fonts.values()):
        for name, file in fonts.items():
            pdfmetrics.registerFont(TTFont(name, str(font_dir / file)))
        pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body", italic="Body-Italic")
    else:
        for name, builtin in {
            "Body": "Helvetica",
            "Body-Italic": "Helvetica-Oblique", "Display": "Times-Roman",
        }.items():
            pdfmetrics.registerFont(pdfmetrics.Font(name, builtin, "WinAnsiEncoding"))
        pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body", italic="Body-Italic")


register_fonts()


def box(c, x, top, width, height, fill=WHITE, stroke=None, radius=0):
    c.setFillColor(fill)
    c.setStrokeColor(stroke or fill)
    c.setLineWidth(0.5)
    if radius:
        c.roundRect(x, H - top - height, width, height, radius, fill=1, stroke=int(stroke is not None))
    else:
        c.rect(x, H - top - height, width, height, fill=1, stroke=int(stroke is not None))


def text(c, value, x, top, size=10, font="Body", color=INK):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawString(x, H - top - size * 0.78, value)


def make_paragraph(value, width, size=10, leading=14, color=INK, font="Body"):
    style = ParagraphStyle("portfolio", fontName=font, fontSize=size, leading=leading,
                           textColor=color, alignment=TA_LEFT, spaceAfter=0)
    p = Paragraph(value, style)
    _, height = p.wrap(width, H)
    return p, height


def paragraph(c, value, x, top, width, size=10, leading=14, color=INK, font="Body", max_height=None):
    p, height = make_paragraph(value, width, size, leading, color, font)
    if max_height is not None and height > max_height + 0.1:
        raise ValueError(f"Text overflow: {height:.1f} > {max_height}: {value[:90]}")
    p.drawOn(c, x, H - top - height)
    return top + height


def rule(c, top, x=M, width=CONTENT, color=LINE):
    c.setStrokeColor(color)
    c.setLineWidth(0.65)
    c.line(x, H - top, x + width, H - top)


def link(c, label, url, x, top, size=8.8, color=BLUE):
    text(c, label, x, top, size, "Body", color)
    width = pdfmetrics.stringWidth(label, "Body", size)
    c.linkURL(url, (x, H - top - size - 2, x + width, H - top + 2), relative=0, thickness=0)
    return x + width


def image_asset(c, name, x, top, width, height, *, crop=False, frame=None, trim=False):
    im = Image.open(ASSETS / name)
    if frame is not None:
        im.seek(frame)
    im = im.convert("RGBA")
    if trim:
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        rgb = Image.alpha_composite(bg, im).convert("RGB")
        bbox = ImageChops.difference(rgb, Image.new("RGB", rgb.size, (255, 255, 255))).getbbox()
        if bbox:
            im = im.crop(bbox)
    if crop:
        ratio = width / height
        iw, ih = im.size
        if iw / ih > ratio:
            new_w = int(ih * ratio)
            left = (iw - new_w) // 2
            im = im.crop((left, 0, left + new_w, ih))
        else:
            new_h = int(iw / ratio)
            upper = (ih - new_h) // 2
            im = im.crop((0, upper, iw, upper + new_h))
        draw_w, draw_h = width, height
    else:
        ratio = min(width / im.width, height / im.height)
        draw_w, draw_h = im.width * ratio, im.height * ratio
    # Optimize only the in-memory PDF embedding. Keep source/site assets intact.
    # 210 dpi is ample for these placed figures and makes internship attachments small.
    target = (max(1, round(draw_w / 72 * 210)), max(1, round(draw_h / 72 * 210)))
    im.thumbnail(target, Image.Resampling.LANCZOS)
    im = Image.alpha_composite(Image.new("RGBA", im.size, (255, 255, 255, 255)), im).convert("RGB")
    buffer = io.BytesIO()
    im.save(buffer, format="JPEG", quality=88, optimize=True, subsampling=0)
    buffer.seek(0)
    c.drawImage(ImageReader(buffer), x + (width - draw_w) / 2,
                H - top - height + (height - draw_h) / 2,
                draw_w, draw_h, mask="auto")


def page_base(c, num, title, subtitle, role, slug, title_size=28):
    box(c, 0, 0, W, H, PAPER)
    box(c, 0, 0, 7, H, BLUE)
    text(c, "SIDDHARTHA GUPTA", M, 31, 10.5, "Body")
    focus = "MECHANICAL DESIGN + SIMULATION"
    focus_width = pdfmetrics.stringWidth(focus, "Body", 7.7)
    text(c, focus, M + CONTENT - focus_width, 33, 7.7, "Body", MUTED)
    education = "NC State, B.S. Mechanical Engineering, Mathematics minor"
    text(c, education, M, 49, 8.4, color=MUTED)
    graduation = "Expected May 2028"
    graduation_width = pdfmetrics.stringWidth(graduation, "Body", 8.4)
    text(c, graduation, M + CONTENT - graduation_width, 49, 8.4, color=MUTED)
    rule(c, 72)
    text(c, title, M, 88, title_size, "Display")
    text(c, subtitle, M, 125, 10, "Body", BLUE)
    text(c, role, M, 142, 8.8, color=MUTED)
    rule(c, 732)
    link(c, "Project details", f"https://sidgupta.dev/projects/{slug}/", M, 748, 8.7)
    text(c, f"{num:02d} / 04", 534, 748, 8.7, "Body", MUTED)
    text(c, "INTERNSHIP PORTFOLIO | OCTOBER 2026", M, 769, 6.8, "Body", MUTED)
    contacts = [
        ("guptasid2008@gmail.com", "mailto:guptasid2008@gmail.com"),
        ("sidgupta.dev", "https://sidgupta.dev"),
        ("LinkedIn", "https://www.linkedin.com/in/siddhartha-gupta-94410a28b/"),
    ]
    contact_widths = [pdfmetrics.stringWidth(label, "Body", 8.2) for label, _ in contacts]
    contact_gap = 16
    x = M + CONTENT - sum(contact_widths) - contact_gap * (len(contacts) - 1)
    for label, url in contacts:
        x = link(c, label, url, x, 768, 8.2) + contact_gap
    c.bookmarkPage(slug)
    c.addOutlineEntry(title, slug, level=0, closed=False)


def metrics(c, items, top=METRIC_TOP, height=METRIC_H):
    box(c, M, top, CONTENT, height, TINT)
    cell = CONTENT / len(items)
    for i, (value, label) in enumerate(items):
        x = M + i * cell + 13
        text(c, value, x, top + 12, 18.5, "Body", BLUE)
        paragraph(c, label, x, top + 37, cell - 24, 7.7, 9.5, MUTED, max_height=22)
        if i:
            c.setStrokeColor(LINE)
            c.line(M + i * cell, H - top - 12, M + i * cell, H - top - height + 12)


def section(c, heading, body, x, top, width, height=150):
    text(c, heading.upper(), x, top, 8.5, "Body", BLUE)
    return paragraph(c, body, x, top + 19, width, 10.2, 14.2, max_height=height - 19)


def outcome(c, heading, body, top, height):
    box(c, M, top, CONTENT, height, WHITE)
    box(c, M, top, 3, height, ORANGE)
    text(c, heading.upper(), M + 13, top + 11, 8.1, "Body", ORANGE)
    paragraph(c, body, M + 13, top + 26, CONTENT - 26, 9.2, 12.5, max_height=height - 38)


def project_text(c, left, right, summary):
    """Share spare space between the text block's upper and lower gaps."""
    body_height = max(make_paragraph(body, COL, 10.2, 14.2)[1] for _, body in (left, right)) + 19
    summary_height = make_paragraph(summary[1], CONTENT - 26, 9.2, 12.5)[1] + 38
    summary_top = SUMMARY_BOTTOM - summary_height
    metrics_bottom = METRIC_TOP + METRIC_H
    gap = (summary_top - metrics_bottom - body_height) / 2
    if gap < 18:
        raise ValueError(f"Insufficient space between project sections: {gap:.1f} pt")
    body_top = metrics_bottom + gap
    section(c, *left, M, body_top, COL, body_height)
    section(c, *right, RIGHT, body_top, COL, body_height)
    outcome(c, *summary, top=summary_top, height=summary_height)


def c4_page(c):
    page_base(c, 1, "C4 competition robot", "FIRST Robotics Competition | Team 900, The Zebracorns", "Design and Mechanical Lead | 2025 season", "c4")
    box(c, M, FIGURE_TOP, MAIN_FIGURE_W, FIGURE_H, WHITE)
    image_asset(c, "c4_cover.jpeg", M, FIGURE_TOP, MAIN_FIGURE_W, FIGURE_H, crop=True)
    box(c, SIDE_FIGURE_X, FIGURE_TOP, SIDE_FIGURE_W, FIGURE_H, WHITE)
    image_asset(c, "c4_belt-gb.png", SIDE_FIGURE_X + 10, FIGURE_TOP + 8, SIDE_FIGURE_W - 20, FIGURE_H - 16)
    text(c, "BUILT ROBOT", M, CAPTION_TOP, 7.2, "Body", MUTED)
    text(c, "ELEVATOR BELT ROUTING + GEARBOX", SIDE_FIGURE_X, CAPTION_TOP, 7.0, "Body", MUTED)
    metrics(c, [("36 to 74 in", "stowed / extended elevator height"), ("<4 in", "elevator thickness, down from >5.5 in"), ("~40%", "cost reduction vs. original manufacturing approach")])
    project_text(c,
        ("Role and design process", "I led 25 mechanical students and five CAD students, designed the elevator and managed the master geometry and Onshape workspace. We left algae scoring and deep climbing out of scope to focus on tuning and driver practice. Prototyping and CAD reviews supported fabrication, integration and elevator testing."),
        ("Elevator and fabrication", "The three-stage elevator combines machined 6061 aluminum, two Kraken X60 motors, a 3:1 gearbox and two internal HTD 5 mm belts. Master sketches defined packaging and belt paths; custom Onshape FeatureScripts generated pulleys and gears. Markforged-printed and waterjet-cut aluminum bearing blocks reduced cost by about 40% and subsystem lead time by about two weeks."),
        ("Competition results", "The elevator had no mechanical failures during competition. The team won the 2025 NC Championship and ranked in the top 11% of FRC teams worldwide, despite our school heavily cutting our mentor team, resources, and funding."))
    c.showPage()


def lspace_architecture(c, x, top, width, height):
    gap = 6
    cell = (width - gap) / 2
    for i, (heading, body) in enumerate([
        ("Station", "Power, charging, thermal support and data relay"),
        ("Scout", "Cold-gas mobility, mapping and hazard sensing"),
    ]):
        cell_x = x + i * (cell + gap)
        box(c, cell_x, top, cell, height, WHITE)
        text(c, heading, cell_x + 8, top + 9, 10, "Display", BLUE)
        paragraph(c, body, cell_x + 8, top + 27, cell - 16, 8.1, 10.5,
                  max_height=height - 33)


def lspace_page(c):
    page_base(c, 3, "L'SPACE mission concept", "NASA L'SPACE Mission Concept Academy | Team 24", "Project Manager | May-August 2026 | Student design study", "lspace")
    main_width, side_width, gap = 308, 216, 12
    side_x = M + main_width + gap
    image_asset(c, "lspace_cover.png", M, FIGURE_TOP, main_width, FIGURE_H)
    map_height = 132
    image_asset(c, "lspace_shackleton_jmars.png", side_x, FIGURE_TOP, side_width, map_height)
    lspace_architecture(c, side_x, FIGURE_TOP + map_height + 6, side_width,
                        FIGURE_H - map_height - 6)
    text(c, "TEAM CONCEPT: BASE STATION + SCOUT", M, CAPTION_TOP, 7.0, "Body", MUTED)
    text(c, "JMARS | SHACKLETON-DE GERLACHE RIDGE", side_x, CAPTION_TOP, 6.8, "Body", MUTED)
    metrics(c, [("20 members", "student team across science, engineering and planning"), ("175 kg", "combined launch-mass ceiling"), ("95 days", "planned surface mission length")])
    project_text(c,
        ("Role and review process", "I managed the 20-member team, coordinated reviews and deliverables, and contributed to vehicle CAD, mechanical integration and science-to-engineering traceability. From May to August 2026, we progressed through MCR, SRR, MDR and PDR, using assigned tasks, soft deadlines, daily tracking and cross-section reviews."),
        ("Mechanical and system interfaces", "Preliminary frame selections were 6061-T6 for the station and 7075-T6 for the scout. The concept included docking alignment, spring-probe charging, a local UHF link and X-band direct-to-Earth communications. Depth and inertial sensing supported terrain mapping. Four planned scout excursions fit within the 95-day surface mission."),
        ("Deliverable and status", "Completed a student Preliminary Design Review with vehicle CAD, science-to-requirement traceability, N-squared interface diagrams, FMEA and verification plans. Propulsion sizing, integrated mass/power/thermal budgets and hardware validation remained open."))
    link(c, "Project overview PDF", "https://sidgupta.dev/assets/LSPACE_Project_Overview.pdf", 305, 748, 8.1)
    c.showPage()


def rover_page(c):
    page_base(c, 2, "Suspended swerve rover", "Four-wheel steering and double-wishbone pushrod suspension", "Mechanical design, basic FEA and early simulation | September 2025-May 2026", "rover")
    gallery_height, main_width, gallery_gap = 230, 304, 12
    side_width = CONTENT - main_width - gallery_gap
    side_x = M + main_width + gallery_gap
    box(c, M, FIGURE_TOP, main_width, gallery_height, WHITE)
    image_asset(c, "rover_completed_concept.png", M, FIGURE_TOP, main_width, gallery_height)
    shot_height = (gallery_height - 8) / 2
    fea_top = FIGURE_TOP + shot_height + 8
    box(c, side_x, FIGURE_TOP, side_width, shot_height, WHITE)
    image_asset(c, "rover_isaac_concept.png", side_x, FIGURE_TOP, side_width, shot_height)
    box(c, side_x, fea_top, side_width, shot_height, WHITE)
    image_asset(c, "rover_upper_link_fea.png", side_x, fea_top, side_width, shot_height)
    metrics(c, [("+/-150 mm", "wheel-travel design target"), ("Double wishbone", "pushrod suspension"), ("+/-5 deg", "camber-range design target")])
    project_text(c,
        ("CAD work", "I modeled the tubular chassis, double wishbones, pushrods and inboard suspension using master sketches, 3D sketches and weldments. Original component selections included 7075 aluminum parts, QA1 coilovers with 350 lb/in springs and AKM42C servomotors. The illustrated hub-drive layout is a later concept revision."),
        ("Future simulation work", "I plan to develop autonomous navigation in Isaac Sim, including terrain mapping, waypoint following, obstacle avoidance and replanning. Edge-case scenes would cover cross-slopes, unequal wheel loading, low traction, steps near suspension travel limits and tight passages. I would compare path tracking, wheel contact/slip, steering error and chassis attitude across these conditions."),
        ("Current status and next steps", "Completed basic suspension-link FEA and basic teleoperation. Next: autonomy and edge-case simulation, detailed component and assembly FEA, and topology or parametric optimization. The geometry values above remain design targets."))
    c.showPage()


def bumpers_page(c):
    page_base(c, 4, "Configurable sheet-metal bumpers", "Parametric Onshape assembly | FIRST Robotics Competition", "Designer | Public CAD release: October 2023", "config_bumpers")
    box(c, M, FIGURE_TOP, CONTENT, FIGURE_H, WHITE)
    image_asset(c, "bumpers.gif", M + 3, FIGURE_TOP + 1, CONTENT - 6, FIGURE_H - 2, frame=0)
    text(c, "TWO-PIECE BUMPER ASSEMBLY | FRAME FROM CAD ANIMATION", M, CAPTION_TOP, 7.0, "Body", MUTED)
    metrics(c, [("150+ teams", "using this design"), ("6 inputs", "frame, spacing, split and mounting parameters"), ("Quick release", "sliding tabs + spring pins")])
    project_text(c,
        ("Parametric design", "I built a configurable two-piece sheet-metal backing assembly in Onshape. Six inputs set frame width and length, bumper spacing, two split openings and mounting height. A second variable studio calculates dependent geometry and updates both parts and assembly mates. Sliding tabs and spring pins provide the mounting interface."),
        ("Public release and reach", "I shared the CAD and configuration instructions in the Zebracorns' Chief Delphi build thread in October 2023. More than 150 teams used this design. My contribution was the original configurable design and public documentation."),
        ("Release scope", "The original model was designed around the 2024 bumper rules. Adaptations for other robots or seasons need mounting-clearance and applicable-rule checks."))
    cad_url = "https://cad.onshape.com/documents/3a3e250de05f1f4195603d03/w/2ff30d34a754fd8f94e2569d/e/8188f19f1adb79387bdd9945"
    link(c, "Public Onshape CAD", cad_url, 307, 748, 8.1)
    c.showPage()


def verify(path):
    reader = PdfReader(path)
    assert len(reader.pages) == 4, f"Expected four pages, got {len(reader.pages)}"
    names = ["C4", "Suspended swerve rover", "L'SPACE", "Configurable sheet-metal bumpers"]
    results = []
    for i, (page, expected) in enumerate(zip(reader.pages, names), 1):
        extracted = page.extract_text()
        assert expected in extracted, (i, expected)
        assert "SIDDHARTHA GUPTA" in extracted
        assert "guptasid2008@gmail.com" in extracted
        assert tuple(round(float(v), 2) for v in page.mediabox) == (0, 0, 612, 792)
        uris = [str(a.get_object().get("/A", {}).get("/URI", "")) for a in page.get("/Annots", [])]
        assert any("/projects/" in u for u in uris), (i, "missing project link")
        assert "\u25a0" not in extracted, (i, "black square glyph")
        results.append({"page": i, "text_characters": len(extracted), "links": uris})
    rover_text = " ".join(reader.pages[1].extract_text().split())
    assert "basic teleoperation" in rover_text
    assert "Simulation validation planned" not in rover_text
    assert "150+ teams" in reader.pages[3].extract_text()
    assert path.stat().st_size < 5_000_000, "Portfolio exceeds the 5 MB attachment limit"
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--render", action="store_true", help="Render all pages to tmp/pdfs with PyMuPDF")
    args = parser.parse_args()
    for name in ["lspace_shackleton_jmars.png", "rover_completed_concept.png", "rover_isaac_concept.png", "rover_upper_link_fea.png"]:
        if not (ASSETS / name).exists():
            raise FileNotFoundError(f"Required final concept visual not available: {ASSETS / name}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    QA.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=(W, H), pageCompression=1)
    c.setTitle("Siddhartha Gupta | Selected Engineering Projects")
    c.setAuthor("Siddhartha Gupta")
    c.setSubject("Four-project internship portfolio: C4, suspended swerve rover, L'SPACE and configurable bumpers")
    c.setCreator("scripts/build_portfolio.py | ReportLab")
    for page in [c4_page, rover_page, lspace_page, bumpers_page]:
        page(c)
    c.save()
    result = verify(OUT)
    shutil.copy2(OUT, PUBLIC)
    (QA / "validation.json").write_text(json.dumps(result, indent=2))
    if args.render:
        import pymupdf
        document = pymupdf.open(OUT)
        for index, page in enumerate(document, 1):
            page.get_pixmap(matrix=pymupdf.Matrix(2, 2), alpha=False).save(QA / f"portfolio-page-{index}.png")
    print(json.dumps({"output": str(OUT), "public_copy": str(PUBLIC), "pages": 4, "bytes": OUT.stat().st_size}))


if __name__ == "__main__":
    main()
