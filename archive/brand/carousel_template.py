import os, asyncio
from playwright.async_api import async_playwright

D = os.path.dirname(os.path.abspath(__file__))
F = f"file://{D}/node_modules/@fontsource"
LOGO = f"file://{D}/logo.png"
OUT = "/home/claude/outputs/rockefeller"
os.makedirs(OUT, exist_ok=True)

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
.cap{{font-family:Int;font-weight:600;letter-spacing:.3em;color:{GOLDT};font-size:24px;text-transform:uppercase}}
.big{{font-family:PF;font-weight:800;color:{G};line-height:1}}
.line{{border-top:1.5px solid {INK}}}
.pg{{position:absolute;right:72px;bottom:58px;font-family:Int;font-weight:600;font-size:21px;letter-spacing:.2em;color:{GOLDT}}}
.ft{{position:absolute;left:72px;right:220px;bottom:48px;font-family:Int;font-style:italic;font-size:23px;line-height:1.5;color:#4a554f}}
.ftc{{position:absolute;left:72px;bottom:58px;font-family:Int;font-weight:500;font-size:19px;letter-spacing:.24em;color:#6b746f}}
.logo{{display:block;margin:0 auto;width:124px}}
.ctr{{text-align:center}}
.s{{font-family:PF;font-weight:400;font-style:normal;line-height:1.35}}
"""

def page(n, right, body, foot=""):
    return f"""<html><head><style>{CSS}</style></head><body>
<div class="hd"><span class="l">MONEY WITH JEESOO</span><span class="r">{right}</span></div>
<div class="wrap">{body}</div>{foot}<div class="pg">{n:02d} / 07</div></body></html>"""

SRC = '<div class="ft">Source: John D. Rockefeller Jr.’s 1920 allowance memo to his son, via Smithsonian Magazine.</div>'
S = []
S.append(page(1, "NO. 04 — FAMILY MONEY", f"""
<div class="ctr" style="margin-top:72px"><img class="logo" src="{LOGO}">
<div class="t" style="font-size:116px;margin-top:44px">The Rockefeller</div>
<div class="i" style="font-size:98px;margin-top:10px;white-space:nowrap">Allowance Contract</div>
<div class="kob" style="font-size:62px;margin-top:20px">록펠러의 용돈 계약서</div>
<div style="width:120px;height:2px;background:{GOLD};margin:46px auto 44px"></div>
<div class="s" style="font-size:42px;color:{INK};line-height:1.35">In 1920, John D. Rockefeller Jr. gave his son<br>$1.50 a week, and written rules.</div>
<div class="ko" style="font-size:30px;margin-top:20px">1920년, 록펠러 2세가 14살 아들에게 준 주 $1.50과 규칙</div></div>
""", f'<div class="ftc" style="color:{GOLDT};font-weight:600">TIME · PROTECTION · PRIORITY</div>'))

S.append(page(2, "THE STORY", f"""
<div class="t" style="font-size:100px;margin-top:40px">Not a trust fund.</div>
<div class="i" style="font-size:100px">A notebook.</div>
<div class="ko" style="font-size:33px;margin-top:16px">신탁 이야기가 아니에요. 공책 한 권 이야기예요.</div>
<div style="height:2px;background:{GOLD};margin:70px 0 56px"></div>
<div style="font-size:31px;line-height:1.55">John D. Rockefeller Jr. was the son of the richest man in America. Yet his kids got a small weekly allowance, with written rules.</div>
<div class="ko" style="font-size:29px;line-height:1.6;margin-top:24px">미국 최고 부자의 아들이었던 록펠러 2세는 자녀에게 큰돈 대신 적은 용돈과 문서로 된 규칙을 줬어요.</div>
<div class="s" style="font-size:40px;color:{INK};margin-top:56px">The goal wasn't money. It was habits.</div>
<div class="ko" style="font-size:28px;margin-top:10px">목표는 돈이 아니라 습관이었어요.</div>
""", SRC))

rules=[("Allowance","$1.50","일주일 용돈"),("Accurate books","+10¢","장부를 정확히 쓰면 인상 (최대 $2)"),("Mistakes","−10¢","틀리면 다음 주 삭감"),("Give","20%+","최소 20%는 기부"),("Save","20%+","최소 20%는 저축")]
rows="".join(f'''<div class="line" style="display:flex;justify-content:space-between;align-items:center;padding:20px 0">
<div><div class="cap" style="font-size:25px">{a}</div><div class="ko" style="font-size:30px;margin-top:8px">{c}</div></div>
<span class="big" style="font-size:80px">{b}</span></div>''' for a,b,c in rules)
S.append(page(3, "THE RULES", f"""
<div class="t" style="font-size:96px;margin-top:10px">The rules</div>
<div class="i" style="font-size:96px">in writing.</div>
<div class="ko" style="font-size:31px;margin-top:12px">규칙은 글로 적어 두었어요.</div>
<div style="margin-top:44px">{rows}<div class="line"></div></div>
""", '<div class="ft">Per week, from the 1920 memo. Every purchase had to be written down. 모든 지출은 장부에 기록.</div>'))

S.append(page(4, "THE MATCH", f"""
<div class="t" style="font-size:100px;margin-top:40px">Save more,</div>
<div class="i" style="font-size:100px">Dad matches.</div>
<div class="ko" style="font-size:33px;margin-top:16px">더 저축하면, 아빠가 같은 금액을 더 넣어줬어요.</div>
<div class="line" style="margin-top:80px"></div>
<div style="display:flex;justify-content:space-between;align-items:center;padding:36px 0"><span class="cap" style="font-size:24px">Extra savings</span><span class="big" style="font-size:110px;color:{INK}">$1</span></div>
<div class="line"></div>
<div style="display:flex;justify-content:space-between;align-items:center;padding:36px 0"><span class="cap" style="font-size:24px">Dad adds</span><span class="big" style="font-size:110px">+$1</span></div>
<div class="line"></div>
<div class="s" style="font-size:44px;color:{INK};margin-top:44px">Sound familiar? It's an employer match.</div>
<div class="ko" style="font-size:29px;margin-top:12px">익숙하죠? 지금의 회사 매칭과 같은 원리예요.</div>
""", SRC))

why=[("Write it down.","You can't manage what you don't see.","기록해야 보여요."),("Set it aside first.","Give and save before spending.","쓰기 전에 먼저 떼어 둬요."),("Reward the habit.","Raises came from good records, not asking.","조르는 게 아니라 습관에 보상해요.")]
wr="".join(f'''<div class="line" style="display:flex;gap:36px;padding:30px 0">
<div class="big" style="font-size:64px;width:100px;color:#9C7230">0{i+1}</div>
<div><div class="t" style="font-size:52px">{a}</div><div style="font-size:30px;margin-top:10px;line-height:1.35">{b}</div><div class="ko" style="font-size:30px;margin-top:6px">{c}</div></div></div>''' for i,(a,b,c) in enumerate(why))
S.append(page(5, "WHY IT WORKED", f"""
<div class="t" style="font-size:96px;margin-top:10px">Why it</div>
<div class="i" style="font-size:96px">worked.</div>
<div class="ko" style="font-size:31px;margin-top:12px">이 계약서가 가르친 세 가지</div>
<div style="margin-top:56px">{wr}<div class="line"></div></div>
"""))

home=[("Weekly allowance","$10"),("Save first · 저축","$2"),("Give · 기부","$2"),("Spend · 쓰는 돈","$6"),("Extra saved? You match","+$1 = +$1")]
hr="".join(f'''<div class="line" style="display:flex;justify-content:space-between;align-items:center;padding:24px 0">
<span class="cap" style="font-size:26px">{a}</span><span class="big" style="font-size:{60 if i==4 else 76}px;{'' if i in (0,4) else 'color:'+INK}">{b}</span></div>''' for i,(a,b) in enumerate(home))
S.append(page(6, "TRY IT AT HOME", f"""
<div class="t" style="font-size:96px;margin-top:10px">A 2026</div>
<div class="i" style="font-size:96px">version.</div>
<div class="ko" style="font-size:31px;margin-top:12px">우리 집 버전으로 바꿔 보면</div>
<div style="margin-top:44px">{hr}<div class="line"></div></div>
<div style="font-size:29px;margin-top:26px">Keep a notebook. Check it together weekly.</div>
<div class="ko" style="font-size:29px;margin-top:8px">작은 공책 하나, 일주일에 한 번 같이 확인하기.</div>
""", '<div class="ft">Example only. Adjust to your family. 예시 금액이에요.</div>'))

S.append(page(7, "CLOSING", f"""
<div class="ctr" style="margin-top:80px"><img class="logo" src="{LOGO}">
<div class="t" style="font-size:112px;margin-top:40px">HABITS</div>
<div class="i" style="font-size:104px">OUTLAST MONEY</div>
<div class="kob" style="font-size:48px;margin-top:14px">습관은 돈보다 오래 남아요</div>
<div class="s" style="font-size:40px;color:{INK};margin-top:44px;line-height:1.35">Small amounts. Clear rules.<br>Started early.</div>
<div class="ko" style="font-size:28px;margin-top:14px">적은 돈, 분명한 규칙, 일찍 시작하기.</div></div>
<div style="margin-top:56px;border:2px solid {G};padding:34px 30px" class="ctr">
<div class="s" style="font-size:38px;color:{G}">Want to see small savings grow?</div>
<div class="t" style="font-size:46px;margin-top:8px">Comment “TIME” for the free calculator.</div>
<div class="ko" style="font-size:29px;margin-top:10px">무료 계산기가 필요하시면 “TIME” 남겨주세요.</div></div>
""", '<div class="ftc">FOR EDUCATIONAL PURPOSES ONLY</div>'))

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        for i, h in enumerate(S, 1):
            fp = f"{D}/r{i}.html"; open(fp,"w").write(h)
            await pg.goto(f"file://{fp}"); await pg.wait_for_timeout(500)
            await pg.screenshot(path=f"{OUT}/Rockefeller_{i:02d}.png")
        await b.close()
asyncio.run(main())
