import re, pathlib, json
P = pathlib.Path('/home/claude/lionlead/project')
ORDER = ['Entry','Main','Login','Home','HomeCalendar','Notify','PreTour','Contract','HandoverLocked','HandoverPartial','HandoverDone','HandoverOverview','HdRecv','HdTicket','HdPnr','HdIns','HdAgr','HdBrief','HdQ','HdRoom','HdList','HdContact','HdOther','RoomExt','RoomExtPreview','PreTourDev','Mine','TourEmpty','Tour','TourDialog','PostTour','Consent','ConsentOffline','ConsentView','ConsentForm','ConsentDrop','ConsentNoMed','ConsentNoRep','ConsentCash','ConsentQR','Roster','RosterRollcall','Daily1','Daily2','DailyAdd','SpotSet','Daily3','WakeTime','Qbox','Transport','Guide','Hotel','Spot','Restaurant','SmsList','SmsEdit','SmsSend','SmsResult','Itinerary','Meeting']
FLUID = {'Entry','Itinerary','Meeting','RoomExtPreview'}

def scope_css(css, sid):
    out = []
    for rule in re.findall(r'([^{}]+)\{([^{}]*)\}', css):
        sel, body = rule[0].strip(), rule[1]
        if not sel or sel.startswith('@'): continue
        if sel == 'body': continue
        sels = [f'#{sid} {x.strip()}' for x in sel.split(',')]
        out.append(','.join(sels) + '{' + body + '}')
    return '\n'.join(out)

screens, css_all, logic = [], [], {}
for name in ORDER:
    f = P / f'{name}.dc.html'
    if not f.exists(): continue
    src = f.read_text(encoding='utf-8')
    sid = 's-' + name
    helmet = re.search(r'<helmet>(.*?)</helmet>', src, re.S).group(1)
    for st in re.findall(r'<style>(.*?)</style>', helmet, re.S):
        css_all.append(scope_css(st, sid))
    markup = re.search(r'</helmet>\s*(.*?)\s*</x-dc>', src, re.S).group(1)
    # links
    markup = re.sub(r'href="([A-Za-z0-9]+)\.dc\.html"', lambda m: f'href="#{m.group(1)}"', markup)
    markup = markup.replace('href="#top"', 'href="#noop"')
    # network icon hook
    markup = markup.replace('aria-label="離線模式"', 'aria-label="離線模式" data-net="1"')
    # logic
    m = re.search(r'class Component extends DCLogic \{(.*)\}\s*</script>', src, re.S)
    body = m.group(1).strip() if m else 'renderVals(){return {};}'
    body = re.sub(r'^\s*renderVals\(\)\s*\{\s*return \{\};\s*\}\s*$', '', body)
    body = re.sub(r"'([A-Za-z0-9]+)\.dc\.html'", lambda m: "'#" + m.group(1) + "'", body)
    logic[name] = body
    cls = 'fluid' if name in FLUID else 'fixed'
    screens.append(f'<section class="screen {cls}" id="{sid}" data-name="{name}"><template>{markup}</template><div class="mount"></div></section>')

logic_js = ',\n'.join(f'{k}: class extends DCLogic {{ {v} }}' for k, v in logic.items() if v.strip())
html = (pathlib.Path('/home/claude/lionlead/scratch/sim_shell.html').read_text(encoding='utf-8')
        .replace('/*SCREEN_CSS*/', '\n'.join(css_all))
        .replace('<!--SCREENS-->', '\n'.join(screens))
        .replace('/*LOGIC*/', logic_js))
# 模擬器用本地圖檔取代畫布的 /_blob 資產
html = (html.replace('/_blob/2d1a352066225910e77963930d4bbb98', 'splash.png')
            .replace('/_blob/28cc5208405c081ca4eaf1cc7f53e26d', 'appicon.png')
            .replace('/_blob/ded9e556750bd49e79cc013301aa5e1a', 'login-bg.jpg'))
import shutil
shutil.copy('/home/claude/lionlead/assets/splash.png', '/home/claude/lionlead/sim/splash.png')
shutil.copy('/home/claude/lionlead/assets/appicon.png', '/home/claude/lionlead/sim/appicon.png')
shutil.copy('/home/claude/lionlead/scratch/login-bg.jpg', '/home/claude/lionlead/sim/login-bg.jpg')
shutil.copy('/home/claude/lionlead/assets/lionlead-logo.jpg', '/home/claude/lionlead/sim/lionlead-logo.jpg')
pathlib.Path('/home/claude/lionlead/sim/index.html').write_text(html, encoding='utf-8')
print(len(screens), 'screens', len(html)//1024, 'KB')
