import os, asyncio
from playwright.async_api import async_playwright

D = os.path.dirname(os.path.abspath(__file__))
F = "file:///home/claude/mwj/node_modules/@fontsource"
LOGO = "file:///home/claude/mwj/logo.png"

G = "#0E4F3C"; GOLD = "#B8893A"; GOLDT = "#8C6A2A"; INK = "#1F2A26"; BG = "#F5EFE4"
CSS = f"""
@font-face{{font-family:PF;font-weight:400;src:url({F}/playfair-display/files/playfair-display-latin-400-normal.woff2)}}
@font-face{{font-family:PF;font-weight:400;font-style:italic;src:url({F}/playfair-display/files/playfair-display-latin-400-italic.woff2)}}
@font-face{{font-family:PF;font-weight:800;src:url({F}/playfair-display/files/playfair-display-latin-800-normal.woff2)}}
@font-face{{font-family:PF;font-weight:800;font-style:italic;src:url({F}/playfair-display/files/playfair-display-latin-800-italic.woff2)}}
@font-face{{font-family:Int;font-weight:400;src:url({F}/inter/files/inter-latin-400-normal.woff2)}}
@font-face{{font-family:Int;font-weight:500;src:url({F}/inter/files/inter-latin-500-normal.woff2)}}
@font-face{{font-family:Int;font-weight:600;src:url({F}/inter/files/inter-latin-600-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{BG};color:{INK};font-family:Int,sans-serif;position:relative;overflow:hidden}}
.hd{{position:absolute;left:72px;right:72px;top:64px;display:flex;justify-content:space-between;font-family:Int;font-weight:600;font-size:20px;letter-spacing:.3em;padding-bottom:22px;border-bottom:2px solid {GOLD}}}
.hd .l{{color:{G}}} .hd .r{{color:{GOLDT}}}
.wrap{{position:absolute;left:72px;right:72px;top:150px}}
.t{{font-family:PF;font-weight:800;color:{G};line-height:1.0;letter-spacing:-.015em}}
.i{{font-family:PF;font-style:italic;font-weight:400;color:#9C7230;line-height:1.05}}
.ko{{font-family:'Noto Serif CJK KR';font-weight:400;color:#3a4540}}
.kob{{font-family:'Noto Serif CJK KR';font-weight:700;color:{G}}}
.cap{{font-family:Int;font-weight:600;letter-spacing:.3em;color:{GOLDT};font-size:26px;text-transform:uppercase}}
.big{{font-family:PF;font-weight:800;color:{G};line-height:1}}
.line{{border-top:1.5px solid {INK}}}
.pg{{position:absolute;right:72px;bottom:58px;font-family:Int;font-weight:600;font-size:23px;letter-spacing:.2em;color:{GOLDT}}}
.ft{{position:absolute;left:72px;right:220px;bottom:48px;font-family:Int;font-style:italic;font-size:26px;line-height:1.5;color:#4a554f}}
.ftc{{position:absolute;left:72px;bottom:58px;font-family:Int;font-weight:500;font-size:23px;letter-spacing:.24em;color:#6b746f}}
.logo{{display:block;margin:0 auto;width:124px}}
.ctr{{text-align:center}}
.s{{font-family:PF;font-weight:400;font-style:normal;line-height:1.35}}
"""

def page(n, right, body, foot="", total=7):
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body>
<div class="hd"><span class="l">MONEY WITH JEESOO</span><span class="r">{right}</span></div>
<div class="wrap">{body}</div>{foot}<div class="pg">{n:02d} / {total:02d}</div></body></html>"""

CENTER_JS = """() => {
  const w = document.querySelector('.wrap'); if (!w) return;
  const f = w.firstElementChild; if (f) f.style.marginTop = '0px';
  const top = document.querySelector('.hd').getBoundingClientRect().bottom;
  let bottom = 1350;
  document.querySelectorAll('.ft,.ftc,.pg').forEach(e => { bottom = Math.min(bottom, e.getBoundingClientRect().top); });
  const h = w.getBoundingClientRect().height;
  w.style.top = Math.max(top + 40, top + (bottom - top - h) / 2 - 12) + 'px';
}"""

OVERFLOW_JS = """() => {
  const w = document.querySelector('.wrap, .body'); if (!w) return 0;
  let bottom = 1350;
  document.querySelectorAll('.ft,.ftc,.pg,.foot').forEach(e => { bottom = Math.min(bottom, e.getBoundingClientRect().top); });
  return Math.round(w.getBoundingClientRect().bottom - bottom);
}"""

async def _render(S, prefix, outdir, center=True):
    os.makedirs(outdir, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        for i, h in enumerate(S, 1):
            fp = f"{D}/_{prefix}{i}.html"; open(fp,"w").write(h)
            await pg.goto(f"file://{fp}"); await pg.wait_for_timeout(500)
            if center:
                await pg.evaluate(CENTER_JS)
            ov = await pg.evaluate(OVERFLOW_JS)
            if ov > 0: print(f"OVERFLOW {prefix} slide {i}: {ov}px")
            await pg.screenshot(path=f"{outdir}/{prefix}_{i:02d}.png")
        await b.close()

def render(S, prefix, outdir="/home/claude/mwj/re/out", center=True):
    asyncio.run(_render(S, prefix, outdir, center))
