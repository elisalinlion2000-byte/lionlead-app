import json, pathlib
P = pathlib.Path('/home/claude/lionlead/project')

HEAD = '''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&amp;display=swap">
<style>
body{{margin:0;font-family:'Noto Sans TC',system-ui,sans-serif}}
a{{color:#222;text-decoration:none}}a:hover{{color:#222}}
.sec{{position:relative;background:#fff;border-radius:12px;padding:20px 18px;display:flex;flex-direction:column;gap:8px}}
.sec::before{{content:"";position:absolute;left:0;top:22px;width:4px;height:26px;background:#E8363D;border-radius:0 2px 2px 0}}
.sec h2{{margin:0;font-size:24px;font-weight:700}}
.in{{box-sizing:border-box;width:100%;height:50px;border:1px solid #bbb;border-radius:4px;padding:0 12px;font-size:18px;font-family:inherit;background:#fff}}
.in::placeholder{{color:#999}}
.lb{{font-size:19px;color:#222;margin-top:6px}}
.q{{display:flex;flex-direction:column;gap:6px;margin-top:10px}}
.q .t{{font-size:20px;font-weight:700}}
.q .d{{font-size:15px;color:#777}}
.stars{{display:flex;justify-content:space-between;align-items:center;font-size:15px;color:#777;margin-top:4px}}
.stars button{{border:0;background:none;padding:0;width:28px;height:28px}}
.stars svg{{width:26px;height:26px;fill:#ddd}}
.tw{{position:relative}}
.tw svg{{position:absolute;right:12px;top:16px;width:18px;height:18px;stroke:#444;fill:none;stroke-width:1.8}}
.del{{width:34px;height:34px;border-radius:17px;border:0;background:#E8363D;display:flex;align-items:center;justify-content:center;padding:0}}
</style>
</helmet>
<div style="width:820px;height:{h}px;box-sizing:border-box;background:#F5F5F5;position:relative;overflow:hidden">
<header style="height:80px;display:flex;align-items:center;justify-content:space-between;padding:0 20px;position:relative">
<a href="{back}" aria-label="返回" style="width:42px;height:42px;border-radius:21px;background:#3b3b3b;display:flex;align-items:center;justify-content:center"><svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4"><path d="M15 5l-7 7 7 7"/></svg></a>
<h1 style="position:absolute;left:0;right:0;text-align:center;margin:0;font-size:22px;font-weight:700;color:#222;pointer-events:none">{title}</h1>
<div style="display:flex;gap:12px">
<a href="Notify.dc.html" aria-label="通知" style="position:relative;width:42px;height:42px;border-radius:21px;background:#fff;display:flex;align-items:center;justify-content:center"><svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="1.8"><path d="M6 17V11a6 6 0 0 1 12 0v6l1.5 2h-15z"/><path d="M10 21h4"/></svg><span style="position:absolute;top:8px;right:9px;width:7px;height:7px;border-radius:4px;background:#E8363D"></span></a>
<button type="button" aria-label="離線模式" style="width:42px;height:42px;border-radius:21px;border:0;background:#FDE4E6;display:flex;align-items:center;justify-content:center;padding:0"><svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#E8363D" stroke-width="1.8"><circle cx="12" cy="12" r="2"/><path d="M7.8 7.8a6 6 0 0 0 0 8.4M16.2 7.8a6 6 0 0 1 0 8.4M4.9 4.9a10 10 0 0 0 0 14.2M19.1 4.9a10 10 0 0 1 0 14.2"/></svg></button>
</div>
</header>
<div style="margin:10px 20px 0;display:flex;flex-direction:column;gap:18px">
'''

TRASH = '<button type="button" class="del" aria-label="刪除"><svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13M10 11v6M14 11v6"/></svg></button>'
CLOCK = '<svg aria-hidden="true" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg>'
STAR = '<path d="M12 2l3 7 7 .6-5.3 4.7L18.5 22 12 18l-6.5 4 1.8-7.7L2 9.6 9 9z"/>'

def times(prefix):
    return f'''<div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:14px">
<div style="display:flex;flex-direction:column;gap:6px"><label class="lb" for="{prefix}s" style="margin:0">開始時間</label><div class="tw"><input class="in" id="{prefix}s" type="text" placeholder="09:00(預計)">{CLOCK}</div></div>
<div style="display:flex;flex-direction:column;gap:6px"><label class="lb" for="{prefix}e" style="margin:0">結束時間</label><div class="tw"><input class="in" id="{prefix}e" type="text" placeholder="09:00(預計)">{CLOCK}</div></div>
</div>
<label style="display:flex;align-items:center;gap:10px;font-size:19px;margin-top:6px"><input type="checkbox" style="width:20px;height:20px;margin:0;accent-color:#E8363D">與說資順序不符合</label>'''

def eval_sec(name, qs, note_label):
    s = f'<section class="sec">\n<h2>{name}</h2>\n'
    for t, d in qs:
        stars = ''.join(f'<button type="button" aria-label="{i} 星"><svg viewBox="0 0 24 24">{STAR}</svg></button>' for i in range(1, 5))
        s += f'<div class="q"><div class="t">{t}</div><div class="d">{d}</div><div class="stars"><span>最低</span>{stars}<span>最高</span></div></div>\n'
    s += f'<label class="lb" for="note" style="font-size:20px;font-weight:700;margin-top:14px">{note_label}</label><input class="in" id="note" type="text" placeholder="請輸入">\n</section>\n'
    return s

PHOTO = '''<section class="sec">
<div style="display:flex;justify-content:space-between;align-items:baseline"><h2>上傳照片</h2><span style="font-size:17px;color:#333">0張</span></div>
<button type="button" style="width:370px;height:280px;border:1px solid #ddd;border-radius:6px;background:#F5F5F5;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;font-family:inherit;font-size:18px;color:#999;margin-top:10px"><span style="font-size:30px;line-height:1">+</span>選擇照片</button>
</section>
'''

def tail(back, h):
    return f'''</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:80px;background:#F5F5F5;display:flex;align-items:center;padding:0 20px">
<a href="{back}" style="flex:1;display:flex;align-items:center;justify-content:center;height:46px;border-radius:8px;background:#E8363D;color:#fff;font-size:21px;font-weight:700">確定</a>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":820,"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''

def build(fname, title, h, top, qs, note_label='備註/其他評論', back='#back', photo=True):
    html = HEAD.format(title=title, h=h, back=back) + top + eval_sec(title, qs, note_label) + (PHOTO if photo else '') + tail(back, h)
    (P / fname).write_text(html, encoding='utf-8')

# 導遊
build('Guide.dc.html', '導遊', 2120,
  f'''<section class="sec">
<div style="display:flex;justify-content:space-between;align-items:center"><h2>導遊</h2>{TRASH}</div>
<label class="lb" for="gname">導遊名稱</label><input class="in" id="gname" type="text" placeholder="請輸入">
</section>
''',
  [('團務配合度','對行程流程、團員狀況、與領隊的配合度'),
   ('解說專業與說話技巧','導覽內容、景點解說是否準確、有趣、引導有層次'),
   ('應對團員能力與親和力','可回應旅客提問、互動及處理臨時狀況的能力'),
   ('時間控管與節奏掌握','是否能掌控景點停留時間、不拖延'),
   ('團隊氣氛營造能力','是否能帶動氛圍、說笑適當、處事圓融')])

# 飯店
build('Hotel.dc.html', '飯店', 1960,
  f'''<section class="sec">
<div style="display:flex;justify-content:space-between;align-items:center"><h2>MERCURE SYDNEY PARRAMATTA</h2>{TRASH}</div>
<div style="text-align:center;margin-top:10px"><a href="#top" style="font-size:19px;text-decoration:underline">複製前一天</a></div>
</section>
''',
  [('服務配合度','櫃台及房務服務態度，包括房間分配及入住安排'),
   ('房間整潔與設施狀況','客房乾淨度、設施完好程度、衛浴水壓與溫度等'),
   ('安全與緊急應變設施','逃生標示、火警設備、安全管理（門禁、監控）'),
   ('公共設施','WIFI提供、無障礙設施及其他設施(健身房、游泳池)等')])

# 景點
build('Spot.dc.html', '景點', 2060,
  f'''<section class="sec">
<div style="display:flex;justify-content:space-between;align-items:center"><h2>徒步體驗雪梨港灣大橋 Sydney Harbour Bridge</h2>{TRASH}</div>
{times('sp')}
</section>
''',
  [('導覽與解說品質','解說內容是否豐富清楚，語音導覽設備是否正常'),
   ('景點設施與動線安排','洗手間、座椅、動線是否友善團體'),
   ('安全與應變措施','是否有清楚標示牌、設施安全、突發狀況應對能力'),
   ('團員反應與滿意度','團員是否覺得值得、覺得有趣、有收穫或放鬆感')])

# 餐廳
build('Restaurant.dc.html', '餐廳', 2220,
  f'''<section class="sec">
<div style="display:flex;justify-content:space-between;align-items:center"><h2 style="display:flex;align-items:center;gap:8px">敬請自理<svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#999" stroke-width="1.8"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/></svg></h2>{TRASH}</div>
{times('rs')}
</section>
''',
  [('餐點品質與份量','菜色口味、溫度、份量是否足夠、團員滿意度'),
   ('上菜速度與順序','是否在合理時間內上完菜、冷熱餐上菜邏輯'),
   ('用餐環境與清潔','桌面、地板、餐具、洗手間是否乾淨，冷氣與通風是否良好'),
   ('餐廳配合度與服務態度','是否配合團體需求（素食、調整時段、事先提供桌次桌型安排）、員工態度'),
   ('動線與集合安排','團體進出動線順暢、集合點明確，無障礙設施/電梯?')])

# 起床及出發時間
wake = HEAD.format(title='起床及出發時間', h=1180, back='#back') + f'''<section class="sec">
<h2>第1天</h2>
<label class="lb" for="w1">起床時間</label><div class="tw"><input class="in" id="w1" type="text" placeholder="09:00(預計)">{CLOCK}</div>
<label class="lb" for="w2">出發時間</label><div class="tw"><input class="in" id="w2" type="text" placeholder="09:00(預計)">{CLOCK}</div>
</section>
''' + tail('#back', 1180)
(P / 'WakeTime.dc.html').write_text(wake, encoding='utf-8')
print('ok')
