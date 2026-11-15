# Límites y valores por defecto: Peer Review Studio 1.0.1

Verificados en el código de la versión 1.0.1 el 15-11-2026, salvo las filas marcadas como estimación. Distinguir siempre el límite del plugin del límite de Moodle o del servidor (tamaño de subida, cron, proveedor de IA).

## Requisitos
| Elemento | Valor |
|---|---|
| Moodle | 4.5 a 5.3 |
| Licencia, clave o ajustes de sitio propios | Ninguno |
| Cron de Moodle | Imprescindible para emparejar por fechas, recordar, reasignar, escalar y publicar |
| IA | Opcional; requiere un proveedor de IA de Moodle con la acción «Generar texto» |

## Entrega
| Elemento | Límite o valor |
|---|---|
| Entregas por alumno y actividad | 1 (editable hasta que tiene revisor) |
| Ficheros por entrega | 20, sin subcarpetas |
| Tamaño de cada fichero | El máximo de subida del curso; el plugin no añade otro |
| Tipos de fichero | Sin restricción propia para entregar |
| Tipo de entrega por defecto | Subida de fichero |
| Nombre de la actividad | Obligatorio, hasta 255 caracteres |

## Revisores y seguimiento
| Elemento | Límite o valor |
|---|---|
| Revisiones que cada alumno debe completar | Por defecto 2, mínimo 1 |
| Objetivo de revisiones recibidas por entrega | Por defecto 2, mínimo 1; máximo real = alumnos con entrega menos 1 |
| Asignación automática | Activada por defecto |
| Modo del grupo de revisores | Por defecto «Cualquier alumno elegible» |
| Evitar revisiones recíprocas | Desactivado por defecto |
| Recordar a revisores inactivos | Por defecto 2 días; 0 lo desactiva; un solo recordatorio por revisión |
| Reasignar revisiones no completadas | Por defecto 4 días; 0 lo desactiva; debe ser mayor que el recordatorio |
| Reasignaciones automáticas | Se reencola mientras la entrega no acumule más de 3 revisiones retiradas |
| Frecuencia de la tarea programada | Cada 10 minutos |
| Espera de bloqueo al emparejar o guardar una entrega | Hasta 10 segundos; si no, mensaje «Tu entrega ya se está guardando…» o se pospone el reparto |
| Mismo revisor para la misma entrega | Nunca dos veces, ni tras una retirada |

## Rúbrica
| Elemento | Límite o valor |
|---|---|
| Criterios | De 1 a 5 |
| Niveles por criterio | De 2 a 4; un criterio con etiqueta y menos de 2 niveles da error |
| Etiquetas de criterio y de nivel | Hasta 255 caracteres |
| Peso del criterio | Por defecto 1; mínimo 0,1 (un valor menor da el error «El peso del criterio debe ser 0,1 o mayor») |
| Puntuación de nivel | No negativa; al menos un nivel del criterio debe valer más de 0 |
| Rúbrica de fábrica | 3 criterios de peso 1, niveles con 1, 2, 3 y 4 puntos |
| Nota mínima con la rúbrica de fábrica | 25 % del máximo de la entrega |
| Con revisiones ya hechas | No se pueden quitar criterios ni niveles; lo demás sí y se recalcula |

## Calificación
| Elemento | Límite o valor |
|---|---|
| Calificación máxima de la entrega | Por defecto 100; no negativa |
| Calificación máxima de revisión | Por defecto 0 (desactivada); no negativa |
| Máximo de la actividad en el libro | Suma de ambos; si la suma es 0, la actividad no tiene calificación |
| Calificación para aprobar | No puede superar esa suma |
| Nota fijada por el docente | Entre 0 y la suma de máximos (se recorta); admite coma o punto decimal |
| Redondeo | 2 decimales |
| Entrega sin ninguna revisión | Sin nota (no 0) |

## Panel del tutor
| Elemento | Límite o valor |
|---|---|
| Filas de participantes por página | 25 |
| Entregas listadas en «Requiere atención» | Hasta 20 |
| Nombres en un aviso de escalado | Hasta 10, después puntos suspensivos |
| Búsqueda | Por nombre; por correo solo si el sitio muestra el correo como dato de identidad |
| Participantes sin entrega | No aparecen |

## Revisión por IA
| Elemento | Límite o valor |
|---|---|
| Activada por defecto | No |
| Peso de la nota de la IA | Por defecto 30 %; de 0 a 100 |
| Respaldo por IA | Desactivado por defecto; solo configurable con la IA activada |
| Escala de las notas de IA | 0 a 100, después se lleva a la escala de la actividad |
| Formatos que la IA puede leer | Texto en línea; documentos .docx y .odt; ficheros de texto (txt, md, csv, tsv, json, xml, yaml, tex, rtf, html, css y código fuente habitual) o cualquier fichero que Moodle identifique como texto |
| Formatos que impiden la nota de IA | Cualquier otro en la entrega: PDF, imágenes, .doc, hojas de cálculo, presentaciones, comprimidos, audio, vídeo |
| Tamaño de fichero legible | Hasta 20 MiB por fichero; uno mayor cuenta como ilegible |
| Cuerpo de un .docx u .odt | Hasta 8 MiB de contenido interno |
| Texto total de una entrega | Hasta 120.000 caracteres; si lo supera, la IA no la califica (no se recorta) |
| Lectura parcial | No existe: o se lee la entrega completa o no se califica |
| Imágenes, tablas incrustadas como imagen, gráficos | No se envían |
| Peticiones por actividad (estimación) | Hasta una por entrega más una por revisión enviada, más las de respaldo |
| A nombre de quién cuenta cada petición | Del autor (entrega) o del revisor (revisión); aplican los límites por usuario y de sitio de Moodle |
| Reintentos ante fallo del proveedor (estimación) | Reintentos automáticos de Moodle con esperas crecientes; el plugin abandona cuando la espera entre dos intentos llega a unos 30 minutos (en torno a una hora en total) |
| Reintentos ante límite de peticiones (estimación) | Igual, pero abandona cuando la espera alcanza unas 4 horas (varias horas en total) |
| Tras abandonar | La evaluación de IA no se vuelve a intentar sola; la nota queda sin esa parte |
| Página de prueba del administrador | Una petición mínima; admite hasta 5 minutos de espera |
| Modelo, temperatura, tokens, coste | No los fija el plugin: dependen del proveedor de IA del sitio |

## Lo que el plugin no hace en 1.0.1
No hay entregas en grupo, autoevaluación, revisión por el docente con rúbrica, borradores de revisión, edición de una revisión enviada, anonimato del revisor frente al tutor, exportación de notas propia, ni límite de carga por revisor. No lee PDF ni imágenes para la IA. No guarda el texto enviado a la IA.
