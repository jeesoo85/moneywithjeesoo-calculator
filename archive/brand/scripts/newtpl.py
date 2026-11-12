"""Shared template for the newer carousel scripts (s09–s18 style), with larger text and overflow check."""
import asyncio, pathlib
from playwright.async_api import async_playwright

ROOT = pathlib.Path("/home/claude/mwj")
F = ROOT / "package/files"
OUT = pathlib.Path("/home/claude/mwj/re/out"); OUT.mkdir(parents=True, exist_ok=True)

CSS = f"""
@font-face{{font-family:PF;src:url('file://{F}/playfair-display-latin-400-normal.woff2');font-weight:400}}
@font-face{{font-family:PF;src:url('file://{F}/playfair-display-latin-800-normal.woff2');font-weight:800}}
@font-face{{font-family:PF;src:url('file://{F}/playfair-display-latin-400-italic.woff2');font-weight:400;font-style:italic}}
:root{{--cream:#F5EFE4;--green:#0E4F3C;--gold:#9C7230;--line:#B8893A;--gsm:#8C6A2A;--ink:#1F2A26;--gray:#4A524E}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:var(--cream);color:var(--ink);font-family:'Noto Serif CJK KR',serif;overflow:hidden}}
.page{{position:relative;width:1080px;height:1350px;padding:0 72px;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:flex-end;padding-top:64px;padding-bottom:18px;border-bottom:2px solid var(--line)}}
.brand{{font-family:Inter;font-weight:600;font-size:20px;letter-spacing:.3em;color:var(--green)}}
.sec{{font-family:Inter;font-weight:600;font-size:25px;letter-spacing:.3em;color:var(--gsm)}}
.body{{flex:1;display:flex;flex-direction:column;justify-content:center;padding:40px 0}}
.foot{{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:56px;gap:40px}}
.note{{font-family:Inter;font-size:26px;line-height:1.4;color:var(--gray)}}
.pg{{font-family:Inter;font-weight:600;font-size:25px;letter-spacing:.15em;color:var(--gsm);white-space:nowrap}}
.lab{{font-family:Inter;font-weight:600;font-size:25px;letter-spacing:.3em;color:var(--gsm);text-transform:uppercase}}
.t{{font-family:PF;font-weight:800;color:var(--green);line-height:1.05}}
.i{{font-family:PF;font-style:italic;font-weight:400;color:var(--gold)}}
.en{{font-family:PF;font-weight:400;font-size:38px;line-height:1.4;color:var(--ink)}}
.kr{{font-size:34px;line-height:1.55;color:var(--gray)}}
.krb{{font-weight:700;color:var(--green)}}
.rule{{width:90px;height:2px;background:var(--line)}}
.num{{font-family:PF;font-weight:800;color:var(--green)}}
.box{{border:2px solid var(--green);padding:40px 44px}}
.box:not(.cta) .en{{font-weight:800;color:var(--green)}}
.box:not(.cta) .kr{{font-weight:700;color:var(--green)}}
table{{width:100%;border-collapse:collapse}}
td,th{{border-bottom:1.5px solid var(--ink);padding:24px 0;text-align:left;vertical-align:middle}}
th{{font-family:Inter;font-weight:600;font-size:25px;letter-spacing:.25em;color:var(--gsm)}}
"""

N = 7
LOGO = '<img src="file:///home/claude/mwj/logo.png" style="width:124px;display:block;margin:0 auto 34px">'

def page(i, sec, body, note=""):
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=page>
<div class=top><div class=brand>MONEY WITH JEESOO</div><div class=sec>{sec}</div></div>
<div class=body>{body}</div>
<div class=foot><div class=note>{note}</div><div class=pg>{i:02d} / {N:02d}</div></div>
</div></body></html>"""

def head(t, i, kr, ts=96, iz=100):
    return f'<div class=t style="font-size:{ts}px">{t}</div><div class=i style="font-size:{iz}px;line-height:1.1">{i}</div><div class=kr style="margin-top:16px;font-size:36px"><span class=krb>{kr}</span></div>'

def listing(items, col=110):
    return "".join(f"""<div style="display:grid;grid-template-columns:{col}px 1fr;padding:26px 0;border-bottom:1.5px solid var(--ink)">
 <div class=num style="font-size:52px;color:var(--gold)">{n}</div>
 <div><div class=en style="font-size:38px;line-height:1.3">{e}</div><div class=kr style="margin-top:6px;font-size:33px">{k}</div></div></div>""" for n, e, k in items)

def cover(no, t, i, kr, en, ko):
    return page(1, no, f"""<div style="text-align:center;display:flex;flex-direction:column;align-items:center">{LOGO}
 <div class=t style="font-size:112px">{t}</div><div class=i style="font-size:124px;line-height:1.1">{i}</div>
 <div class="kr krb" style="font-size:54px;margin-top:36px;line-height:1.35">{kr}</div>
 <div class=rule style="margin:48px 0 40px"></div>
 <div class=en style="font-size:40px">{en}</div><div class=kr style="margin-top:18px;font-size:34px">{ko}</div></div>""", note="TIME · PROTECTION · PRIORITY")

def closing(n, t, i, kr, en, q, kw, ko, offer="the free calculator"):
    return page(n, "CLOSING", f"""<div style="text-align:center;display:flex;flex-direction:column;align-items:center">{LOGO}
 <div class=t style="font-size:100px;letter-spacing:.02em">{t}</div><div class=i style="font-size:116px;line-height:1.1">{i}</div>
 <div class="kr krb" style="font-size:44px;margin-top:22px">{kr}</div>
 <div class=en style="font-size:40px;margin-top:30px">{en}</div>
 <div class="box cta" style="margin-top:60px;width:100%">
  <div class=en style="font-size:40px">{q}</div>
  <div class=en style="font-size:38px;margin-top:16px;color:var(--green);font-weight:800">Comment “{kw}” for {offer}.</div>
  <div class=kr style="margin-top:14px">{ko}</div></div></div>""", note="FOR EDUCATIONAL PURPOSES ONLY")

def grid3(cells):
    out = []
    for k, (big, small) in enumerate(cells):
        pad = "34px 20px 34px 0" if k == 0 else ("34px 0 34px 24px" if k == 2 else "34px 20px")
        br = "border-right:1.5px solid var(--ink);" if k < 2 else ""
        out.append(f'<div style="padding:{pad};{br}"><div class=num style="font-size:58px">{big}</div><div class=kr style="font-size:33px;margin-top:8px">{small}</div></div>')
    return '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;margin-top:60px;border-top:1.5px solid var(--ink);border-bottom:1.5px solid var(--ink)">' + "".join(out) + "</div>"

OVERFLOW_JS = """() => { const b=document.querySelector('.body'); let o=0; for (const c of b.children){ const r=c.getBoundingClientRect(); const br=b.getBoundingClientRect(); o=Math.max(o, r.bottom-br.bottom, br.top-r.top); } return Math.round(Math.max(o, b.scrollHeight-b.clientHeight)); }"""

def render(S, prefix):
    async def main():
        async with async_playwright() as p:
            b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
            pg = await b.new_page(viewport={"width": 1080, "height": 1350})
            for k, html in enumerate(S, 1):
                f = OUT / f"_{prefix}{k}.html"; f.write_text(html)
                await pg.goto(f"file://{f}"); await pg.wait_for_timeout(400)
                ov = await pg.evaluate(OVERFLOW_JS)
                if ov > 0: print(f"OVERFLOW {prefix} slide {k}: {ov}px")
                await pg.screenshot(path=str(OUT / f"{prefix}_{k:02d}.png"))
            await b.close()
    asyncio.run(main())
