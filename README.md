# Atlas del Mercado Eléctrico Mayorista — Chile

Dashboard de seguimiento sobre el mercado eléctrico mayorista chileno: composición, transmisión, competencia y regulación. Datos públicos primarios.

## Contenido

- **Dashboard principal** (`index.html`): visualizaciones D3.js sobre composición de la matriz, costos marginales, sistema de transmisión, plan de expansión, concentración de mercado, posiciones regulatorias. Diseño editorial "edición impresa" sobre fondo crema con tipografía Fraunces / Inter / JetBrains Mono, paleta de rojo mercantil, verde bosque, oro viejo y púrpura. Numeración romana I–VIII para secciones, folio rotado en margen, pull-quotes, case studies y filtros interactivos en 3 charts (Capacidad, Generación y CMg mensual).
- **Estudio técnico** (`docs/estudio_mercado_2026Q3.md`): análisis escrito de ~7.000 palabras con marco regulatorio, composición, transmisión, concentración, plan de expansión, posiciones regulatorias.
- **Plan de actualización** (`docs/plan_actualizacion.md`): cadencia por fuente con tiempos estimados.
- **Metodología de posiciones** (`docs/metodologia_posiciones.md`): protocolo de panoramas por sector institucional.

## Estructura

```
Atlas_Mercado_Electrico/
├── index.html                                  # Dashboard editorial (14 charts D3.js)
├── favicon.svg                                 # Rayo estilizado · rojo mercantil
├── og-preview.png                              # Preview 1200×630 para redes sociales
├── data/                                       # 9 JSON con datos primarios
│   ├── capacidad_instalada.json
│   ├── generacion_real.json
│   ├── costos_marginales.json
│   ├── plan_expansion_transmision.json
│   ├── concentracion_mercado.json
│   ├── ingreso_tarifario_vatt.json
│   ├── precio_nudo_promedio.json
│   ├── posiciones_mercado.json
│   └── indicador_competencia.json
├── docs/
│   ├── estudio_mercado_2026Q3.md
│   ├── plan_actualizacion.md
│   ├── metodologia_posiciones.md
│   └── changelog.md
├── src/
│   └── build_og_preview.py                     # Generador del OG preview con PIL
├── assets/                                     # Reservado para futuras imágenes
└── README.md
```

## Datos y fuentes

Todos los datos provienen de fuentes públicas primarias:

- **CEN** (Coordinador Eléctrico Nacional): informes mensuales, balances anuales, Informe de Monitoreo de la Competencia
- **CNE** (Comisión Nacional de Energía): fijación de precios de nudo, valorización VATT, informes técnicos del Plan de Expansión
- **Ministerio de Energía**: Decretos de Expansión, resoluciones tarifarias
- **SEC** (Superintendencia de Electricidad y Combustibles): fiscalización
- **TDLC** (Tribunal de Defensa de la Libre Competencia): fallos sobre libre competencia
- **FNE** (Fiscalía Nacional Económica): informes de mercado
- **Universidad de Chile / USM** (AC3E, Centro de Energía): estudios técnicos
- **ACERA** (Asociación Chilena de Energías Renovables y Almacenamiento): balances anuales
- **Generadoras de Chile**: boletines mensuales
- **GIE** (Generadoras Independientes): reportes mensuales
- **Energía Abierta** (CNE): datos horarios
- **BCN** (Biblioteca del Congreso Nacional): normativa

## Indicador de Competencia del Mercado Eléctrico (ICME)

Score compuesto 0-100 que mide la competencia efectiva del mercado chileno. A mayor valor, mayor competencia. Cinco sub-indicadores:

- HHI de capacidad instalada (peso 25%)
- HHI del segmento BESS (peso 15%)
- Concentración de transmisión (peso 20%)
- Razón Precio de Nudo / Costo Marginal (peso 20%)
- Diversidad de actores en el Plan de Expansión (peso 20%)

Interpretación:
- 0-25: Mercado muy concentrado - alerta regulatoria
- 25-50: Concentración moderada - requiere vigilancia
- 50-75: Competencia razonable - segmento con focos de atención
- 75-100: Mercado desconcentrado - competencia funcional

## Actualización

- **Mensual**: actualización de los JSON con datos del CEN, CNE, GIE.
- **Trimestral**: reescritura del estudio técnico.
- **Por evento**: cuando hay un decreto de expansión, fallo del TDLC, o reforma regulatoria.
- **Anual**: revisión estructural completa (cambio de versión).

Para detalles del plan, ver `docs/plan_actualizacion.md`.

## Despliegue

El dashboard es 100% HTML estático + JSON. Se puede desplegar en cualquier servidor web o hosting estático. No requiere backend.

Para uso local: abrir `index.html` en un navegador moderno (o servir con `python -m http.server` desde el directorio raíz).

## Licencia y uso

El proyecto es de uso público. Los datos son públicos; los análisis son del autor. Se permite la reutilización con atribución.

## Contacto

Miguel Ortiz C.
- LinkedIn: https://linkedin.com/in/mortizcoilla
- Email: mortizcoilla@gmail.com
- WhatsApp: https://wa.me/56933293943
- Portafolio: https://mortizcoilla.vercel.app/

---

*Versión actual: v2026Q3.4 — Lanzamiento 21 de julio de 2026.*
