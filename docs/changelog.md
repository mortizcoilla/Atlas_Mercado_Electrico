# Changelog — Atlas del Mercado Eléctrico Mayorista

## v2026Q3.3 (21 de julio de 2026) — Responsividad, favicon, metadatos y portafolio

### Responsividad mejorada
- **4 breakpoints** en lugar de 1: `1440px+`, `1100px`, `960px`, `768px`, `480px`. Cada uno ajusta tipografía, grid, padding y elementos decorativos.
- **Mobile (≤768px)**:
  - Hero h1: 36px en tablet → 30px en mobile chico
  - Subscores del ICME: 5 columnas → 2 columnas → 1 columna
  - El número "68" del ICME: 156px → 92px → 76px
  - Botones de filtro: layout flexible, "Mostrar todas" baja a línea completa
  - Tablas: padding reducido, font 12px
  - Folio rotado se oculta bajo 1100px (ya estaba)
- **Tablet (768–960px)**: grids de charts colapsan a 1 columna, sec-num de 78px a 56px
- **Print stylesheet** agregado: oculta folio, flechas y filtros, evita page-breaks dentro de figuras

### Favicon
- `favicon.svg` con un rayo eléctrico estilizado en rojo mercantil sobre fondo crema. Bordes negros redondeados. 64×64.
- Mismo SVG usado como `apple-touch-icon` y `mask-icon`.
- PNG de respaldo (`og-preview.png`) referenciado como `alternate icon` para navegadores legacy.

### Metadatos optimizados
- **Open Graph** completo: `og:type=article`, `og:title`, `og:description`, `og:locale=es_CL`, `og:site_name`, `og:url`, `og:image` (1200×630), `og:image:width/height/alt`, `og:image:secure_url`.
- **Twitter Card**: `summary_large_image` con título, descripción e imagen.
- **Article meta**: `article:published_time`, `article:modified_time`, `article:author`, `article:section=Energy`, `article:tag` para keywords.
- **Meta estándar**: `description` reescrito, `author`, `keywords`, `robots`, `language`, `theme-color=#f4ede0`, `color-scheme=light`, `format-detection=telephone=no`.
- **Canonical** link relativo `./`.
- **DNS prefetch** a `d3js.org` y `preconnect` a Google Fonts.
- **JSON-LD Article estructurado** con `@context=schema.org`, headline, author con sameAs (LinkedIn, WhatsApp), publisher, citation al CEN/CNE/MINENERGIA, inLanguage, about.
- **D3.js** ahora se carga con `defer` para no bloquear el render.

### Vínculo visible al portafolio
- **Callout editorial "Lecturas adicionales"** agregado antes del byline block: caja con border negro de 1px, border-left rojo mercantil de 4px, fondo paper-2. Texto serif italic invitando a explorar más proyectos. Botón con link a `mortizcoilla.vercel.app/` con flecha animada (mueve 4px al hover).
- **4to botón en el byline block**: "Portafolio" con icono SVG de link-externo, fondo tinta negra (más prominente que los otros 3). Hover cambia a rojo mercantil.
- **Vínculos totales al portafolio**: 5 en el documento (HTML body, JSON-LD author, JSON-LD publisher, og:image, callout y botón).

### Performance
- `og-preview.png` generado con PIL (90 KB, 1200×630) con diseño editorial coherente con el dashboard.
- `src/build_og_preview.py` incluido en el repo para regenerar el preview si cambia el diseño.

---

## v2026Q3.2 (21 de julio de 2026) — Limpieza editorial + interactividad

### Correcciones de revisión pública
- **Endnotes**: eliminado el bloque "Documentación interna" del endnotes. Solo se mantiene la lista de "Fuentes primarias" (CEN, CNE, Ministerio de Energía).
- **Masthead**: eliminada la fecha larga "Santiago de Chile, martes 21 de julio de 2026". El header ahora muestra solo `Atlas · Vol. III · № 03` y los metadatos de cierre de datos / próxima edición.
- **Colofón**: eliminados los links a `Estudio técnico · Metodología · Plan de actualización · Changelog`. Reemplazados por la línea sobria "Compilado y publicado en Chile".

### Gráficos
- **Nombres de ejes**: agregados axis titles en 11 charts que no los tenían. Estilo JetBrains Mono 9.5px uppercase con letter-spacing 0.18em (formato paper). Charts afectados: cap-evol, gen-evol, hhi-seg, hhi-evol, hhi-zona, top4, participacion, vatt, vatt-seg, plan-exp, pn-cmg, cmg-mensual, cliente.
- **HHI por zona geográfica**: arreglado el solapamiento entre el nombre de la zona y la etiqueta numérica. La etiqueta `35% / 72%` ahora se posiciona al final de la barra Top-3 (no a la izquierda del axis), con margen derecho ampliado a 60px para que no se salga del SVG. También se agregó eje X con label "% participación de mercado".
- **VATT segmento**: reposicionado el X axis arriba de la leyenda mini para que el label "% del VATT total del SEN" no se superponga con la leyenda de colores.

### Interactividad nueva
- **Botones de filtrado en 3 charts**:
  - `Capacidad instalada 2010–2025` (FIG. 1): botones para mostrar/ocultar cada capa (Térmica / Hidroeléctrica / Eólica / Solar) + botón "Mostrar todas".
  - `Generación real 2010–2025` (FIG. 4): misma lógica.
  - `CMg promedio mensual 2024–2025` (FIG. 5): botones para mostrar/ocultar cada barra (Crucero / Pan de Azúcar / Quillota / Puerto Montt).
- **Estilo de los botones**: paper-print con JetBrains Mono uppercase 9.5px, dot de color a la izquierda del nombre, estado `active` invierte a tinta negra sobre papel claro, estado `muted` atenúa la capa o línea a 8–12% de opacidad.
- **Reset**: cada grupo de filtros tiene un botón "Mostrar todas" alineado a la derecha que restaura todos los estados.
- **Animación**: las capas y líneas tienen `transition: opacity 0.18s` para que el feedback sea suave.

### Estilo
- Nuevas clases CSS: `.chart-filter`, `.chart-filter button`, `.axis-title`, `.axis-title-x`, `.layer.muted`, `.line-group.muted`.
- Los ejes Y ahora rotan su label 90° en sentido antihorario, anclados al medio del eje. Los ejes X se centran bajo el chart con anchor middle.

---

## v2026Q3.1 (21 de julio de 2026) — Rediseño visual editorial

### Cambios de imagen
- **Concepto visual nuevo**: "Edición impresa" sobre **fondo crema cálido** (`#f4ede0`) — opuesto directo al dark mode editorial del Atlas de Infraestructura Crítica. Ambos proyectos ahora se ven claramente distintos en la primera lectura.
- **Paleta editorial de acentos**: rojo mercantil `#a82e1f` (alertas, hechos negativos), verde bosque `#2c5f3f` (positivo, ERNC, desconcentración), oro viejo `#b08520` (advertencia, hidro/térmica), púrpura `#6b3b8a` (BESS, segmento crítico). Sin gradientes oscuros, sin glow, sin blur.
- **Tipografía editorial**: Fraunces en display con uso explícito de **italic variable** para acentos narrativos, Inter para cuerpo, JetBrains Mono para datos técnicos. Numeración romana (I–VIII) para secciones, reemplazando los 01–08 arábigos anteriores.
- **Membrete ICME en lugar de gauge**: bloque con número gigante serif (156px), drop-cap en la bajada, sub-scores en columnas con barras mini. Mucho más editorial que el ring técnico anterior.
- **Elementos nuevos**: folio rotado en margen ("ATLAS · MERCADO ELÉCTRICO · CHILE" / "v2026Q3 · EDICIÓN IMPRESA"), pull-quotes entre secciones, tabla de contenidos con paginación tipo paper, header de doble regla gruesa estilo tabloid, tabla comparativa con veredictos en caja tipográfica, dos case studies de Plan de Expansión con border-left rojo mercantil.
- **Eliminados por contraste con el otro Atlas**: sticky nav con scroll-spy, score ring con tick marks, tarjetas con border sutil, tooltips con backdrop-blur, paleta teal/ámbar/violeta. La sensación de "dashboard técnico" se reemplaza por la de "informe de mercado".

### Datos y estructura preservados
- Los 9 archivos JSON intactos, sin cambios de schema.
- Los 14 charts D3 preservados con los mismos IDs y la misma lógica de carga (`fetch('data/*.json')`).
- `docs/estudio_mercado_2026Q3.md`, `docs/metodologia_posiciones.md`, `docs/plan_actualizacion.md` y `README.md` sin cambios.
- Bloque de autor conserva la regla hard: solo nombre "Miguel Ortiz C." + 3 botones LinkedIn/Email/WhatsApp, sin títulos universitarios.

---

## v2026Q3 (21 de julio de 2026) — Lanzamiento

### Datos cargados
- `data/capacidad_instalada.json` — Capacidad por tecnología y empresa 2010-2025 (CEN Informe Monitoreo 2025)
- `data/generacion_real.json` — Generación anual 2010-2025 por tecnología (CEN Reporte Anual Art. 72-15)
- `data/costos_marginales.json` — CMg histórico por barra representativa 2017-2025 (CEN, GPM, CNE)
- `data/plan_expansion_transmision.json` — 9 planes anuales de expansión 2017-2025 con decretos, inversiones y obras (CNE, MINENERGIA)
- `data/concentracion_mercado.json` — HHI histórico y por segmento 2015-2025 (CEN Monitoreo, FNE, BCN)
- `data/ingreso_tarifario_vatt.json` — VATT por empresa transmisora, marco normativo (CNE 2024-2027, BCN)
- `data/precio_nudo_promedio.json` — Precio de Nudo regulado 2015-2025, comparación cliente libre vs regulado (CNE)
- `data/posiciones_mercado.json` — Panoramas por sector institucional sobre 5 temas clave
- `data/indicador_competencia.json` — ICME 2015-2025 con 5 sub-scores

### Dashboard
- `index.html` — Dashboard con 8 secciones técnicas + ICME gauge + 14 visualizaciones D3.js
- Navegación: 8 anclas a secciones
- Bloque de autor al pie con LinkedIn / Email / WhatsApp (sin títulos universitarios, regla hard)

### Estudio y documentación
- `docs/estudio_mercado_2026Q3.md` — Análisis técnico de ~7.000 palabras con 11 secciones
- `docs/plan_actualizacion.md` — Cadencia por fuente con tiempos estimados
- `docs/metodologia_posiciones.md` — Protocolo de panoramas por sector

### Próximas actualizaciones planeadas
- **v2026Q4 (octubre 2026)**: actualización mensual de JSON + recálculo ICME + revisión del estudio.
- **v2026 anual (enero 2027)**: cierre anual con datos CEN 2026 + balance ACERA + nueva valorización si corresponde.

---

*Mantenedor: Miguel Ortiz C. · Estructura del changelog inspirada en Keep a Changelog 1.1.0.*
