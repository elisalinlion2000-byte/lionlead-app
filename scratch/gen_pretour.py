import pathlib
P = pathlib.Path('/home/claude/lionlead/project')

FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&amp;display=swap">'
BASECSS = "body{margin:0;font-family:'Noto Sans TC',system-ui,sans-serif}\na{color:#222;text-decoration:none}a:hover{color:#222}"
BELL = '<a href="Notify.dc.html" aria-label="通知" style="position:relative;width:42px;height:42px;border-radius:21px;background:#fff;display:flex;align-items:center;justify-content:center"><svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="1.8"><path d="M6 17V11a6 6 0 0 1 12 0v6l1.5 2h-15z"/><path d="M10 21h4"/></svg><span style="position:absolute;top:8px;right:9px;width:7px;height:7px;border-radius:4px;background:#E8363D"></span></a>'
BCAST = '<button type="button" aria-label="離線模式" style="width:42px;height:42px;border-radius:21px;border:0;background:#FDE4E6;display:flex;align-items:center;justify-content:center;padding:0"><svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#E8363D" stroke-width="1.8"><circle cx="12" cy="12" r="2"/><path d="M7.8 7.8a6 6 0 0 0 0 8.4M16.2 7.8a6 6 0 0 1 0 8.4M4.9 4.9a10 10 0 0 0 0 14.2M19.1 4.9a10 10 0 0 1 0 14.2"/></svg></button>'
def back(href):
    return f'<a href="#back" aria-label="返回" style="width:42px;height:42px;border-radius:21px;background:#3b3b3b;display:flex;align-items:center;justify-content:center"><svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4"><path d="M15 5l-7 7 7 7"/></svg></a>'
def header_center(title, href):
    return f'<header style="height:80px;display:flex;align-items:center;justify-content:space-between;padding:0 20px;position:relative">{back(href)}<h1 style="position:absolute;left:0;right:0;text-align:center;margin:0;font-size:22px;font-weight:700;color:#222;pointer-events:none">{title}</h1><div style="display:flex;gap:12px">{BELL}{BCAST}</div></header>'
TABCSS = '''.tab{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;width:56px;height:54px;border-radius:27px;font-size:12px;color:#333;background:#fff}
.tab.on{background:#E8363D;color:#fff}
.tab svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:1.8}'''
def tabbar(active):
    def t(name, href, icon):
        on = ' on' if name == active else ''
        return f'<a class="tab{on}" href="{href}">{icon}{name}</a>'
    home = t('首頁','Home.dc.html','<svg viewBox="0 0 24 24"><path d="M4 11l8-7 8 7v9H4z"/><path d="M10 20v-6h4v6"/></svg>')
    pre = t('出團前','PreTour.dc.html','<svg viewBox="0 0 24 24"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9zM8 11h8M8 15h8"/></svg>')
    tour = t('帶團中','Tour.dc.html','<svg viewBox="0 0 24 24"><path d="M6 21V4h12l-3 4 3 4H6"/></svg>')
    after = t('回團後','PostTour.dc.html','<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M8 12l3 3 5-6"/></svg>')
    mine = t('我的','Mine.dc.html','<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg>')
    return f'<nav aria-label="主選單" style="position:absolute;left:245px;bottom:26px;width:330px;height:64px;box-sizing:border-box;border-radius:40px;background:#3b3b3b;display:flex;align-items:center;justify-content:space-between;padding:3px">{home}<div style="display:flex;background:#fff;border-radius:27px;height:54px;align-items:center">{pre}{tour}{after}</div>{mine}</nav>'

def page_raw(title, css, inner, w=820):
    return f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONT}
<style>
{BASECSS}
{css}
</style>
</helmet>
{inner}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":1180}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''

def page(title, css, body, w=820, h=1180):
    return f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONT}
<style>
{BASECSS}
{css}
</style>
</helmet>
<div style="width:{w}px;height:{h}px;box-sizing:border-box;background:#F5F5F5;position:relative;overflow:hidden">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''

# ---------- 出團前 ----------
FN_ICON = {
  '行程表':'<svg viewBox="0 0 24 24"><path d="M5 3h11v18H5z"/><path d="M8 7h5M8 11h5M8 15h3"/><path d="M14 13l4 2-4 2z"/></svg>',
  '說明會資料':'<svg viewBox="0 0 24 24"><path d="M5 3h11v18H5z"/><path d="M8 7h5M8 11h5"/><circle cx="16" cy="16" r="3"/><path d="M18 18l3 3"/></svg>',
  '團體大表':'<svg viewBox="0 0 24 24"><path d="M5 3h11v18H5z"/><path d="M8 7h5M8 11h5"/><circle cx="17" cy="16" r="2.5"/><path d="M13 22c0-2 2-3 4-3s4 1 4 3"/></svg>',
  '分房表':'<svg viewBox="0 0 24 24"><path d="M5 3h11v18H5z"/><path d="M8 7h5M8 11h5"/><path d="M13 15h7v6h-7z"/><path d="M15 15v-2h3v2"/></svg>',
  '交班文件':'<svg viewBox="0 0 24 24"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9z"/><path d="M8 11h8M8 15h8"/></svg>',
  '同意書':'<svg viewBox="0 0 24 24"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9z"/><path d="M8 13l3 3 5-6"/></svg>',
  '日報表':'<svg viewBox="0 0 24 24"><rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M8 3v4M16 3v4"/><path d="M9 15l2 2 4-4"/></svg>',
  '發送簡訊':'<svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-4 4z"/><path d="M8 9h8M8 12h5"/></svg>',
  'APP公告':'<svg viewBox="0 0 24 24"><path d="M3 10v4h4l6 4V6L7 10z"/><path d="M16 9a4 4 0 0 1 0 6"/></svg>',
}
def fn(label, href, gate):
    # gate: '' always on; 'sign' needs signed; 'tour' needs 帶團中; 'ready' needs red 可交班
    cls = 'fn' + (f' need-{gate}' if gate else '')
    return f'<a class="{cls}" href="#{href}">{FN_ICON[label]}{label}</a>'

# ---------- 出團前：四團＝四種狀態（固定展示） ----------
PRE_STATES = {
 'unsigned': ('', '<a href="#Contract" class="pb pb-main" style="background:#E8363D;color:#fff">填寫委任契約書</a>'),
 'grey':     ('signed', '<span class="pb pb-main" style="background:#E5E5E5;color:#aaa">線上交班準備中</span>'),
 'ready':    ('signed ready', '<a href="#HandoverDone" class="pb pb-main" style="background:#E8363D;color:#fff">線上交班</a>'),
 'done':     ('signed ready done', '<span class="pb pb-main" style="background:#E5E5E5;color:#777">準備出發</span>'),
}
PRE_TEAMS = [
 ('unsigned','2026/11/30(一)~2026/12/05(六)','26JPN30BRA','日本東京迪士尼遊透透','28人 / 0人'),
 ('grey','2026/12/06(日)~2026/12/10(四)','26JKD06BXE-T','ITF特選釜山雙樂園滑車塗鴉好好逛5日','28人 / 0人'),
 ('ready','2026/12/10(四)~2026/12/15(二)','26SKD01BRD-T','經典漫遊金邊吳哥(無購物)長榮6日','28人 / 0人'),
 ('done','2026/12/18(四)~2026/12/25(五)','26EGD18BR-T','每月一物特選德國浪漫大道輕旅行8日','28人 / 0人'),
]
def pre_group(dep, no, name, pax):
    return f'''<div style="display:flex"><span class="k">出團日</span><span class="v">{dep}</span></div>
<div style="display:flex"><span class="k">團號</span><a class="v" href="#Itinerary" style="color:#E8363D;text-decoration:underline">{no}</a></div>
<div style="display:flex"><span class="k">團名</span><span class="v">{name}</span></div>
<div style="display:flex"><span class="k">旅客名單</span><span class="v">{pax} <span style="color:#999;font-size:14px">(KK/Join)</span></span></div>'''
def pre_grid():
    return f'''<div class="fgrid">
{fn('行程表','Itinerary','')}{fn('說明會資料','Meeting','sign')}{fn('團體大表','Roster','tour')}
{fn('分房表','noop','tour')}{fn('交班文件','HandoverDone','ready')}{fn('同意書','Consent','done')}
{fn('日報表','Daily3','tour')}{fn('發送簡訊','SmsSend','sign')}
</div>'''
def pre_card(state, dep, no, name, pax, live=False):
    caps, banner = PRE_STATES[state]
    pid = ' id="preLive"' if live else ''
    if live:
        caps = ''
        banner = '<a id="pbLive" href="#Contract" class="pb pb-main" style="background:#E8363D;color:#fff">填寫委任契約書</a>'
    return f'''<div class="pcard {caps}"{pid} style="background:#fff;border-radius:14px;box-shadow:0 2px 8px rgba(0,0,0,.08);box-sizing:border-box;padding:14px 14px 12px;display:flex;flex-direction:column;gap:10px">
{banner}
{pre_group(dep, no, name, pax)}
{pre_grid()}
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:2px"><button type="button" style="border:0;background:none;padding:0;font-family:inherit;font-size:17px;color:#999">RC/TP/OP ⌄</button><a href="#Qbox" style="font-size:18px;color:#222;border-bottom:2px dashed #999;line-height:1.4">Q 信箱</a></div>
</div>'''
pre_css = TABCSS + '''
.k{color:#333;font-size:16px;width:84px;flex:none}
.v{color:#222;font-size:16px;line-height:1.5}
.pb{height:44px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:700;text-decoration:none}
.fgrid{display:grid;grid-template-columns:repeat(3, minmax(0, 1fr));gap:10px;margin-top:4px}
.fn{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;height:72px;border:1px solid #ddd;border-radius:8px;background:#fff;color:#222;font-size:15px;text-decoration:none}
.fn svg{width:30px;height:30px;stroke:#E8363D;fill:none;stroke-width:1.8}
.pcard + .pcard{margin-top:14px}
.pcard:not(.signed) .need-sign,.pcard .need-tour,.pcard:not(.ready) .need-ready,.pcard:not(.done) .need-done{color:#bbb;pointer-events:none}
.pcard:not(.signed) .need-sign svg,.pcard .need-tour svg,.pcard:not(.ready) .need-ready svg,.pcard:not(.done) .need-done svg{stroke:#bbb}'''
pre_cards = '\n'.join(pre_card(*t, live=(i == 0)) for i, t in enumerate(PRE_TEAMS))
pre_body = f'''<header style="height:80px;display:flex;align-items:center;justify-content:space-between;padding:0 20px 0 26px"><h1 style="margin:0;font-size:22px;font-weight:700;color:#222">出團前</h1><div style="display:flex;gap:12px">{BELL}{BCAST}</div></header>
<div style="display:flex;align-items:center;justify-content:space-between;margin:0 20px"><div style="display:flex;align-items:center;gap:14px"><button type="button" style="display:flex;align-items:center;gap:6px;height:42px;padding:0 16px;border:1px solid #ddd;border-radius:21px;background:#fff;font-family:inherit;font-size:18px"><svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="2"><circle cx="11" cy="11" r="6"/><path d="M16 16l4 4"/></svg>查找</button><span style="font-size:17px;color:#999">輸入團號或日期查找</span></div><span style="font-size:17px">共4筆</span></div>
<div style="margin:14px 20px 0">
{pre_cards}
</div>
{tabbar('出團前')}'''
pre_inner = f'''<div style="width:820px;min-height:1180px;box-sizing:border-box;background:#F5F5F5;position:relative;padding-bottom:180px">
{pre_body}
</div>'''
(P/'PreTour.dc.html').write_text(page_raw('出團前', pre_css, pre_inner), encoding='utf-8')

# ---------- 回團後：四種情境（固定展示） ----------
POST_ITEMS = ['行程表','說明會資料','團體大表','分房表','交班文件','同意書','日報表','發送簡訊','APP公告']
POST_HREF = {'行程表':'Itinerary','說明會資料':'Meeting','團體大表':'Roster','交班文件':'HandoverDone','同意書':'Consent','日報表':'Daily3','發送簡訊':'SmsSend'}
def post_active(state, label):
    if state == 's1': return True
    if state == 's2': return label != '日報表'
    if state == 's3': return label == '日報表'
    return False  # s4：全部不可點
def post_grid(state):
    cells = ''
    for lb in POST_ITEMS:
        act = post_active(state, lb)
        href = POST_HREF.get(lb, 'noop')
        cls = 'fn' if act else 'fn afoff'
        hx = f' href="#{href}"' if act else ''
        cells += f'<a class="{cls}"{hx}>{FN_ICON[lb]}{lb}</a>'
    return f'<div class="fgrid">{cells}</div>'
CHECK = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#1aa260" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M8 12l3 3 5-6"/></svg>'
FLAG = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#E8363D" stroke-width="2"><path d="M4 5h16v11H9l-4 4z"/><path d="M8 9h8"/></svg>'
def rev_box():
    return (f'<div class="rev"><div class="revh"><span class="lbl">{FLAG} 評論</span>'
            f'<span style="color:#999">意見表 20 份</span></div>'
            f'<div class="revs"><div><b>80</b><span>服務</span></div><div><b>80</b><span>專車</span></div>'
            f'<div><b>10</b><span>導遊</span></div><div><b>2</b><span>客訴</span></div></div></div>')
def post_card(state, done, days, dep, no, name, pax, live=False):
    badge = f'<span class="rdone">完成 {CHECK}</span>' if done else ''
    grid_html = '' if state == 's4' else post_grid(state)  # 情境4：全部不可點，按鈕不顯示
    pid = ' id="postLive"' if live else ''   # 情境1＝剛回團的東京迪士尼團，按回團日24:00 才出現
    hide = 'display:none;' if live else ''
    return f'''<div class="pcard"{pid} style="{hide}background:#fff;border-radius:14px;box-shadow:0 2px 8px rgba(0,0,0,.08);box-sizing:border-box;padding:14px 14px 12px;display:flex;flex-direction:column;gap:10px">
<div class="rbanner"><span class="rdays">共 <b>{days}</b> 天</span>{badge}</div>
{pre_group(dep, no, name, pax)}
{rev_box()}
{grid_html}
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:2px"><button type="button" style="border:0;background:none;padding:0;font-family:inherit;font-size:17px;color:#999">RC/TP/OP ⌄</button><a href="#Qbox" style="font-size:18px;color:#222;border-bottom:2px dashed #999;line-height:1.4">Q 信箱</a></div>
</div>'''
POST_TEAMS = [
 ('s1', False, '6', '2026/11/30(一)~2026/12/05(六)', '26JPN30BRA', '日本東京迪士尼遊透透', '28人 / 0人'),
 ('s2', True,  '2', '2026/12/02(二)~2026/12/03(三)', '26TED02MKK-T', '旅展Z宜花大人囝仔買菜2日', '28人 / 0人'),
 ('s3', False, '2', '2026/10/07(二)~2026/10/08(三)', '26TMO07MIU-T', '99Z投秋賞九九峰氦氣球清境2日', '28人 / 0人'),
 ('s4', True,  '1', '2026/10/01(四)~2026/10/01(四)', '26TNO01DSL-T', '秋賞特選Z桃大人囝仔大溪落羽松1日', '28人 / 0人'),
]
post_css = TABCSS + '''
.k{color:#333;font-size:16px;width:84px;flex:none}
.v{color:#222;font-size:16px;line-height:1.5}
.fgrid{display:grid;grid-template-columns:repeat(3, minmax(0, 1fr));gap:10px;margin-top:4px}
.fn{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;height:72px;border:1px solid #ddd;border-radius:8px;background:#fff;color:#222;font-size:15px;text-decoration:none}
.fn svg{width:30px;height:30px;stroke:#E8363D;fill:none;stroke-width:1.8}
.fn.afoff{color:#bbb;pointer-events:none}
.fn.afoff svg{stroke:#bbb}
.pcard + .pcard{margin-top:14px}
.rbanner{display:flex;justify-content:space-between;align-items:center}
.rdays{font-size:18px;font-weight:700;color:#222}
.rdays b{color:#E8363D}
.rdone{display:flex;align-items:center;gap:5px;color:#1aa260;font-size:16px;font-weight:700}
.rev{border:1px solid #eee;border-radius:10px;padding:10px 12px;display:flex;flex-direction:column;gap:8px}
.revh{display:flex;align-items:center;gap:10px;font-size:15px}
.revh .lbl{display:flex;align-items:center;gap:5px;color:#E8363D;font-weight:700}
.revs{display:flex;justify-content:space-around;text-align:center}
.revs div{display:flex;flex-direction:column;gap:2px}
.revs b{font-size:22px;color:#222}
.revs span{font-size:13px;color:#999}'''
post_cards = '\n'.join(post_card(*t, live=(t[0] == 's1')) for t in POST_TEAMS)
post_body = f'''<header style="height:80px;display:flex;align-items:center;justify-content:space-between;padding:0 20px 0 26px"><h1 style="margin:0;font-size:22px;font-weight:700;color:#222">回團後</h1><div style="display:flex;gap:12px">{BELL}{BCAST}</div></header>
<div style="display:flex;align-items:center;justify-content:space-between;margin:0 20px"><div style="display:flex;align-items:center;gap:14px"><button type="button" style="display:flex;align-items:center;gap:6px;height:42px;padding:0 16px;border:1px solid #ddd;border-radius:21px;background:#fff;font-family:inherit;font-size:18px"><svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="2"><circle cx="11" cy="11" r="6"/><path d="M16 16l4 4"/></svg>查找</button><span style="font-size:17px;color:#999">輸入團號或日期查找</span></div><span style="font-size:17px" id="postCount">共3筆</span></div>
<div style="margin:14px 20px 0">
{post_cards}
<div style="text-align:center;color:#bbb;font-size:16px;padding:18px 0 4px">已經到底了！</div>
</div>
{tabbar('回團後')}'''
post_inner = f'''<div style="width:820px;min-height:1180px;box-sizing:border-box;background:#F5F5F5;position:relative;padding-bottom:180px">
{post_body}
</div>'''
(P/'PostTour.dc.html').write_text(page_raw('回團後', post_css, post_inner), encoding='utf-8')

# ---------- 同意書 模組 ----------
CHK_ON = '<span style="width:22px;height:22px;background:#E8363D;border-radius:5px;display:inline-flex;align-items:center;justify-content:center;flex:none"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M5 12l5 5 9-10"/></svg></span>'
CHK_OFF = '<span style="width:22px;height:22px;border:1.5px solid #c4c4c4;border-radius:5px;display:inline-block;flex:none"></span>'
RAD_ON = '<span style="width:20px;height:20px;border:1.5px solid #E8363D;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;flex:none"><span style="width:11px;height:11px;background:#E8363D;border-radius:50%"></span></span>'
RAD_OFF = '<span style="width:20px;height:20px;border:1.5px solid #c4c4c4;border-radius:50%;display:inline-block;flex:none"></span>'
def ac_head(active):
    s1 = 'background:#E8363D;color:#fff' if active == 'set' else 'color:#888'
    s2 = 'background:#E8363D;color:#fff' if active == 'view' else 'color:#888'
    return f'''<header style="height:72px;display:flex;align-items:center;justify-content:space-between;padding:0 20px;position:relative">
<a href="#back" aria-label="返回" style="width:40px;height:40px;border-radius:20px;background:#3b3b3b;display:flex;align-items:center;justify-content:center"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4"><path d="M15 5l-7 7 7 7"/></svg></a>
<h1 style="position:absolute;left:0;right:0;text-align:center;margin:0;font-size:21px;font-weight:700;color:#222;pointer-events:none">同意書</h1>
<div style="display:flex;gap:10px">{BELL}{BCAST}</div>
</header>
<div style="display:flex;margin:4px 20px 0;background:#ECECEC;border-radius:22px;padding:3px">
<a href="Consent.dc.html" style="flex:1;text-align:center;padding:9px 0;border-radius:20px;font-size:17px;font-weight:600;text-decoration:none;{s1}">同意書設定</a>
<a href="ConsentView.dc.html" style="flex:1;text-align:center;padding:9px 0;border-radius:20px;font-size:17px;font-weight:600;text-decoration:none;{s2}">同意書檢視</a>
</div>'''
def ac_step(label, sub=''):
    s = f'<div style="color:#999;font-size:14px;line-height:1.6;margin-top:6px">{sub}</div>' if sub else ''
    return (f'<div style="display:flex;align-items:center;gap:8px;margin-top:24px"><span style="width:4px;height:19px;background:#E8363D;border-radius:2px"></span>'
            f'<span style="font-size:18px;font-weight:700;color:#222">{label}</span></div>{s}')
AC_CSS = TABCSS + '''
.ac-cb{appearance:none;-webkit-appearance:none;width:22px;height:22px;border:1.5px solid #c4c4c4;border-radius:5px;margin:0;flex:none;cursor:pointer;position:relative;background:#fff}
.ac-cb:checked{background:#E8363D;border-color:#E8363D}
.ac-cb:checked::after{content:"";position:absolute;left:6px;top:2px;width:6px;height:11px;border:solid #fff;border-width:0 3px 3px 0;transform:rotate(45deg)}
.ac-rad{appearance:none;-webkit-appearance:none;width:20px;height:20px;border:1.5px solid #c4c4c4;border-radius:50%;margin:0;flex:none;cursor:pointer;position:relative;background:#fff}
.ac-rad:checked{border-color:#E8363D}
.ac-rad:checked::after{content:"";position:absolute;left:3.5px;top:3.5px;width:10px;height:10px;border-radius:50%;background:#E8363D}
.seg{border:1px solid #d5d5d5;color:#555;background:#fff;border-radius:22px;padding:10px 0;text-align:center;font-size:16px;cursor:pointer;display:block}
.seg:has(input:checked){border:1.5px solid #E8363D;color:#E8363D;font-weight:600}
.typ{display:block;border:1px solid #ddd;color:#333;background:#fff;border-radius:10px;padding:14px 16px;font-size:17px;cursor:pointer}
.typ:has(input:checked){border:1.5px solid #E8363D;color:#E8363D;font-weight:600}
.shopname{display:none;width:100%;box-sizing:border-box;border:1px solid #ddd;border-radius:8px;padding:11px 14px;font-size:16px;margin-top:12px;font-family:inherit}
.verwrap:has(input[value="no"]:checked) .shopname{display:block}
.ac-orow{display:flex;align-items:center;gap:10px;padding:12px 4px}
.ac-cline{display:flex;align-items:center;gap:12px;flex:1;cursor:pointer;min-width:0}
.ac-rc{display:flex;align-items:center;gap:5px;color:#555;font-size:15px;cursor:pointer}
.ac-exp{width:26px;height:26px;border:1px solid #ccc;border-radius:50%;background:#fff;color:#888;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex:none}
.ac-sub{flex-direction:column;gap:2px;padding:0 4px 8px 34px}
.ac-paxrow{display:flex;align-items:center;gap:12px;padding:9px 0;font-size:16px;color:#333;cursor:pointer}
.ac-divider{height:1px;background:#eee}'''
def seg(name, text, val, checked=False):
    c = ' checked' if checked else ''
    return f'<label class="seg"><input type="radio" name="{name}" value="{val}" hidden{c}>{text}</label>'
def typ(text, checked=False):
    c = ' checked' if checked else ''
    return f'<label class="typ"><input type="radio" name="ac-type" hidden{c}>{text}</label>'
def orow(idx):
    sub = ''.join(f'<label class="ac-paxrow"><input type="checkbox" class="ac-cb">旅客{i+1}：李小明</label>' for i in range(4))
    return (f'<div class="ac-orow"><label class="ac-cline"><input type="checkbox" class="ac-cb ord-chk">'
            f'<span style="font-size:17px;color:#222">2026-111072</span></label>'
            f'<label class="ac-rc"><input type="radio" name="rc{idx}" data-sub="sub{idx}" data-role="order" class="ac-rad">訂單</label>'
            f'<label class="ac-rc"><input type="radio" name="rc{idx}" data-sub="sub{idx}" data-role="pax" class="ac-rad">旅客</label>'
            f'<button type="button" class="ac-exp" data-t="sub{idx}">＋</button></div>'
            f'<div class="ac-sub" id="sub{idx}" style="display:none">{sub}</div><div class="ac-divider"></div>')
set_orders = ''.join(orow(i) for i in range(1, 5))
consent_body = f'''{ac_head('set')}
{ac_step('Step-1：選擇版型','為雄獅出團的團體有雄獅 logo 版；若自行輸入旅行社名稱則為無 logo 版。')}
<div class="verwrap"><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px">{seg('ver','雄獅 logo','lion',True)}{seg('ver','無 Logo 版','no')}</div>
<input class="shopname" placeholder="請輸入旅行社名稱"></div>
{ac_step('Step-2：選擇同意書')}
<div style="display:flex;flex-direction:column;gap:12px;margin-top:12px">
{typ('行程變更同意書', True)}{typ('脫隊確認書')}{typ('不就醫同意書')}{typ('不報案同意書')}{typ('代金領取同意書')}
</div>
{ac_step('Step-3：選擇發送名單','選擇訂單會生成該訂單旅客的同意書；選擇旅客可單獨指定旅客生成同意書。')}
<label class="ac-cline" style="padding:14px 4px 12px"><input type="checkbox" class="ac-cb ac-all"><span style="font-size:17px;color:#222;font-weight:600">訂單編號（全選）</span></label>
<div class="ac-divider"></div>
{set_orders}
<div style="display:flex;gap:14px;margin:26px 4px 0">
<a href="PreTour.dc.html" style="flex:1;text-align:center;padding:13px 0;border:1px solid #ccc;border-radius:10px;color:#555;font-size:18px;text-decoration:none">取消</a>
<button type="button" class="ac-next" style="flex:1;padding:13px 0;background:#E8363D;border:0;border-radius:10px;color:#fff;font-size:18px;font-weight:600;font-family:inherit;cursor:pointer">下一步</button>
</div>'''
consent_inner = f'''<div style="width:820px;min-height:1180px;box-sizing:border-box;background:#fff;position:relative;padding:0 20px 60px">
{consent_body}
</div>'''
(P/'Consent.dc.html').write_text(page_raw('同意書', AC_CSS, consent_inner), encoding='utf-8')
# --- 同意書檢視 ---
def cv_rec(status, color, has_qr=True, voided=False):
    pill = f'<span style="display:flex;align-items:center;gap:5px;font-size:15px;color:{color}"><span style="width:8px;height:8px;border-radius:50%;background:{color}"></span>{status}</span>'
    qr = '<a href="ConsentQR.dc.html" style="flex:1;text-align:center;padding:9px 0;background:#E8363D;border-radius:8px;color:#fff;font-size:16px;font-weight:600;text-decoration:none">開啟QR-CODE</a>' if has_qr else ''
    void = '<span style="display:flex;align-items:center;gap:4px;color:#E8363D;font-size:15px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#E8363D" stroke-width="2"><path d="M4 7h16M9 7V5h6v2M7 7l1 13h8l1-13"/></svg>作廢</span>' if voided else ''
    btns = (f'<div style="display:flex;gap:12px;margin-top:12px"><a href="ConsentForm.dc.html" style="flex:1;text-align:center;padding:9px 0;border:1px solid #E8363D;border-radius:8px;color:#E8363D;font-size:16px;text-decoration:none">預覽</a>{qr}</div>') if not voided else ''
    void_row = f'<div style="display:flex;justify-content:flex-end;margin-top:8px">{void}</div>' if voided else ''
    return (f'<div style="background:#fff;border-left:4px solid #E8363D;border-radius:10px;box-shadow:0 2px 8px rgba(0,0,0,.08);padding:16px">'
            f'<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-size:18px;font-weight:700;color:#222">行程變更同意書</span>{pill}</div>'
            f'<div style="color:#555;font-size:15px;line-height:1.9;margin-top:8px">訂單編號 2026-111072<br>旅客姓名 李小明<br>設定日期 2025/08/10　簽署日期 2025/08/10</div>'
            f'{btns}{void_row}</div>')
cv_recs = (cv_rec('已簽署', '#1aa260')
  + cv_rec('未簽署', '#E8363D', has_qr=True, voided=True)
  + cv_rec('已作廢', '#999', has_qr=False)
  + cv_rec('已簽署', '#1aa260')
  + cv_rec('已簽署', '#1aa260'))
view_body = f'''{ac_head('view')}
<div style="display:flex;align-items:center;gap:10px;margin:12px 20px 0;background:#fff;border:1px solid #e3e3e3;border-radius:22px;height:44px;padding:0 16px">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#999" stroke-width="2"><circle cx="11" cy="11" r="6"/><path d="M16 16l4 4"/></svg>
<span style="color:#999;font-size:16px">選擇同意書類型、狀態或條件查找</span></div>
<div style="display:flex;flex-direction:column;gap:14px;margin:16px 20px 0">
{cv_recs}
<div style="text-align:center;color:#bbb;font-size:16px;padding:14px 0 4px">已經到底了！</div>
</div>'''
view_inner = f'''<div style="width:820px;min-height:1180px;box-sizing:border-box;background:#F5F5F5;position:relative;padding-bottom:60px">
{view_body}
</div>'''
(P/'ConsentView.dc.html').write_text(page_raw('同意書', TABCSS, view_inner), encoding='utf-8')
# --- 行程變更同意書 表單 ---
def cf_info():
    rows = ('<div style="display:grid;grid-template-columns:52px 1fr 1.5fr;background:#efefef;border-radius:6px;padding:8px 10px;font-size:14px;color:#666;margin-top:10px"><span>序號</span><span>訂單編號</span><span>旅客名單</span></div>'
      '<div style="display:grid;grid-template-columns:52px 1fr 1.5fr;padding:9px 10px;font-size:15px;color:#333"><span>1</span><span>2026-111072</span><span>李小明、李小明</span></div>'
      '<div style="display:grid;grid-template-columns:52px 1fr 1.5fr;padding:9px 10px;font-size:15px;color:#333"><span>2</span><span>2026-111072</span><span>李小明、李小明、李小明</span></div>')
    return (f'<div style="background:#fafafa;border:1px solid #eee;border-radius:10px;padding:14px 16px;margin-top:12px">'
      f'<div style="display:flex;gap:46px;font-size:16px;margin-bottom:10px"><span style="color:#888">版型</span><span>Logo版</span></div>'
      f'<div style="display:flex;gap:46px;font-size:16px"><span style="color:#888">同意書</span><span>行程變更同意書</span></div>{rows}</div>')
def cf_price(dirword):
    return (f'<div style="border:1px solid #F3B5BA;border-radius:10px;padding:14px 16px;margin-top:12px">'
      f'<div style="font-size:15px;line-height:1.7;color:#333">變更後之旅遊行程<span style="color:#E8363D">較原定旅遊行程價格{dirword}</span>，旅客同意補付價差予當團領隊／導遊 每人價差<span style="color:#E8363D">＊</span></div>'
      f'<div style="margin-top:12px;color:#888;font-size:14px">幣別</div><div style="border:1px solid #ddd;border-radius:8px;padding:11px 14px;display:flex;justify-content:space-between;font-size:16px;margin-top:4px">NTD 新台幣<span style="color:#999">⌄</span></div>'
      f'<div style="border:1px solid #ddd;border-radius:8px;padding:11px 14px;display:flex;justify-content:space-between;font-size:16px;margin-top:10px;color:#999">請輸入<span>元</span></div></div>')
form_body = f'''<header style="height:72px;display:flex;align-items:center;justify-content:space-between;padding:0 20px;position:relative">
<a href="#back" aria-label="返回" style="width:40px;height:40px;border-radius:20px;background:#3b3b3b;display:flex;align-items:center;justify-content:center"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4"><path d="M15 5l-7 7 7 7"/></svg></a>
<h1 style="position:absolute;left:0;right:0;text-align:center;margin:0;font-size:21px;font-weight:700;color:#222;pointer-events:none">同意書</h1>
<div style="display:flex;gap:10px">{BELL}{BCAST}</div></header>
<div style="color:#555;font-size:15px;line-height:1.9;margin:8px 20px 0">團號公司　15J0714BR<br>標準團名　放天下經典SL尼泊爾9日<br>訂單狀況　2024/11/05~2024/11/10</div>
<div style="margin:0 20px">
{ac_step('基本資訊')}
{cf_info()}
{ac_step('行程變更同意書')}
<div style="border:1.5px solid #E8363D;color:#E8363D;font-weight:600;border-radius:10px;padding:13px 16px;font-size:17px;margin-top:12px">無價差</div>
{cf_price('高')}
{cf_price('低')}
<div style="display:flex;gap:14px;margin:26px 0 0">
<a href="ConsentView.dc.html" style="flex:1;text-align:center;padding:13px 0;border:1px solid #E8363D;border-radius:10px;color:#E8363D;font-size:18px;text-decoration:none">取消</a>
<a href="ConsentView.dc.html" style="flex:1;text-align:center;padding:13px 0;background:#E8363D;border-radius:10px;color:#fff;font-size:18px;font-weight:600;text-decoration:none">完成</a>
</div></div>'''
form_inner = f'''<div style="width:820px;min-height:1180px;box-sizing:border-box;background:#fff;position:relative;padding-bottom:50px">
{form_body}</div>'''
(P/'ConsentForm.dc.html').write_text(page_raw('同意書', TABCSS, form_inner), encoding='utf-8')
# --- QR-CODE 光箱 ---
def qr_svg():
    import random as _r
    _r.seed(7)
    cells = ''
    for y in range(21):
        for x in range(21):
            corner = (x < 7 and y < 7) or (x > 13 and y < 7) or (x < 7 and y > 13)
            on = corner and (x in (0,6) or y in (0,6) or (2 <= x <= 4 and 2 <= y <= 4) or (x > 13 and (x in (14,20))) )
            if not corner:
                on = _r.random() > 0.5
            if (x < 7 and y < 7):
                on = (x in (0,6) or y in (0,6) or (2 <= x <= 4 and 2 <= y <= 4))
            if (x > 13 and y < 7):
                xx = x - 14
                on = (xx in (0,6) or y in (0,6) or (2 <= xx <= 4 and 2 <= y <= 4))
            if (x < 7 and y > 13):
                yy = y - 14
                on = (x in (0,6) or yy in (0,6) or (2 <= x <= 4 and 2 <= yy <= 4))
            if on:
                cells += f'<rect x="{x}" y="{y}" width="1" height="1"/>'
    return f'<svg width="190" height="190" viewBox="0 0 21 21" shape-rendering="crispEdges" fill="#111">{cells}</svg>'
qr_body = f'''<div style="position:absolute;inset:0;background:rgba(0,0,0,.5);display:flex;align-items:center;justify-content:center;padding:40px">
<div style="background:#fff;border-radius:18px;width:420px;max-width:100%;padding:26px 24px;position:relative;box-sizing:border-box">
<a href="ConsentView.dc.html" aria-label="關閉" style="position:absolute;left:16px;top:16px;width:30px;height:30px;border-radius:15px;background:#3b3b3b;display:flex;align-items:center;justify-content:center"><svg width="14" height="14" viewBox="0 0 24 24" stroke="#fff" stroke-width="2.6" fill="none"><path d="M6 6l12 12M18 6L6 18"/></svg></a>
<div style="display:flex;justify-content:center;margin-top:18px">{qr_svg()}</div>
<div style="display:flex;gap:12px;margin-top:22px">
<span style="flex:1;text-align:center;padding:11px 0;background:#E8363D;border-radius:8px;color:#fff;font-size:17px;font-weight:600">複製連結</span>
<a href="ConsentForm.dc.html" style="flex:1;text-align:center;padding:11px 0;background:#E8363D;border-radius:8px;color:#fff;font-size:17px;font-weight:600;text-decoration:none">開啟同意書</a></div>
<div style="color:#555;font-size:15px;line-height:2;margin-top:18px"><span style="display:inline-block;width:68px;color:#888">頻型</span>行程變更同意書<br><span style="display:inline-block;width:68px;color:#888">訂單編號</span>2026-111072<br><span style="display:inline-block;width:68px;color:#888;vertical-align:top">旅客名單</span><span style="display:inline-block;width:240px">李小明、李小明、李小明、李小明、李小明、李小明、李小明、李小明</span></div>
</div></div>'''
qr_inner = f'''<div style="width:820px;min-height:1180px;box-sizing:border-box;background:#F5F5F5;position:relative">
{qr_body}</div>'''
(P/'ConsentQR.dc.html').write_text(page_raw('同意書', TABCSS, qr_inner), encoding='utf-8')
# --- 其他同意書表單版型 ---
def cf_bar():
    return (f'<header style="height:72px;display:flex;align-items:center;justify-content:space-between;padding:0 20px;position:relative">'
      f'<a href="#back" aria-label="返回" style="width:40px;height:40px;border-radius:20px;background:#3b3b3b;display:flex;align-items:center;justify-content:center"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4"><path d="M15 5l-7 7 7 7"/></svg></a>'
      f'<h1 style="position:absolute;left:0;right:0;text-align:center;margin:0;font-size:21px;font-weight:700;color:#222;pointer-events:none">同意書</h1>'
      f'<div style="display:flex;gap:10px">{BELL}{BCAST}</div></header>')
def cf_info_g(title):
    rows = ('<div style="display:grid;grid-template-columns:52px 1fr 1.5fr;background:#efefef;border-radius:6px;padding:8px 10px;font-size:14px;color:#666;margin-top:10px"><span>序號</span><span>訂單編號</span><span>旅客名單</span></div>'
      '<div style="display:grid;grid-template-columns:52px 1fr 1.5fr;padding:9px 10px;font-size:15px;color:#333"><span>1</span><span>2026-111072</span><span>李小明、李小明</span></div>'
      '<div style="display:grid;grid-template-columns:52px 1fr 1.5fr;padding:9px 10px;font-size:15px;color:#333"><span>2</span><span>2026-111072</span><span>李小明、李小明、李小明</span></div>')
    return (f'<div style="background:#fafafa;border:1px solid #eee;border-radius:10px;padding:14px 16px;margin-top:12px">'
      f'<div style="display:flex;gap:46px;font-size:16px;margin-bottom:10px"><span style="color:#888">版型</span><span>Logo版</span></div>'
      f'<div style="display:flex;gap:46px;font-size:16px"><span style="color:#888">同意書</span><span>{title}</span></div>{rows}</div>')
def flab(t, req=True):
    r = '<span style="color:#E8363D">＊</span>' if req else ''
    return f'<div style="color:#444;font-size:15px;margin-top:16px">{t}{r}</div>'
def finput(ph='請輸入'):
    return f'<input placeholder="{ph}" style="width:100%;box-sizing:border-box;border:1px solid #ddd;border-radius:8px;padding:12px 14px;font-size:16px;margin-top:6px;font-family:inherit">'
def ftext(ph='請輸入'):
    return f'<textarea placeholder="{ph}" style="width:100%;box-sizing:border-box;border:1px solid #ddd;border-radius:8px;padding:12px 14px;font-size:16px;margin-top:6px;min-height:92px;font-family:inherit;resize:none"></textarea>'
def fdate():
    return '<div style="border:1px solid #ddd;border-radius:8px;padding:12px 14px;display:flex;justify-content:space-between;color:#999;font-size:16px;margin-top:6px">YYYY/MM/DD<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#888" stroke-width="1.8"><rect x="4" y="5" width="16" height="16" rx="2"/><path d="M4 10h16M8 3v4M16 3v4"/></svg></div>'
def fsel(v):
    return f'<div style="border:1px solid #ddd;border-radius:8px;padding:12px 14px;display:flex;justify-content:space-between;font-size:16px;margin-top:6px">{v}<span style="color:#999">⌄</span></div>'
def fbox(ph):
    return f'<div style="flex:1;border:1px solid #ddd;border-radius:8px;padding:12px 14px;color:#999;font-size:16px">{ph}</div>'
def frow2(a, b):
    return f'<div style="display:flex;gap:10px;margin-top:6px">{a}{b}</div>'
def cf_bottom():
    return ('<div style="display:flex;gap:14px;margin:26px 0 0">'
      '<a href="ConsentView.dc.html" style="flex:1;text-align:center;padding:13px 0;border:1px solid #E8363D;border-radius:10px;color:#E8363D;font-size:18px;text-decoration:none">取消</a>'
      '<a href="ConsentView.dc.html" style="flex:1;text-align:center;padding:13px 0;background:#E8363D;border-radius:10px;color:#fff;font-size:18px;font-weight:600;text-decoration:none">完成</a></div>')
def consent_form(slug, title, section):
    body = (f'{cf_bar()}'
      f'<div style="color:#555;font-size:15px;line-height:1.9;margin:8px 20px 0">團號公司　15J0714BR<br>標準團名　放天下經典SL尼泊爾9日<br>訂單狀況　2024/11/05~2024/11/10</div>'
      f'<div style="margin:0 20px">{ac_step("基本資訊")}{cf_info_g(title)}{ac_step(title)}{section}{cf_bottom()}</div>')
    inner = f'<div style="width:820px;min-height:1180px;box-sizing:border-box;background:#fff;position:relative;padding-bottom:50px">{body}</div>'
    (P/(slug+'.dc.html')).write_text(page_raw('同意書', TABCSS, inner), encoding='utf-8')
consent_form('ConsentNoMed', '不就醫同意書', flab('原因')+ftext()+flab('不就醫同意日期')+fdate())
consent_form('ConsentNoRep', '不報案同意書', flab('原因')+ftext()+flab('不報案同意日期')+fdate())
consent_form('ConsentCash', '代金領取同意書', flab('原因')+ftext()+flab('幣別')+fsel('NTD 新台幣')+flab('金額')+finput()+flab('領取日期')+fdate())
drop_section = ('<div style="font-size:16px;font-weight:700;color:#222;margin-top:14px">1.脫隊確認書</div>'
  + flab('脫隊日期（起）') + frow2(fbox('年/月/日'), fbox('hh:mm'))
  + flab('脫隊地點') + finput()
  + flab('歸隊日期（迄）') + frow2(fbox('年/月/日'), fbox('hh:mm'))
  + flab('歸隊地點') + finput()
  + '<div style="font-size:16px;font-weight:700;color:#222;margin-top:22px">2.脫隊期間旅客之聯絡方式</div>'
  + flab('聯絡方式') + finput()
  + '<div style="font-size:16px;font-weight:700;color:#222;margin-top:22px">3.領隊交辦事項</div>'
  + flab('航班資訊', False) + fsel('桃園機場(TPE) &gt; 成田機場(NRT)')
  + flab('其他注意事項', False) + finput())
consent_form('ConsentDrop', '脫隊確認書', drop_section)
# --- 離線不支援 ---
off_body = f'''{ac_head('set')}
<div style="position:absolute;left:0;right:0;top:420px;display:flex;flex-direction:column;align-items:center;gap:22px">
<svg width="70" height="70" viewBox="0 0 24 24" fill="none" stroke="#D5D5D5" stroke-width="1.5"><path d="M12 3l9 16H3z"/><path d="M12 9v5M12 16.5v.5"/></svg>
<div style="color:#C4C4C4;font-size:19px">離線模式不支援此功能</div></div>
<div style="position:absolute;left:20px;right:20px;bottom:24px;display:flex;gap:14px">
<span style="flex:1;text-align:center;padding:13px 0;border:1px solid #ddd;border-radius:10px;color:#bbb;font-size:18px">取消</span>
<span style="flex:1;text-align:center;padding:13px 0;background:#E0E0E0;border-radius:10px;color:#fff;font-size:18px">下一步</span></div>'''
off_inner = f'''<div style="width:820px;height:1180px;box-sizing:border-box;background:#fff;position:relative;overflow:hidden;padding:0 20px">
{off_body}</div>'''
(P/'ConsentOffline.dc.html').write_text(page_raw('同意書', AC_CSS, off_inner), encoding='utf-8')

# ---------- 交班文件 三種狀態 ----------
ITEMS = ['交班總覽','收件一覽表','開票名單','PNR','保單','合約書／手配書','說明會資料','Q 信箱','分房表','其他交班文件']
LINKS = {'交班總覽':'HandoverOverview','收件一覽表':'HdRecv','開票名單':'HdTicket','PNR':'HdPnr','保單':'HdIns','合約書／手配書':'HdAgr','說明會資料':'HdBrief','Q 信箱':'HdQ','分房表':'HdRoom','團體名單':'HdList','旅客及同行聯絡資料表':'HdContact','其他交班文件':'HdOther'}
ho_css = '''.it{display:flex;align-items:center;justify-content:space-between;height:48px;padding:0 16px;border-radius:10px;font-size:18px}
.it.on{background:#fff;color:#222;box-shadow:0 1px 3px rgba(0,0,0,.06)}
.it.off{background:#E5E5E5;color:#777}
.it svg{width:16px;height:16px;stroke:#666;fill:none;stroke-width:2}
.chk{width:18px;height:18px;border-radius:9px;background:#E8363D;display:inline-flex;align-items:center;justify-content:center;margin-left:8px;vertical-align:middle}
.chk svg{width:11px;height:11px;stroke:#fff;fill:none;stroke-width:3}'''
def handover(fname, title, active_count, checked):
    rows = ''
    for i, name in enumerate(ITEMS):
        on = i < active_count
        href = (LINKS[name] + '.dc.html') if (on and name in LINKS) else '#top'
        mark = '<span class="chk"><svg viewBox="0 0 24 24"><path d="M5 12l5 5 9-9"/></svg></span>' if (on and i in checked) else ''
        if on:
            rows += f'<a class="it on" href="{href}"><span>{name}{mark}</span><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg></a>\n'
        else:
            rows += f'<span class="it off">{name}</span>\n'
    body = header_center('交班文件', 'PreTour.dc.html') + f'''
<div style="margin:0 20px;display:flex;flex-direction:column;gap:8px">{rows}</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:150px;display:flex;flex-direction:column;align-items:center;gap:12px;padding-top:8px">
<span style="background:#333;color:#fff;font-size:15px;padding:8px 18px;border-radius:20px">交班狀態，只支援連線操作</span>
<span style="color:#E8363D;font-size:15px">ⓘ 請務必仔細閱讀交班文件，完成交班作業！</span>
<span style="width:780px;height:44px;border-radius:8px;background:#E5E5E5;color:#aaa;font-size:19px;font-weight:700;display:flex;align-items:center;justify-content:center">交班文件無誤</span>
</div>'''
    (P/fname).write_text(page(title, ho_css, body), encoding='utf-8')

handover('HandoverLocked.dc.html', '交班文件 產品準備中', 0, set())
handover('HandoverPartial.dc.html', '交班文件 產品簽核完成', 4, set())
handover('HandoverDone.dc.html', '交班文件 TL交班完成', 12, set())

# ---------- 交班總覽 ----------
ov_css = '''.sec{position:relative;background:#fff;border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}
.sec::before{content:"";position:absolute;left:0;top:18px;width:4px;height:24px;background:#E8363D;border-radius:0 2px 2px 0}
.sec h2{margin:0 0 4px;font-size:20px;font-weight:700}
.r{display:flex;font-size:17px;line-height:1.6}.r .k{width:90px;flex:none;color:#333}
.li{font-size:17px;line-height:1.7}
.cb{display:flex;align-items:flex-start;gap:10px;font-size:16px;color:#999;line-height:1.5}
.cb input{width:18px;height:18px;margin:3px 0 0;flex:none;accent-color:#E8363D}
.ovbtn{flex:1;height:44px;border-radius:8px;font-size:19px;font-weight:700;display:flex;align-items:center;justify-content:center;font-family:inherit;border:0}
.ovbtn.rep{background:#fff;border:1px solid #ccc;color:#888}
.ovok{background:#E5E5E5;color:#aaa}
.ovok.en{background:#E8363D;color:#fff;cursor:pointer}'''
ov_body = header_center('交班總覽', 'HandoverDone.dc.html') + '''
<div style="margin:0 20px;display:flex;flex-direction:column;gap:12px">
<section class="sec"><h2>基本資料</h2>
<div class="r"><span class="k">團號</span><span>24XI929SL</span></div>
<div class="r"><span class="k">領隊</span><span>林○○</span></div>
<div class="r"><span class="k">總人數</span><span>15+1大、1嬰、1小</span></div>
<div class="r"><span class="k">出發地與人數</span><span>台北出發 16人</span></div></section>
<section class="sec"><h2>餐食特別需求</h2><div class="li">1.蛋奶素</div><div class="li">2.忌牛</div></section>
<section class="sec"><h2>特別回程 / 特殊安排</h2><div class="li">1.全團台北來回</div><div class="li" style="color:#E8363D">2.電扶梯問卷：12人 陪同坐 8位/長者樓 4位</div><div class="li">3.艦票自帶(含領隊)：19人</div></section>
<section class="sec"><h2>領隊注意事項</h2><div class="li">1.提醒帶回ED卡</div><div class="li">2.核對護照證件</div><div class="li">3.嚴禁託帶菸酒等規定</div></section>
<section class="sec"><h2>緊急聯絡電話</h2>
<div class="r"><span class="k">團控</span><span>林秀輪 0987-675-836</span></div>
<div class="r"><span class="k">線控</span><span>高文娟 0929-991-030</span></div>
<div class="r"><span class="k">主管</span><span>施俊佑 0955-183-158</span></div></section>
<section style="background:#F2F2F2;border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;gap:10px"><h2 style="margin:0;font-size:18px;color:#E8363D">請確認交班文件</h2>
<label class="cb" style="color:#222"><input type="checkbox" class="confchk">已核對護照、簽證之旅客英文姓名須相符</label>
<label class="cb" style="color:#222"><input type="checkbox" class="confchk">已確認護照、簽證之效期足夠</label></section>
</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:110px;background:#fff;border-top:1px solid #eee;display:flex;flex-direction:column;align-items:center;gap:10px;padding-top:8px">
<span style="color:#E8363D;font-size:15px">ⓘ 請務必仔細閱讀交班文件，完成交班作業！</span>
<div style="display:flex;gap:14px;width:780px"><button type="button" class="ovbtn rep" data-act="hdReport">問題回報</button><button type="button" class="ovbtn ovok" data-act="docOk">資料無誤</button></div>
</div>'''
(P/'HandoverOverview.dc.html').write_text(page('交班總覽', ov_css, ov_body, h=1400), encoding='utf-8')

# ---------- 交班文件 各項內容頁 ----------
hd_css = '''.hsec{position:relative;margin:0 20px;display:flex;flex-direction:column;gap:12px}
.hsec h2{margin:0;font-size:19px;font-weight:700;padding-left:12px;position:relative}
.hsec h2::before{content:"";position:absolute;left:0;top:1px;width:4px;height:20px;background:#E8363D;border-radius:0 2px 2px 0}
.hcard{background:#fff;border:1px solid #e8e8e8;border-radius:10px;padding:14px 16px;display:flex;flex-direction:column;gap:7px;font-size:16px;line-height:1.5}
.hr{display:flex}.hr .k{width:92px;flex:none;color:#333}.hr .v{color:#222}
.hview{display:flex;justify-content:space-between;align-items:center;background:#fff;border:1px solid #e8e8e8;border-radius:10px;padding:14px 16px;font-size:18px;font-weight:700;position:relative}
.hview.bar{padding-left:20px}.hview.bar::before{content:"";position:absolute;left:0;top:14px;bottom:14px;width:4px;background:#E8363D;border-radius:0 2px 2px 0}
.vbtn{border:1px solid #d6d6d6;color:#888;border-radius:8px;padding:6px 18px;font-size:16px;font-weight:700;background:#F0F0F0;font-family:inherit}
.hconfirm{background:#F2F2F2;border-radius:10px;padding:14px 16px;display:flex;flex-direction:column;gap:10px}
.hconfirm h3{margin:0 0 2px;font-size:17px;color:#E8363D;font-weight:700}
.hcb{display:flex;align-items:flex-start;gap:10px;font-size:16px;line-height:1.5}
.hcb input{width:20px;height:20px;margin-top:1px;flex:none;accent-color:#E8363D}
.hbarf{background:#fff;border-top:1px solid #eee;display:flex;flex-direction:column;gap:8px;align-items:center;padding:10px 0 14px}
.hbarf .warn{color:#E8363D;font-size:14px}
.hbarf .btns{display:flex;gap:14px;width:780px}
.hbarf .btns button{flex:1;height:46px;border-radius:8px;font-size:19px;font-weight:700;display:flex;align-items:center;justify-content:center;font-family:inherit;border:0}
.hbarf .rep{background:#fff;border:1px solid #ccc;color:#888}
.hbarf .ovok{background:#E5E5E5;color:#aaa}
.hbarf .ovok.en{background:#E8363D;color:#fff;cursor:pointer}'''

def row(k, v):
    return f'<div class="hr"><span class="k">{k}</span><span class="v">{v}</span></div>'
def confirm(items):
    rows = ''.join(f'<label class="hcb"><input type="checkbox" class="confchk"><span>{t}</span></label>' for t in items)
    return f'<div class="hsec"><div class="hconfirm"><h3>請確認交班文件</h3>{rows}</div></div>'
def hd(fname, title, item, inner):
    inner_html = f'''<div style="width:820px;min-height:1180px;box-sizing:border-box;background:#F5F5F5;display:flex;flex-direction:column;position:relative">
{header_center(title, 'HandoverDone.dc.html')}
<div style="flex:1;display:flex;flex-direction:column;gap:14px;padding:4px 0 12px">
{inner}
</div>
<div class="hbarf"><span class="warn">ⓘ 請務必仔細閱讀交班文件，完成交班作業！</span><div class="btns"><button type="button" class="rep" data-act="hdReport">問題回報</button><button type="button" class="ovok" data-act="hdOk" data-item="{item}">資料無誤</button></div></div>
</div>'''
    (P/fname).write_text(page_raw(title, hd_css, inner_html), encoding='utf-8')

pax_recv = ''.join(f'<div class="hcard">{row("序號",n)}{row("中文姓名","陳○○")}{row("英文姓名","chan/zero zero")}{row("收件","V")}{row("訂單編號","5-123454")}{row("業務","直售 王○○")}{row("同行公司","台北-內湖")}{row("備註","")}</div>' for n in (1,2,3))
hd('HdRecv.dc.html','收件一覽表','收件一覽表',
   f'<div class="hsec"><h2>旅客資料</h2><div style="font-size:15px;color:#333">自帶護照：20人　　收件護照：3人</div>{pax_recv}</div>' + confirm(['已確認護照與簽證資訊相符且效期足夠']))

flt = ''.join(f'<div class="hcard">{row("班機","BX794")}{row("出發日期","2025/09/27 13:25")}{row("行程","TPE/PUS")}</div>' for _ in range(2))
pax_tk = ''.join(f'<div class="hcard">{row("序號",n)}{row("性別","MR")}{row("英文姓名","chan/zero zero")}{row("票號","1")}{row("中文姓名","陳○○")}{row("備註","忌牛")}</div>' for n in (1,2,3))
hd('HdTicket.dc.html','開票名單','開票名單',
   f'<div class="hsec"><h2>航班資料</h2>{flt}</div><div class="hsec"><h2>旅客資料</h2>{pax_tk}</div>')

pnr_block = f'<div class="hsec"><div class="hview bar">PNR<button class="vbtn">查看</button></div>' + ''.join(f'<div class="hcard">{row("班機","BX794")}{row("出發日期","2025/09/27 13:25")}{row("行程","TPE/PUS")}</div>' for _ in range(2)) + '</div>'
hd('HdPnr.dc.html','PNR','PNR', pnr_block + pnr_block + confirm(['已確認機票名單正確無誤','已確認航段、日期無誤']))

hd('HdIns.dc.html','保單','保單',
   '<div class="hsec"><div class="hview bar">中文保單<button class="vbtn">查看</button></div></div><div class="hsec"><div class="hview bar">英文保單<button class="vbtn">查看</button></div></div>' + confirm(['已核對保單日期、人數相符']))

hd('HdBrief.dc.html','說明會資料','說明會資料',
   '<div class="hsec"><div class="hview bar">說明會資料<button class="vbtn">查看</button></div></div>' + confirm(['已核對說資行程表與供應商、Local合約書(ITN)','已核對票卷日期時間、數量相符']))

qmsg = '這團客人比較重細節，再麻煩你多費心照看。行程中有任何狀況隨時聯繫，祝帶團順利、合作愉快！'
qbox = ''.join(f'<div class="hcard">{row("訂單號碼","4-791692")}{row("時間","08/12 09：00")}{row("業務","直售 陳○○")}{row("輸入","直售 王○○")}<div class="hr"><span class="k">內容</span><span class="v" style="line-height:1.6">{qmsg}</span></div></div>' for _ in range(3))
hd('HdQ.dc.html','Q信箱','Q 信箱', f'<div class="hsec"><h2>Q信箱</h2>{qbox}</div>' + confirm(['特殊需求是否已確認或妥善安排']))

other = ''.join(f'<div class="hcard">{row("序號","1")}{row("項目","東京迪士尼門票成人票")}{row("數量","15")}' + ('<div style="display:flex;justify-content:flex-end"><button class="vbtn">查看</button></div>' if n in (1,3) else '') + '</div>' for n in (1,2,3))
hd('HdOther.dc.html','其他項目','其他交班文件', f'<div class="hsec"><h2>其他項目</h2>{other}</div>')

for fn2, title2, item2 in [('HdAgr.dc.html','合約書／手配書','合約書／手配書'),('HdList.dc.html','團體名單','團體名單'),('HdContact.dc.html','旅客及同行聯絡資料表','旅客及同行聯絡資料表')]:
    hd(fn2, title2, item2, f'<div class="hsec"><div class="hview bar">{title2}<button class="vbtn">查看</button></div></div>' + confirm([f'已確認{title2}內容無誤']))
# 分房表（名單帶入團體名單、房號順序、人數依卡牌）
PAX28 = [
 ('吳伯良','WU /PO LIANG',1978,1),('藍建豪','LAN /CHIEN HAO',1987,1),('李逸婕','LI /YI CHIEH',1981,0),
 ('劉承翰','LIU /CHENG HAN',1991,1),('李浩然','LI /HAO JAN',1996,1),('李沛芸','LI /PEI YUN',2001,0),
 ('林欣怡','LIN /HSIN YI',2001,0),('黃俊傑','HUANG /CHUN CHIEH',1979,1),('劉佩君','LIU /PEI CHUN',1992,0),
 ('蔡嘉倫','TSAI /CHIA LUN',1985,1),('楊欣穎','YANG /HSIN YING',1991,0),('許志銘','HSU /CHIH MING',1977,1),
 ('鄭郁琪','CHENG /YU CHI',1986,0),('謝宇霖','HSIEH /YU LIN',1982,1),('洪淑萍','HUNG /SHU PING',1980,0),
 ('曾家豪','TSENG /CHIA HAO',1989,1),('周欣瑜','CHOU /HSIN YU',1993,0),('徐承威','HSU /CHENG WEI',1984,1),
 ('高雅文','KAO /YA WEN',1990,0),('呂柏軒','LU /PO HSUAN',1976,1),('郭芷茹','KUO /CHIH JU',1987,0),
 ('蕭宇傑','HSIAO /YU CHIEH',1983,1),('潘欣怡','PAN /HSIN YI',1991,0),('范家宇','FAN /CHIA YU',1979,1),
 ('蘇淑玲','SU /SHU LING',1985,0),('彭志翔','PENG /CHIH HSIANG',1988,1),('葉宇庭','YEH /YU TING',1992,0),
 ('丁家恩','TING /CHIA EN',1981,1),
]
def rm_pax(p):
    cn, en, yr, g = p
    icon = '<span style="color:#2E7CF6">♂</span>' if g else '<span style="color:#E8368A">♀</span>'
    return (f'<div style="padding:10px 2px"><div style="font-size:17px;color:#222">{cn}　<span style="color:#999;font-size:15px">{2026-yr}歲</span>　{icon}</div>'
            f'<div style="font-size:14px;color:#999">{en}</div></div>')
def rm_card(idx, members, first=False):
    disp = 'block' if first else 'none'
    chev = '⌃' if first else '⌄'
    paxes = ''.join(rm_pax(p) for p in members)
    return (f'<div style="background:#fff;border-radius:12px;box-shadow:0 1px 4px rgba(0,0,0,.06);overflow:hidden">'
            f'<div class="rmhead" data-t="rm{idx}" style="display:flex;align-items:center;justify-content:space-between;padding:14px 16px;cursor:pointer">'
            f'<span style="font-size:18px;font-weight:600;color:#222">第 {idx} 間</span>'
            f'<span style="display:flex;align-items:center;gap:14px;color:#555;font-size:16px">{len(members)} 人 <span class="chev" style="color:#aaa">{chev}</span></span></div>'
            f'<div class="rmbody" id="rm{idx}" style="display:{disp};padding:0 16px 8px;border-top:1px solid #f0f0f0">{paxes}</div></div>')
# 版型1：14 間，全部兩人房
rooms_html_v1 = ''.join(rm_card(i+1, PAX28[i*2:i*2+2], first=(i == 0)) for i in range(14))
# 版型2：第 1 間改為三人房（其餘維持），末間為單人房以容納 28 位
V2 = [PAX28[0:3]] + [PAX28[i:i+2] for i in range(3, 27, 2)] + [PAX28[27:28]]
rooms_html_v2 = ''.join(rm_card(i+1, V2[i], first=(i == 0)) for i in range(len(V2)))
RAD_ON2 = '<span style="width:20px;height:20px;border:1.5px solid #E8363D;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;flex:none"><span style="width:11px;height:11px;background:#E8363D;border-radius:50%"></span></span>'
RAD_OFF2 = '<span style="width:20px;height:20px;border:1.5px solid #c4c4c4;border-radius:50%;display:inline-block;flex:none"></span>'
room_days = ''.join(
  f'<div class="rsday" data-d="{d}" data-dt="{dt}" style="display:flex;align-items:center;justify-content:space-between;padding:14px 2px;border-bottom:1px solid #f0f0f0;font-size:17px;cursor:pointer">'
  f'<span><b style="color:#E8363D">第 {d} 天</b>　|　{dt}</span><span class="rsradio">{RAD_ON2 if i==0 else RAD_OFF2}</span></div>'
  for i, (d, dt) in enumerate([(1,'12/26'),(2,'12/27'),(3,'12/28'),(4,'12/29'),(5,'12/30'),(6,'12/31'),(7,'01/01')]))
room_sheet = (f'<div class="roomsheet" style="display:none;position:absolute;inset:0;background:rgba(0,0,0,.45);z-index:50;align-items:flex-end">'
  f'<div style="background:#fff;border-radius:18px 18px 0 0;width:100%;box-sizing:border-box;padding:18px 20px 22px;max-height:80%;overflow:auto">'
  f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:6px"><button type="button" class="rsclose" style="border:0;background:none;font-size:22px;color:#333;cursor:pointer;padding:0">✕</button><span style="font-size:18px;font-weight:700">切換住宿日期</span></div>'
  f'{room_days}'
  f'<div style="display:flex;align-items:center;gap:8px;color:#E8363D;font-size:17px;padding:16px 2px"><span style="font-size:22px;line-height:1">＋</span>新增一天</div>'
  f'<button type="button" class="rsclose" style="width:100%;padding:13px 0;background:#E8363D;border:0;border-radius:10px;color:#fff;font-size:18px;font-weight:600;font-family:inherit;cursor:pointer">確認</button>'
  f'</div></div>')
_mono = 'font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;color:#222;letter-spacing:.2px'
_badge = '<span style="margin-left:8px;font-size:12px;font-weight:700;color:#E8363D;background:#FDE4E6;border-radius:6px;padding:1px 8px;vertical-align:middle">版型2</span>'
_dates = [
 ('2026/11/25','KOKO HOTEL TOMAKOMAI(DR同泊)★一泊二食','T:81-144-33-0333　F:81-48-423-5776(武蔵野経由)',''),
 ('2026/11/26','鹿之湯集團 定山溪 花紅葉','T:81-138-59-2335　F:81-138-59-3580',_badge),
 ('2026/11/27','SMILE HOTEL PREMIUM SAPPORO SUSUKINO','T:81-11-251-7055',''),
 ('2026/11/28','SMILE HOTEL PREMIUM SAPPORO SUSUKINO','T:81-11-251-7055',''),
]
_date_rows = ''.join(
  f'<div style="margin-top:8px"><div style="color:#222"><b>{d}</b>　{name}{tag}</div>'
  f'<div style="color:#999;font-size:13px">{tf}</div></div>' for d, name, tf, tag in _dates)
rsfinal_box = (
  '<div class="rsfinalbox" style="display:none;margin-top:12px;background:#fafafa;border:1px solid #eee;border-radius:10px;padding:14px 16px;font-size:14px;color:#333;line-height:1.7">'
  f'<div style="{_mono}">FINAL&nbsp;&nbsp;09 TWIN + 0 DBL + 2 TRP + 1 SGL = 12 ROOMS</div>'
  f'<div style="{_mono}">FINAL&nbsp;&nbsp;23 ADT&nbsp; + 0 CHD + 1 T/L + 1 T/G = 25 PAX</div>'
  f'<div style="margin-top:12px">{_date_rows}</div>'
  '<div style="margin-top:12px;color:#E8363D;font-size:13px;line-height:1.8">'
  '<div>※全部【禁煙ルーム】でご手配をお願い致します※</div>'
  '<div>※2歳未満のINFは食事不要です※</div>'
  '<div>※子供も大人と同食です※</div></div>'
  '</div>')
room_inner = (f'<div style="padding:4px 16px 0">'
  f'<div style="display:flex;align-items:center;justify-content:space-between">'
  f'<div class="rstrigger" style="border:1px solid #ddd;border-radius:8px;padding:9px 14px;display:flex;gap:10px;align-items:center;font-size:16px;cursor:pointer">第 1 天 | 12/26 <span style="color:#999">⌄</span></div>'
  f'<span class="rsfinal" style="color:#E8363D;font-size:16px;cursor:pointer">ⓘ 分房Final <span class="rsfchev" style="font-size:13px">⌄</span></span></div>'
  f'{rsfinal_box}'
  # 飯店／地址區塊：版型與飯店依所選天數自動帶入（第2天＝版型2＋湯之川溫泉，其餘固定）
  f'<div class="rmhotel" style="margin-top:14px;border:1px solid #f0e0e0;border-radius:10px;padding:12px 14px;background:#fff">'
  f'<div style="display:flex;align-items:center;justify-content:space-between">'
  f'<span class="rm-vlabel" style="font-size:13px;font-weight:700;color:#E8363D;background:#FDE4E6;border-radius:6px;padding:2px 9px">版型1</span></div>'
  f'<div style="font-size:14px;color:#888;margin-top:10px">地址</div>'
  f'<div class="rm-hotel-name" style="font-size:16px;color:#222;margin-top:2px;line-height:1.5">HF 伊帕內瑪花園飯店 HF IPANEMA PARK</div></div>'
  f'<div class="rm-rooms rm-v1" style="display:flex;flex-direction:column;gap:12px;margin-top:14px">{rooms_html_v1}</div>'
  f'<div class="rm-rooms rm-v2" style="display:none;flex-direction:column;gap:12px;margin-top:14px">{rooms_html_v2}</div>'
  f'</div>{room_sheet}')
hd('HdRoom.dc.html', '分房表', '分房表', room_inner)

# ========== 行中·分房表（帶團中功能按鈕進入，獨立於 交班文件>分房表 HdRoom）==========
RX_CSS = '''
.rx-wrap{padding:6px 18px 40px}
.rx-top{display:flex;align-items:center;justify-content:space-between}
.rx-day{border:1px solid #ddd;border-radius:8px;padding:9px 14px;display:flex;gap:10px;align-items:center;font-size:17px;color:#222}
.rx-final{color:#E8363D;font-size:17px}
.rx-hotel{margin-top:14px;border:1px solid #f0e0e0;border-radius:10px;padding:13px 15px;background:#fff}
.rx-vlabel{font-size:14px;font-weight:700;color:#E8363D;background:#FDE4E6;border-radius:6px;padding:3px 10px}
.rx-carry{margin-top:14px;background:#FFF4E5;border:1px solid #F3D9A6;border-radius:10px;padding:13px 15px;display:flex;align-items:center;justify-content:space-between;gap:10px}
.rx-carry span.q{color:#8a6d3b;font-size:17px}
.rx-apply{background:#E8363D;color:#fff;border:0;border-radius:8px;padding:8px 18px;font-size:16px;font-weight:700;font-family:inherit;cursor:pointer}
.rx-carry-x{border:0;background:none;font-size:22px;color:#c08a3b;cursor:pointer;line-height:1;padding:0 2px}
.rx-rooms{display:flex;flex-direction:column;gap:12px;margin-top:16px}
.rx-card{background:#fff;border-radius:12px;box-shadow:0 1px 4px rgba(0,0,0,.07);overflow:hidden}
.rx-head{display:flex;align-items:center;gap:12px;padding:14px 16px;cursor:pointer}
.rx-no{width:120px;border:1px solid #d7d7d7;border-radius:8px;padding:10px 12px;font-size:18px;font-family:inherit;color:#222}
.rx-no.err{border-color:#E8363D;background:#FDECEC}
.rx-head .fang{font-size:18px;color:#222;font-weight:600}
.rx-head .cnt{margin-left:auto;color:#555;font-size:17px}
.rx-head .rxchev{color:#aaa;font-size:16px}
.rx-body{padding:4px 16px 12px;border-top:1px solid #f0f0f0}
.rx-pax{padding:10px 2px}
.rx-note{width:100%;box-sizing:border-box;border:1px solid #e3e3e3;border-radius:8px;padding:11px 12px;font-size:16px;font-family:inherit;margin-top:8px;resize:none}
.rx-export{display:block;width:100%;margin:22px auto 0;padding:15px 0;background:#fff;border:1.5px solid #E8363D;border-radius:10px;color:#E8363D;font-size:20px;font-weight:700;font-family:inherit;cursor:pointer}
.rxtoast{position:absolute;left:50%;bottom:150px;transform:translateX(-50%);background:#333;color:#fff;padding:12px 22px;border-radius:24px;font-size:16px;display:none;z-index:70;white-space:nowrap;box-shadow:0 6px 20px rgba(0,0,0,.3)}
/* 輸出預覽（分房表 RoomList 寬版） */
.rp-wrap{padding:16px 22px 30px}
.rp-top{display:flex;align-items:center;gap:16px;margin-bottom:14px}
.rp-logo{display:flex;flex-direction:column;line-height:1.05}
.rp-lion{color:#E8363D;font-weight:800;font-size:16px;letter-spacing:.5px}
.rp-lion2{color:#E8363D;font-size:12px}
.rp-tour{color:#333;font-size:14px}
.rp-htitle{flex:1;text-align:center;font-size:20px;font-weight:800;color:#222}
.rp-tl,.rp-op{color:#333;font-size:14px}
.rp-table{width:100%;border-collapse:collapse;font-size:12.5px;background:#fff}
.rp-table th,.rp-table td{padding:6px 8px;text-align:left;vertical-align:top;border:0}
.rp-table th{color:#444;font-weight:700;border-bottom:2px solid #333;white-space:nowrap}
.rp-table td.c{text-align:left}
.rp-table td:first-child,.rp-table th:first-child{text-align:center;width:34px}
.rp-table .rtop td{border-top:1.5px solid #333}
.rp-table tbody tr td{border-bottom:1px solid #f0f0f0}
.rp-table .rp-no{color:#E8363D;font-weight:700}
.rp-table td:nth-child(3),.rp-table td:nth-child(4){color:#1a56c4}
.rp-finalbox{margin-top:18px;border:2px solid #E8363D;border-radius:8px;padding:12px 16px;display:inline-block;min-width:360px}
.rp-finalttl{color:#E8363D;font-weight:800;font-size:15px;letter-spacing:1px;margin-bottom:8px}
.rp-finline{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;color:#222;line-height:1.7}
.rp-finnote{font-size:12px;color:#E8363D;margin-top:8px;line-height:1.7}
.rp-bar{display:flex;align-items:center;justify-content:center;gap:14px;background:#fff;border-top:1px solid #eee;padding:20px}
.rp-bar button{flex:1;max-width:330px;padding:15px 0;border-radius:10px;font-size:19px;font-weight:700;font-family:inherit;cursor:pointer}
.rp-back{background:#fff;border:1.5px solid #E8363D;color:#E8363D}
.rp-out{background:#E8363D;border:0;color:#fff}
'''
def rx_pax(p, notes):
    cn, en, yr, g = p
    icon = '<span style="color:#2E7CF6">♂</span>' if g else '<span style="color:#E8368A">♀</span>'
    return (f'<div class="rx-pax"><div style="font-size:18px;color:#222">{cn}　<span style="color:#999;font-size:15px">{2026-yr}歲</span>　{icon}</div>'
            f'<div style="font-size:14px;color:#999">{en}</div>'
            f'<div style="font-size:13px;color:#bbb;margin-top:2px">備註　{notes.get(p, "—")}</div></div>')
def rx_card(idx, members, notes, first=False):
    disp = 'block' if first else 'none'
    chev = '⌃' if first else '⌄'
    paxes = ''.join(rx_pax(p, notes) for p in members)
    return (f'<div class="rx-card">'
            f'<div class="rx-head"><input class="rx-no" inputmode="numeric" placeholder="999" aria-label="房號">'
            f'<span class="fang">房</span><span class="cnt">{len(members)} 人</span>'
            f'<span class="rxchev">{chev}</span></div>'
            f'<div class="rx-body" id="rx{idx}" style="display:{disp}">{paxes}'
            f'<textarea class="rx-note" rows="2" placeholder="輸入房間備註"></textarea></div></div>')
# 分房分組（共 6 間）：僅第 2 天第 1 間為三人房（多出李浩然），其餘天第 1 間為雙人房
_A, _B = PAX28[0], PAX28[1]                             # 吳伯良, 藍建豪
_LCH = PAX28[3]                                         # 劉承翰 35
_LHJ = PAX28[4]                                         # 李浩然 30
_rest2 = PAX28[5:13]                                    # 其餘 8 位 → 4 間雙人
_pairs2 = [_rest2[i:i+2] for i in range(0, 8, 2)]
V1_GROUPS = [[_A, _B], [_LCH, _LHJ]] + _pairs2         # 第1天：第2間 劉承翰+李浩然（DBL）
V2_GROUPS = [[_A, _B, _LHJ], [_LCH]] + _pairs2         # 第2天：第1間三人（含李浩然）、第2間 劉承翰 單人（SGL）
RX_NOTES_V1 = {_LCH: 'DBL'}                             # 第 1 天（版型1）備註
RX_NOTES_V2 = {_LCH: 'SGL'}                             # 第 2 天（版型2）備註
RX_ROOMS_V1 = ''.join(rx_card(i+1, g, RX_NOTES_V1, first=True) for i, g in enumerate(V1_GROUPS))
RX_ROOMS_V2 = ''.join(rx_card(i+1, g, RX_NOTES_V2, first=True) for i, g in enumerate(V2_GROUPS))
rx_inner = (header_center('分房表', 'Tour.dc.html') + f'''
<div class="rx-wrap">
  <div class="rx-top">
    <div class="rx-day rx-daytrig" style="cursor:pointer">第 1 天 | 12/26 <span style="color:#999">⌄</span></div>
    <span class="rx-final rsfinal" style="cursor:pointer">ⓘ 分房Final <span class="rsfchev" style="font-size:13px">⌄</span></span>
  </div>
  {rsfinal_box}
  <div class="rx-hotel">
    <div style="display:flex;justify-content:space-between;align-items:center"><span class="rx-vlabel">版型1</span></div>
    <div style="font-size:14px;color:#888;margin-top:10px">地址</div>
    <div class="rx-hotel-name" style="font-size:17px;color:#222;margin-top:2px;line-height:1.5">HF 伊帕內瑪花園飯店 HF IPANEMA PARK</div>
  </div>
  <div class="rx-rooms rx-rooms-v1">{RX_ROOMS_V1}</div>
  <div class="rx-rooms rx-rooms-v2" style="display:none">{RX_ROOMS_V2}</div>
  <button type="button" class="rx-export">輸出分房表</button>
</div>''')
(P/'RoomExt.dc.html').write_text(page_raw('分房表 行中', RX_CSS, rx_inner), encoding='utf-8')

# 輸出預覽（參照實際分房表 RoomList 版型）
_rtymap = {3:'TRP', 2:'TWN', 1:'SGL'}
_orders = ['6-11250111','6-11250113','6-11250116','6-11250123','6-11250125','6-11250128']
_diet = ['', '忌牛 No Beef', '忌羊 No Lamb', '忌牛 No Beef 忌羊', '忌羊 No Lamb 忌魚', '']
_stat = ['已付小費', '已選位', '已選位/已付小費', '已付小費', '忌生食/已付小費', '已付小費']
def _pax_detail(i, yr, g):
    bm = (i*7) % 12 + 1; bd = (i*13) % 28 + 1
    birth = f'{yr}/{bm:02d}/{bd:02d} ({2026-yr})'
    pp = f'{3+i%6}{(i*7654321+1234567)%100000000:08d}'[:9]
    ey = 2028 + i % 9; em = (i*5)%12+1; ed = (i*9)%28+1
    ppexp = f'{ey}/{em:02d}/{ed:02d}'
    rid = f'{chr(65+(i*3)%26)}{"1" if g else "2"}{(i*1357911+2468)%100000000:08d}'
    return birth, pp, ppexp, rid
# 以 V2（含李浩然）為母表，讓每位旅客的護照/生日/證號固定不隨版型改變
_master = []
for _grp in V2_GROUPS:
    for _p in _grp:
        if _p not in _master: _master.append(_p)
_pidx = {en: i for i, (cn, en, yr, g) in enumerate(_master)}
def _note(i, first, rty):
    parts = []
    if first: parts.append(rty)
    d = _diet[i % len(_diet)]
    if d: parts.append(d)
    parts.append(_stat[i % len(_stat)])
    return ' '.join(parts)
def _prev_rows(groups):
    rows = ''; n = 0
    for ri, grp in enumerate(groups):
        rty = _rtymap.get(len(grp), '')
        order = _orders[(ri // 2) % len(_orders)]
        for mj, (cn, en, yr, g) in enumerate(grp):
            n += 1
            pi = _pidx[en]
            birth, pp, ppexp, rid = _pax_detail(pi, yr, g)
            note = _note(pi, mj == 0, rty)
            title = 'MR' if g else 'MS'
            nocell = f'<td class="c rp-no" data-room="{ri}"></td>'
            cls = ' class="rtop"' if mj == 0 else ''
            rows += (f'<tr{cls}><td class="c">{n}</td>{nocell}'
                     f'<td>{cn}</td><td>{title} {en}</td><td class="c">{order}</td>'
                     f'<td>{note}</td><td class="c">{pp}</td><td class="c">{ppexp}</td>'
                     f'<td class="c">{birth}</td><td class="c">{rid}</td></tr>')
    return rows
def _final_lines(groups):
    twn = sum(1 for g in groups if len(g) == 2)
    trp = sum(1 for g in groups if len(g) == 3)
    sgl = sum(1 for g in groups if len(g) == 1)
    rooms = len(groups); pax = sum(len(g) for g in groups)
    l1 = f'FINAL　{twn:02d} TWIN ＋ 0 DBL ＋ {trp:d} TRP ＋ {sgl:d} SGL ＝ {rooms:02d} ROOMS'
    l2 = f'FINAL　{pax:02d} ADT ＋ 0 CHD ＋ 0 T/L ＋ 0 T/G ＝ {pax:02d} PAX'
    return l1, l2
def _finalbox(groups, cls, hidden=False):
    a, b = _final_lines(groups)
    st = ' style="display:none"' if hidden else ''
    return (f'<div class="rp-finalbox {cls}"{st}>'
            f'<div class="rp-finalttl">分房FINAL</div>'
            f'<div class="rp-finline">{a}</div><div class="rp-finline">{b}</div>'
            f'<div class="rp-finnote">※全部【禁煙ルーム】でご手配をお願い致します※<br>房號依分房表輸入內容壓入</div></div>')
FINALBOX_V1 = _finalbox(V1_GROUPS, 'rp-fin-v1')
FINALBOX_V2 = _finalbox(V2_GROUPS, 'rp-fin-v2', hidden=True)
PREV_V1 = _prev_rows(V1_GROUPS)
PREV_V2 = _prev_rows(V2_GROUPS)
_thead = ('<thead><tr><th>NO</th><th>房號</th><th>中文姓名</th><th>英文姓名</th><th>訂單編號</th>'
          '<th>備註</th><th>護照號碼</th><th>護照效期</th><th>生日</th><th>身分證字號</th></tr></thead>')
rp_inner = ('<div class="rp-screen">' + header_center('輸出預覽', 'RoomExt.dc.html') + f'''
<div class="rp-wrap">
  <div class="rp-top">
    <div class="rp-logo"><span class="rp-lion">LION TRAVEL</span><span class="rp-lion2">雄獅旅遊</span></div>
    <div class="rp-tour">TOUR：26JPN30BRA T</div>
    <div class="rp-htitle">分房表 RoomList</div>
    <div class="rp-tl">TL：林欣怡</div>
    <div class="rp-op">OP：古芨良</div>
  </div>
  <table class="rp-table rp-v1">{_thead}<tbody>{PREV_V1}</tbody></table>
  <table class="rp-table rp-v2" style="display:none">{_thead}<tbody>{PREV_V2}</tbody></table>
  {FINALBOX_V1}
  {FINALBOX_V2}
</div>
<div class="rp-bar"><button type="button" class="rp-back">返回</button><button type="button" class="rp-out">選擇輸出方式</button></div>
</div>''')
(P/'RoomExtPreview.dc.html').write_text(page_raw('輸出預覽', RX_CSS, rp_inner), encoding='utf-8')

# ========== 團體大表（詳細卡片版 + 設定顯示項目）==========
RO_CSS = '''
.ro-wrap{padding:8px 14px 40px;background:#F5F5F5}
.ro-group{margin-bottom:18px}
.ro-ghead{background:#e9ecef;border-radius:10px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;font-size:18px}
.ro-gno{font-weight:600;color:#222}
.ro-i{color:#aaa;font-size:15px}
.ro-gcnt{color:#555}
.ro-gbody{display:flex;flex-direction:column;gap:12px;margin-top:10px}
.ro-pax{background:#fff;border:1px solid #ededed;border-radius:12px;box-shadow:0 1px 4px rgba(0,0,0,.06);padding:15px 16px}
.ro-ghead{cursor:pointer}
.ro-chev{color:#aaa;margin-left:10px}
.ro-i{cursor:pointer;padding:0 2px;font-size:2em;line-height:1;vertical-align:middle;display:inline-block}
.ro-tabs{display:flex;gap:10px;padding:12px 16px 2px}
.ro-tab{flex:1;text-align:center;padding:12px 0;border-radius:24px;font-size:18px;font-family:inherit;border:0;cursor:pointer;background:#e9ecef;color:#555;text-decoration:none;display:block}
.ro-tab.on{background:#E8363D;color:#fff;font-weight:700}
.ro-name{font-size:19px;color:#222;font-weight:700}
.ro-name .age{color:#2E7CF6;font-size:15px;font-weight:400}
.ro-latin{font-size:14px;color:#999;margin-top:2px;margin-bottom:10px}
.ro-sec{display:flex;flex-direction:column;gap:7px}
.ro-row{display:flex;font-size:16px;line-height:1.4}
.ro-row .rk{width:76px;color:#999;flex:none}
.ro-row .rv{color:#222;flex:1;word-break:break-all}
.ro-row .lk{color:#1a56c4}
.ro-hr{border:0;border-top:1px solid #eee;margin:11px 0}
'''
_remarks = ['忌牛 No Beef', '行動不便', '—', '素食者', '需協助', '—']
_reqs = ['低樓層', '安靜房', '近電梯', '高樓層', '—', '雙床房']
_foods = ['一般', '不吃牛', '全素', '不吃海鮮', '兒童餐', '不吃羊']
def _pnr(i):
    A = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    return f'{A[i%24]}{i%10}{A[(i*3+5)%24]}{(i*7)%10}{A[(i*5+2)%24]}{(i*9)%10}'
def ro_pax(i, cn, en, yr, g):
    birth, pp, ppexp, rid = _pax_detail(i, yr, g)
    tb = f'{(i*8311+10000017)%90000000+10000000:08d}'
    tbexp = f'{2029+i%7}/{(i*3)%12+1:02d}/{(i*7)%28+1:02d}'
    ph = f'09{(i*7654321+11111111)%100000000:08d}'[:10]; phone = f'{ph[:4]}-{ph[4:7]}-{ph[7:]}'
    if cn == '李逸婕':
        tel_no, phone = '0988096305', '0988-096-305'
    else:
        tel_no = ph
    cph = f'09{(i*1234567+22222222)%100000000:08d}'[:10]; cphone = f'{cph[:4]}-{cph[4:7]}-{cph[7:]}'
    email = f'guest{i+1:02d}@liontravel.com'
    bus = f'{(i%12)+1}{"ABCD"[i%4]}'
    rm = f'{101+i//2}'
    gic = ('<span style="color:#2E7CF6">♂</span>' if g
           else '<span style="color:#E8368A">♀</span>')
    def row(k, v, fc=''):
        return f'<div class="ro-row {fc}"><span class="rk">{k}</span><span class="rv">{v}</span></div>'
    return (
        '<div class="ro-pax">'
        f'<div class="ro-name">{cn}　<span class="age">{2026-yr}歲</span>　{gic}</div>'
        f'<div class="ro-latin">{en}</div>'
        '<div class="ro-sec">'
        + row('生日', birth.split(' ')[0])
        + row('電話', f'<a target="_top" href="tel:{tel_no}" class="lk">{phone}</a> <span class="f-ds" style="color:#E8363D">（電說）</span>')
        + row('護照', f'{pp} | {ppexp}', 'f-pp')
        + row('台胞證', f'{tb} | {tbexp}', 'f-tb')
        + row('身分證', rid, 'f-id')
        + row('PNR', _pnr(i), 'f-pnr')
        + '</div><hr class="ro-hr f-remark"><div class="ro-sec f-remark">'
        + row('需求', _reqs[i % len(_reqs)])
        + row('飲食', _foods[i % len(_foods)])
        + '</div><hr class="ro-hr f-order"><div class="ro-sec f-order">'
        + row('同行公司', 'CompanyName')
        + row('訂單聯絡人', '王文文 | <a target="_top" href="tel:0912345678" class="lk">0912-345-678</a>')
        + row('業務員', '王文文（內湖）')
        + '</div><hr class="ro-hr f-contact"><div class="ro-sec f-contact">'
        + row('Email', email)
        + row('住家地址', '台灣台北市114內湖區石潭路151號')
        + row('緊急聯絡人', f'{cn[0]}先生 | <a target="_top" href="tel:{cph}" class="lk">{cphone}</a>')
        + '</div></div>'
    )
SET_ICON = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="1.8"><path d="M4 8h9M18 8h2M4 16h2M11 16h9"/><circle cx="15.5" cy="8" r="2.3"/><circle cx="8.5" cy="16" r="2.3"/></svg>'
ro_header = (f'<header style="height:80px;display:flex;align-items:center;justify-content:space-between;padding:0 20px;position:relative">'
             f'{back("Tour.dc.html")}'
             f'<h1 style="position:absolute;left:0;right:0;text-align:center;margin:0;font-size:22px;font-weight:700;color:#222;pointer-events:none">團體大表</h1>'
             f'<div style="display:flex;gap:12px"><button type="button" class="ro-settings" aria-label="設定顯示項目" style="width:42px;height:42px;border-radius:21px;border:0;background:#fff;display:flex;align-items:center;justify-content:center;padding:0;cursor:pointer">{SET_ICON}</button>{BCAST}</div></header>')
RO_GROUPS = [PAX28[i:i+2] for i in range(0, 28, 2)]
_ro_body = ''
_rpi = 0
for gi, grp in enumerate(RO_GROUPS):
    ono = f'6-1125{111+gi*2:04d}'
    paxes = ''.join(ro_pax(_rpi+j, *p) for j, p in enumerate(grp)); _rpi += len(grp)
    _ro_body += (f'<div class="ro-group"><div class="ro-ghead" data-t="rg{gi}">'
                 f'<span class="ro-gno">No. {ono} <span class="ro-i ro-oinfo" data-order="{ono}" data-cnt="{len(grp)}">ⓘ</span></span>'
                 f'<span class="ro-gcnt">{len(grp)} 人 <span class="ro-chev">⌃</span></span></div>'
                 f'<div class="ro-gbody" id="rg{gi}">{paxes}</div></div>')
ro_tabs = ('<div class="ro-tabs"><button type="button" class="ro-tab on">團體大表</button>'
           '<a class="ro-tab" href="RosterRollcall.dc.html">點名模式</a></div>')
ro_inner = ro_header + ro_tabs + f'<div class="ro-wrap">{_ro_body}</div>'
(P/'Roster.dc.html').write_text(page_raw('團體大表', RO_CSS, ro_inner), encoding='utf-8')

SIG_SVG ='<svg viewBox="0 0 260 90" style="width:200px;height:70px"><path d="M30 68 C40 20 48 18 50 55 C52 72 58 40 66 38 C74 36 70 66 82 60 C96 54 92 24 104 26 M120 30 L120 70 M112 40 L150 40 M160 66 C150 40 176 30 182 46 C188 60 168 64 170 70 C172 74 196 66 210 44 C220 28 214 70 230 58" fill="none" stroke="#111" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
LEGAL = [
 ('一、旅遊行程','團名：沖繩旅遊|星野BANTA咖啡·雙樂園～美之海水族館～海豚秀＆DMM水族館～可愛企鵝·神宮祈福四日｜升等1晚星野OMO5<br>團號：25JO805BRE-T'),
 ('二、委任期間','自民國 104 年 10 月 10 日起至 104 年 10 月 15 日止。<br>團號：25JO805BRE-T<br>如遇有行程變更致行程日數增減，委任期間自動展延至團體返國之日止。'),
 ('三、委任事務','受任人應依據旅客與委任人簽訂之旅遊定型化契約書、行程表內容、說明會資料、領隊交班單、<b>領隊出團標準作業化流程規範 SOP</b> 及委任人所交付行程相關文件之指示，執行接待或引導觀光旅客旅遊業務，提供旅客全程隨團服務並協助處理必要之旅遊事務。'),
 ('四、授權範圍','受任人執行委任事務，應依據第三條之指示文件辦理。受任人與委任人均應受觀光法規及旅遊契約及其他為旅行事業、旅遊目的或保護旅客權益的等相關法規之限制，不得逕自變更委任事務項目。惟遇有不可抗力或不可歸責之事由，或因突發之緊急事故，或為維護旅客之生命、身體、財產之安全，受任人應依領隊專業職能判斷並為妥善處理，可依程度調整或變更委任事務項目，惟受任人需於第一時間通知委任人，徵求委任人之同意並由委任人提供必要之協助。'),
 ('五、報酬給付','受任人之報酬，由雙方另以書面約定之。'),
 ('六、權利義務','''<div style="display:flex;flex-direction:column;gap:8px">
<div>1. 受任人應以善良管理人之注意義務執行委任事務。如因故意、過失或逾越委任事務範圍致生損害，受任人應負損償之責任。受任人因不可抗力或不可歸責之情事，或為維護旅客之法益，而需變更或調整委任事務，非客觀上無法通知委任人，否則應先取得委任人之事前同意，且前述之變更或調整，應以旅客之權益為優先考量。</div>
<div>2. 受任人執行委任事務，如委任人所提供之食宿、交通、行程、觀光點及旅遊覽內容與第三條所載之文件有品質或數量不符或有闕漏之情事，受任人應以旅客權益為優先考量並妥善處理，並應第一時間通知委任人，經委任人確認後之指示，協助與旅客進行溝通以取得圓滿的處理方案。</div>
<div>3. 受任人執行委任事務如需代支付款項，委任人得預先撥付相關費用予受任人。</div>
<div>4. 如旅客行使終止契約權而有墊付返國費用等必要支出款項，或因委任事務項目變更，或產生原定行程預算外之費用支出，受任人應於第一時間通知委任人並取得其同意。前述墊付費用等情形，經委任人通知委任人並取得同意後，受任人得要求委任人返還之。</div>
<div>5. 為檢核暨驗收委任事務項目，受任人應於行程結束之三個工作天內提供下列文件：<br>　a「領隊返國報告書」及其它指定文件：向委任人說明團體進行之狀況以確認雙方就委任事務之完成。<br>　b.「領隊報帳單」：檢附收據或詳實憑証，結清相關代收代付金額，如代收代付金額產生爭議，受任人有配合委任人進行調查之義務。<br>　C.「顧客滿意度調查表」：為提升旅遊服務品質，受任人應協助旅客填寫並於完成後妥善封存避免個資外洩，若為線上填寫亦應主動告知。</div>
<div>6. 除第三條委任事務外，受任人得委託受任人另為其他委任業務，例如行程中協助拍攝旅遊景點或餐食圖、文及相關資料收集之處理，惟其他委任業務不得阻礙或減損本委任契約書第三條之執行，亦不得違背本國或他國法令。受任人執行其他委任業務所取得之智慧財產權歸屬於委任人。</div>
<div>7. 受任人執行接待或引導觀光旅客旅遊業務期間，應按雙方約定內容執行委任事務，非不可抗力或不可歸責之因素，受任人應本於委任人之意旨完成委任事務，不得擅自解約，如造成委任人商譽或旅客權益受損，應負損害賠償責任。</div>
<div>8. 受任人於執行接待或引導觀光旅客旅遊業務因服務態度不佳、品德不良經查證屬實，委任人可隨時解約，受任人不得主張任何權利。</div>
<div>9. 受任人於執行委任人交付之業務所知悉旅客參團資訊，包括但不限於個人資料、參團資訊及參團期間所發生之個人事務，未經委任人書面同意，受任人均不得以任何形式洩漏予第三人知悉，相關文件亦應於執行業務結束時交回，若有違反應負民、刑事責任。</div>
<div>10. 交班資料內含有旅客個人資料之文件，應確實點收，結團時須全數繳回，交接人員會依簽收進行清點，該文件應妥善保管，倘若遺失、外洩、任意丟棄，或未經公司同意將該文件以任何形式交付予第三人或為其他利用，違者將追究相關民刑事責任。</div>
</div>'''),
]
clauses = ''.join(f'<h3 class="ch">{t}</h3><div class="cp">{b}</div>' for t, b in LEGAL)
FIELDS = [('身份證字號','A123456789'),('連絡電話','A123456789'),('通訊地址','台北市內湖區石潭路151號'),('戶籍地址','台北市內湖區石潭路151號'),('委任人','雄獅旅行社股份有限公司'),('法定代理人','王文傑'),('統一編號','04655091'),('地址','台北市內湖區石潭路151號')]
fields = ''.join(f'<div class="fr"><span class="fk">{k}：</span><span class="fv">{v}</span></div>' for k, v in FIELDS)
CHK_SECTIONS = [
('出團前','''<ol>
<li>請與OP確認交團時間，若有卡團，請提早與OP確認。</li>
<li>請確認交團資料夾資料(旅客名單、保險單、供應商預訂單、司機領隊簽收領據、車貼條、散客：上下車地點/特殊餐食)是否齊全，並於交班單上勾選；確認無誤後，交班單簽名後將白聯及約聘領隊需每團簽「領隊委任書」(專任領隊一年一簽「領隊委任書」)提供給OP留底。</li>
<li>請確認交團資料點收完成，與該團線控/業務確認是否有特殊交辦事項；並和供應商確認預訂時間及數量。</li>
<li>請與駕駛確認次日車輛報到時間、地點、礦泉水箱數；散客成團需另確認座位表遊覽車上座位排數。</li>
<li>散客成團請進行電話說明會及再次確認旅客上下車地點及特殊餐食；若無人接聽請留言或發簡訊給旅客。</li>
<li>團體包團請與旅客聯絡窗口確認次日出團相關事宜(是否有其他特殊需求及細節)。</li></ol>'''),
('出團中','''<ol>
<li>出團當日領隊於集合時間前20分鐘抵達集合地點(台北車站雄獅站前門市請另找值班線控簽到，並於報到區就定位開始劃位)；遲到者請繳交300元罰金給導領部。</li>
<li>確認團員特殊需求(含餐食、床型、團費含小費及特殊加價需求等)無誤。</li>
<li>教學使用手機掃描QR CODE及從雄獅B2C網頁進入意調表入口畫面。</li></ol>'''),
('出團後','''<ol>
<li>團體中支出款項，請帶回有公司統編/抬頭的三聯式發票、正式收據(需蓋有「有統編的免用統一發票」)及供應商的私章)。</li>
<li>司領支出請簽署簽收紅白黃三聯單，凡現金支出均務必載明清楚款項明細，並將黃聯交由領款人留存，紅白聯隨團帳黏貼至收據黏貼表繳回公司。</li>
<li>團體中支出款項，請回填在支出預算表；並協助載明結帳明細(桌數素食/票種人數)。</li>
<li>團體中所有收據/發票/簽收單，請依照支出預算表浮貼至收據黏貼表。</li>
<li>回團後，請於三天內返回公司交團；若遇連團(可先與OP拿回團資料寄送牛皮紙袋)，請協助將回團資料夾於雄獅各門市寄回，回團款項請與OP確認後，直接匯款回公司帳戶(通知OP匯款帳號後5碼)。</li></ol>'''),
('注意事項','''<ol>
<li style="color:#E8363D">公司抬頭統編(請確認出團統編為甚麼公司別，請勿開錯)<br>統一編號：04655091<br>抬頭：雄獅旅行社股份有限公司<br>統一編號：23755606<br>抬頭：寶獅旅行社股份有限公司</li>
<li>未取得公播權利影片時，均不得在遊覽車上播送、播放影片及音樂。</li>
<li>未經公司同意，請勿使用私人信用卡刷卡結帳。</li>
<li>非行程表上排定之旅遊活動、行程提早回程時間或取消行程，須向全團旅客取得同意書，方可進行。若未取得同意書進行發生意外事件，領隊及公司皆須負加重之責任，請領隊務必慎行！</li></ol>'''),
('領團服儀標準規範','''<ol>
<li>應著有領白色上衣;襯衫、Polo衫皆可</li>
<li>搭配雄獅新背心(紅面)</li>
<li>應著深色西裝褲或長褲;不得穿著牛仔褲及運動褲</li>
<li>應著深色包鞋</li>
<li>應使用乾淨無破損之領隊旗</li>
<li>髮型儀容整齊乾淨;髮色應為自然髮色。自帶工作包不宜太過花俏。</li></ol>'''),
('帶團須知','''<div style="margin-bottom:6px">須知：</div><ol>
<li>非特殊情況時，說明會請領隊本人親自出席。</li>
<li>確實按行程表督導、配合當地旅行社，完成既定的行程。</li>
<li>確保旅途中團員及自身之生命財產安全。</li>
<li>執行公司託付之角色與工作，收集通報旅行相關之資料及訊息。</li>
<li>協助團員解決困難，提供適切之協助。</li>
<li>隨機應變，掌握局勢，以求圓滿完成任務。</li>
<li>早餐時間領隊一定要到餐廳，早上要比預定時間早一些起床，早一點到櫃檯結帳。</li>
<li>帶團期間不得穿著運動服或無領衫、短褲、拖鞋等（海邊旅遊區除外）。</li>
<li style="color:#E8363D;font-weight:700">認真操作體驗等等搶答有好禮喔～</li></ol>'''),
]
checkitems = ''.join(f'<div class="accwrap"><button type="button" class="accitem" data-act="acc"><span>{t}</span><span class="cv">⌄</span></button><div class="acccontent">{c}</div></div>' for t, c in CHK_SECTIONS)

ct_css = '''.cscroll{position:absolute;top:80px;bottom:82px;left:0;right:0;overflow:auto;background:#fff;padding:18px 22px}
.clogo{display:flex;align-items:center;gap:8px}
.ctitle{text-align:center;font-size:26px;font-weight:700;margin:12px 0 16px}
.cintro{font-size:14px;line-height:1.9;color:#222}
.cfill{display:inline-block;min-width:70px;background:#f0f0f0;border-radius:4px;padding:1px 10px;text-align:center}
.ch{font-size:16px;font-weight:700;margin:18px 0 6px}
.cp{font-size:13px;line-height:1.9;color:#333}
.fields{margin-top:24px;display:flex;flex-direction:column;gap:14px}
.fr{display:flex;align-items:center;gap:12px;font-size:15px}
.fk{width:84px;flex:none;color:#222}
.fv{background:#f0f0f0;border-radius:4px;padding:6px 12px}
.sigrow{display:flex;align-items:center;gap:14px}
.sigbox{width:180px;height:88px;border-radius:6px;background:#FDEBEE;color:#E8363D;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:17px;line-height:1.4;border:0;cursor:pointer}
.sigbox.done{background:#fff;border:1px solid #ddd}
.cbar{position:absolute;left:0;right:0;bottom:0;height:82px;background:#fff;border-top:1px solid #eee;display:flex;gap:14px;align-items:center;padding:0 20px}
.cbar a,.cbar button{flex:1;height:48px;border-radius:8px;font-size:20px;font-weight:700;display:flex;align-items:center;justify-content:center;font-family:inherit;border:0}
.cbar .cancel{background:#fff;border:1px solid #E8363D;color:#E8363D}
.cbar .ok{background:#E5E5E5;color:#aaa}
.cbar .ok.en{background:#E8363D;color:#fff;cursor:pointer}
.cmodal{position:absolute;inset:0;background:rgba(0,0,0,.45);display:flex;align-items:center;justify-content:center;z-index:8}
.cmodal.hide{display:none}
.mbox{width:330px;background:#fff;border-radius:14px;padding:22px 20px;display:flex;flex-direction:column;gap:12px}
.mhd{display:flex;justify-content:space-between;align-items:center}
.mhd h2{margin:0;font-size:20px;font-weight:700}
.mx{border:0;background:none;font-size:22px;cursor:pointer;padding:0}
.mbox-chk{width:740px;max-height:1060px}
.accscroll{flex:1;overflow:auto;display:flex;flex-direction:column;gap:8px;margin:2px 0}
.accwrap{display:flex;flex-direction:column}
.accitem{display:flex;justify-content:space-between;align-items:center;height:48px;padding:0 14px;border:0;border-radius:8px;background:#F0F0F0;font-family:inherit;font-size:18px;font-weight:700;cursor:pointer}
.accitem.read{background:#FDEBEE;color:#E8363D}
.accwrap.open .accitem .cv{transform:rotate(180deg)}
.acccontent{display:none;padding:10px 10px 14px;font-size:15px;line-height:1.85;color:#333}
.acccontent ol{margin:0;padding-left:24px;display:flex;flex-direction:column;gap:7px}
.accwrap.open .acccontent{display:block}
.mhint{color:#E8363D;font-size:14px;text-align:center}
.mbtn{height:46px;border-radius:8px;border:0;font-size:18px;font-weight:700;background:#E5E5E5;color:#aaa;font-family:inherit}
.mbtn.en{background:#E8363D;color:#fff;cursor:pointer}
.sigpad{height:190px;border:1px solid #ddd;border-radius:8px;display:flex;align-items:center;justify-content:center}
.sigpad.empty svg{display:none}
.padrow{display:flex;gap:12px;justify-content:space-between}
.padrow button{flex:1;height:44px;border-radius:8px;font-size:18px;font-weight:700;font-family:inherit;border:1px solid #E8363D;background:#fff;color:#E8363D;cursor:pointer}
.padrow button.pri{background:#E8363D;color:#fff;border:0}
.ctoast{position:absolute;left:50%;bottom:110px;transform:translateX(-50%);background:rgba(50,50,50,.92);color:#fff;font-size:16px;padding:12px 22px;border-radius:24px;z-index:6;white-space:nowrap}
.ctoast.hide{display:none}'''

ct_body = header_center('委任契約書', 'PreTour.dc.html') + f'''
<div class="cscroll">
<div class="clogo"><svg aria-hidden="true" width="34" height="27" viewBox="0 0 80 64"><path d="M12 48c-6-10 0-30 16-34 8-2 18 2 26 10 6 6 8 14 6 22-2 8-10 12-18 12H20c-4 0-6-4-8-10z" fill="#E8363D"/></svg><span style="display:flex;flex-direction:column;line-height:1.1"><b style="font-size:16px;letter-spacing:1px">LION TRAVEL</b><span style="font-size:13px;letter-spacing:3px">雄獅旅遊</span></span></div>
<div class="ctitle">領隊委任契約書</div>
<div class="cintro">本公司茲委任 <span class="cfill">李小明</span> 君，身分證字號 <span class="cfill">A123456789</span>，擔任委任人旅遊團體之領隊人員，執行旅遊接待或引導觀光旅客之業務，提供行程所需之各項旅遊服務。雙方同意就委任業務履行下列協議事項：</div>
{clauses}
<div class="fields">
<div class="fr sigrow"><span class="fk">受任人：</span><button type="button" class="sigbox" data-act="signPad">簽章處<br>(請點擊)</button><span>君（簽章）</span></div>
{fields}
</div>
</div>
<div class="cbar"><a href="#PreTour" class="cancel">取消</a><button type="button" class="ok" data-act="sign">完成</button></div>
<div class="ctoast hide">請點擊簽章處，進行契約書簽署</div>
<div class="cmodal checklist"><div class="mbox mbox-chk">
<div class="mhd"><h2>自檢表(國內旅遊)</h2><button type="button" class="mx" data-act="closeChk">✕</button></div>
<div class="accscroll">{checkitems}</div>
<div class="mhint">ⓘ 需展開內容並閱讀完後，點擊我已閱讀。</div>
<button type="button" class="mbtn" data-act="ackList">我已閱讀</button>
</div></div>
<div class="cmodal signpad hide"><div class="mbox">
<div class="mhd"><h2>簽名板</h2></div>
<div class="sigpad">{SIG_SVG}</div>
<div class="padrow"><button type="button" data-act="closePad">取消</button><button type="button" data-act="padRedo">重寫</button><button type="button" class="pri" data-act="padOk">確認</button></div>
</div></div>'''
(P/'Contract.dc.html').write_text(page('委任契約書', ct_css, ct_body), encoding='utf-8')
print('ok')
