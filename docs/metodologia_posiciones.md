# Metodología de panoramas de posiciones regulatorias

## Propósito

Esta metodología documenta el procedimiento para construir los panoramas de posiciones regulatorias por sector institucional, sobre temas clave del mercado eléctrico chileno. El objetivo es producir un mapa equilibrado, verificable y sin editorial, de dónde está cada sector en temas estructuralmente disputados.

## Diferencia con declaraciones individuales

Este proyecto **no documenta declaraciones individuales de personajes políticos**. Eso se hace en el proyecto hermano Atlas de Infraestructura Crítica.

Aquí se documentan **posiciones agregadas de sectores institucionales**: Ministerio de Energía, CNE, CEN, SEC, Panel de Expertos, TDLC, FNE, academia (USM, U. de Chile), gremios (Generadoras de Chile, ACERA, GIE), y bloques políticos (oficialismo, oposición).

Una posición agregada se construye a partir de:
- Documentos oficiales del sector (resoluciones, oficios, sentencias).
- Declaraciones públicas de sus voceros autorizados.
- Papers académicos de centros asociados.
- Posiciones programáticas en el caso de bloques políticos.

## Estructura de cada panorama

Cada panorama tiene tres componentes:

1. **Identificación del sector**: nombre, rol institucional, mecanismo de toma de decisiones.
2. **Posición documentada**: cita textual cuando es posible, paráfrasis agregada cuando no. La posición se construye a partir de las fuentes públicas disponibles.
3. **Fuente verificable**: URL al documento original o a la cobertura periodística con cita confirmada.

## Criterios de selección de sectores

Los sectores se eligen por su relevancia estructural en el mercado eléctrico, no por su presencia mediática. Los sectores incluidos son:

- **Entes regulatorios y operadores**: Ministerio de Energía, CNE, CEN, SEC, Panel de Expertos, TDLC, FNE.
- **Academia**: USM (ingeniería eléctrica con foco en sistema), U. de Chile (ingeniería eléctrica con foco en regulación).
- **Gremios**: Generadoras de Chile (gremio de generadores grandes), ACERA (gremio de ERNC), GIE (gremio de pequeños y medianos).
- **Bloques políticos**: Oficialismo (gobierno actual), Oposición parlamentaria (los bloques con representación en el Congreso).

Se excluyen:
- Personas individuales (cubierto en el proyecto hermano).
- Medios de comunicación (cubierto como fuentes secundarias).
- Empresas individuales (cubierto dentro de los gremios).

## Criterios de selección de temas

Los temas se eligen por su relevancia estructural en el mercado:

1. **Plan de Expansión de Transmisión y su ejecución**: tema donde hay acuerdo sobre el problema y discrepancia sobre la solución.
2. **Integración vertical generación-transmisión**: tema técnico donde hay vigilancia regulatoria.
3. **Umbral de clientes libres**: tema donde hubo reforma reciente (RE 58/2024) y es relevante para la competencia.
4. **Hidroelectricidad y almacenamiento**: tema donde la transición tecnológica ha cambiado el rol de la hidro.
5. **Concentración y competencia**: tema transversal que cruza los anteriores.

Cada tema tiene entre 4 y 7 sectores con posición documentada.

## Estado de cada panorama

Cada tema incluye al final una **"lectura"** que sintetiza el panorama:

- **Acuerdo amplio**: todos los sectores están alineados. La política regulatoria debería reflejar el consenso.
- **Posiciones encontradas**: hay acuerdo sobre el problema pero discrepancia sobre la solución. La política regulatoria requiere arbitraje.
- **Mayoría vs minoría**: una posición predomina pero hay disidencia documentada. La política regulatoria puede avanzar pero debe considerar la disidencia.
- **Posiciones irreconciliables**: hay desacuerdo fundamental. La política regulatoria es inevitablemente política.

## Limitaciones declaradas

- Las posiciones agregadas son aproximaciones. Un sector puede tener posiciones internas diversas. El documento refleja la posición pública agregada.
- Las posiciones pueden evolucionar con el tiempo. La actualización se hace cuando hay un hecho nuevo (documento, declaración, fallo) que modifique materialmente la posición.
- El documento no pretende cerrar debates. Documenta dónde está cada sector para que el lector pueda formarse una visión propia.
- Las fuentes son públicas. Si una posición se basa en información no pública, se omite.

## Procedimiento de actualización

1. **Detección del cambio**: monitorear documentos oficiales, fallos, papers, comunicados.
2. **Verificación de la fuente**: confirmar que la cita o paráfrasis corresponde a la fuente citada.
3. **Contraste con el panorama anterior**: ¿la nueva posición modifica materialmente lo documentado?
4. **Actualización**: si la modificación es material, actualizar la posición documentada.
5. **Publicación**: actualizar el JSON `posiciones_mercado.json` y la sección 7 del dashboard.

## Compromisos editoriales

- No se incluye opinión editorial más allá de la "lectura" del panorama.
- No se usan adjetivos valorativos.
- Las citas son textuales, sin edición, cuando son textuales. Las paráfrasis se identifican como tales.
- Las fuentes son URL verificables, no capturas de pantalla.
- Las contradicciones internas de un sector se documentan, no se ocultan.

---

*Documento de trabajo del Atlas del Mercado Eléctrico Mayorista — Chile. Versión 1.0 — julio 2026.*
