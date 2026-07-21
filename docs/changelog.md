# Changelog — Atlas del Mercado Eléctrico Mayorista

## v2026Q3.5 (21 de julio de 2026) — Sec VII: spectrum por sector

### Cambio de paradigma en sección VII
La sección "Posiciones regulatorias" abandona el formato de cards de texto (que resultaba en 26 bloques pesados, ~3.000 palabras visibles) y adopta un **spectrum chart**: cada tema se mapea en una línea horizontal donde los sectores se distribuyen según su postura agregada (stance 1-5).

### Datos
- **Scoreo manual de las 26 posiciones** en una escala 1-5 (conservador → reformista), con criterio explícito:
  - 1 = defiende el status quo (verde bull)
  - 2 = acepta con ajustes (verde soft)
  - 3 = neutral técnico (oro warn)
  - 4 = crítico, pide cambios (merc soft)
  - 5 = muy crítico, pide transformación (merc)
- Cada tema incluye un `eje` (label izquierdo) y `eje_der` (label derecho) que describen el espectro.
- Cada sector tiene `codigo` (3 letras para el chart) y `categoria` (reguladores / industria / academia / política) para habilitar el filtro.

### Visualización
- **Rail horizontal** con gradiente bull → warn → merc de fondo (opacidad 0.22) como pista visual del espectro.
- **Ticks sutiles** en las posiciones 1-5 (sin números, los labels de los extremos son suficientes).
- **Dots** centrados en el track, color interpolado según el stance. **12px de diámetro** con borde 1.5px y sombra.
- **Clusters apilados**: cuando 2+ sectores comparten el mismo stance, los dots se apilan verticalmente centrados en el track (offset 10px). Los labels se apilan 13px abajo.
- **Labels en JetBrains Mono** con el código del sector (MIN, CNE, CEN, USM, UCh, etc.).
- **Consenso σ (desviación estándar)** calculado en vivo para cada tema y mostrado en el header:
  - σ < 0.6 → "Consenso amplio" (bull)
  - σ 0.6-1.0 → "Acuerdo moderado" (warn)
  - σ 1.0-1.4 → "Discrepancia" (warn)
  - σ > 1.4 → "Polarización" (merc)
- **Click sobre un dot o label** abre la cita completa en un panel con border-left merc, fondo paper-2, nombre del sector, rol, cita textual, fuente.

### Filtros
- Barra de filtros arriba del primer spectrum: **Todos / Reguladores / Industria / Academia / Política**.
- Cuando se activa un filtro, los dots y labels que NO coinciden con la categoría se atenúan (opacity 0.18 / 0.32) sin desaparecer — el usuario sigue viendo el contexto completo pero con foco en la categoría seleccionada.

### Estructura del cambio
- **Eliminado**: ~95 líneas de CSS para `.pos-tema`, `.pos-tema-hd`, `.pos-grid`, `.pos-card`, `.pos-sector`, `.pos-rol`, `.pos-text`, `.pos-fuente`.
- **Eliminado**: función `drawPosiciones()` con render de cards (reemplazada por spectrum).
- **Agregado**: ~140 líneas de CSS para spectrum (rail, dots, labels, filtros, quote panel).
- **Agregado**: `STANCE_COLOR_SCALE` con interpolación d3 entre bull/warn/merc.
- **JSON**: agregados campos `eje`, `eje_der`, `stance` a las posiciones; agregados `codigo` y `categoria` a los sectores.

### Lo que el lector ve ahora
- Antes: 26 cards de texto, ~30 segundos de lectura pesada, ningún patrón visual.
- Ahora: 5 spectrums compactos (~120px cada uno), patrón visual inmediato (clusters de consenso, outliers de polarización, gradiente de stance), cita expandible bajo demanda. Lectura de patrones en 10 segundos, lectura profunda solo si hace click.

### Hallazgos del scoring
- T1 (Plan de Expansión): σ=1.16, **bimodal** — 3 reguladores vs 3 industria/academia + 1 oposición.
- T2 (Integración vertical): σ=1.12, **gradiente parejo** — los 4 sectores se distribuyen sin clusters.
- T3 (Umbral clientes libres): σ=1.37, **bimodal** — 3 pro-ampliación vs 2 pro-regulación.
- T4 (Hidroelectricidad): σ=0.89, **acuerdo moderado** — el más consensuado de los 5.
- T5 (Concentración): σ=1.12, **gradiente parejo** — 4 sectores escalonados.

---

## v2026Q3.4 (21 de julio de 2026) — Bug fixes · etiquetas y datos

### Bug crítico en JSON de VATT
- **Causa raíz**: en `data/ingreso_tarifario_vatt.json`, el registro de Engie Transmission tenía la llave mal escrita como `participacion_vct_pct` (VCT en vez de VATT). El código lee `participacion_vatt_pct`, por lo que el valor llegaba como `undefined` → `x(undefined) = NaN` → la barra y la etiqueta de Engie quedaban invisibles en el chart FIG. 9. SVG no lanza excepción con NaN en atributos — los elementos simplemente no se renderizan, así que pasaba desapercibido en la vista rápida.
- **Fix**: corregida la llave a `participacion_vatt_pct` con valor 8.
- **Verificación**: inspección DOM de los 14 charts con `getAttribute('width')` y `getAttribute('x')` confirmó cero NaN después del fix. Engie Transmission ahora aparece con su barra gris de 8%.

### Etiqueta solapada en FIG. 7 (Precio final)
- **Causa raíz**: la etiqueta grande "$120" en Fraunces 44px ocupaba desde y≈70 hasta y=100, pero la etiqueta pequeña "USD / MWh" en JetBrains Mono 9px estaba en y=82 — literalmente dentro del bounding box del número grande. Resultado: la unidad se renderizaba superpuesta en la mitad superior del valor.
- **Fix**: eliminada la etiqueta "USD / MWh" sobre las barras. Era redundante: el eje Y ya muestra `$0, $50, $100, $150` y el símbolo `$` deja implícita la unidad. La cifra grande de cada barra mantiene la prominencia editorial sin ruido visual.
- **Limpieza adicional**: removidos los `console.log` de debug que había dejado en `drawCliente()` para investigar el bug.

### Verificación de los 14 charts
- Inspección DOM confirma `ALL CLEAN`: cero atributos NaN en los 14 charts. El bug de Engie explica los `<rect width="NaN">` y `<text x="NaN">` que aparecían en consola y que el navegador silenciosamente descartaba.

---

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
- **D3.js** se carga sin `defer` (síncrono) desde `d3js.org`. Inicialmente se había puesto `defer` para no bloquear el render, pero rompía los charts porque el código inline del dashboard corre antes que d3. Sin `defer` el script bloquea ~50ms pero garantiza el orden correcto de carga.

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
