import io
INS = []
def add(f, anchor, turns, notes):
    INS.append((f, anchor, turns, notes))

# ---- EP1 : Estai 1995 ----
add("ep1_a.txt", "VALDÉS: Prefiero un precedente a veintidós familias en la tele.", [
"ÁLVARO: Hay otro precedente, señora secretaria. En mil novecientos noventa y cinco Canadá apresó al Estai, un arrastrero gallego, en aguas internacionales. ||| 다른 선례도 있습니다, 차관님. 1995년에 캐나다가 국제 해역에서 갈리시아 선적 트롤선 에스타이호를 나포했죠.",
"MARINA: Y España no resolvió aquello pagando lo que pedía Canadá. Lo resolvió Bruselas, con un acuerdo entre la Unión Europea y Canadá. Había observadores a bordo, y el barco volvió a Vigo. ||| 그리고 스페인은 캐나다가 요구한 걸 내서 해결하지 않았어요. 브뤼셀이 해결했죠. 유럽연합과 캐나다 사이의 합의로요. 배에 관측원이 승선했고, 배는 비고로 돌아왔어요.",
"GASPAR: Fue otro océano y otro país. Entonces teníamos una ministra... un ministro con mucha presencia en los medios. ||| 다른 바다, 다른 나라였어요. 그때는 언론에 존재감이 큰 장관이 있었죠.",
"ÁLVARO: Cambia el país, no la lección: un apresamiento se resuelve cambiando el marco, no pagando la factura. Cuando uno paga la factura, acepta que la factura era justa. ||| 나라는 바뀌어도 교훈은 같습니다. 나포는 청구서를 내서가 아니라 틀을 바꿔서 풀리죠. 청구서를 내면 그 청구서가 정당했다고 인정하는 게 됩니다.",
], [
"+ crisis del Estai (1995) = 캐나다가 갈리시아 선적 트롤선 Estai를 국제 해역에서 나포한 사건. 스페인 단독이 아니라 EU–캐나다 합의(관측원 승선 등)로 풀렸다. 이 화의 해법 방향(청구서가 아니라 틀을 바꾼다)의 역사적 논거",
"+ cambiar el marco = 틀을 바꾸다. 협상에서 '쟁점이 놓인 구조'를 바꾼다는 뜻의 핵심 표현",
])
# fix a line that said 'una ministra... un ministro' (keep natural)
# ---- EP2 : Tordesillas ----
add("ep2_b.txt", "AMINATA: Se lo cuento porque usted preguntó por un mapa", [
"IBRAHIMA: Permítame una nota de historiador. En mil cuatrocientos noventa y cuatro, Castilla y Portugal se disputaban el océano. No hubo guerra. Hubo el Tratado de Tordesillas: una línea trazada sobre un mapa. ||| 역사학자로서 한마디 하겠습니다. 1494년에 카스티야와 포르투갈이 대양을 두고 다퉜습니다. 전쟁은 없었죠. 토르데시야스 조약이 있었습니다. 지도 위에 그은 선 하나였죠.",
"ÁLVARO: Trescientas setenta leguas al oeste de las islas de Cabo Verde. Lo estudié en el instituto. ||| 카보베르데 제도에서 서쪽으로 370레구아. 고등학교 때 배웠습니다.",
"IBRAHIMA: Lo que no le enseñaron es que la línea del Papa estaba mucho más cerca, a cien leguas. Portugal pidió moverla y se movió. Dos reinos resolvieron un problema enorme moviendo una línea, no ganando una batalla. ||| 가르쳐 주지 않은 건, 교황의 선이 훨씬 가까운 100레구아에 있었다는 겁니다. 포르투갈이 옮겨 달라고 했고 옮겨졌죠. 두 왕국은 거대한 문제를 전투에서 이겨서가 아니라 선을 옮겨서 풀었습니다.",
"AMINATA: Mi marido cree que todos los conflictos se arreglan con una línea. ||| 제 남편은 모든 갈등이 선 하나로 풀린다고 믿어요.",
"ÁLVARO: Quizá no todos. Pero el mapa de zonas de Kandara cambió de nombre hace tres meses. ||| 전부는 아닐지도요. 하지만 칸다라의 해역 지도는 석 달 전에 이름이 바뀌었습니다.",
"IBRAHIMA: Entonces quien movió esa línea quería hablar de otra cosa. Siempre se mueve una línea para hablar de otra cosa. ||| 그렇다면 그 선을 옮긴 사람은 다른 얘기를 하고 싶었던 겁니다. 선은 늘 다른 얘기를 하려고 옮기는 법이죠.",
], [
"+ Tratado de Tordesillas (1494) = 카스티야와 포르투갈이 대서양 분할선을 교황 칙서의 100레구아에서 서쪽 370레구아로 옮겨 합의한 조약. '선(지도)을 옮겨 문제를 푼다'는 선례",
"+ leguas = 레구아(옛 거리 단위, 약 5.5km). 'trescientas setenta leguas'는 370레구아",
])
# ---- EP3 : Simancas / Fontainebleau ----
add("ep3_b.txt", "EVARISTO: Todo lo que sale de aquí deja un hueco en el libro de préstamos", [
"MARINA: ¿Esa regla es de este archivo o de todos? ||| 그 규칙은 이 문서고만의 것인가요, 모든 문서고의 것인가요?",
"EVARISTO: De todos los buenos. Simancas, que fundó Carlos Quinto en mil quinientos cuarenta, ya lo sabía. Un Estado que no archiva no recuerda. Y uno que archiva mal recuerda solo lo que le conviene. ||| 좋은 문서고라면 다 그렇소. 1540년에 카를 5세가 세운 시만카스는 이미 알고 있었지. 기록하지 않는 국가는 기억하지 못하고, 잘못 기록하는 국가는 자기에게 유리한 것만 기억하오.",
"ÁLVARO: Y los secretos acaban saliendo. ||| 그리고 비밀은 결국 새어 나오죠.",
"EVARISTO: Siempre. Fontainebleau, mil ochocientos siete. Godoy firmó con Napoleón el reparto de Portugal, con cláusulas secretas. Se comentaba en las tabernas antes que en las Cortes. Seis meses después, el motín de Aranjuez. Y luego, la guerra. ||| 늘 그렇소. 1807년 퐁텐블로. 고도이가 나폴레옹과 포르투갈 분할을 비밀 조항과 함께 서명했지. 의회보다 술집에서 먼저 얘기가 돌았소. 몇 달 뒤 아랑후에스 폭동이 났고, 그 뒤엔 전쟁이었지.",
"ÁLVARO: ¿Dice que un papel secreto derribó un reino? ||| 비밀 문서 하나가 왕국을 무너뜨렸다고 하시는 겁니까?",
"EVARISTO: Digo que ningún secreto de Estado ha vivido más que el papel que lo sostiene. Lo único que se decide es quién lo cuenta primero. ||| 어떤 국가 기밀도 그것을 지탱하는 종이보다 오래 살지 못했다는 말이오. 결정할 수 있는 건 누가 먼저 말하느냐뿐이지.",
], [
"+ Archivo de Simancas = 스페인 최초의 국가 문서고. 카를 5세가 1540년 설립. 기록과 국가 기억의 관계를 보여 주는 상징",
"+ Tratado de Fontainebleau (1807) = 고도이가 나폴레옹과 맺은 포르투갈 분할 조약. 비밀 조항이 알려지며 아랑후에스 폭동(1808)과 독립전쟁으로 이어졌다. '비밀 문서의 파괴력'을 보여 주는 역사 사례",
"+ las Cortes = 스페인 의회. 역사적으로는 신분제 의회를 가리킨다",
])
# ---- EP4 : La Malinche ----
add("ep4_a.txt", "FERMÍN: Todavía no lo sé. Llevo veintiocho años intentando averiguarlo.", [
"MARINA: Los intérpretes siempre cargan con la culpa. ||| 통역관은 늘 책임을 떠안죠.",
"FERMÍN: Pregúntele a la Malinche. Sin ella, Cortés no habría podido decir ni buenos días en Tenochtitlan. Quinientos años después la sigue cargando la palabra «traidora». Nadie pregunta qué le dejaron decir. ||| 말린체에게 물어보시오. 그녀가 없었다면 코르테스는 테노치티틀란에서 인사 한마디 못 했을 거요. 500년이 지난 지금도 '배신자'라는 말이 그녀를 짓누르지. 그녀가 뭘 말하도록 허락받았는지는 아무도 묻지 않소.",
"ÁLVARO: Una intérprete que traducía bajo las órdenes de otros. ||| 남의 지시 아래서 통역한 사람이군요.",
"FERMÍN: Como yo. La historia no perdona a quien traduce, y olvida a quien dicta. ||| 나처럼. 역사는 통역한 사람은 용서하지 않고, 불러 준 사람은 잊어버리오.",
], [
"+ La Malinche = 코르테스의 통역관이자 협력자. 오랫동안 '배신자'로 불렸으나, 통역자가 지시자의 책임까지 떠안는 구조를 보여 주는 역사 사례",
"+ la historia no perdona a quien traduce y olvida a quien dicta = 'a quien + 직설법' 구문. 지시자와 통역자의 책임 불균형을 압축한 문장",
])
# ---- EP5 : Estai + Isla de los Faisanes ----
add("ep5_b.txt", "BASTIEN: Eso protege mis barcos.", [
"CATARINA: ¿Existe algún precedente de algo así? Preferiría no ser la primera en apoyar una idea sin historia. ||| 이런 선례가 있습니까? 역사 없는 아이디어를 제일 먼저 지지하는 사람이 되고 싶진 않네요.",
"ÁLVARO: Hay dos. El primero lo conocen bien: la crisis del Estai, en mil novecientos noventa y cinco. Canadá apresó un arrastrero gallego. España sola no consiguió nada. Cuando negoció Bruselas, se firmó un acuerdo con observadores a bordo y el barco volvió a Vigo. ||| 두 가지가 있습니다. 첫째는 잘 아시는 1995년 에스타이 사태입니다. 캐나다가 갈리시아 트롤선을 나포했죠. 스페인 혼자서는 아무것도 얻지 못했습니다. 브뤼셀이 협상하자 관측원 승선 합의가 나왔고 배는 비고로 돌아왔어요.",
"ELISE: Es cierto. De aquel caso salió la idea de que Europa negocia por sus barcos. ||| 맞아요. 그 사건에서 유럽이 자국 선박을 위해 협상한다는 생각이 나왔죠.",
"BASTIEN: Y yo le doy el segundo, aunque me cueste. En mil seiscientos cincuenta y nueve, Francia y España firmamos la paz de los Pirineos en una isla del Bidasoa, la isla de los Faisanes. Desde entonces la gobernamos entre los dos: seis meses cada uno. ||| 둘째는 제가 드리죠, 내키지 않지만. 1659년에 프랑스와 스페인은 비다소아강의 섬, 꿩의 섬에서 피레네 평화조약을 맺었습니다. 그 뒤로 우리 둘이 그 섬을 6개월씩 번갈아 통치하죠.",
"ÁLVARO: Una cogestión de casi cuatro siglos. ||| 거의 4세기 된 공동 관리군요.",
"BASTIEN: Si dos países de carácter tan difícil gestionan una isla desde hace casi cuatrocientos años, quizá se pueda cogestionar una cuenta. ||| 성격이 그렇게 까다로운 두 나라가 거의 400년 동안 섬 하나를 관리해 왔다면, 계좌 하나쯤은 공동 관리할 수 있겠죠.",
"ÁLVARO: Eso es lo más hermoso que me ha dicho un francés. ||| 프랑스 분이 제게 해 준 말 중 가장 아름답군요.",
"BASTIEN: No se acostumbre. ||| 익숙해지지 마세요.",
], [
"+ isla de los Faisanes = 비다소아강의 '꿩의 섬'. 1659년 피레네 조약이 체결된 곳으로, 지금도 스페인·프랑스가 6개월씩 번갈아 통치하는 공동 주권 섬이다. 공동 관리 계좌 아이디어의 역사적 논거",
"+ cogestión = 공동 관리. co- + gestión",
"+ no se acostumbre = 익숙해지지 마시오. 접속법 현재의 부정 명령(usted)",
])
# ---- EP6 : Vergara + pacto del olvido ----
add("ep6_a.txt", "BERNI: No es una trampa. Es una puerta.", [
"BERNI: Y no es una idea nueva. Mil ochocientos treinta y nueve. El Convenio de Vergara. Maroto, general carlista; Espartero, liberal. Siete años de guerra civil. ¿Cómo acabó? ||| 새로운 생각도 아니야. 1839년. 베르가라 협약. 카를로스파 장군 마로토와 자유주의자 에스파르테로. 7년간의 내전이었지. 어떻게 끝났나?",
"ÁLVARO: Con un abrazo. Delante de los dos ejércitos. ||| 포옹으로요. 두 군대 앞에서요.",
"BERNI: Con un abrazo y una cláusula: los oficiales carlistas que aceptaran la paz conservarían sus grados. Nadie perdió la cara. Quienes cedían lo hacían con dignidad. Esa es la puerta: no se trata de vencer, sino de que el otro pueda ceder sin que parezca que se rinde. ||| 포옹과 한 가지 조항으로요. 평화를 받아들이는 카를로스파 장교들은 계급을 유지한다는. 아무도 체면을 잃지 않았지. 양보하는 쪽이 존엄을 지키며 양보했어. 그게 문이야. 이기는 게 아니라 상대가 항복한 듯 보이지 않게 양보할 수 있게 해 주는 것.",
"ÁLVARO: Una salida con honor. ||| 명예로운 출구요.",
"BERNI: Con honor. Eso Valdés puede aceptarlo. Un castigo, no. ||| 명예로운. 그건 발데스가 받아들일 수 있어. 처벌은 못 받아들이지.",
], [
"+ Convenio de Vergara (1839) = 1차 카를로스 전쟁을 끝낸 협약. 마로토와 에스파르테로의 '베르가라의 포옹'. 카를로스파 장교들의 계급을 인정해 체면을 지키게 한 해법. 이 화의 '통제된 고백'이 가진 논리의 역사적 근거",
"+ no se trata de vencer, sino de que + 접속법 = 이기는 게 아니라 ~하게 하는 문제이다. 'no se trata de A, sino de B'",
])
add("ep6_b.txt", "VALDÉS: No. Para los míos, siempre seré la que firmó.", [
"ÁLVARO: España ya hizo una vez un pacto de silencio por razones de Estado. En la Transición. Se llamó el «pacto del olvido» y sirvió durante un tiempo para evitar otra guerra. Pero los pactos de silencio tienen fecha de caducidad. ||| 스페인은 국가 사유로 침묵의 협약을 한 번 맺은 적이 있습니다. 민주화 이행기에요. '망각의 협약'이라 불렸고 한동안 또 다른 전쟁을 막는 데 쓸모가 있었죠. 하지만 침묵의 협약에는 유통기한이 있습니다.",
"VALDÉS: No compares mi anexo con la Transición. ||| 내 부속서를 민주화 이행기와 비교하지 말게.",
"ÁLVARO: No lo comparo. Digo que el silencio que protege a un país unos años no protege a una persona veintiocho. Y cuando caduca, quien lo firmó no tiene a quién echarle la culpa. ||| 비교하는 게 아닙니다. 나라를 몇 년 지켜 준 침묵이 한 사람을 28년 지켜 주진 못한다는 말입니다. 그리고 유통기한이 지나면 서명한 사람은 탓할 곳이 없어요.",
], [
"+ pacto del olvido = '망각의 협약'. 스페인 민주화 이행기(Transición)에 과거 청산을 미룬 묵시적 합의를 가리키는 말. 침묵의 협약이 갖는 시한성을 논하는 비유로 쓰였다",
"+ fecha de caducidad = 유통기한, 만료일. 침묵의 효력에도 시한이 있다는 비유",
])
# ---- EP7 : Bernardino de Mendoza ----
add("ep7_b.txt", "REBECA: Es lo que puedo ofrecer. Soy espía, no monja.", [
"ÁLVARO: No me dices nada nuevo. Es un oficio sucio. ||| 새로운 얘긴 아니야. 더러운 직업이지.",
"REBECA: Es un oficio más viejo que tú y que yo. Bernardino de Mendoza, embajador de Felipe Segundo en Londres y luego en París, sobornaba cortesanos, pagaba espías y financiaba conspiraciones. El servicio exterior español nació sucio. ||| 너나 나보다 훨씬 오래된 직업이야. 펠리페 2세의 런던 대사였다가 파리 대사가 된 베르나르디노 데 멘도사는 궁정 신하를 매수하고 첩자를 사고 음모에 자금을 댔어. 스페인 외교는 더럽게 태어났지.",
"ÁLVARO: Y su información excelente no evitó el desastre de la Armada. ||| 그리고 훌륭한 정보도 무적함대의 참사를 막지 못했죠.",
"REBECA: Le faltó método para usarla. La información no gana batallas; las gana quien sabe qué quiere conseguir con ella. ||| 사용할 방법이 부족했지. 정보가 전투를 이기는 게 아니야. 정보로 무엇을 얻고 싶은지 아는 사람이 이기는 거지.",
"ÁLVARO: Por eso será un escudo, no una espada. ||| 그래서 방패이고 칼이 아닌 겁니다.",
], [
"+ Bernardino de Mendoza = 펠리페 2세의 런던·파리 주재 대사. 첩보망과 매수로 유명했으나 무적함대 원정(1588)은 실패했다. 스페인 외교의 '더러운 수단' 전통과 한계를 함께 보여 주는 인물",
"+ nació sucio = 더럽게 태어났다. 'nacer + 형용사'는 출발 상태를 말한다",
])
# ---- EP8 : Antonio Pérez ----
add("ep8_b.txt", "ÁLVARO: Es lo que tengo.", [
"PALOMA: No sería la primera vez que alguien filtra la mitad de un secreto. ||| 비밀의 절반만 유출하는 사람이 처음은 아닐 테죠.",
"ÁLVARO: Antonio Pérez. Secretario de Felipe Segundo. Huyó de España, publicó sus «Relaciones» con parte de los secretos del rey y calló la parte que lo comprometía a él. ||| 안토니오 페레스. 펠리페 2세의 비서관이었죠. 스페인을 탈출해 왕의 비밀 일부를 담은 『보고서(Relaciones)』를 펴냈고, 자신을 곤란하게 하는 부분은 침묵했습니다.",
"PALOMA: Y alimentó la Leyenda Negra. ||| 그리고 '검은 전설'을 키웠죠.",
"ÁLVARO: Una media verdad sirvió para fabricar una imagen de España que costó siglos corregir. Por eso le pido que espere: una verdad a medias hace daño mucho más tiempo que una mentira entera. ||| 반쪽 진실이 스페인에 대한 이미지를 만들어 냈고 그걸 바로잡는 데 수 세기가 걸렸습니다. 그래서 기다려 달라는 겁니다. 반쪽 진실은 완전한 거짓보다 훨씬 오래 해를 입히니까요.",
], [
"+ Antonio Pérez = 펠리페 2세의 비서관. 몰락 후 망명해 『Relaciones』를 출간하며 군주의 비밀 일부를 폭로, 이른바 '검은 전설(Leyenda Negra)' 형성에 영향을 줬다. '절반만 유출하는 자는 무엇을 감추는가'라는 이 화의 논점을 보여 주는 사례",
"+ Leyenda Negra = 스페인 제국에 대한 부정적 이미지(검은 전설). 선택적 정보로 형성된 이미지의 대표 사례",
])

for f, anchor, turns, notes in INS:
    lines = io.open(f, encoding="utf8").read().split("\n")
    idx = next((i for i, l in enumerate(lines) if l.startswith(anchor)), None)
    assert idx is not None, (f, anchor)
    lines[idx+1:idx+1] = turns + notes
    io.open(f, "w", encoding="utf8").write("\n".join(lines))
    print("ok", f, len(turns))
