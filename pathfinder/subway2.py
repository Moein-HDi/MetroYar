from pathfinder.backend import SubwaySystem, Station, Stop

subway2 = SubwaySystem()

# Create station objects

a1 = Station('تجریش', ['l1'])
a2 = Station('قیطریه', ['l1'])
a3 = Station('شهید صدر', ['l1'])
a4 = Station('قلهک', ['l1'])
a5 = Station('دکتر شریعتی', ['l1'])
a6 = Station('میرداماد', ['l1'])
a7 = Station('شهید حقانی', ['l1'])
a8 = Station('شهید همت', ['l1'])
a9 = Station('مصلی امام خمینی', ['l1'])

a10 = Station('شهید بهشتی', [])
a10l1 = Station('شهید بهشتی1', ['l1'])
a10l3 = Station('شهید بهشتی2', ['l3'])

a11 = Station('شهید مفتح', ['l1'])
a12 = Station('شهدای هفت تیر', ['l1'])
a13 = Station('طالقانی', ['l1'])

a14 = Station('دروازه دولت', [])
a14l1 = Station('دروازه دولت1', ['l1'])
a14l4 = Station('دروازه دولت2', ['l4'])


a15 = Station('سعدی', ['l1'])

a16 = Station('امام خمینی', [])
a16l1 = Station('امام خمینی1', ['l1'])
a16l2 = Station('امام خمینی2', ['l2'])

a17 = Station('پانزده خرداد', ['l1'])
a18 = Station('خیام', ['l1'])

a19 = Station('میدان محمدیه', [])
a19l1 = Station('میدان محمدیه1', ['l1'])
a19l7 = Station('میدان محمدیه2', ['l7'])

a20 = Station('شوش', ['l1'])
a21 = Station('پایانه جنوب', ['l1'])
a22 = Station('شهید بخارائی', ['l1'])
a23 = Station('علی آباد', ['l1'])
a24 = Station('جوانمرد قصاب', ['l1'])
a25 = Station('شهرری', ['l1'])
a26 = Station('پالایشگاه', ['l1'])

a27 = Station('شاهد', ['l1', 'l1w'])
a27l1 = Station('شاهد1', ['l1'])
a27l1w = Station('شاهد2', ['l1w'])

a28 = Station('حرم مطهر امام خمینی', ['l1'])
a29 = Station('کهریزک', ['l1'])
#l1w
aw1 = Station('شهر آفتاب', ['l1w'])
aw2 = Station('فرودگاه امام خمینی', ['l1w'])
#l2
b1 = Station('تهران (صادقیه)', [])
b1l2 = Station('تهران (صادقیه)1', ['l2'])
b1l5 = Station('تهران (صادقیه)2', ['l5'])


b2 = Station('طرشت', ['l2'])
b3 = Station('دانشگاه شریف', ['l2'])

b4 = Station('شادمان', [])
b4l2 = Station('شادمان1', ['l2'])
b4l4 = Station('شادمان2', ['l4'])

b5 = Station('شهید نواب صفوی', [])
b5l2 = Station('شهید نواب صفوی1', ['l2'])
b5l7 = Station('شهید نواب صفوی2', ['l7'])


b6 = Station('میدان حر', ['l2'])
b7 = Station('دانشگاه امام علی', ['l2'])
b8 = Station('حسن آباد', ['l2'])
b9 = Station('ملت', ['l2'])
b10 = Station('بهارستان', ['l2'])

b11 = Station('دروازه شمیران', [])
b11l2 = Station('دروازه شمیران1', ['l2'])
b11l4 = Station('دروازه شمیران2', ['l4'])


b12 = Station('امام حسین', [])
b12l2 = Station('امام حسین1', ['l2'])
b12l6e = Station('امام حسین2', ['l6e'])


b13 = Station('شهید مدنی', ['l2'])
b14 = Station('سبلان', ['l2'])
b15 = Station('فدک', ['l2'])
b16 = Station('جانبازان', ['l2'])
b17 = Station('سرسبز', ['l2'])
b18 = Station('دانشگاه علم و صنعت', ['l2'])
b19 = Station('شهید باقری', ['l2'])
b20 = Station('تهرانپارس', ['l2'])
b21 = Station('فرهنگسرا', ['l2'])
#l3
c1 = Station('آزادگان', ['l3'])
c2 = Station('نعمت آباد', ['l3'])
c3 = Station('عبدل آباد', ['l3'])
c4 = Station('شهرک شریعتی', ['l3'])
c5 = Station('زمزم', ['l3'])
c6 = Station('جوادیه', ['l3'])
c7 = Station('راه آهن', ['l3'])

c8 = Station('مهدیه', [])
c8l3 = Station('مهدیه1', ['l3'])
c8l7 = Station('مهدیه2', ['l7'])

c9 = Station('منیریه', ['l3'])

c10 = Station('تئاتر شهر', [])
c10l3 = Station('تئاتر شهر1', ['l3'])
c10l4 = Station('تئاتر شهر2', ['l4'])

c11 = Station('میدان ولیعصر', ['l3'])
c12 = Station('میدان جهاد', ['l3'])
c13 = Station('میرزای شیرازی', ['l3'])
c14 = Station('سهروردی', ['l3'])
c15 = Station('شهید قدوسی', ['l3'])
c16 = Station('شهید صیاد شیرازی', ['l3'])
c17 = Station('خواجه عبدالله انصاری', ['l3'])
c18 = Station('شهید زین الدین', ['l3'])
c19 = Station('میدان هروی', ['l3'])
c20 = Station('حسین آباد', ['l3'])
c21 = Station('نوبنیاد', ['l3'])
c22 = Station('اقدسیه', ['l3'])
c23 = Station('شهید محلاتی', ['l3'])
c24 = Station('قائم', ['l3'])
#l4
d1 = Station('ارم سبز', [])
d1l4 = Station('ارم سبز1', ['l4'])
d1l5 = Station('ارم سبز2', ['l5'])

d2 = Station('شهرک اکباتان', ['l4'])

d3 = Station('بیمه', [])
d3l4 = Station('بیمه1', ['l4'])
d3l4s = Station('بیمه2', ['l4s'])

d4 = Station('میدان آزادی', ['l4'])
d5 = Station('استاد معین', ['l4'])
d6 = Station('دکتر حبیب اله', ['l4'])

d7 = Station('توحید', [])
d7l4 = Station('توحید1', ['l4'])
d7l7 = Station('توحید2', ['l7'])

d8 = Station('میدان انقلاب اسلامی', ['l4'])
d9 = Station('فردوسی', ['l4'])

d10 = Station('میدان شهدا', [])
d10l4 = Station('میدان شهدا1', ['l4'])
d10l6e = Station('میدان شهدا2', ['l6e'])

d11 = Station('ابن سینا', ['l4'])
d12 = Station('پیروزی', ['l4'])
d13 = Station('نبرد', ['l4'])
d14 = Station('نیروی هوایی', ['l4'])
d15 = Station('شهید کلاهدوز', ['l4'])
#l4s
ds1 = Station('پایانه 1و2 فرودگاه مهرآباد', ['l4s'])
ds2 = Station('پایانه 4و6 فرودگاه مهرآباد', ['l4s'])
#l5
e1 = Station('گلشهر', [])
e1l5 = Station('گلشهر1', ['l5'])
e1l5w = Station('گلشهر2', ['l5w'])

e2 = Station('محمدشهر', ['l5'])
e3 = Station('کرج', ['l5'])
e4 = Station('اتمسفر', ['l5'])
e5 = Station('گرمدره', ['l5'])
e6 = Station('وردآورد', ['l5'])
e7 = Station('ایران خودرو', ['l5'])
e8 = Station('چیتگر', ['l5'])
e9 = Station('ورزشگاه آزادی', ['l5'])
#l5w
ew1 = Station('شهید سپهبد سلیمانی', ['l5w'])
#l6e
fe1 = Station('امیرکبیر', ['l6e'])
fe2 = Station('شهید رضایی', ['l6e'])
fe3 = Station('بعثت', ['l6e'])
fe4 = Station('کیانشهر', ['l6e'])
fe5 = Station('دولت آباد', ['l6e'])
#l6w
fw1 = Station('شهید ستاری', ['l6w'])
fw2 = Station('شهید اشرفی اصفهانی', ['l6w'])
fw3 = Station('یادگار امام', ['l6w'])
fw4 = Station('مرزداران', ['l6w'])
fw5 = Station('شهرک آزمایش', ['l6w'])

fw6 = Station('دانشگاه تربیت مدرس', [])
fw6l6w = Station('دانشگاه تربیت مدرس1', ['l6w'])
fw6l7 = Station('دانشگاه تربیت مدرس2', ['l7'])

#l7
g1 = Station('میدان صنعت', ['l7'])
g2 = Station('برج میلاد', ['l7'])
g3 = Station('بوستان گفتگو', ['l7'])
g4 = Station('مدافعان سلامت', ['l7'])
g5 = Station('رودکی', ['l7'])
g6 = Station('کمیل', ['l7'])
g7 = Station('بریانک', ['l7'])
g8 = Station('هلال احمر', ['l7'])
g9 = Station('مولوی', ['l7'])
g10 = Station('میدان قیام', ['l7'])
g11 = Station('شهدای 17 شهریور', ['l7'])
g12 = Station('چهل تن دولاب', ['l7'])
g13 = Station('آهنگ', ['l7'])
g14 = Station('بسیج', ['l7'])


# Add stations to subway system
subway2.add_station(a1)
subway2.add_station(a2)
subway2.add_station(a3)
subway2.add_station(a4)
subway2.add_station(a5)
subway2.add_station(a6)
subway2.add_station(a7)
subway2.add_station(a8)
subway2.add_station(a9)
subway2.add_station(a10)
subway2.add_station(a11)
subway2.add_station(a12)
subway2.add_station(a13)
subway2.add_station(a14)
subway2.add_station(a15)
subway2.add_station(a16)
subway2.add_station(a17)
subway2.add_station(a18)
subway2.add_station(a19)
subway2.add_station(a20)
subway2.add_station(a21)
subway2.add_station(a22)
subway2.add_station(a23)
subway2.add_station(a24)
subway2.add_station(a25)
subway2.add_station(a26)
subway2.add_station(a27)
subway2.add_station(a28)
subway2.add_station(a29)
subway2.add_station(aw1)
subway2.add_station(aw2)
subway2.add_station(b1)
subway2.add_station(b2)
subway2.add_station(b3)
subway2.add_station(b4)
subway2.add_station(b5)
subway2.add_station(b6)
subway2.add_station(b7)
subway2.add_station(b8)
subway2.add_station(b9)
subway2.add_station(b10)
subway2.add_station(b11)
subway2.add_station(b12)
subway2.add_station(b13)
subway2.add_station(b14)
subway2.add_station(b15)
subway2.add_station(b16)
subway2.add_station(b17)
subway2.add_station(b18)
subway2.add_station(b19)
subway2.add_station(b20)
subway2.add_station(b21)
subway2.add_station(c1)
subway2.add_station(c2)
subway2.add_station(c3)
subway2.add_station(c4)
subway2.add_station(c5)
subway2.add_station(c6)
subway2.add_station(c7)
subway2.add_station(c8)
subway2.add_station(c9)
subway2.add_station(c10)
subway2.add_station(c11)
subway2.add_station(c12)
subway2.add_station(c13)
subway2.add_station(c14)
subway2.add_station(c15)
subway2.add_station(c16)
subway2.add_station(c17)
subway2.add_station(c18)
subway2.add_station(c19)
subway2.add_station(c20)
subway2.add_station(c21)
subway2.add_station(c22)
subway2.add_station(c23)
subway2.add_station(c24)
subway2.add_station(d1)
subway2.add_station(d2)
subway2.add_station(d3)
subway2.add_station(d4)
subway2.add_station(d5)
subway2.add_station(d6)
subway2.add_station(d7)
subway2.add_station(d8)
subway2.add_station(d9)
subway2.add_station(d10)
subway2.add_station(d11)
subway2.add_station(d12)
subway2.add_station(d13)
subway2.add_station(d14)
subway2.add_station(d15)
subway2.add_station(ds1)
subway2.add_station(ds2)
subway2.add_station(e1)
subway2.add_station(e2)
subway2.add_station(e3)
subway2.add_station(e4)
subway2.add_station(e5)
subway2.add_station(e6)
subway2.add_station(e7)
subway2.add_station(e8)
subway2.add_station(e9)
subway2.add_station(ew1)
subway2.add_station(fe1)
subway2.add_station(fe2)
subway2.add_station(fe3)
subway2.add_station(fe4)
subway2.add_station(fe5)
subway2.add_station(fw1)
subway2.add_station(fw2)
subway2.add_station(fw3)
subway2.add_station(fw4)
subway2.add_station(fw5)
subway2.add_station(fw6)
subway2.add_station(g1)
subway2.add_station(g2)
subway2.add_station(g3)
subway2.add_station(g4)
subway2.add_station(g5)
subway2.add_station(g6)
subway2.add_station(g7)
subway2.add_station(g8)
subway2.add_station(g9)
subway2.add_station(g10)
subway2.add_station(g11)
subway2.add_station(g12)
subway2.add_station(g13)
subway2.add_station(g14)


subway2.add_station(a10l1)
subway2.add_station(a10l3)
subway2.add_station(a14l1)
subway2.add_station(a14l4)
subway2.add_station(a19l1)
subway2.add_station(a19l7)
subway2.add_station(a27l1)
subway2.add_station(a27l1w)
subway2.add_station(a16l1)
subway2.add_station(a16l2)
subway2.add_station(b1l2)
subway2.add_station(b1l5)
subway2.add_station(b4l2)
subway2.add_station(b4l4)
subway2.add_station(b5l2)
subway2.add_station(b5l7)
subway2.add_station(b11l2)
subway2.add_station(b11l4)
subway2.add_station(b12l2)
subway2.add_station(b12l6e)
subway2.add_station(c8l3)
subway2.add_station(c8l7)
subway2.add_station(c10l3)
subway2.add_station(c10l4)
subway2.add_station(d1l4)
subway2.add_station(d1l5)
subway2.add_station(d3l4)
subway2.add_station(d3l4s)
subway2.add_station(d7l4)
subway2.add_station(d7l7)
subway2.add_station(d10l4)
subway2.add_station(d10l6e)
subway2.add_station(e1l5)
subway2.add_station(e1l5w)
subway2.add_station(fw6l6w)
subway2.add_station(fw6l7)






# Add connections between stations
subway2.add_connection(a1, a2, 2)
subway2.add_connection(a2, a3, 2)
subway2.add_connection(a3, a4, 2)
subway2.add_connection(a4, a5, 3)
subway2.add_connection(a5, a6, 2)
subway2.add_connection(a6, a7, 3)
subway2.add_connection(a7, a8, 2)
subway2.add_connection(a8, a9, 2)
subway2.add_connection(a9, a10l1, 2)
subway2.add_connection(a10l1, a11, 2)
subway2.add_connection(a11, a12, 2)
subway2.add_connection(a12, a13, 3)
subway2.add_connection(a13, a14l1, 2)
subway2.add_connection(a14l1, a15, 2)
subway2.add_connection(a15, a16l1, 2)
subway2.add_connection(a16l1, a17, 2)
subway2.add_connection(a17, a18, 2)
subway2.add_connection(a18, a19l1, 3)
subway2.add_connection(a19l1, a20, 2)
subway2.add_connection(a20, a21, 2)
subway2.add_connection(a21, a22, 2)
subway2.add_connection(a22, a23, 3)
subway2.add_connection(a23, a24, 2)
subway2.add_connection(a24, a25, 4)
subway2.add_connection(a25, a26, 5)
subway2.add_connection(a26, a27l1, 3)
subway2.add_connection(a27l1, a28, 3)
subway2.add_connection(a28, a29, 4)

subway2.add_connection(a27l1w, aw1, 7)
subway2.add_connection(aw1, aw2, 33)

subway2.add_connection(b1l2, b2, 2)
subway2.add_connection(b2, b3, 2)
subway2.add_connection(b3, b4l2, 2)
subway2.add_connection(b4l2, b5l2, 3)
subway2.add_connection(b5l2, b6, 3)
subway2.add_connection(b6, b7, 2)
subway2.add_connection(b7, b8, 3)
subway2.add_connection(b8, a16l2, 2)
subway2.add_connection(a16l2, b9, 3)
subway2.add_connection(b9, b10, 2)
subway2.add_connection(b10, b11l2, 2)
subway2.add_connection(b11l2, b12l2, 2)
subway2.add_connection(b12l2, b13, 3)
subway2.add_connection(b13, b14, 2)
subway2.add_connection(b14, b15, 2)
subway2.add_connection(b15, b16, 2)
subway2.add_connection(b16, b17, 3)
subway2.add_connection(b17, b18, 2)
subway2.add_connection(b18, b19, 2)
subway2.add_connection(b19, b20, 2)
subway2.add_connection(b20, b21, 2)
subway2.add_connection(c1, c2, 1)
subway2.add_connection(c2, c3, 2)
subway2.add_connection(c3, c4, 2)
subway2.add_connection(c4, c5, 2)
subway2.add_connection(c5, c6, 2)
subway2.add_connection(c6, c7, 2)
subway2.add_connection(c7, c8l3, 3)
subway2.add_connection(c8l3, c9, 2)
subway2.add_connection(c9, c10l3, 3)
subway2.add_connection(c10l3, c11, 4)
subway2.add_connection(c11, c12, 3)
subway2.add_connection(c12, c13, 3)
subway2.add_connection(c13, a10l3, 3)
subway2.add_connection(a10l3, c14, 2)
subway2.add_connection(c14, c15, 2)
subway2.add_connection(c15, c16, 2)
subway2.add_connection(c16, c17, 3)
subway2.add_connection(c17, c18, 3)
subway2.add_connection(c18, c19, 2)
subway2.add_connection(c19, c20, 2)
subway2.add_connection(c20, c21, 2)
subway2.add_connection(c21, c22, 2)
subway2.add_connection(c22, c23, 4)
subway2.add_connection(c23, c24, 5)
subway2.add_connection(d1l4, d2, 2)
subway2.add_connection(d2, d3l4, 3)
subway2.add_connection(d3l4, d4, 2)
subway2.add_connection(d4, d5, 2)
subway2.add_connection(d5, d6, 2)
subway2.add_connection(d6, b4l4, 3)
subway2.add_connection(b4l4, d7l4, 2)
subway2.add_connection(d7l4, d8, 2)
subway2.add_connection(d8, c10l4, 3)
subway2.add_connection(c10l4, d9, 3)
subway2.add_connection(d9, a14l4, 2)
subway2.add_connection(a14l4, b11l4, 3)
subway2.add_connection(b11l4, d10l4, 3)
subway2.add_connection(d10l4, d11, 2)
subway2.add_connection(d11, d12, 2)
subway2.add_connection(d12, d13, 2)
subway2.add_connection(d13, d14, 2)
subway2.add_connection(d14, d15, 2)
subway2.add_connection(d3l4s, ds1, 2)
subway2.add_connection(ds1, ds2, 2)
subway2.add_connection(e1l5, e2, 5)
subway2.add_connection(e2, e3, 6)
subway2.add_connection(e3, e4, 7)
subway2.add_connection(e4, e5, 4)
subway2.add_connection(e5, e6, 12)
subway2.add_connection(e6, e7, 6)
subway2.add_connection(e7, e8, 6)
subway2.add_connection(e8, e9, 5)
subway2.add_connection(e9, d1l5, 4)
subway2.add_connection(d1l5, b1l5, 6)

subway2.add_connection(ew1, e1l5w, 40)

subway2.add_connection(b12l6e, d10l6e, 2)
subway2.add_connection(d10l6e, fe1, 2)
subway2.add_connection(fe1, fe2, 4)
subway2.add_connection(fe2, fe3, 2)
subway2.add_connection(fe3, fe4, 3)
subway2.add_connection(fe4, fe5, 5)

subway2.add_connection(fw1, fw2, 1)
subway2.add_connection(fw2, fw3, 2)
subway2.add_connection(fw3, fw4, 2)
subway2.add_connection(fw4, fw5, 2)
subway2.add_connection(fw5, fw6l6w, 6)
subway2.add_connection(g1, g2, 2)
subway2.add_connection(g2, g3, 3)
subway2.add_connection(g3, fw6l7, 2)
subway2.add_connection(fw6l7, g4, 3)
subway2.add_connection(g4, d7l7, 2)
subway2.add_connection(d7l7, b5l7, 2)
subway2.add_connection(b5l7, g5, 2)
subway2.add_connection(g5, g6, 2)
subway2.add_connection(g6, g7, 2)
subway2.add_connection(g7, g8, 2)
subway2.add_connection(g8, c8l7, 2)
subway2.add_connection(c8l7, a19l7, 3)
subway2.add_connection(a19l7, g9, 2)
subway2.add_connection(g9, g10, 2)
subway2.add_connection(g10, g11, 2)
subway2.add_connection(g11, g12, 3)
subway2.add_connection(g12, g13, 3)
subway2.add_connection(g13, g14, 3)



subway2.add_connection(a10, a10l1, 1000)
subway2.add_connection(a10, a10l3, 1000)
subway2.add_connection(a10l1, a10l3, 1000)

subway2.add_connection(a14, a14l1, 1000)
subway2.add_connection(a14, a14l4, 1000)
subway2.add_connection(a14l1, a14l4, 1000)

subway2.add_connection(a16, a16l1, 1000)
subway2.add_connection(a16, a16l2, 1000)
subway2.add_connection(a16l1, a16l2, 1000)

subway2.add_connection(a19, a19l1, 1000)
subway2.add_connection(a19, a19l7, 1000)
subway2.add_connection(a19l7, a19l1, 1000)

subway2.add_connection(a27, a27l1, 1000)
subway2.add_connection(a27, a27l1w, 1000)
subway2.add_connection(a27l1, a27l1w, 1000)

subway2.add_connection(b1, b1l2, 1000)
subway2.add_connection(b1, b1l5, 1000)
subway2.add_connection(b1l2, b1l5, 1000)

subway2.add_connection(b4, b4l2, 1000)
subway2.add_connection(b4, b4l4, 1000)
subway2.add_connection(b4l2, b4l4, 1000)

subway2.add_connection(b5, b5l2, 1000)
subway2.add_connection(b5, b5l7, 1000)
subway2.add_connection(b5l2, b5l7, 1000)

subway2.add_connection(b11, b11l2, 1000)
subway2.add_connection(b11, b11l4, 1000)
subway2.add_connection(b11l2, b11l4, 1000)

subway2.add_connection(b12, b12l2, 1000)
subway2.add_connection(b12, b12l6e, 1000)
subway2.add_connection(b12l2, b12l6e, 1000)

subway2.add_connection(c8, c8l3, 1000)
subway2.add_connection(c8, c8l7, 1000)
subway2.add_connection(c8l3, c8l7, 1000)

subway2.add_connection(c10, c10l3, 1000)
subway2.add_connection(c10, c10l4, 1000)
subway2.add_connection(c10l3, c10l4, 1000)

subway2.add_connection(d1, d1l4, 1000)
subway2.add_connection(d1, d1l5, 1000)
subway2.add_connection(d1l4, d1l5, 1000)

subway2.add_connection(d3, d3l4, 1000)
subway2.add_connection(d3, d3l4s, 1000)
subway2.add_connection(d3l4, d3l4s, 1000)

subway2.add_connection(d7, d7l4, 1000)
subway2.add_connection(d7, d7l7, 1000)
subway2.add_connection(d7l4, d7l7, 1000)

subway2.add_connection(d10, d10l4, 1000)
subway2.add_connection(d10, d10l6e, 1000)
subway2.add_connection(d10l4, d10l6e, 1000)

subway2.add_connection(e1, e1l5, 1000)
subway2.add_connection(e1, e1l5w, 1000)
subway2.add_connection(e1l5, e1l5w, 1000)

subway2.add_connection(fw6, fw6l6w, 1000)
subway2.add_connection(fw6, fw6l7, 1000)
subway2.add_connection(fw6l6w, fw6l7, 1000)


def calculate(origin, destination):
        fpath, cost = subway2.shortest_path(str(origin), str(destination))

        list1 = []
        lines = []
        for station in fpath:
            if station.name[-1] == '1' or station.name[-1] == '2':
                station.name = station.name[:-1]
                list1.append(station)
            else:
                list1.append(station)
            
        for index, station in enumerate(list1):
            if index == 0 and list1[0].name != list1[1].name:
                lines.append(list1[index+1].lines[0])
            elif index < len(list1)-2 and list1[index].name == list1[index+1].name:
                lines.append(list1[index+1].lines[0])
                cost -= 1000
                cost += 8
        

        if list1[0].name == list1[1].name:
            list1.pop(0)
        if list1[-1-1].name == list1[-1].name:
            list1.pop(-1)
            cost -= 1000
            cost += 8

        stops = []

        for station in list1:
            stops.append(Stop(station.name, station.lines[0]))
        return (stops, lines, cost)


















