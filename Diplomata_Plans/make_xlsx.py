# -*- coding: utf-8 -*-
import importlib.util
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

HERE = Path(__file__).parent
def load(name, var):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return getattr(m, var)

SERIES = [load("plan_ru","RU"), load("plan_nl","NL"), load("plan_it","IT"),
          load("plan_de","DE"), load("plan_br","BR"), load("plan_jp","JP"), load("plan_fr","FR")]

P3MOD = load("part3_cases","P3")
ES3 = load("part3_cases","ES3")
for key, s in zip(["RU","NL","IT","DE","BR","JP","FR"], SERIES):
    s["parts"][2] = P3MOD[key]["part"]
    s["episodes"] = [e for e in s["episodes"] if e[0] != 3] + P3MOD[key]["eps"]

FONT = "Malgun Gothic"
NAVY = "1F2A44"; ACCENT = "8A1C2B"; SAND = "F3EEE6"; BLUE = "EEF1F7"
PART_FILL = {1: "E8F0E4", 2: "FFF3D6", 3: "F6E3E3"}
thin = Side(style="thin", color="C9C9C9")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)

def f(bold=False, size=10, color="000000", italic=False):
    return Font(name=FONT, bold=bold, size=size, color=color, italic=italic)
def fill(c): return PatternFill("solid", start_color=c, end_color=c)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(wrap_text=True, vertical="center", horizontal="center")

def put(ws, r, c, v, font=None, fl=None, al=WRAP, border=True):
    cell = ws.cell(row=r, column=c, value=v)
    cell.font = font or f(); cell.alignment = al
    if fl: cell.fill = fill(fl)
    if border: cell.border = BORDER
    return cell

def title(ws, text, sub=None, width=8):
    ws.cell(row=1, column=1, value=text).font = f(True, 16, NAVY)
    if sub:
        ws.cell(row=2, column=1, value=sub).font = f(False, 10, "555555")
    ws.sheet_view.showGridLines = False

def header(ws, r, labels, start=1):
    for i, t in enumerate(labels):
        put(ws, r, start+i, t, f(True, 10, "FFFFFF"), NAVY, CENTER)

def widths(ws, ws_widths):
    for i, w in enumerate(ws_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

wb = Workbook()

# ---------- 개요 ----------
ws = wb.active; ws.title = "개요"
title(ws, "외교관 시리즈 3부작 기획안 (7개 언어)", "언어별 완전히 독립된 세계·사건·인물 / 3부 × 12화 = 36화 / 화당 100~200턴 / B2–C1 / 해법의 근거로 해당국 역사 사례를 사용")
header(ws, 4, ["언어","시리즈 제목","주인공","1부","2부","3부","핵심 해법 방식","한 줄 소개"])
for i, s in enumerate(SERIES):
    r = 5 + i
    prot = s["protagonist"].split("—")[0].strip()
    put(ws, r, 1, s["lang"], f(True), SAND)
    put(ws, r, 2, f'{s["title"]}\n({s["title_ko"]})', f(True, 10, ACCENT))
    put(ws, r, 3, prot)
    for j in range(3):
        p = s["parts"][j]
        put(ws, r, 4+j, f'{p[1]}\n{p[2]}\n— {p[3]}')
    put(ws, r, 7, s["style"].replace("지문 없이 대사만. ",""))
    put(ws, r, 8, s["tagline"])
    ws.row_dimensions[r].height = 150
widths(ws, [20,22,22,40,40,40,34,40])
ws.freeze_panes = "B5"
r = 12
ws.cell(row=r, column=1, value="참고").font = f(True, 11, NAVY)
notes = [
 "· 스페인어 버전(EL AGREGADO)은 별도로 1부 12화를 완성했습니다(Diplomata_ES 폴더). 이 파일은 나머지 7개 언어의 기획안입니다.",
 "· 프랑스어 버전(LA NUANCE)을 추가해 스페인어를 제외한 7개 언어가 모두 포함됩니다(총 8개 언어 중 스페인어는 제작 중).",
 "· 모든 국가·정치인·기업은 가상이며, 역사 사례만 실제 사건을 인용합니다. 사례의 연도·내용은 집필 단계에서 다시 한 번 검증합니다.",
 "· '에피소드 종합' 시트는 252화 전체를 한 표로 모아 필터·정렬할 수 있습니다.",
]
for k, t in enumerate(notes):
    ws.cell(row=r+1+k, column=1, value=t).font = f()

# ---------- 공통 규칙 ----------
ws = wb.create_sheet("공통 규칙")
title(ws, "공통 규칙", "6개 언어 모두에 적용")
rows = [
 ("출력 형식","화별 Word(.docx) + PDF. 외국어 줄 다음에 한국어 대역 줄, 섹션 끝에 표현 주석 4~7개"),
 ("분량","화당 100~200턴 기본(평균 150~170). 개막·클라이맥스·최종화는 180~210까지 허용"),
 ("지문","지문 없이 대사만으로 구성(스페인어 버전과 동일)"),
 ("레벨","B2–C1(중상급). 언어별 문법 포인트는 각 시트의 '레벨' 항목 참조"),
 ("독립성","언어마다 세계관·사건·인물·비밀이 모두 다름. 공통점은 직업(40대 현지 국적 외교관), 형식, 협상 유형 틀뿐"),
 ("협상 유형","정공법 / 물밑 / 조사·음모 / 비밀 폭로 / 일반 협상 / 내부 대결 / 더러운 수단 / 언론전 / 배신 / 결산"),
 ("해법의 순간","화마다 대화(상대·주변 인물의 한마디, 통역 실수, 사소한 습관)에서 해법이 떠오르는 순간을 하나 배정"),
 ("역사 사례","화마다 해당국의 실제 역사 사례를 1개 이상, 해법의 논거로 대사에 쓰고 주석에 사건·연도·교훈을 단다"),
 ("복선 장부","언어마다 '비밀·복선 장부'를 만들어 화 간 회수를 관리(스페인어 바이블 방식)"),
 ("3부 구조","3부는 한 화에 사건 하나가 아니라 4개의 사건을 각각 3화(발생·심화/반전·해결/대가)에 걸쳐 푸는 구조. 4개 사건은 3부의 상위 실마리 하나로 묶이고, 사건마다 지배적 협상 유형이 다름"),
 ("1·2부 구조","1부와 2부는 하나의 큰 사건을 12화에 걸쳐 푸는 연속 구조"),
 ("집필 순서","시리즈 바이블 → 1부 시놉시스 → 1화 시범 → 확인 후 나머지 화 → 2·3부 상세화"),
]
header(ws, 4, ["항목","내용"])
for i,(a,b) in enumerate(rows):
    put(ws, 5+i, 1, a, f(True), SAND); put(ws, 5+i, 2, b)
widths(ws, [18, 110])

# ---------- 스페인어 참고 ----------
ws = wb.create_sheet("스페인어(완성) 참고")
title(ws, "스페인어 버전 1부 현황 (EL AGREGADO · LA CLÁUSULA CERO)", "이미 완성된 12화 — 다른 언어 기획의 기준선")
es = [
 (1,"El atunero retenido","억류된 참치잡이배",165),(2,"La cena de los jueves","목요일 만찬",144),
 (3,"El archivo de Alcalá","알칼라 문서고",159),(4,"El hombre del maletín","서류가방의 남자",177),
 (5,"Mesa en Bruselas","브뤼셀 협상",155),(6,"Lo que sabía Valdés","발데스는 알고 있었다",171),
 (7,"Un favor sucio","더러운 호의",179),(8,"La filtración","유출",154),
 (9,"Gaspar","가스파르",178),(10,"Ginebra a ciegas","제네바 맹인 협상",165),
 (11,"La cláusula cero","영 조항",203),(12,"Quien firma, paga","서명한 자가 대가를 치른다",208)]
header(ws, 4, ["화","원어 제목","한국어 제목","턴 수"])
for i,(a,b,c,d) in enumerate(es):
    put(ws, 5+i, 1, a, al=CENTER); put(ws, 5+i, 2, b); put(ws, 5+i, 3, c); put(ws, 5+i, 4, d, al=CENTER)
put(ws, 17, 3, "합계", f(True), SAND); put(ws, 17, 4, "=SUM(D5:D16)", f(True), SAND, CENTER)
widths(ws, [8,30,30,10])
r0 = 20
ws.cell(row=r0, column=1, value="스페인어 3부 설계 (4사건 × 3화)").font = f(True, 12, NAVY)
header(ws, r0+1, ["화","원어 제목","한국어 제목","사건","줄거리","해법이 떠오르는 순간","역사 사례"])
for i, e in enumerate(ES3["eps"]):
    r = r0 + 2 + i
    put(ws, r, 1, e[1], al=CENTER); put(ws, r, 2, e[2]); put(ws, r, 3, e[3]); put(ws, r, 4, e[8], f(True))
    put(ws, r, 5, e[5]); put(ws, r, 6, e[6]); put(ws, r, 7, e[7])
    ws.row_dimensions[r].height = 48
ws.column_dimensions["D"].width = 24; ws.column_dimensions["E"].width = 50; ws.column_dimensions["F"].width = 40; ws.column_dimensions["G"].width = 40

# ---------- 언어별 시트 ----------
allrows = []
for s in SERIES:
    ws = wb.create_sheet(s["sheet"])
    title(ws, f'{s["lang"]} — {s["title"]} ({s["title_ko"]})', s["tagline"])
    r = 4
    info = [("주인공", s["protagonist"]), ("세계관", s["world"]), ("레벨", s["level"]), ("형식·학습 포인트", s["style"])]
    for k, v in info:
        put(ws, r, 1, k, f(True), SAND)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=8)
        put(ws, r, 2, v)
        for c in range(3, 9): ws.cell(row=r, column=c).border = BORDER
        ws.row_dimensions[r].height = 48
        r += 1
    r += 1
    ws.cell(row=r, column=1, value="주요 인물").font = f(True, 11, NAVY); r += 1
    header(ws, r, ["이름","역할"]); 
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=8); r += 1
    for n, d in s["cast"]:
        put(ws, r, 1, n, f(True))
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=8)
        put(ws, r, 2, d)
        for c in range(3, 9): ws.cell(row=r, column=c).border = BORDER
        r += 1
    r += 1
    ws.cell(row=r, column=1, value="3부작 개요").font = f(True, 11, NAVY); r += 1
    header(ws, r, ["부","원제","한국어 제목","핵심 사건","핵심 비밀","해결과 결말","2·3부로 이어지는 실마리"])
    r += 1
    for k, p in enumerate(s["parts"], 1):
        put(ws, r, 1, p[0], f(True), PART_FILL[k], CENTER)
        put(ws, r, 2, p[1], f(True, 10, ACCENT), PART_FILL[k])
        put(ws, r, 3, p[2], f(True), PART_FILL[k])
        put(ws, r, 4, p[3], fl=PART_FILL[k]); put(ws, r, 5, p[4], fl=PART_FILL[k])
        put(ws, r, 6, p[5], fl=PART_FILL[k]); put(ws, r, 7, p[6], fl=PART_FILL[k])
        ws.row_dimensions[r].height = 95
        r += 1
    r += 1
    ws.cell(row=r, column=1, value="에피소드 36화").font = f(True, 11, NAVY); r += 1
    head_r = r
    header(ws, r, ["부","화","원어 제목","한국어 제목","협상 유형","줄거리","해법이 떠오르는 순간","역사 사례(논거)","사건(3부는 4사건×3화)"])
    r += 1
    for row_ in s["episodes"]:
        (pt, ep, orig, ko, typ, log, trig, hist, *rest) = row_
        case = rest[0] if rest else "—"
        fl = PART_FILL[pt]
        put(ws, r, 1, f"{pt}부", f(True), fl, CENTER); put(ws, r, 2, ep, f(True), fl, CENTER)
        put(ws, r, 3, orig, f(True, 10, ACCENT), fl); put(ws, r, 4, ko, f(True), fl)
        put(ws, r, 5, typ, fl=fl, al=CENTER)
        put(ws, r, 6, log); put(ws, r, 7, trig); put(ws, r, 8, hist); put(ws, r, 9, case, f(True), fl, CENTER)
        ws.row_dimensions[r].height = 62
        allrows.append((s["lang"], pt, ep, orig, ko, typ, log, trig, hist, case))
        r += 1
    ws.auto_filter.ref = f"A{head_r}:I{r-1}"
    widths(ws, [14,6,28,24,12,52,44,44,22])
    ws.freeze_panes = "A4"

# ---------- 종합 ----------
ws = wb.create_sheet("에피소드 종합")
title(ws, "에피소드 종합 (252화)", "필터로 언어·부·협상 유형·역사 사례를 걸러 볼 수 있음")
header(ws, 4, ["언어","부","화","원어 제목","한국어 제목","협상 유형","줄거리","해법이 떠오르는 순간","역사 사례(논거)","사건(3부)"])
for i, row in enumerate(allrows):
    r = 5 + i
    fl = PART_FILL[row[1]]
    for c, v in enumerate(row, 1):
        put(ws, r, c, (f"{v}부" if c == 2 else v), f(c in (3,4,5) and False), fl if c <= 6 else None,
            CENTER if c in (2,3,6,10) else WRAP)
    ws.row_dimensions[r].height = 58
ws.auto_filter.ref = f"A4:J{4+len(allrows)}"
ws.freeze_panes = "A5"
widths(ws, [22,6,6,28,24,12,52,44,44,22])

out = HERE / "외교관시리즈_7개국어_3부작_기획안.xlsx"
wb.save(out)
print(out, len(allrows))
