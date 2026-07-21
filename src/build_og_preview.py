"""Genera og-preview.png para Open Graph (1200x630) con layout limpio."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
PAPER = (244, 237, 224)
PAPER_2 = (251, 246, 234)
INK = (26, 23, 20)
INK_2 = (61, 56, 51)
INK_3 = (107, 99, 88)
RULE = (194, 181, 154)
MERC = (168, 46, 31)

img = Image.new('RGB', (W, H), PAPER)
d = ImageDraw.Draw(img)

def font(size):
    for c in [r'C:\Windows\Fonts\georgia.ttf',
              r'C:\Windows\times.ttf',
              r'C:\Windows\Fonts\arial.ttf']:
        if os.path.exists(c):
            try: return ImageFont.truetype(c, size)
            except: pass
    return ImageFont.load_default()

def font_i(size):
    for c in [r'C:\Windows\Fonts\georgiai.ttf',
              r'C:\Windows\Fonts\timesi.ttf']:
        if os.path.exists(c):
            try: return ImageFont.truetype(c, size)
            except: pass
    return font(size)

# ====== Tipografía ======
f_mono  = font(19)
f_h1    = font(64)        # headline línea 1 (sin italic)
f_hi    = font_i(64)      # italic
f_sub   = font(22)
f_stat  = font(108)       # 68
f_stat_u= font(32)        # /100
f_trend = font(20)
f_foot  = font(17)
f_by    = font(22)

# ====== TOP ======
d.rectangle([60, 60, W-60, 64], fill=INK)
d.rectangle([60, 70, W-60, 72], fill=RULE)
d.text((60, 90), 'ATLAS  ·  MERCADO ELÉCTRICO MAYORISTA  ·  CHILE', fill=MERC, font=f_mono)

# ====== HEADLINE (columna izquierda 60-820) ======
x_h = 60
y_h = 160
# L1: El mercado eléctrico que
d.text((x_h, y_h), 'El mercado eléctrico que', fill=INK, font=f_h1)
# L2: se transformó, y el cuello
w_so = d.textbbox((0, 0), 'se transformó', font=f_hi)
d.text((x_h, y_h + 76), 'se transformó', fill=MERC, font=f_hi)
d.text((x_h + (w_so[2] - w_so[0]) + 12, y_h + 76), ', y el cuello', fill=INK, font=f_h1)
# L3: de botella que viene.
d.text((x_h, y_h + 152), 'de botella que viene.', fill=INK, font=f_h1)

# ====== STAT ICME (columna derecha 880-1140) ======
x_s = 900
y_s = 160
# label
d.text((x_s, y_s - 4), 'ICME 2025', fill=MERC, font=f_mono)
# número 68
d.text((x_s, y_s + 14), '68', fill=INK, font=f_stat)
w68 = d.textbbox((0, 0), '68', font=f_stat)
d.text((x_s + (w68[2] - w68[0]) + 8, y_s + 96), '/100', fill=INK_3, font=f_stat_u)
# trend
d.text((x_s, y_s + 168), '−10 puntos desde 2023 (peak)', fill=INK_2, font=f_trend)
d.text((x_s, y_s + 198), 'alerta preventiva', fill=MERC, font=f_trend)
# mini bar
y_bar = y_s + 244
d.rectangle([x_s, y_bar, x_s + 200, y_bar + 4], fill=RULE)
d.rectangle([x_s, y_bar, x_s + 136, y_bar + 4], fill=MERC)  # 68% de 200

# ====== BAJADA (parte inferior, full width) ======
y_sub = 446
d.text((60, y_sub),       'SEN  ·  matriz eléctrica  ·  costos marginales  ·  transmisión', fill=INK_2, font=f_sub)
d.text((60, y_sub + 30),  'Plan de expansión  ·  concentración  ·  posiciones regulatorias', fill=INK_2, font=f_sub)

# ====== BOTTOM ======
d.rectangle([60, 540, W-60, 542], fill=RULE)
d.rectangle([60, 548, W-60, 552], fill=INK)
d.text((60, 568), 'Desarrollado por', fill=INK_3, font=f_foot)
d.text((60, 590), 'Miguel Ortiz C.', fill=INK, font=f_by)
d.text((W-300, 568), 'Portafolio', fill=INK_3, font=f_foot)
d.text((W-300, 590), 'mortizcoilla.vercel.app', fill=MERC, font=f_by)

img.save(r'C:\Workspace\Atlas_Mercado_Electrico\og-preview.png', 'PNG', optimize=True)
print('OK', os.path.getsize(r'C:\Workspace\Atlas_Mercado_Electrico\og-preview.png'), 'bytes')
