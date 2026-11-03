#!/usr/bin/env python3
"""Build learning-to-think.pptx from the same source as the blog and reveal views.

Reads _includes/presentations/2026-11-03-learning-to-think.md, and for each
slide (separated by '---'):
  * an SVG diagram becomes a full-bleed PNG slide (rendered with Inkscape); any
    <a data-box> links in the SVG become clickable areas
  * a site photo (/assets/...jpg) becomes a full-bleed picture, cropped to 16:9
  * a YouTube iframe becomes an online video that plays inside the slide
    (needs PowerPoint for Microsoft 365 and an internet connection)
  * the text after 'Note:' becomes the PowerPoint speaker notes

Needs Inkscape and python-pptx (pip install python-pptx).

Usage:
    python3 _scripts/learning-to-think/make_diagrams.py
    python3 _scripts/learning-to-think/build_pptx.py

To copy each new build to another machine as well, set PPTX_SEND_TO to an scp destination,
e.g. PPTX_SEND_TO=myhost:Downloads/
"""
import os
import re
import subprocess
import urllib.request

from PIL import Image, ImageDraw
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.oxml import parse_xml
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import nsdecls, qn
from pptx.util import Emu, Inches, Pt

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC = os.path.join(ROOT, "_includes", "presentations", "2026-11-03-learning-to-think.md")
RES = os.path.join(ROOT, "assets", "images", "presentation_resources", "2026-11-03")
OUT = os.path.join(RES, "learning-to-think.pptx")


def to_png(svg):
    png = svg[:-4] + ".png"
    if not os.path.exists(png) or os.path.getmtime(png) < os.path.getmtime(svg):
        subprocess.run(["inkscape", svg, "--export-type=png", f"--export-filename={png}", "-w", "1920"],
                       check=True, capture_output=True)
    return png


def thumbnail(video_id):
    path = os.path.join(RES, f"video-{video_id}.jpg")
    if not os.path.exists(path):
        req = urllib.request.Request(f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg",
                                     headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as r, open(path, "wb") as fh:
            fh.write(r.read())
    return path


def poster(video_id):
    """The YouTube thumbnail with a play button drawn on, shown until the video starts."""
    path = os.path.join(RES, f"video-{video_id}-poster.jpg")
    img = Image.open(thumbnail(video_id)).convert("RGB")
    w, h = img.size
    draw = ImageDraw.Draw(img)
    r = h * 0.16
    cx, cy = w / 2, h / 2
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0xC0, 0x48, 0x3F))
    tri = r * 0.5
    draw.polygon([(cx - tri * 0.6, cy - tri), (cx - tri * 0.6, cy + tri), (cx + tri, cy)], fill=(255, 255, 255))
    img.save(path, quality=90)
    return path


def embed_url(video_id, start, end):
    """The YouTube player URL PowerPoint uses for an online video, with the clip's start and end."""
    params = [f"start={start.group(1)}"] if start else []
    params += [f"end={end.group(1)}"] if end else []
    params.append("feature=oembed")
    return f"https://www.youtube.com/embed/{video_id}?" + "&".join(params)


def add_online_video(slide, url, poster_path, left, top, width, height):
    """Add a YouTube video that plays inside the slide, like PowerPoint's Insert > Video > Online Video.

    python-pptx can only embed video files, so this builds the same media picture it uses for those,
    but with the video linked to the YouTube player URL instead of a file inside the .pptx.
    """
    video_rId = slide.part.relate_to(url, RT.VIDEO, is_external=True)
    _, poster_rId = slide.part.get_or_add_image_part(poster_path)
    shape_id = slide.shapes._next_shape_id
    pic = parse_xml(
        f'<p:pic {nsdecls("a", "p", "r")}>'
        f'<p:nvPicPr><p:cNvPr id="{shape_id}" name="Online video {shape_id}">'
        f'<a:hlinkClick r:id="" action="ppaction://media"/></p:cNvPr>'
        f'<p:cNvPicPr><a:picLocks noGrp="1" noRot="1" noChangeAspect="1"/></p:cNvPicPr>'
        f'<p:nvPr><a:videoFile r:link="{video_rId}"/></p:nvPr></p:nvPicPr>'
        f'<p:blipFill><a:blip r:embed="{poster_rId}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>'
        f'<p:spPr><a:xfrm><a:off x="{left}" y="{top}"/><a:ext cx="{width}" cy="{height}"/></a:xfrm>'
        f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>')
    slide.shapes._spTree.append(pic)
    slide.shapes._add_video_timing(pic)


def add_svg_links(slide, svg_path, sw, sh):
    """Make each <a href data-box="x,y,w,h"> area in the SVG clickable on the slide image."""
    svg = open(svg_path).read()
    vw, vh = (float(v) for v in re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg).groups())
    for href, box in re.findall(r'<a href="([^"]+)"[^>]*data-box="([^"]+)"', svg):
        x, y, w, h = (float(v) for v in box.split(","))
        r = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Emu(int(x / vw * sw)), Emu(int(y / vh * sh)),
                                   Emu(int(w / vw * sw)), Emu(int(h / vh * sh)))
        r.line.fill.background()
        r.fill.solid()
        r.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        # fully transparent, but still filled so the whole area takes the click
        r.fill._xPr.find(qn("a:solidFill"))[0].append(parse_xml(f'<a:alpha {nsdecls("a")} val="0"/>'))
        r.click_action.hyperlink.address = href


def add_full_bleed_photo(slide, path, sw, sh):
    """Fill the slide with a photo, trimming equal amounts from two edges rather than stretching it."""
    pic = slide.shapes.add_picture(path, 0, 0, sw, sh)
    w, h = Image.open(path).size
    excess = 1 - (w / h) / (sw / sh)  # >0: too tall for the slide, <0: too wide
    if excess > 0:
        pic.crop_top = pic.crop_bottom = excess / 2
    elif excess < 0:
        trim = 1 - (sw / sh) / (w / h)
        pic.crop_left = pic.crop_right = trim / 2


def notes_text(chunk):
    """Turn the Markdown after 'Note:' into plain speaker-notes text."""
    m = re.search(r"Note:\s*\{%\s*endif\s*%\}(.*)", chunk, re.S)
    if not m:
        return ""
    s = m.group(1)
    s = re.sub(r"\{%\s*unless include\.pres\s*%\}.*?\{%\s*endunless\s*%\}", "", s, flags=re.S)  # blog-only
    s = re.sub(r"\{%.*?%\}", "", s)
    s = re.sub(r"\[([^\]]+)\]\((/[^)]+)\)", r"\1 (lightenna.com\2)", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"\*(.+?)\*", r"\1", s)
    s = re.sub(r"^\s*\* ", "• ", s, flags=re.M)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def main():
    src = open(SRC).read()
    chunks = re.split(r"\n---\n", src)

    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    blank = prs.slide_layouts[6]
    sw, sh = prs.slide_width, prs.slide_height

    for chunk in chunks:
        svg = re.search(r"\"(/?[\w./-]+\.svg)\"", chunk)
        yt = re.search(r"youtube(?:-nocookie)?\.com/embed/([\w-]{11})", chunk)
        photo = re.search(r"\"(/assets/[\w./-]+\.(?:jpg|jpeg|png))\"", chunk)
        if not (svg or yt or photo):
            continue
        slide = prs.slides.add_slide(blank)
        if photo and not svg:
            add_full_bleed_photo(slide, os.path.join(ROOT, photo.group(1).lstrip("/")), sw, sh)
            label = os.path.basename(photo.group(1))
        elif svg:
            ref = svg.group(1)  # a file in this talk's folder, or a site path such as /assets/svg/x.svg
            svg_path = os.path.join(ROOT, ref.lstrip("/")) if ref.startswith("/") else os.path.join(RES, ref)
            pptx_only = svg_path[:-4] + "-pptx.svg"
            if os.path.exists(pptx_only):  # a PowerPoint-only variant, e.g. naming the school
                svg_path = pptx_only
            slide.shapes.add_picture(to_png(svg_path), 0, 0, sw, sh)
            add_svg_links(slide, svg_path, sw, sh)
            label = os.path.basename(svg_path)
        else:
            vid = yt.group(1)
            start = re.search(r"[?&](?:amp;)?start=(\d+)", chunk)
            end = re.search(r"[?&](?:amp;)?end=(\d+)", chunk)
            url = f"https://www.youtube.com/watch?v={vid}"
            if start:
                url += f"&t={start.group(1)}s"
            # white slide, the video as large as fits; the video's own frame carries its title
            pw = Inches(11.6)
            ph = Emu(int(pw * 9 / 16))
            left, top = Emu(int((sw - pw) / 2)), Emu(int((sh - ph) / 2))
            add_online_video(slide, embed_url(vid, start, end), poster(vid), left, top, pw, ph)
            # a small, quiet fallback link in the bottom-right corner, in case the video won't play
            lw, lh = Inches(2.4), Inches(0.3)
            tb = slide.shapes.add_textbox(Emu(int(sw - lw - Inches(0.25))), Emu(int(sh - lh - Inches(0.06))), lw, lh)
            p = tb.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.RIGHT
            p.text = "Open on YouTube ↗"
            p.font.size = Pt(10)
            p.font.color.rgb = RGBColor(0xA0, 0xA6, 0xAE)
            # link the box rather than the text, so PowerPoint doesn't restyle it as a blue underlined link
            tb.click_action.hyperlink.address = url
            label = f"video {vid}"
        slide.notes_slide.notes_text_frame.text = notes_text(chunk)
        print("slide", len(prs.slides), label)

    prs.save(OUT)
    print("wrote", os.path.relpath(OUT, ROOT))
    dest = os.environ.get("PPTX_SEND_TO")
    if dest:
        subprocess.run(["scp", "-o", "BatchMode=yes", OUT, dest], check=True)
        print("sent to", dest)


if __name__ == "__main__":
    main()
