# Estudio técnico — El mercado eléctrico mayorista chileno

**Período:** 2010–2025
**Actualización:** trimestral
**Corte de datos:** 21 de julio de 2026
**Versión:** 2026Q3

---

## 1. Marco regulatorio e institucional

El mercado eléctrico chileno está estructurado como un **pool obligatorio** con costos de generación auditados y un mercado mayorista spot horario. La arquitectura legal data del DFL 1/1982, refundido en el DFL 4/20018, conocida como **Ley General de Servicios Eléctricos (LGSE)**. La LGSE fue reformada sustancialmente por la **Ley 20.936/2016** (que modernizó la transmisión) y la **Ley 21.721/2024** (Ley de Transición Energética, que ajustó la regulación a la nueva matriz de generación). El marco operativo del SEN se rige por el **DS 125/2017** (Reglamento de Coordinación y Operación del Sistema Eléctrico Nacional).

### 1.1. Los cuatro segmentos del mercado

La LGSE separa las actividades en cuatro segmentos con tratamiento regulatorio diferenciado:

- **Generación**: libre entrada, mercado competitivo basado en tarificación a costo marginal. Los generadores venden su energía en el mercado spot horario o mediante contratos bilaterales de tipo financiero con clientes libres o distribuidoras.
- **Transmisión**: monopolio natural regulado. Tres subsegmentos: **nacional** (sistema troncal 500 kV y 220 kV), **zonal** (sistemas A-F a tensiones menores) y **dedicada** (uso exclusivo). Existe también la categoría de **polos de desarrollo** para evacuación de generación en zonas de alto potencial renovable.
- **Distribución**: monopolio natural regulado por zona de concesión. Tarifas fijadas por la CNE cada cuatro años mediante procesos tarifarios.
- **Comercialización**: los generadores pueden vender directamente o a través de comercializadores independientes (figura poco desarrollada en Chile).

### 1.2. Los seis entes del mercado

La arquitectura institucional descansa en seis entes con funciones diferenciadas:

| Ente | Sigla | Función |
|---|---|---|
| Ministerio de Energía | MINENERGIA | Rector de política. Dicta Decretos de Expansión, fija resoluciones tarifarias |
| Comisión Nacional de Energía | CNE | Regulador técnico-económico. Aprueba Planes de Expansión. Fija Precios de Nudo y tarifas de distribución |
| Coordinador Eléctrico Nacional | CEN | Operador independiente del sistema. Coordina despacho. Propone expansión. Monitorea competencia |
| Superintendencia de Electricidad y Combustibles | SEC | Fiscalizador. Calidad de servicio. Seguridad de instalaciones. Sanciona |
| Panel de Expertos | — | Resuelve discrepancias técnicas entre agentes y regulador |
| Tribunal de Defensa de la Libre Competencia | TDLC | Resuelve sobre libre competencia. Aplica multas. Aprueba/rechaza operaciones de concentración |

Adicionalmente, la **Fiscalía Nacional Económica (FNE)** es el órgano persecutor de prácticas anticompetitivas, y el **Ministerio Público** puede llevar casos penales en casos graves.

### 1.3. El modelo de mercado spot

El SEN opera bajo un modelo de despacho centralizado: el CEN determina hora a hora qué central debe generar en cada barra del sistema, minimizando el costo total de operación. La unidad marginal define el **Costo Marginal (CMg)** horario en cada barra. La energía se valoriza al CMg en el mercado spot, mientras que la potencia se valoriza al precio de nudo de la potencia, fijado por la CNE.

El mercado spot coexiste con **contratos bilaterales de tipo financiero** entre generadores y clientes libres o distribuidoras. Los contratos financieros permiten a las partes fijar precios independientes del spot, reduciendo la exposición a la volatilidad. El **75% de la energía del SEN se transa bajo contratos** y el 25% en el spot, según datos del CEN.

El mercado spot es **cerrado a los generadores**: sólo ellos pueden participar como vendedores. Los clientes libres y regulados compran a generadores o, en el caso de los regulados, a través de las distribuidoras que contratan a precio de nudo.

### 1.4. Clientes regulados vs libres

La LGSE define dos regímenes para los usuarios finales:

- **Cliente regulado**: potencia conectada ≤ 500 kW. Está sujeto a precio de nudo fijado por la CNE. La distribuidora actúa como intermediario.
- **Cliente libre**: potencia conectada ≥ 5.000 kW. Puede negociar contratos directamente con generadores a precios libremente acordados.

Históricamente, los clientes con potencia entre 500 kW y 5.000 kW podían optar entre uno u otro régimen. La **Resolución Exenta N°58/2024 del Ministerio de Energía** redujo el umbral para ser cliente libre a 300 kW, y la **RE N°13/2025** reglamentó el período de transición. Esta ampliación busca profundizar la liberalización del mercado, aunque su impacto efectivo depende de las barreras de entrada para nuevos clientes libres.

El **Precio de Nudo (PN)** es el precio regulado que cobran las distribuidoras a clientes finales con potencia ≤ 500 kW. Se fija semestralmente en abril y octubre por la CNE. Tiene dos componentes: Precio de la Energía (PE) y Precio de la Potencia de Punta (PP). El cliente regulado paga además un cargo de distribución y un peaje de transmisión troncal (VATT), completando el **precio final regulado**.

## 2. Composición de la matriz y actores

### 2.1. Capacidad instalada 2025

A diciembre de 2025, el SEN tiene **39.104 MW** instalados. La composición por tecnología es:

| Tecnología | MW | % |
|---|---|---|
| Solar fotovoltaica | 12.222 | 31,3% |
| Eólica | 6.349 | 16,2% |
| Hídrica total | 7.550 | 19,3% |
| — Embalse | 3.515 | 9,0% |
| — Pasada | 4.035 | 10,3% |
| Térmica total | 12.889 | 33,0% |
| — Gas natural | 5.266 | 13,5% |
| — Carbón | 3.515 | 9,0% |
| — Diésel | 3.087 | 7,9% |
| — Otros térmicos | 906 | 2,3% |
| Termosolar | 114 | 0,3% |
| Geotérmica | 95 | 0,2% |

La capacidad instalada de **almacenamiento con baterías (BESS)** es 1.529 MW, con Engie liderando (355 MW) seguido de AES Andes (340 MW). Hay 737 MW adicionales en pruebas y 6.770 MW en construcción.

### 2.2. Evolución histórica

La capacidad instalada del SEN se multiplicó por 2,4 entre 2010 y 2025:

- 2010: 16.000 MW (75% térmica, 33% hidro, casi 0% ERNC)
- 2015: 18.500 MW (71% térmica, 29% hidro, 7,5% ERNC)
- 2020: 27.200 MW (46% térmica, 22% hidro, 30% ERNC)
- 2025: 39.104 MW (33% térmica, 19% hidro, 48% ERNC)

El cambio de composición es la transformación estructural más profunda del sector en 15 años. La hidroelectricidad se mantuvo prácticamente estable (5.300 MW en 2010 vs 7.550 MW en 2025); el crecimiento fue solar y eólica, multiplicándose por 30 y 12 respectivamente.

### 2.3. Concentración de mercado

A diciembre de 2025, los cuatro conglomerados principales controlan el **50,5% de la capacidad instalada** del SEN, una caída respecto al 78% que controlaban en 2015:

| Conglomerado | MW estimados | % | Posición |
|---|---|---|---|
| Enel | 9.268 | 23,7% | Líder absoluto, casi duplica al segundo |
| Grupo Matte (Colbún) | 4.575 | 11,7% | Segundo |
| AES Corporation (AES Andes) | 3.091 | 7,9% | Tercero |
| Engie | 2.816 | 7,2% | Cuarto |
| EDF | 1.330 | 3,4% | Quinto |
| Mainstream Renewable Power | 1.251 | 3,2% | Sexto (puro eólico) |
| EnfraGen (ex Prime Energía) | 900 | 2,3% | Séptimo |
| Sonnedix | 700 | 1,8% | Octavo (solar) |
| Tamakaya Energía | 700 | 1,8% | Noveno |
| Otros (PMGD + pequeñas) | 14.473 | 37,0% | Múltiples actores atomizados |

La desconcentración observada en la última década se explica principalmente por la entrada masiva de generadores solares y eólicos pequeños (PMGD), que atomizaron el mercado. Pero la concentración agregada esconde diferencias importantes por segmento:

- **Solar**: HHI 880, muy desconcentrado
- **Eólica**: HHI 720, muy desconcentrado
- **Hidroeléctrica**: HHI 1.780, moderadamente concentrado
- **Térmica**: HHI 2.050, moderadamente concentrado
- **BESS**: HHI 1.980, moderadamente concentrado (Engie + AES Andes = 45,5%)

### 2.4. Límites a la integración vertical

La **Ley 20.936/2016** introdujo límites explícitos a la integración vertical entre generación y transmisión, con el objetivo de evitar conductas estratégicas:

- Una empresa generadora no puede participar individualmente en el segmento de transmisión nacional con más del **8%** del valor de inversión total del sistema.
- La participación conjunta de un grupo empresarial en generación y transmisión no puede superar el **40%** del valor de inversión del sistema de transmisión nacional.

Estos límites son verificados periódicamente por el CEN en sus Informes de Monitoreo de la Competencia.

## 3. Generación real y mercados spot

### 3.1. Generación 2025

La generación bruta del SEN en 2025 fue **85.064 GWh**, una caída del 0,5% respecto a 2024 (85.519 GWh) por menor hidrología. La composición:

| Tecnología | GWh | % |
|---|---|---|
| Solar | 22.636 | 26,6% |
| Hídrica | 20.600 | 24,2% |
| Eólica | 13.088 | 15,4% |
| Térmica | 30.600 | 36,0% |
| Biomasa y otras ERNC | 4.800 | 5,6% |

La generación hidroeléctrica cayó 25% respecto a 2024 (de 27,1 a 20,6 TWh), obligando a mayor despacho térmico. Este cambio en el mix explica la evolución de los costos marginales que se analiza más adelante.

### 3.2. Costos marginales (CMg)

El CMg es el precio spot del mercado mayorista: el costo variable de la unidad más cara operando en un instante dado. Se fija horario en cada barra del sistema. El CMg es la variable más volátil del mercado y refleja la hidrología, la disponibilidad de renovables y la congestión de transmisión.

**Serie anual CMg promedio (USD/MWh):**

| Año | Crucero | Pan de Azúcar | Quillota | Puerto Montt |
|---|---|---|---|---|
| 2017 | 38 | — | 51 | 78 |
| 2021 | 81 | 75 | 71 | 88 |
| 2024 | 38 | 37 | 38 | 56 |
| 2025 | 65 | 62 | 70 | 90 |

El 2021 marca el peak de la megasequía, con CMg Quillota en 71 USD/MWh. El 2024 refleja mayor disponibilidad hidro y mayor participación solar/eólica. El 2025 muestra un alza significativa (+50% en Quillota, +60% en Puerto Montt) driven por menor hidrología y mayor despacho térmico.

**Hechos puntuales relevantes en 2025:**
- Quillota 220 kV en junio 2025: 112,87 USD/MWh (+110% vs mismo mes 2024)
- Crucero 220 kV en junio 2025: 90,71 USD/MWh (+67,8% vs 2024)
- Diferencial promedio Charrúa-Puerto Montt: 18,9 USD/MWh, indicador de congestión centro-sur

**Estructura marginal 2024**: el 25,8% de las horas en Quillota 220 kV, el CMg fue fijado por centrales con costo variable cercano a cero (solar, eólica, hidro pasada). Esta participación de "Cmg cero" es un indicador de la penetración renovable en el despacho.

### 3.3. Costo total de operación

El costo total de operación del SEN en 2024 fue **1.670 millones USD**, una caída del 39,1% respecto a 2023 (2.745 MUSD). El menor costo refleja mayor disponibilidad hidro y mayor participación de ERNC con costo variable cercano a cero. Sin embargo, en 2025 el costo total volvió a subir por menor hidrología.

### 3.4. Precio de Nudo regulado

El **Precio de Nudo (PN)** se fija semestralmente por la CNE (abril y octubre) y se compone de dos elementos: Precio de la Energía (PE) y Precio de la Potencia (PP). Serie anual:

| Año | PE (USD/MWh) | PP (USD/MWh) | PN total | Razón PN/CMg |
|---|---|---|---|---|
| 2015 | 75 | 12 | 87 | 1,71 |
| 2021 | 95 | 12 | 107 | 1,51 |
| 2024 | 55 | 11 | 66 | 1,74 |
| 2025 | 70 | 12 | 82 | 1,17 |

El PN siempre es mayor que el CMg promedio porque incluye: (a) costo de capacidad, (b) cálculo sobre escenarios hidrológicos críticos, (c) anualidad del VATT. La razón PN/CMg varía entre 1,17 y 1,74 según el año. En 2025, con CMg al alza, la razón se acercó a 1 por primera vez en cinco años.

El **precio final al cliente regulado** incluye además un cargo de distribución (35% del total) y un peaje de transmisión (5%). El precio final regulado en 2025 fue aproximadamente 120 USD/MWh, mientras que el cliente libre paga en promedio 80 USD/MWh (30% menos).

### 3.5. Comparativa cliente regulado vs libre

| Régimen | Composición | Precio 2025 | Composición del consumo |
|---|---|---|---|
| Cliente regulado | PN + cargo distribución + peaje VATT + IVA | ~120 USD/MWh | 51% del consumo total |
| Cliente libre | Contratos bilaterales | ~80 USD/MWh | 49% del consumo total |

La composición del consumo libre: 51% gran industria minera, 28% industriales manufactureros, 12% retail y servicios, 9% otros. La ampliación del umbral de cliente libre a 300 kW (RE 58/2024) busca profundizar la competencia, aunque su impacto efectivo depende de las barreras de entrada (información, garantías contractuales, gestión de riesgo de precio).

## 4. Sistema de transmisión

### 4.1. Topología del SEN

El Sistema Eléctrico Nacional se extiende **3.100 km** desde Arica y Parinacota hasta la Isla Grande de Chiloé. La topología tiene tres componentes principales:

- **Columna vertebral 500 kV**: une el norte solar con el centro de carga. Recorre Nueva Maitencillo – Nueva Pan de Azúcar – Cardones – Polpaico – Alto Jahuel. Este es el único enlace de 500 kV que conecta la zona de mayor generación con el centro de carga, lo que explica la vulnerabilidad operativa expuesta por el apagón del 25-F.
- **Red 220 kV**: complementa la 500 kV en el centro y se extiende al sur (Alto Jahuel – Charrúa – Puerto Montt).
- **Sistemas zonales A-F** (66 kV a 220 kV): abastecen regiones específicas. Sistema A: norte grande. B: norte chico. C/D/E: centro. F: sur.

### 4.2. Segmentos y subsegmentos

La LGSE define cuatro segmentos de transmisión:

- **Nacional**: sistema troncal de alta tensión (220 kV y 500 kV), uso común, remunerado por VATT. Lo opera principalmente Transelec.
- **Zonal**: sistemas de tensión menor por zona geográfica (A a F), uso común, remunerado por VATT zonal. Lo operan varias firmas: CGE, Chilquinta, Saesa, Edelaysen, etc.
- **Polos de desarrollo**: infraestructura para evacuación de generación en zonas de alto potencial renovable, declarada mediante Decreto Exento del Ministerio de Energía.
- **Dedicada**: infraestructura para uso exclusivo de un usuario (generador o consumidor), sin acceso abierto. Remunerada por el usuario, no por el sistema.

### 4.3. Marco regulatorio de la transmisión

La regulación del segmento transmisión está contenida en el **Título III de la LGSE** (Arts. 73° a 113°), reformada sustancialmente por la **Ley 20.936/2016**. Los puntos clave:

- **Planificación centralizada**: el CEN propone un Plan de Expansión anual, la CNE aprueba el Informe Técnico Definitivo, y el Ministerio de Energía dicta un Decreto Exento fijando las obras. Los decretos establecen la obligación del CEN de licitar las obras dentro de los doce meses siguientes.
- **Valorización**: el Valor Agregado de Transmisión Troncal (VATT) se fija cada cuatro años por la CNE mediante un estudio de valorización de instalaciones. La metodología es **CRAND** (Costo de Reposición a Nuevo Depreciado) con tasa de descuento del 10% real anual.
- **Acceso abierto**: cualquier generador o usuario puede usar la red pagando el peaje correspondiente. El CEN coordina el acceso y resuelve congestiones mediante redespacho.
- **Límites a la integración vertical**: una empresa generadora no puede tener más del 8% individual ni 40% conjunto del valor de inversión del sistema de transmisión nacional (Art. 7° Ley 20.936/2016).
- **Resolución de discrepancias**: el Panel de Expertos resuelve las discrepancias técnicas entre agentes y entre agentes y regulador.

### 4.4. El VATT y la remuneración de la transmisión

El **VATT total del SEN** es aproximadamente **US$1.000 millones anuales**, distribuidos por empresa transmisora:

| Empresa | % del VATT | Ingreso anual estimado |
|---|---|---|
| Transelec | 38% | US$380M |
| ISA Interchile | 28% | US$280M |
| CGE Transmission | 12% | US$120M |
| Engie Transmission | 8% | US$80M |
| Otros (Chilquinta, Saesa, Edelaysen, Statkraft) | 14% | US$140M |

La distribución por segmento geográfico es: 55% sistema nacional, 9,5% zonal A, 7,5% zonal B, 18% zonales C/D/E, 10% zonal F.

El segmento de transmisión es un **oligopolio natural**: tres firmas (Transelec, ISA Interchile, CGE) concentran el 78% del VATT. El Estado no controla las firmas transmisoras, pero sí regula el precio (VATT) y los planes de expansión (vía Decreto del Ministerio).

## 5. Plan de Expansión de Transmisión

### 5.1. El proceso anual

El proceso de expansión anual de la transmisión sigue un calendario regulatorio definido en los Arts. 87° y 91° de la LGSE:

1. **CEN presenta propuesta** (julio-agosto de cada año).
2. **CNE publica Informe Técnico Preliminar (ITP)** con consulta ciudadana.
3. **CNE publica Informe Técnico Definitivo (ITD)** incorporando observaciones.
4. **Ministerio de Energía dicta Decreto Exento** fijando las obras de ampliación (publicación en Diario Oficial).
5. **CEN inicia proceso de licitación** de las obras en los doce meses siguientes.
6. **Construcción y entrada en operación** según plazos definidos en el decreto (típicamente 36-72 meses).

El último valorización del VATT vigente cubre el período 2024-2027. La actualización del próximo ciclo 2028-2031 está en proceso.

### 5.2. Planes emitidos 2017-2025

| Plan | Decreto | Inversión ref. | N° de obras | Estado 2026 |
|---|---|---|---|---|
| 2017 | D.S. 418/2017 | US$1.100M | 30 | En operación, parcialmente |
| 2018 | D.S. 231/2019 | US$700M | 22 | Operación mayoritaria |
| 2019 | D.S. 171/2020 | US$540M | 23 | Operación parcial |
| 2020 | D.S. 257/2021 | US$250M | 16 | Operación mayoritaria |
| 2021 | D.S. 200/2022 | US$320M | 18 | Operación parcial |
| 2022 | D.E. 4/2024 | US$200M | 16 | Licitación en curso |
| 2023 | D.E. 266/2024 | US$389M | 45 | Licitación en curso |
| 2024 | D.E. 354/2025 | US$580M | 23 | Inicio de licitaciones |
| 2025 | (pendiente) | US$1.100M | 91 | ITD en proceso |

**Inversión acumulada planes 2017-2025**: US$5.179M, con 204 obras en diferentes estados de avance.

### 5.3. Obras emblemáticas

**Nueva Línea 2×500 kV Nueva Chuquicamata – Miraje** (Plan 2024, D.E. 354/2025):
- Inversión referencial: US$90M
- Plazo constructivo: 60-72 meses
- Objetivo técnico: permitir evacuación de generación solar del norte grande sin saturar el corredor 500 kV existente
- Vínculo con el 25-F: es redundancia geográfica del único enlace que falló en el apagón

**Sistema Tiquel – Tiuquilemu 500 kV** (Plan 2024):
- Inversión total: US$190M (conjunto)
- Componentes: Nueva S/E Tiquel (US$125M), línea 500 kV Tiquel-Tiuquilemu (US$24,6M), línea 220 kV Tiquel-Las Delicias (US$41,3M), subestaciones Tiuquilemu, La Calle, Cambrales
- Objetivo: aumentar capacidad de transferencia centro-sur, habilitar nuevos polos de inyección renovable

### 5.4. Atrasos crónicos en la construcción

La ejecución del Plan de Expansión muestra un patrón sistemático de atrasos. ACERA reporta que a noviembre de 2025, **más del 70% de las obras de transmisión en desarrollo presentaban atrasos**, con un retraso promedio de 1,7 años. Las causas principales son:

- **Complejidad técnica** de las obras (corredores 500 kV en zonas remotas).
- **Procesos de evaluación ambiental** prolongados.
- **Licencias sectoriales** (MOP, BBNN, MINVU) que requieren coordinación interinstitucional.
- **Quiebra de contratistas** (caso Astaldi con Punilla 2021).
- **Falta de oferentes** en licitaciones (caso Punilla 2025).

El atraso se manifiesta en la tasa de ocupación de los corredores: en varios momentos del año, el corredor 500 kV del norte opera al 100% de su capacidad, lo que obliga a vertimiento de generación renovable.

## 6. Concentración de mercado y libre competencia

### 6.1. Evolución del HHI

El Índice de Herfindahl-Hirschman (HHI) mide la concentración de mercado. Se calcula como la suma de los cuadrados de las participaciones porcentuales de cada empresa.

| Año | HHI | Interpretación |
|---|---|---|
| 2015 | 1.850 | Moderadamente concentrado |
| 2017 | 1.700 | Caída por entrada solar |
| 2020 | 1.520 | Desconcentrado |
| 2023 | 1.180 | Mínimo histórico |
| 2025 | 1.180 | Estable en zona desconcentrada |

La desconcentración del mercado de generación se explica por la entrada masiva de PMGD (Pequeños Medios de Generación Distribuida) solares y eólicos. La estabilización desde 2022 sugiere que la fase de desconcentración se agotó; queda un piso estructural concentrado en activos termoeléctricos e hidroeléctricos.

### 6.2. Concentración por segmento

| Segmento | HHI 2025 | Interpretación |
|---|---|---|
| Capacidad instalada total | 1.180 | Desconcentrado |
| Solar | 880 | Muy desconcentrado |
| Eólica | 720 | Muy desconcentrado |
| Hidroeléctrica | 1.780 | Moderadamente concentrado |
| Térmica | 2.050 | Moderadamente concentrado |
| BESS | 1.980 | Moderadamente concentrado (alerta) |

El segmento BESS es el flanco nuevo de concentración. Engie y AES Andes concentran el 45,5% del almacenamiento operativo. Si este patrón se mantiene en la construcción (6.770 MW en pipeline), Chile enfrenta el riesgo de reproducir la concentración que se desconcentró en generación.

### 6.3. Concentración por zona geográfica

| Zona | Top 1 | Top 3 |
|---|---|---|
| Antofagasta-Atacama (norte grande) | 35% | 72% |
| Coquimbo-Valparaíso (norte chico-centro) | 28% | 65% |
| Metropolitana-Maule (centro) | 32% | 70% |
| Ñuble-Los Lagos (sur) | 24% | 58% |

El sur es la zona menos concentrada por la presencia de muchas hidroeléctricas medianas. El centro tiene mayor concentración por el peso de Enel y la térmica. El norte está dominado por solar y eólica con actores diversificados.

### 6.4. Concentración en transmisión

El segmento de transmisión es un **oligopolio natural** con HHI calculado de 2.450 (top 3 = 78% del VATT). Esta concentración es estructural y reconocida por la regulación:

- Las instalaciones de transmisión son bienes nacionales de uso público (Art. 17° LGSE).
- La concesionaria tiene obligación de servicio pero el precio está regulado (VATT).
- La entrada al segmento requiere una concesión del Ministerio de Energía, que se otorga por decreto.

Esto significa que el Estado no puede introducir competencia directa en transmisión, pero sí puede regular el precio y planificar la expansión.

## 7. Apagón del 25 de febrero de 2025

El apagón del 25 de febrero de 2025 dejó sin suministro a 7 millones de hogares entre Arica y Los Lagos durante más de 8 horas. La causa oficial del CEN y la SEC fue la siguiente:

A las 13:35 horas, personal de **ISA Interchile S.A.** reportó al CEN un módulo de comunicaciones deshabilitado en la protección diferencial 87L de la línea 2×500 kV Nueva Maitencillo – Nueva Pan de Azúcar, entre Vallenar y Coquimbo. A las 15:13, sin informar al CEN ni pedir autorización, el personal de Interchile intentó resincronizar el módulo siguiendo el procedimiento del fabricante. La resincronización disparó incorrectamente la protección y abrió ambos circuitos de la línea, que en ese momento transmitía 1.800 MW (16% de la demanda nacional).

**Secuencia de colapso:**
- t+0: apertura ambos circuitos 500 kV
- t+1,5s: enlace respaldo 220 kV colapsa por sobrecarga
- t+2-4s: SEN se separa en dos islas (norte y centro-sur)
- t+4-8s: isla centro-sur colapsa (mayor demanda, menor inercia)
- t+8-15s: isla norte colapsa
- t+30s+: apagón total del SEN

La académica Claudia Rahmann (U. de Chile) fue categórica: "Para evitar mitos o supuestos que no corresponden, no hubo un corto circuito, no hubo una falla, y tampoco hubo ningún problema relacionado con las grandes inyecciones de energía solar en el norte del país." La causa fue una **falla humana técnica** en Interchile, no un problema de la matriz.

Lo que el apagón expuso fue la **vulnerabilidad sistémica** del SEN:
1. **Transmisión única sin redundancia**: el corredor 500 kV que conecta el norte solar con el centro de carga es uno solo. Cuando falla, no hay alternativa operativa.
2. **Almacenamiento distribuido insuficiente**: la isla centro-sur colapsó en 4 segundos, evidencia de insuficiente reserva rotante y almacenamiento para responder a la contingencia.
3. **Esquemas de defensa no probados para esta topología de matriz**: los EDAC (Esquemas de Desprendimiento Automático de Carga) tuvieron desempeño deficiente, los protocolos SCADA de Transelec fallaron.

El **Informe de Monitoreo de la Competencia 2025** del CEN confirma que el 70% de las obras de transmisión en desarrollo presentan atrasos. La respuesta regulatoria post-25-F incluyó la aceleración de obras del Plan de Expansión 2024 y la priorización del corredor Chuquicamata-Miraje como redundancia del corredor Maitencillo-Pan de Azúcar.

## 8. Posiciones regulatorias por sector

Esta sección documenta la posición de cada sector institucional sobre temas clave del mercado. Las posiciones se construyen a partir de documentos oficiales: oficios del Ministerio al Congreso, resoluciones de la CNE, fallos del TDLC, papers de la academia, comunicados de gremios.

### 8.1. Plan de Expansión de Transmisión

| Sector | Posición |
|---|---|
| Ministerio de Energía | "Cada plan se ejecuta con la celeridad que permite el proceso regulatorio. Los decretos se dictan en los plazos legales." |
| CNE | "La CNE aprueba ITD con criterios técnicos y consulta ciudadana. Los atrasos son por complejidad técnica." |
| CEN | "El CEN ejecuta las licitaciones. Los plazos constructivos son los acordados." |
| USM | "Hay un desfase estructural entre velocidad de instalación de renovables (5 años) y velocidad de construcción de transmisión (10-15 años). El Plan es necesario pero insuficiente." |
| ACERA | "El 70% de las obras en desarrollo presenta atrasos, con 1,7 años de retraso promedio. El sistema ha pasado del 100% de capacidad del corredor 500 kV en varios momentos del año." |
| Generadoras de Chile | "El Plan debe acelerarse. La conexión de nuevos proyectos renovables depende de obras de transmisión con años de atraso." |
| Oposición parlamentaria | "La lentitud de la ejecución es responsabilidad de la empresa transmisora privada. Plantean que la transmisión debería ser estatal." |

**Lectura:** Hay acuerdo amplio en que la ejecución del Plan es insuficiente. La discrepancia está en la solución: unos piden más Estado (oposición), otros piden más agilidad regulatoria con el modelo actual (gremios).

### 8.2. Integración vertical

| Sector | Posición |
|---|---|
| TDLC | "Vigilancia permanente. La integración vertical puede crear incentivos a obstaculizar acceso a redes por parte de competidores." |
| CNE | "Los límites legales (8% individual, 40% conjunto) son suficientes para evitar integración excesiva." |
| USM | "Los límites son razonables pero la concentración efectiva del mercado muestra riesgos distintos. El BESS, que será el cuello de botella futuro, está moderadamente concentrado." |
| Generadoras de Chile | "Las reglas actuales permiten un mercado funcional. Cambios afectarían inversiones ya realizadas." |

**Lectura:** Posiciones encontradas. El TDLC vigila; la CNE cree que los límites bastan; la academia ve riesgos emergentes; las generadoras defienden el statu quo.

### 8.3. Umbral de clientes libres

| Sector | Posición |
|---|---|
| Ministerio de Energía | "La rebaja del umbral de 500 kW a 300 kW amplía la libertad de elección." |
| CNE | "La ampliación es consistente con el modelo de libre mercado." |
| U. de Chile | "La ampliación es razonable en teoría, pero el impacto efectivo depende de las barreras de entrada." |
| FNE | "La libre competencia debe asegurarse con fiscalización activa, no solo con ampliación de umbrales." |
| Oposición | "La ampliación es positiva pero debe ir acompañada de mayor regulación de los contratos bilaterales." |
| Oficialismo | "Apoya la ampliación como profundización del mercado." |

**Lectura:** Amplio apoyo a la ampliación, con matices sobre la implementación efectiva. Ningún sector importante se opuso.

### 8.4. Hidroelectricidad y almacenamiento

| Sector | Posición |
|---|---|
| Ministerio de Energía | "El Plan de Descarbonización reconoce el rol de la hidroelectricidad y el almacenamiento como complemento a las ERNC." |
| U. de Chile | "La hidroelectricidad de embalse cumple un rol sistémico (inercia, reserva rodante, almacenamiento estacional) que las ERNC no reemplazan." |
| ACERA | "El sistema necesita expansión simultánea de transmisión, almacenamiento y capacidad de respaldo. Chile tiene sobrecapacidad solar pero falta dónde almacenarla." |
| Generadoras de Chile | "Defiende el parque térmico como respaldo. Critica la velocidad de cierre de carbón sin reemplazo hidroeléctrico equivalente." |
| Oposición | "Históricamente crítico con grandes proyectos hidroeléctricos. Apoya el almacenamiento distribuido como alternativa." |

**Lectura:** Acuerdo en que la hidroelectricidad tiene rol sistémico, pero discrepancia en el peso de nuevas grandes hidroeléctricas vs almacenamiento distribuido.

## 9. Cierre integrado: ¿qué cambió en 15 años?

| Indicador | 2015 | 2025 | Δ | Veredicto |
|---|---|---|---|---|
| Capacidad instalada SEN | 16.000 MW | 39.104 MW | +144% | Mejoró mucho |
| Participación ERNC en capacidad | 5% | 48% | +43 pp | Mejoró mucho |
| HHI capacidad instalada | 1.850 | 1.180 | -36% | Mejoró |
| Top 4 participación | 78% | 50,5% | -27 pp | Mejoró |
| Solar+eólica en generación | 0,3% | 42% | +42 pp | Mejoró mucho |
| Capacidad BESS operativa | 0 | 1.529 MW | nuevo | Mejoró |
| HHI segmento BESS | n/a | 1.980 | nuevo, zona moderada | Vigilar |
| Precio de Nudo regulado | 87 USD/MWh | 82 USD/MWh | -6% real | Mejoró |
| CMg Quillota promedio anual | 51 | 70 | +37% | Empeoró |
| HHI transmisión troncal (Top 3) | 2.500 | 2.450 | estable | Estructural |
| Atraso obras de transmisión | n/d | 70% con 1,7 años prom. | nuevo | Empeoró |

**Lectura:** 5 indicadores mejoraron sustancialmente, 2 empeoraron, 1 estable, 3 nuevos a vigilar. La transformación tecnológica del mercado de generación es genuina y profunda. La estructura oligopólica de la transmisión es estable. El cuello de botella se desplazó de generación a transmisión y almacenamiento.

**Indicador Compuesto de Competencia del Mercado Eléctrico (ICME):** calculado en 68/100 para 2025, una caída de 7 puntos respecto al peak de 2023 (78/100). La desconcentración agregada de generación se ha estabilizado, mientras que la concentración del segmento BESS marca alerta preventiva.

## 10. Preguntas abiertas

El mercado eléctrico chileno enfrenta cinco preguntas regulatorias abiertas en 2026:

1. **¿Acelera la ejecución del Plan de Expansión 2024-2025?** La respuesta depende de la capacidad de los privados (Transelec, ISA) y del MOP para ejecutar las obras del Plan 2024 en los plazos comprometidos.

2. **¿Se regula la concentración del BESS?** El FNE y el TDLC no han anunciado investigaciones específicas sobre el segmento. La concentración efectiva está en el límite moderado-alto (HHI 1.980).

3. **¿Ampliación del umbral de cliente libre avanza?** La RE 58/2024 amplió el umbral a 300 kW. La implementación efectiva depende de las barreras de entrada y de la respuesta de las distribuidoras.

4. **¿La nacionalización de la transmisión vuelve al debate?** El debate bajó de intensidad tras el cambio de gobierno. La propuesta no avanzó en el Congreso. Kast no la ha retomado.

5. **¿Cómo se cierra el carbón?** El Plan de Descarbonización está en marcha, pero la velocidad de cierre de centrales a carbón sin reemplazo hidroeléctrico equivalente preocupa a las generadoras.

## 11. Conclusión

El mercado eléctrico chileno es un sistema en transición. La transformación tecnológica de la última década (ERNC de 5% a 48% de la capacidad) ha sido genuina y ha desconcentrado el mercado de generación. Pero esa transformación se hizo sobre una red de transmisión y un sistema de almacenamiento que no han acompañado el ritmo. La vulnerabilidad operativa expuesta por el apagón del 25-F y la concentración del segmento BESS son señales de que la próxima fase de la transición requiere atención a la infraestructura, no sólo a la capacidad instalada.

La política regulatoria tiene tres tareas pendientes: (a) acelerar la ejecución del Plan de Expansión de Transmisión, (b) vigilar la concentración incipiente del BESS antes de que se consolide, y (c) facilitar la transición de los clientes regulados a libres sin dejar a los más pequeños con la peor parte de la curva de carga.

Para el estudio personal de un diplomado en regulación eléctrica, este mercado ofrece un caso de estudio excepcional: la transición de un mercado térmico-hidroeléctrico concentrado a un mercado mayoritariamente renovable en apenas 15 años, con todos los dilemas regulatorios que eso implica (concentración en nuevos segmentos, vulnerabilidad operativa, tarifas, integración vertical, mercado spot vs contratos).

---

*Documento de trabajo del Atlas del Mercado Eléctrico Mayorista — Chile. Próxima actualización: octubre 2026 (corte 2026Q4).*
