# Plan de actualización — Atlas del Mercado Eléctrico Mayorista

## Filosofía

El plan de actualización se construye **a mi criterio** según la disponibilidad real de información de las fuentes. No todas las fuentes tienen la misma cadencia, por lo que un plan mensual único no aplica. La estructura es por fuente, con su propia frecuencia de actualización.

## Fuentes primarias y cadencia

| Fuente | Qué entrega | Frecuencia | URL |
|---|---|---|---|
| **CEN — Informes Mensuales del SEN** | Capacidad instalada, generación, costos marginales, despacho, vertimiento | Mensual (~día 20 de cada mes) | coordinador.cl |
| **CEN — Reporte Anual de Desempeño (Art. 72-15)** | Balance anual completo del SEN | Anual (abril) | coordinador.cl |
| **CEN — Informe de Monitoreo de la Competencia** | HHI, concentración, posiciones dominantes | Anual (abril-mayo) | coordinador.cl |
| **CNE — Fijación de Precios de Nudo** | PN semestral (abril y octubre) | Semestral | cne.cl |
| **CNE — Informes de Valorización de Instalaciones de Transmisión** | VATT cada 4 años | Cada 4 años (próximo 2028) | cne.cl |
| **CNE — Informes técnicos de Plan de Expansión** | ITP e ITD anuales | Anual (octubre-noviembre) | cne.cl |
| **Ministerio de Energía — Decretos de Expansión** | Decretos fijando obras nuevas | Cuando se publican (~febrero-marzo) | energia.gob.cl |
| **SEC — Resoluciones y fiscalizaciones** | Sanciones, dictámenes | Cuando se publican | sec.cl |
| **TDLC — Fallos** | Sentencias sobre libre competencia | Cuando se publican | tdlc.cl |
| **FNE — Informes de mercado** | Estudios de competencia | Cuando se publican | fne.gob.cl |
| **ACERA — Balance anual** | Estado del sector ERNC | Anual (enero-febrero) | acera.cl |
| **Generadoras de Chile — Boletín mensual** | Datos operativos del SEN | Mensual | generadoras.cl |
| **GIE — Reporte mensual Systep** | Datos operativos SEN, PMGD | Mensual | gie.cl |
| **Universidad de Chile — Estudios post eventos** | Informes técnicos (ej. post-25F) | Cuando se publican | uchile.cl |

## Plan trimestral de actualización

### Julio 2026 (cierre 2026Q2)
- Actualizar todos los JSON con datos a junio 2026.
- Recalcular ICME con nuevo HHI y nuevos CMg.
- Revisión intermedia del estudio técnico si hay datos materiales nuevos.

### Octubre 2026 (cierre 2026Q3)
- Cierre trimestral completo.
- Estudio técnico reescrito (versión 2026Q3).
- Actualización de Plan de Expansión si se publicó Decreto del Plan 2025.

### Enero 2027 (cierre 2026 anual)
- Cierre anual completo.
- Estudio técnico reescrito (versión 2026 anual).
- Recálculo completo del ICME con datos del año completo.
- Nueva valorización VATT si corresponde (próximo ciclo 2028-2031).

### Abril 2027
- Recálculo con datos Q1.
- Si hay Informe de Monitoreo 2026 del CEN, se actualiza HHI.

## Por evento (no programado)

| Evento | Acción |
|---|---|
| Decreto de Plan de Expansión publicado | Actualizar plan_expansion_transmision.json |
| Fallo del TDLC relevante para el sector | Documentar en posiciones_mercado.json |
| Apagón o contingencia mayor | Crear ficha técnica en docs/contingencias/ |
| Reforma legal (nueva ley) | Documentar en marco normativo |
| Publicación de nuevo valor VATT | Actualizar ingreso_tarifario_vatt.json |
| Cambio en PN semestral | Actualizar precio_nudo_promedio.json |

## Estimación de tiempo por ciclo

| Componente | Frecuencia | Tiempo |
|---|---|---|
| Datos mensuales + JSON | Mensual | 1.5–2 horas |
| Recálculo ICME | Mensual | 30 minutos (automatizable) |
| Estudio técnico reescrito | Trimestral | 4–6 horas |
| Documentación de eventos | Por evento | 1–2 horas |

## Decisiones de diseño

1. **No se automatiza el scraping**: la complejidad de las fuentes chilenas (PDFs, formatos heterogéneos) hace que la extracción manual con verificación sea más confiable que un scraper automático. La verificación humana es clave para evitar errores de parsing que contaminen los datos.

2. **No se hace publicación automática**: el dashboard es HTML estático, lo que da control fino sobre qué se muestra y cuándo. La actualización es manual y deliberada.

3. **El ICME se recalcula manualmente en cada ciclo**: el cálculo es suficientemente simple para que un humano lo haga en 30 minutos, y la verificación humana es parte del valor del producto.

4. **El estudio técnico se reescribe completo en cada ciclo trimestral**: la cantidad de cambios es suficiente para que una reescritura completa sea más eficiente que una edición incremental.

5. **Las posiciones regulatorias se actualizan sólo cuando hay un hecho nuevo**: la mayoría de los sectores no cambian su posición trimestre a trimestre. Actualizar cuando hay una declaración relevante, un fallo, o un documento nuevo.

## Limitaciones declaradas

- El plan depende de la disponibilidad real de las fuentes. Si el CEN o la CNE no publican un informe esperado, se actualiza con los datos disponibles.
- Las fechas de publicación de informes no son siempre predecibles. El plan mensual se ajusta a la realidad.
- El cálculo del ICME es una métrica de autor. No es oficial ni normativo. Su valor está en la coherencia metodológica, no en la precisión absoluta.
- Las posiciones regulatorias son aproximaciones. Un sector puede tener posiciones internas diversas; el documento refleja la posición agregada pública.

## Indicador de actualización

El dashboard muestra en el header la fecha de última actualización y el cierre de datos. Esto es la primera señal de freshness para el lector.
