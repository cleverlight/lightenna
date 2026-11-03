#!/usr/bin/env python3
"""Generate the slide diagrams for "Learning to think" as 16:9 SVGs.

Each slide is a self-contained 1600x900 SVG, so the same file works as a
reveal.js slide, an image in the blog post, and a full-bleed PowerPoint slide.

Usage:
    PPTX_VENUE="..." python3 _scripts/learning-to-think/make_diagrams.py
    python3 _scripts/learning-to-think/build_pptx.py     # PNGs + .pptx

PPTX_VENUE (optional) names the venue on the PowerPoint's title slide only.

Edit the slide text in the SLIDE DATA section, then re-run both scripts.
"""
import base64
import os
import urllib.request
from html import escape

from PIL import ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "assets", "images", "presentation_resources", "2026-11-03")

W, H = 1600, 900
M = 80  # side margin

# Palette, matching assets/svg/ai-agent-loop.svg
BLUE, TEAL, AMBER, RED = "#3B5F8A", "#1E8073", "#DB9126", "#C0483F"
BLUE_D, TEAL_D, AMBER_D, RED_D = "#33547B", "#146258", "#97600C", "#AC3B33"
GREY = "#8A919C"
PURPLE, PURPLE_D = "#7A5BA6", "#5E4387"  # used only for innovation
INK, INK2 = "#14171D", "#4A515C"
SANS = "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, 'DejaVu Sans Mono', Menlo, Consolas, monospace"
FOOTER = "lightenna.com"

# Measure with Noto Sans (the local fallback, wider than Helvetica/Segoe), plus a
# small safety margin, so text that fits here fits everywhere.
_FONTS = {
    False: "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
    True: "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
}
_cache = {}


def text_w(s, size, bold=False):
    key = (size, bold)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(_FONTS[bold], size)
    return _cache[key].getlength(s) * 1.04


def wrap(s, size, maxw, bold=False):
    lines, cur = [], ""
    for word in s.split():
        trial = (cur + " " + word).strip()
        if text_w(trial, size, bold) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    for ln in lines:
        assert text_w(ln, size, bold) <= maxw + 1, f"word too long for {maxw}px: {ln!r}"
    return lines


def t(x, y, s, size=20, weight=400, fill=INK, anchor="start", family=SANS, extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{extra}>{escape(s)}</text>')


def para(x, y, s, size, maxw, lh=None, weight=400, fill=INK, anchor="start"):
    """Wrapped paragraph; y is the first baseline. Returns (svg, height)."""
    lh = lh or round(size * 1.3)
    lines = wrap(s, size, maxw, weight >= 600)
    out = [t(x, y + i * lh, ln, size, weight, fill, anchor) for i, ln in enumerate(lines)]
    return "\n".join(out), len(lines) * lh


def chip(x, y, w, s, color, size=19, fill_op=0.10):
    """Rounded label with a coloured left bar. Returns (svg, height)."""
    pad_x, pad_y, lh = 16, 9, round(size * 1.25)
    lines = wrap(s, size, w - pad_x - 12)
    h = len(lines) * lh + 2 * pad_y - 4
    out = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{color}" fill-opacity="{fill_op}"/>',
        f'<rect x="{x}" y="{y}" width="6" height="{h}" rx="3" fill="{color}"/>',
    ]
    for i, ln in enumerate(lines):
        out.append(t(x + pad_x, y + pad_y + size * 0.85 + i * lh, ln, size))
    return "\n".join(out), h


def arrow_defs():
    out = ["<defs>"]
    for name, col in (("aBlue", BLUE), ("aTeal", TEAL), ("aAmber", AMBER), ("aRed", RED), ("aGrey", GREY)):
        out.append(f'<marker id="{name}" viewBox="0 0 10 10" refX="8.6" refY="5" markerWidth="5" markerHeight="5" '
                   f'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="{col}"/></marker>')
        # "Base" variant: the head starts where the line ends, so it doesn't cover the end of the line
        out.append(f'<marker id="{name}Base" viewBox="0 0 10 10" refX="0.5" refY="5" markerWidth="5" markerHeight="5" '
                   f'orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="{col}"/></marker>')
    out.append("</defs>")
    return "\n".join(out)


def page(title, desc, heading, sub, body, sources=""):
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
        f'aria-labelledby="t d">',
        f'<title id="t">{escape(title)}</title>',
        f'<desc id="d">{escape(desc)}</desc>',
        arrow_defs(),
        f'<rect x="0" y="0" width="{W}" height="{H}" fill="#FFFFFF"/>',
    ]
    if heading:
        parts.append(t(M, 98, heading, 50, 700, INK, extra=' letter-spacing="-0.8"'))
    if sub:
        parts.append(t(M, 144, sub, 25, 400, INK2))
    parts.append(body)
    parts.append(f'<line x1="{M}" y1="858" x2="{W - M}" y2="858" stroke="#E3E6EA" stroke-width="2"/>')
    if sources:
        assert text_w(sources, 15) < W - 2 * M - 160, f"sources line too long: {sources!r}"
        parts.append(t(M, 884, sources, 15, 400, GREY))
    parts.append(t(W - M, 884, FOOTER, 15, 400, GREY, "end"))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


# ---------------------------------------------------------------------------
# SLIDE DATA
# ---------------------------------------------------------------------------

PROFESSION_SLIDES = [
    {
        "file": "02-health-science-education.svg",
        "heading": "Health, science and education",
        "sub": "AI takes the volume work, so professionals spend more time on people and discovery",
        "sources": "Sources: GOV.UK (Jun 2026); NHS England ambient scribing guidance; Google DeepMind; Imperial College London / BBC (Feb 2025); Oak National Academy",
        "rows": [
            {
                "name": "Medicine & healthcare",
                "example": "AI tools have already helped over 4 million NHS patients get a faster lung cancer diagnosis or all-clear.",
                "ai": ["Reading scans and flagging possible cancers early",
                       "Writing up notes while you talk to the patient",
                       "Triage, letters and appointment admin"],
                "you": ["Examining, diagnosing, deciding with the patient",
                        "Explaining risk with empathy",
                        "Spotting when the AI has got it wrong"],
                "start": "Get care experience (volunteering, a hospital or care-home placement) and ask the clinicians you meet how AI is changing their work.",
            },
            {
                "name": "Scientific research",
                "example": "AlphaFold has been used by 3 million+ researchers. Google's AI co-scientist reached, in 2 days, a superbug hypothesis that took an Imperial team years.",
                "ai": ["Predicting protein structures in minutes",
                       "Reading thousands of papers to suggest hypotheses",
                       "Running and analysing simulations"],
                "you": ["Asking the question worth answering",
                        "Designing the experiment that proves it",
                        "Judging what is new, true and useful"],
                "start": "Explore the free AlphaFold Protein Structure Database for a molecule you've studied, and read one research summary a month in a field you love.",
            },
            {
                "name": "Teaching & education",
                "example": "Oak National Academy's free AI assistant, Aila, helps UK teachers plan lessons, slides and quizzes in minutes.",
                "ai": ["Drafting lesson plans, resources and quizzes",
                       "Personalised practice for every pupil",
                       "Marking routine work and spotting gaps"],
                "you": ["Inspiring and motivating",
                        "Knowing each pupil as a person",
                        "Teaching judgement and integrity"],
                "start": "Tutor, coach or mentor younger students. Notice which explanations land, and why: that's the expertise AI can't supply.",
            },
        ],
    },
    {
        "file": "03-law-finance-business.svg",
        "heading": "Law, finance and business",
        "sub": "The first draft is now instant; the advice, the decision and the responsibility are yours",
        "sources": "Sources: Solicitors Regulation Authority (May 2025); public statements from major audit firms on AI-assisted audit",
        "rows": [
            {
                "name": "Law",
                "example": "In 2025 the SRA authorised Garfield.Law, the first AI-driven law firm in England and Wales, with named solicitors still accountable.",
                "ai": ["Reviewing thousands of pages of contracts",
                       "Legal research and first drafts",
                       "Due-diligence checklists"],
                "you": ["Advising clients on what to do",
                        "Negotiating and arguing the case",
                        "Taking responsibility for the advice"],
                "start": "Moot, debate or join a mock trial. Follow legal news on AI, and ask firms at open days how trainees use it.",
            },
            {
                "name": "Accounting & finance",
                "example": "Audit is moving from checking a sample of transactions to AI-assisted analysis of every transaction.",
                "ai": ["Reconciling and categorising transactions",
                       "Testing every transaction, not a sample",
                       "Building forecasts and first-cut reports"],
                "you": ["Explaining what the numbers mean",
                        "Spotting risk, fraud and odd patterns",
                        "Advising on the decision"],
                "start": "Get properly fluent with spreadsheets, then run a mock portfolio or the budget for a club or enterprise project.",
            },
            {
                "name": "Business, marketing & management",
                "example": "A small team can now research a market, test dozens of campaign versions and analyse the results in a week.",
                "ai": ["Market and competitor research",
                       "Drafting campaigns in many versions",
                       "Analysing customer data"],
                "you": ["Understanding customers as people",
                        "Choosing the strategy",
                        "Leading teams of people and AI agents"],
                "start": "Start something small outside school (a stall, a club, a channel) and use AI tools to help you run it. Keep notes on what worked.",
            },
        ],
    },
    {
        "file": "04-software-engineering-creative.svg",
        "heading": "Software, engineering and the creative industries",
        "sub": "AI builds the options at speed; you decide what's worth making and make sure it's right",
        "sources": "Sources: Semafor, Google CEO on AI-generated code (Apr 2026); Google DeepMind, Genie 4 (Oct 2026)",
        "rows": [
            {
                "name": "Software & computing",
                "example": "Google says 75% of its new code is now AI-generated, then reviewed and approved by engineers (up from 25% in 2024).",
                "ai": ["Writing most of the routine code",
                       "Writing tests and hunting bugs",
                       "Explaining unfamiliar code"],
                "you": ["Deciding what to build, and why",
                        "Designing systems and reviewing the work",
                        "Security, safety and quality"],
                "start": "Build something you'd use, with an AI coding assistant, outside your coursework. Make sure you can explain every line.",
            },
            {
                "name": "Engineering",
                "example": "Generative design lets engineers explore hundreds of lighter, stronger part designs, then test them in simulation.",
                "ai": ["Generating hundreds of design options",
                       "Running simulations overnight",
                       "Predicting failures before they happen"],
                "you": ["Setting constraints: safety, cost, carbon",
                        "Choosing and signing off the design",
                        "Working on site with people"],
                "start": "Join a Year 12 industry scheme (e.g. EDT's Engineering Education Scheme) or a build team, and design, make and test something physical.",
            },
            {
                "name": "Creative industries",
                "example": "Google DeepMind's Genie 4 generates explorable, interactive worlds from a text description, in real time.",
                "ai": ["Concepts, mood boards and storyboards",
                       "Rough cuts, translation and dubbing",
                       "Prototype worlds, sounds and characters"],
                "you": ["Taste, story and point of view",
                        "Directing: choosing what is good",
                        "Original work audiences trust"],
                "start": "Keep a portfolio of your own original work. Experiment with AI tools on personal projects, and be open about how you used them.",
            },
        ],
    },
]


# ---------------------------------------------------------------------------
# SLIDE BUILDERS
# ---------------------------------------------------------------------------

def slide_title(venue="Grammar school presentation"):
    body = []
    # fan-out motif on the right: one person directing many agents
    cx, cy = 1180, 470
    body.append(f'<circle cx="{cx}" cy="{cy}" r="74" fill="{BLUE}" fill-opacity="0.13" stroke="{BLUE}" stroke-width="3"/>')
    body.append(t(cx, cy + 11, "You", 32, 700, BLUE_D, "middle"))
    import math
    n = 9
    for i in range(n):
        a = math.radians(-70 + i * 140 / (n - 1))
        x2, y2 = cx + 290 * math.cos(a), cy + 290 * math.sin(a)
        x1, y1 = cx + 82 * math.cos(a), cy + 82 * math.sin(a)
        xe, ye = cx + 250 * math.cos(a), cy + 250 * math.sin(a)
        body.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{xe:.1f}" y2="{ye:.1f}" stroke="{TEAL}" stroke-width="3" '
                    f'stroke-opacity="0.7" marker-end="url(#aTeal)"/>')
        body.append(f'<circle cx="{x2:.1f}" cy="{y2:.1f}" r="30" fill="{TEAL}" fill-opacity="0.13" stroke="{TEAL}" stroke-width="2.5"/>')
        body.append(t(x2, y2 + 7, "AI", 19, 700, TEAL_D, "middle", MONO))
    # mirrored arrows back into "you" (the checking step)
    body.append(f'<path d="M {cx - 100} {cy + 170} A 220 220 0 0 1 {cx - 96} {cy - 170}" fill="none" stroke="{AMBER}" '
                f'stroke-width="4" stroke-dasharray="10 8" marker-start="url(#aAmber)" marker-end="url(#aAmber)"/>')
    # what "you" do with what comes back: verbs spaced along the outside of the arc, top to bottom.
    # The arc above has radius 220 and runs from (cx-100, cy+170) to (cx-96, cy-170), so its centre is
    # about 140px right of the chord's midpoint.
    acx, acy, ar = cx - 98 + math.sqrt(220 ** 2 - 170 ** 2), cy, 220 + 22
    verbs = ["check", "manage", "integrate", "inspire", "guide", "verify", "correct"]
    for i, verb in enumerate(verbs):
        a = math.radians(222 - i * (222 - 138) / (len(verbs) - 1))
        body.append(t(acx + ar * math.cos(a), acy + ar * math.sin(a) + 7, verb, 20, 600, AMBER_D, "end"))

    body.append(t(M, 330, "Learning", 92, 800, INK, extra=' letter-spacing="-2"'))
    body.append(t(M, 432, "to think", 92, 800, TEAL, extra=' letter-spacing="-2"'))
    p, _ = para(M, 500, "How AI is reshaping the jobs you're heading into, and the skills that will get you hired",
                30, 760, weight=400, fill=INK2)
    body.append(p)
    body.append(t(M, 680, "Alex Stanhope", 28, 700, INK))
    body.append(t(M, 718, f"Lightenna  ·  {venue}  ·  November 2026", 22, 400, INK2))
    return page("Learning to think",
                "Title slide. One person at the centre directs many AI agents and checks what comes back.",
                None, None, "\n".join(body))


def slide_rewired():
    """Three working weeks as stacked bars. Bands join the same kind of work between weeks, so you can see
    where the time goes: AI takes the producing, then experience grows judgement and leading people appears."""
    body = []
    lx, lw = M, 230                   # row labels
    bx0, bx1 = M + lw + 20, W - M - 130  # bars; the space on the right labels slivers too narrow to hold text
    bw = bx1 - bx0
    bar_h = 72
    rows = [  # (name, descriptor, top y, segments: (key, label, percent, colour))
        ("Graduate, 2000", "Mostly producing", 222, [
            ("produce", "Gathering information", 23, GREY), ("produce", "First drafts", 22, GREY),
            ("produce", "Formatting & admin", 14, GREY), ("check", "Checking", 13, AMBER),
            ("innovate", "Inno-\nvation", 9, PURPLE),
            ("people", "People", 14, RED), ("decide", "Decisions & judgement", 5, BLUE)]),
        ("Graduate, 2026", "Directing, checking, people", 394, [
            ("direct", "Briefing & directing AI agents", 28, TEAL), ("check", "Checking & testing", 28, AMBER),
            ("innovate", "Innovation", 12, PURPLE), ("people", "People: clients, patients, colleagues", 26, RED), ("decide", "Decisions & judgement", 6, BLUE)]),
        ("Experienced colleague, 2026", "Plus judgement and leading", 566, [
            ("direct", "Briefing & directing AI", 22, TEAL), ("check", "Checking & testing", 16, AMBER),
            ("people", "People: clients, patients, colleagues", 40, RED, ("Managing people", 20)),
            ("decide", "Decisions & judgement", 22, BLUE)]),
    ]

    # column headings, as on the profession slides
    body.append(t(lx, 200, "WHO", 18, 700, INK2, extra=' letter-spacing="1.5"'))
    body.append(t(bx0, 200, "A TYPICAL WORKING WEEK", 18, 700, INK2, extra=' letter-spacing="1.5"'))
    body.append(t(W - M, 200, "illustrative", 17, 400, GREY, "end", extra=' font-style="italic"'))

    # measure each row: x extents per segment, and per kind of work for the bands
    spans = []
    for _, _, y, segs in rows:
        x, segx, kinds = bx0, [], {}
        for key, label, pct, col, *_ in segs:
            w = bw * pct / 100
            segx.append((x, w))
            k0, k1 = kinds.get(key, (x, x + w))
            kinds[key] = (min(k0, x), x + w)
            x += w
        assert abs(x - bx1) < 0.5, "segments must add up to 100%"
        spans.append(kinds)

    # bands between consecutive weeks (drawn first, so the bars sit on top)
    body.append(f'<defs><linearGradient id="greyToTeal" x1="0" y1="0" x2="0" y2="1">'
                f'<stop offset="0" stop-color="{GREY}"/><stop offset="1" stop-color="{TEAL}"/></linearGradient></defs>')
    flows = [  # (from week, kind, to week, kind, fill)
        (0, "produce", 1, "direct", "url(#greyToTeal)"), (0, "check", 1, "check", AMBER), (0, "people", 1, "people", RED),
        (0, "innovate", 1, "innovate", PURPLE), (0, "decide", 1, "decide", BLUE),
        (1, "direct", 2, "direct", TEAL), (1, "check", 2, "check", AMBER), (1, "people", 2, "people", RED),
        (1, "decide", 2, "decide", BLUE),
    ]
    for r0, k0, r1, k1, fill in flows:
        (a0, a1), (b0, b1) = spans[r0][k0], spans[r1][k1]
        yt, yb = rows[r0][2] + bar_h + 3, rows[r1][2] - 3
        ym = (yt + yb) / 2
        body.append(f'<path d="M {a0 + 3:.1f} {yt} C {a0 + 3:.1f} {ym}, {b0 + 3:.1f} {ym}, {b0 + 3:.1f} {yb} '
                    f'L {b1 - 3:.1f} {yb} C {b1 - 3:.1f} {ym}, {a1 - 3:.1f} {ym}, {a1 - 3:.1f} {yt} Z" '
                    f'fill="{fill}" fill-opacity="0.10"/>')

    halo = ' stroke="#FFFFFF" stroke-width="7" stroke-linejoin="round" paint-order="stroke"'
    body.append(t(bx0 + 16, 352, "AI agents take on the gathering, drafting and formatting", 20, 700, TEAL_D, extra=halo))
    d0, d1 = spans[2]["decide"]
    body.append(t(d1, 540, "Experience grows judgement", 20, 700, BLUE_D, "end", extra=halo))
    # innovation has no band into the colleague's week: they are too busy doing the job
    i0, i1 = spans[1]["innovate"]
    body.append(t((i0 + i1) / 2, 494, "No time left to innovate", 18, 700, PURPLE_D, "middle", extra=halo))

    # the weeks
    for (name, desc, y, segs), _ in zip(rows, spans):
        name_lines = wrap(name, 24, bx0 - 20 - lx, True)
        for j, ln in enumerate(name_lines):
            body.append(t(lx, y + 32 + j * 29, ln, 24, 700, INK))
        body.append(t(lx, y + 58 + (len(name_lines) - 1) * 29, desc, 17, 400, INK2))
        x = bx0
        for i, (key, label, pct, col, *rest) in enumerate(segs):
            w = bw * pct / 100
            pill = f'x="{x + 3:.1f}" y="{y}" width="{w - 6:.1f}" height="{bar_h}" rx="8"'
            body.append(f'<rect {pill} fill="{col}" fill-opacity="0.12"/>')
            body.append(f'<rect x="{x + 3:.1f}" y="{y}" width="6" height="{bar_h}" rx="3" fill="{col}"/>')
            if rest:
                # part of this pill is a sub-activity, shaded darker inside the same pill
                sub_label, sub_pct = rest[0]
                sw = bw * sub_pct / 100
                sx = x + w - 3 - sw
                cid = f"pill{len(body)}"
                body.append(f'<clipPath id="{cid}"><rect {pill}/></clipPath>')
                body.append(f'<rect x="{sx:.1f}" y="{y}" width="{sw:.1f}" height="{bar_h}" fill="{col}" fill-opacity="0.20" '
                            f'clip-path="url(#{cid})"/>')
                body.append(f'<line x1="{sx:.1f}" y1="{y + 10}" x2="{sx:.1f}" y2="{y + bar_h - 10}" stroke="{col}" '
                            f'stroke-width="2" stroke-dasharray="4 4"/>')
                sub_lines = wrap(sub_label, 17, sw - 30, True)
                assert len(sub_lines) <= 2, f"sub-label too long: {sub_label!r}"
                ty = y + bar_h / 2 + 6 - (len(sub_lines) - 1) * 11
                for j, ln in enumerate(sub_lines):
                    body.append(t(sx + 16, ty + j * 22, ln, 17, 700, INK))
                w_text = w - sw
            else:
                w_text = w
            if "\n" in label:
                lines = label.split("\n")
                assert all(text_w(ln, 17, True) <= w_text - 26 for ln in lines), f"label too wide: {label!r}"
            else:
                lines = wrap(label, 17, w_text - 30, True) if w_text > 100 else None
            if lines and len(lines) <= 2:
                ty = y + bar_h / 2 + 6 - (len(lines) - 1) * 11
                for j, ln in enumerate(lines):
                    body.append(t(x + 20, ty + j * 22, ln, 17, 700, INK))
            else:
                # a sliver: label it in the space to the right of the bar
                assert i == len(segs) - 1, f"only the last segment can be labelled outside the bar: {label!r}"
                dark = {BLUE: BLUE_D, TEAL: TEAL_D, AMBER: AMBER_D, RED: RED_D, GREY: INK2, PURPLE: PURPLE_D}[col]
                out = wrap(label, 16, W - M - bx1 - 14, True)
                ty = y + bar_h / 2 + 6 - (len(out) - 1) * 10
                for j, ln in enumerate(out):
                    body.append(t(bx1 + 14, ty + j * 20, ln, 16, 700, dark))
            x += w

    # the step from graduate to colleague, in the card style of the skills slide
    cy, ch, gap = 678, 150, 24
    cw = (W - 2 * M - gap) / 2
    cards = [
        (BLUE, BLUE_D, "Grow your experience",
         "Graduates make few big calls at first. Experience is what earns better decisions, so start collecting it now."),
        (RED, RED_D, "Learn to lead people",
         "Time with people grows at every step, and half of it becomes managing them. Practise now: captain, mentor, organise."),
    ]
    for i, (col, dark, head, txt) in enumerate(cards):
        x = M + i * (cw + gap)
        body.append(f'<rect x="{x:.1f}" y="{cy}" width="{cw:.1f}" height="{ch}" rx="14" fill="{col}" fill-opacity="0.08" '
                    f'stroke="{col}" stroke-width="3"/>')
        body.append(t(x + 30, cy + 46, head, 27, 700, dark))
        p, h = para(x + 30, cy + 86, txt, 20, cw - 60, lh=28)
        assert 86 + h - 28 + 20 < ch, f"card text overflows: {head!r}"
        body.append(p)

    return page("Your job, rewired",
                "Three working weeks as stacked bars: a graduate in 2000, mostly gathering, drafting and formatting; a "
                "graduate in 2026, briefing and directing AI agents, checking, some innovation and working with people; and an "
                "experienced colleague in 2026, who has no time left to innovate but does far more decisions and judgement and "
                "managing people. Bands "
                "show where the time moves. Two cards name the step up: grow your experience, and learn to lead people.",
                "Your job, rewired",
                "A graduate's week now looks like a colleague's. The gap is judgement and leading people.",
                "\n".join(body))


def slide_profession(data):
    body = []
    # columns
    cx_name, w_name = M, 250
    cx_ai, w_ai = 352, 352
    cx_you, w_you = 752, 352
    cx_start, w_start = 1130, W - M - 1130
    head_y = 202
    heads = [(cx_name, "Profession", INK2, None),
             (cx_ai, "AI takes on", TEAL_D, TEAL),
             (cx_you, "You focus on", BLUE_D, BLUE),
             (cx_start, "Start now", AMBER_D, AMBER)]
    for x, label, col, dot in heads:
        if dot:
            body.append(f'<circle cx="{x + 9}" cy="{head_y - 7}" r="9" fill="{dot}"/>')
            body.append(t(x + 26, head_y, label.upper(), 18, 700, col, extra=' letter-spacing="1.5"'))
        else:
            body.append(t(x, head_y, label.upper(), 18, 700, col, extra=' letter-spacing="1.5"'))

    # lay out rows, measuring first
    rendered = []
    for row in data["rows"]:
        parts, hs = [], []
        name_lines = wrap(row["name"], 26, w_name, True)
        for i, ln in enumerate(name_lines):
            parts.append(("name", i, ln))
        nh = len(name_lines) * 32
        ex_svg, ex_h = para(0, 0, row["example"], 16, w_name, lh=21, fill=INK2)
        hs.append(nh + 14 + ex_h)
        col_h = []
        for items in (row["ai"], row["you"]):
            hh = 0
            for it in items:
                _, h = chip(0, 0, w_ai, it, TEAL, size=18)
                hh += h + 7
            col_h.append(hh - 7)
        st_svg, st_h = para(0, 0, row["start"], 18, w_start - 40, lh=24)
        col_h.append(st_h + 30)
        rendered.append((row, name_lines, max(hs + col_h)))
        print(f"  {row['name']}: name+example={hs[0]} ai={col_h[0]} you={col_h[1]} start={col_h[2]}")

    gap = 26
    total = sum(r[2] for r in rendered) + gap * (len(rendered) - 1)
    avail = 840 - 226
    assert total <= avail, f"{data['file']}: rows need {total}px, only {avail}px available"
    gap = (avail - sum(r[2] for r in rendered)) / max(1, len(rendered) - 1)
    gap = min(gap, 44)
    y = 228

    for idx, (row, name_lines, rh) in enumerate(rendered):
        if idx:
            body.append(f'<line x1="{M}" y1="{y - gap / 2:.1f}" x2="{W - M}" y2="{y - gap / 2:.1f}" stroke="#E3E6EA" stroke-width="2"/>')
        # name + example
        for i, ln in enumerate(name_lines):
            body.append(t(cx_name, y + 24 + i * 32, ln, 26, 700, INK))
        ey = y + 24 + len(name_lines) * 32 + 8
        p, _ = para(cx_name, ey, row["example"], 16, w_name, lh=21, fill=INK2)
        body.append(p)
        # AI chips, arrow, you chips
        for items, x, col in ((row["ai"], cx_ai, TEAL), (row["you"], cx_you, BLUE)):
            cy = y
            for it in items:
                s, h = chip(x, cy, w_ai, it, col, size=18)
                body.append(s)
                cy += h + 7
        mid = y + rh / 2
        body.append(f'<line x1="{cx_ai + w_ai + 8}" y1="{mid:.1f}" x2="{cx_you - 10}" y2="{mid:.1f}" stroke="{GREY}" '
                    f'stroke-width="3.5" marker-end="url(#aGrey)"/>')
        # start now card
        body.append(f'<rect x="{cx_start}" y="{y}" width="{w_start}" height="{rh:.1f}" rx="10" fill="{AMBER}" '
                    f'fill-opacity="0.10" stroke="{AMBER}" stroke-width="2.5"/>')
        p, _ = para(cx_start + 20, y + 30, row["start"], 18, w_start - 40, lh=24)
        body.append(p)
        y += rh + gap

    return page(data["heading"],
                f"{data['heading']}: for each profession, what AI now takes on, what the professional focuses on instead, "
                f"a current real-world example, and one thing a sixth-former can start now.",
                data["heading"], data["sub"], "\n".join(body), data["sources"])


def slide_skills():
    import math
    body = []
    cx, cy, r = 410, 462, 190
    steps = [  # (angle deg, colour, dark, num, word)
        (-90, BLUE, BLUE_D, "01", "Context"),
        (0, TEAL, TEAL_D, "02", "Goal"),
        (90, AMBER, AMBER_D, "03", "Measure"),
        (180, RED, RED_D, "04", "Improve"),
    ]
    arrows = [(BLUE, "aBlue"), (TEAL, "aTeal"), (AMBER, "aAmber"), (RED, "aRed")]
    for i, (col, mk) in enumerate(arrows):
        a0 = math.radians(-90 + i * 90 + 21)
        a1 = math.radians(-90 + (i + 1) * 90 - 21)
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        body.append(f'<path d="M {x0:.1f} {y0:.1f} A {r} {r} 0 0 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{col}" '
                    f'stroke-width="5" marker-end="url(#{mk})"/>')
    for ang, col, dark, num, word in steps:
        a = math.radians(ang)
        nx, ny = cx + r * math.cos(a), cy + r * math.sin(a)
        body.append(f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="54" fill="{col}" fill-opacity="0.13" stroke="{col}" stroke-width="3"/>')
        body.append(t(nx, ny - 4, num, 24, 500, dark, "middle", MONO, ' letter-spacing="2"'))
        body.append(t(nx, ny + 24, word, 18, 700, dark, "middle"))
    # centre: you + agents
    body.append(t(cx, cy - 22, "You", 30, 800, INK, "middle"))
    body.append(t(cx, cy + 8, "directing", 19, 400, INK2, "middle"))
    for i in range(5):
        ax = cx - 64 + i * 32
        body.append(f'<circle cx="{ax}" cy="{cy + 48}" r="12" fill="{TEAL}" fill-opacity="0.18" stroke="{TEAL}" stroke-width="2"/>')
    body.append(t(cx, cy + 90, "many AI agents", 19, 400, INK2, "middle"))

    # skill cards
    cards = [
        (BLUE, BLUE_D, "01  Give context",
         "Explain clearly what you know, what matters and what good looks like.", "Skill: clear writing",
         "\u201cI'm applying to vet school. Here's my work experience so far...\u201d"),
        (TEAL, TEAL_D, "02  Set the goal",
         "Break a big problem into precise jobs an AI can actually do.", "Skill: problem decomposition",
         "\u201cGive me five questions a vet-school interviewer might ask, hardest first.\u201d"),
        (AMBER, AMBER_D, "03  Measure the result",
         "Check, test and fact-check. Never trust, always verify.", "Skill: critical thinking",
         "\u201cWhich of these claims could be wrong? Where would I check?\u201d"),
        (RED, RED_D, "04  Improve and repeat",
         "Say what was wrong, try again, or run several attempts and compare.", "Skill: iteration and curiosity",
         "\u201cQuestion 3 is too easy. Make it about animal-welfare ethics.\u201d"),
    ]
    x, y, w, h = 740, 192, W - M - 740, 126
    for col, dark, head, txt, skill, eg in cards:
        body.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{col}" fill-opacity="0.08" stroke="{col}" stroke-width="2.5"/>')
        body.append(t(x + 24, y + 38, head, 24, 700, dark))
        body.append(t(x + w - 24, y + 38, skill, 18, 600, dark, "end"))
        p, ph = para(x + 24, y + 72, txt, 20, w - 48, lh=27)
        body.append(p)
        assert ph <= 27, f"card text wraps: {txt!r}"
        body.append(t(x + 24, y + 106, eg, 18, 400, INK2, extra=' font-style="italic"'))
        assert text_w(eg, 18) < w - 48, f"example too long: {eg!r}"
        y += h + 14

    # foundation band
    fy = 760
    body.append(f'<rect x="{M}" y="{fy}" width="{W - 2 * M}" height="78" rx="12" fill="{INK}" fill-opacity="0.06" stroke="{INK2}" stroke-width="2"/>')
    body.append(t(M + 28, fy + 33, "THE FOUNDATIONS YOU'RE BUILDING NOW, BY DOING YOUR OWN WORK", 17, 700, INK2, extra=' letter-spacing="1.5"'))
    body.append(t(M + 28, fy + 62, "Subject knowledge  ·  Reasoning  ·  Clear writing  ·  Integrity  ·  Working with people", 22, 700, INK))

    return page("The AI-fluent expert",
                "A four-step loop around 'you directing many AI agents': give context, set the goal, measure the result, "
                "improve and repeat. Each step maps to a learnable skill: clear writing, problem decomposition, critical "
                "thinking, iteration. The loop rests on foundations built at school by doing your own work.",
                "The AI-fluent expert",
                "Four learnable skills on top of the foundations school is already giving you",
                "\n".join(body),
                "The loop: Positive Futures for AI, part 4, 'A thousand typewriters' (lightenna.com)")


def slide_action():
    body = []
    stages = [
        (BLUE, BLUE_D, "This week", [
            "Pick a profession. Ask someone in it: \"How do you use AI in your job?\"",
            "Try two different AI assistants on the same personal question. Compare the answers.",
            "List three things you're curious about. They're your project ideas.",
        ]),
        (TEAL, TEAL_D, "This year, in sixth form", [
            "Keep schoolwork 100% yours. It builds the judgement AI can't give you.",
            "Start one AI project outside school: an app, a plan, a question you love.",
            "Take a free course: Elements of AI, or Anthropic's AI Fluency for Students.",
        ]),
        (AMBER, AMBER_D, "Uni, apprenticeship or first job", [
            "Learn your institution's AI rules, and follow them.",
            "Where AI is allowed, log what you asked, what you checked and what you changed.",
            "Build a portfolio that shows your judgement, not just the outputs.",
        ]),
        (RED, RED_D, "Day one at work", [
            "Arrive able to brief, check and improve an AI's work.",
            "Say: \"Here's how I'd use AI on this, and how I'd check it.\"",
            "Ask which tools the team uses, and get good at them fast.",
        ]),
    ]
    n = len(stages)
    gap = 26
    cw = (W - 2 * M - gap * (n - 1)) / n
    ty = 214
    body.append(f'<line x1="{M}" y1="{ty}" x2="{W - M - 6}" y2="{ty}" stroke="{INK2}" stroke-width="4" marker-end="url(#aGrey)"/>')
    for i, (col, dark, head, items) in enumerate(stages):
        x = M + i * (cw + gap)
        body.append(f'<circle cx="{x + 22}" cy="{ty}" r="15" fill="#FFFFFF" stroke="{col}" stroke-width="5"/>')
        body.append(f'<rect x="{x}" y="{ty + 34}" width="{cw:.1f}" height="444" rx="14" fill="{col}" fill-opacity="0.07" stroke="{col}" stroke-width="2.5"/>')
        hl = wrap(head, 25, cw - 44, True)
        for j, ln in enumerate(hl):
            body.append(t(x + 22, ty + 78 + j * 31, ln, 25, 700, dark))
        y = ty + 78 + len(hl) * 31 + 16
        for it in items:
            body.append(f'<rect x="{x + 22}" y="{y - 17}" width="18" height="18" rx="4" fill="none" stroke="{col}" stroke-width="2.5"/>')
            p, h = para(x + 52, y, it, 19, cw - 74, lh=26)
            body.append(p)
            y += h + 14
        assert y < ty + 34 + 444, f"stage '{head}' overflows its card"

    # golden rule
    gy = 706
    body.append(f'<rect x="{M}" y="{gy}" width="{W - 2 * M}" height="128" rx="14" fill="{AMBER}" fill-opacity="0.14" stroke="{AMBER}" stroke-width="3"/>')
    body.append(t(M + 32, gy + 50, "Never trust, always verify. Always be honest about how you used AI.", 32, 800, INK))
    body.append(t(M + 32, gy + 94, "Do that, and you won't just be ready for the job. You'll be the person who shows everyone else how.", 23, 400, INK2))

    return page("Your head start",
                "A timeline of actions: this week, this year in sixth form, at university or apprenticeship, and on day one "
                "at work. A banner states the golden rule: never trust, always verify, and always be honest about how you used AI.",
                "Your head start",
                "Small steps now, in the right order, put you ahead on day one",
                "\n".join(body),
                "Free courses: elementsofai.com  ·  Anthropic Academy, 'AI Fluency for Students'  ·  alphafold.ebi.ac.uk")


VIDEOS = [  # (link, short link shown, thumbnail: YouTube id or a .jpg in OUT, colour, title, description, details)
    ("https://youtu.be/d95J8yzvjbQ", "youtu.be/d95J8yzvjbQ", "d95J8yzvjbQ", BLUE, "The Thinking Game (full documentary)",
     "The whole story, from learning Atari games to AlphaFold", "Google DeepMind · 1 h 24 min"),
    ("https://youtu.be/r4-hXO7MLVU", "youtu.be/r4-hXO7MLVU", "r4-hXO7MLVU", TEAL, "AlphaFold: The 50-year grand challenge cracked by AI",
     "How AI cracked a 50-year problem in biology", "Google DeepMind · 2:05"),
    ("https://youtu.be/aSY_vFFmkW0", "youtu.be/aSY_vFFmkW0", "aSY_vFFmkW0", AMBER, "Generating novel scientific hypotheses with Co-Scientist",
     "Scientists and AI coming up with new ideas together", "Google DeepMind · 6:25"),
    ("https://youtu.be/sFfPkUJd_Jk", "youtu.be/sFfPkUJd_Jk", "sFfPkUJd_Jk", RED, "Genie 4: A new generation of world simulation",
     "Describe a world in words, then walk around inside it", "Google DeepMind · 2:27"),
    ("https://x.com/lukas_m_ziegler/status/1592502558127722497", "x.com/lukas_m_ziegler", "video-ziegler-nana-korobi-thumb.jpg",
     PURPLE, "Nana korobi, ya oki: fall down seven times, stand up eight",
     "Robots failing, and getting back up", "Lukas Ziegler on X · 1:19"),
]


def video_thumb(ref):
    """Small thumbnail as a data URI: a YouTube id (fetched once and cached next to the slides, so rebuilds
    work offline) or the name of a .jpg already in OUT."""
    path = os.path.join(OUT, ref if ref.endswith(".jpg") else f"video-{ref}-thumb.jpg")
    if not os.path.exists(path):
        req = urllib.request.Request(f"https://i.ytimg.com/vi/{ref}/mqdefault.jpg", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as r, open(path, "wb") as fh:
            fh.write(r.read())
    with open(path, "rb") as fh:
        return "data:image/jpeg;base64," + base64.b64encode(fh.read()).decode()


def slide_videos():
    """Questions, with a compact watch-next list along the bottom. Each row is a link; build_pptx.py reads
    data-box to make the same area clickable in PowerPoint."""
    body = []
    rh, gap = 76, 10
    tw, th = 112, 63
    y = 836 - len(VIDEOS) * rh - (len(VIDEOS) - 1) * gap
    body.append(t(M, y - 20, "WATCH NEXT", 16, 700, INK2, extra=' letter-spacing="1.5"'))
    link_x = W - M - 22
    text_x = M + 20 + tw + 22
    text_w_max = link_x - 260 - text_x
    for i, (url, short, thumb, col, title, desc, meta) in enumerate(VIDEOS):
        dark = {BLUE: BLUE_D, TEAL: TEAL_D, AMBER: AMBER_D, RED: RED_D, PURPLE: PURPLE_D}[col]
        body.append(f'<a href="{escape(url)}" target="_blank" data-box="{M},{y},{W - 2 * M},{rh}">')
        body.append(f'<rect x="{M}" y="{y}" width="{W - 2 * M}" height="{rh}" rx="10" fill="{col}" fill-opacity="0.05" '
                    f'stroke="{col}" stroke-opacity="0.45" stroke-width="1.5"/>')
        body.append(f'<rect x="{M}" y="{y}" width="6" height="{rh}" rx="3" fill="{col}"/>')
        ty = y + (rh - th) / 2
        body.append(f'<clipPath id="thumb{i}"><rect x="{M + 20}" y="{ty}" width="{tw}" height="{th}" rx="6"/></clipPath>')
        body.append(f'<image x="{M + 20}" y="{ty}" width="{tw}" height="{th}" preserveAspectRatio="xMidYMid slice" '
                    f'clip-path="url(#thumb{i})" href="{video_thumb(thumb)}"/>')
        line2 = f"{desc}  ·  {meta}"
        assert text_w(title, 19, True) <= text_w_max, f"video title too long: {title!r}"
        assert text_w(line2, 15) <= text_w_max, f"video description too long: {line2!r}"
        body.append(t(text_x, y + 33, title, 19, 700, INK))
        body.append(t(text_x, y + 58, line2, 15, 400, INK2))
        body.append(t(link_x, y + rh / 2 + 6, short, 17, 600, dark, "end", MONO))
        body.append("</a>")
        y += rh + gap
    return page("Questions",
                "Questions. Along the bottom, five videos to watch next, each with a link: The Thinking Game, AlphaFold, "
                "the AI co-scientist, Genie 4, and Lukas Ziegler's 'Nana korobi, ya oki' robot clip.",
                "Questions",
                "",
                "\n".join(body))


def main():
    os.makedirs(OUT, exist_ok=True)
    # the website keeps the school anonymous; set PPTX_VENUE to name it on the PowerPoint's title
    # slide (build_pptx.py uses a "-pptx" variant of a slide when one exists, and .gitignore keeps
    # those variants out of the public repo)
    slides = [("00-title.svg", slide_title())]
    venue = os.environ.get("PPTX_VENUE")
    if venue:
        slides.append(("00-title-pptx.svg", slide_title(venue)))
    slides.append(("01-your-job-rewired.svg", slide_rewired()))
    slides += [(d["file"], slide_profession(d)) for d in PROFESSION_SLIDES]
    slides += [("05-ai-fluent-expert.svg", slide_skills()), ("06-your-head-start.svg", slide_action()),
               ("07-watch-next.svg", slide_videos())]
    for name, svg in slides:
        with open(os.path.join(OUT, name), "w") as fh:
            fh.write(svg)
        print("wrote", os.path.relpath(os.path.join(OUT, name), ROOT))


if __name__ == "__main__":
    main()
