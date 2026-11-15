# Límites y valores por defecto: 0.8.0

Valores verificados en la revisión estática del 15-11-2026. Un límite documentado es un hecho; que haya causado un caso concreto es una conclusión aparte.

## Ajustes del sitio (valores de fábrica)
| Ajuste en pantalla | Valor de fábrica | Límites y notas |
|---|---|---|
| Activar las funciones de IA | No | Interruptor general |
| Proveedor IA | Subsistema de IA de Moodle | Alternativas: OpenAI, Anthropic (Claude), Google Gemini, DeepSeek |
| Clave de API | Vacío | Solo con proveedor directo |
| Modelos | Vacío | Uno por línea; el primero es el predeterminado; vacío = lista propia del proveedor |
| Timeout de petición IA | 60 segundos | Mínimo efectivo 5 s; 0 o vacío equivale a 60 s |
| Máximo de caracteres enviados a la IA | 2500 | Mínimo efectivo 200; 0 o vacío equivale a 2500 |
| Modo de anonimización | Estricta | Alternativa: básica |
| Conservar el texto enviado a la IA | No | |
| Un docente aprueba cada evaluación de la IA (por defecto) | Sí | Solo valor inicial de actividades nuevas |
| Confianza necesaria para liberar automáticamente (por defecto) | 0.65 | Se acota entre 0 y 1 |
| Peso de la IA en la nota (%) (por defecto) | 30 | Se acota entre 0 y 100 |

Modelos de la lista propia cuando «Modelos» está vacío: OpenAI gpt-4.1-mini, gpt-4o-mini, gpt-4.1; Anthropic claude-opus-5-5, claude-sonnet-5-5, claude-haiku-5-5; Google Gemini gemini-2.5-flash, gemini-2.5-pro; DeepSeek deepseek-chat. Que un nombre figure en esa lista no garantiza que el proveedor lo siga ofreciendo: comprobarlo en la página de prueba.
Con el subsistema de IA de Moodle no hay elección de modelo en el plugin y el tiempo de espera configurado en el plugin no se aplica.

## Ajustes de la actividad (valores de fábrica)
| Ajuste en pantalla | Valor de fábrica | Límites y notas |
|---|---|---|
| Nombre de la actividad | — | Obligatorio, hasta 255 caracteres |
| Partir de | Respuesta coordinada a una incidencia crítica | Tres plantillas o escenario vacío; solo al crear |
| Justificación escrita | Opcional | Sin justificación, Opcional, Obligatoria |
| Mostrar en el resultado las opciones no elegidas | No | Los docentes las ven siempre |
| Intentos permitidos | 1 | Ilimitado, 1, 2, 3, 4, 5 o 10 |
| Método de calificación | Calificación más alta | Más alta, media, primer intento, último intento |
| Calificación máxima | 100 | Debe ser mayor que 0 |
| Un docente revisa cada intento antes de publicar la nota | No | |
| Límite de tiempo | Desactivado | Sin máximo propio |
| Número máximo de decisiones | 0 | De 0 a 50; 0 = hasta un final |
| Evaluar con IA las justificaciones escritas | No | Requiere justificación no desactivada |
| Para qué se usa la IA | Solo feedback | O feedback y parte de la nota |
| Peso de la puntuación de la IA en la nota (%) | El del sitio (30) | De 1 a 100 cuando la IA cuenta para nota |
| Feedback de la IA que ve el alumnado | Solo el feedback general | Nada, general, o general con detalle |
| Un docente aprueba cada evaluación de la IA | El del sitio (sí) | |
| Qué valora la IA en las justificaciones | Tres criterios con pesos 40, 30 y 30 | Máximo 8 criterios; peso mayor que 0; etiqueta hasta 200 caracteres |
| Orientaciones para la IA | Vacío | Sin límite propio comprobado |
| Modelo de IA | Primero de la lista del sitio | No aparece con el subsistema de IA de Moodle |
| Confianza necesaria para liberar automáticamente | La del sitio (0.65) | De 0 a 1 |
| Intentos a finalizar (finalización) | Sin marcar; 1 al marcar | No se valida contra los intentos permitidos |

Las actividades creadas antes de 0.8.0 conservan «Último intento» como método y, si tenían IA, siguen combinándola en la nota.

## Intentos y tiempo
- Tope absoluto de 50 decisiones por intento, también cuando el máximo es 0. Protege frente a escenarios con bucles.
- Un intento en curso cuenta para «Intentos permitidos». Solo puede haber un intento en curso por alumno y actividad.
- La justificación del alumno no tiene longitud mínima ni máxima en el plugin; se guarda como texto sin formato.
- El límite de tiempo no admite pausas. Los avisos accesibles de la cuenta atrás se dan a los 5 minutos, 1 minuto y 10 segundos.
- La cuenta atrás se muestra en tono de urgencia cuando quedan 2 minutos o menos.
- No existen fechas de apertura y cierre propias de la actividad.
- Cambiar la «Calificación máxima» no recalcula las notas de intentos ya terminados.

## Texto enviado a la IA
- El máximo de caracteres se reparte a partes iguales entre todas las decisiones del intento, tengan o no justificación. Cada justificación se corta por el final al llegar a su parte.
- Cada decisión conserva siempre al menos 200 caracteres. Por eso, con más decisiones que el máximo dividido entre 200 (más de 12 con el valor de fábrica), el total enviado puede superar el máximo configurado.
- Texto de la situación: hasta 600 caracteres por decisión, sin formato. No cuenta para el máximo anterior.
- También se envían las opciones disponibles y la elegida, sin recorte propio.
- Ejemplo: 2500 caracteres y 5 decisiones dan 500 caracteres por justificación.

## Respuesta de la IA
- Comentario por criterio: hasta 300 caracteres. Comentario por decisión: hasta 400. Feedback general: se pide de hasta 600 y se guarda hasta 800.
- Alertas: hasta 10 por evaluación.
- Puntuación por criterio acotada entre 0 y 100; confianza entre 0 y 1; si falta la confianza se toma 0, lo que retiene la evaluación para un docente.
- Si la respuesta no trae puntuaciones utilizables de ningún criterio ni una puntuación global, la evaluación falla.
- Mensaje de error guardado: hasta 255 caracteres; el detalle del proveedor, hasta 180.

## Proveedores directos
- Sin reintentos automáticos ante fallos. Única excepción: con OpenAI o DeepSeek, si el modelo rechaza el parámetro de temperatura, se repite una vez sin él.
- Temperatura 0,2 con OpenAI, DeepSeek y Gemini; con Anthropic no se envía.
- Solo conexiones seguras y sin seguir redirecciones. Espera de conexión: entre 3 y 10 segundos, la mitad del tiempo de espera configurado.
- No hay dirección de servidor configurable ni proveedores «compatibles»: solo los cuatro citados o el subsistema de IA de Moodle.
- No hay cuotas, topes de gasto ni límites por usuario en el plugin. El control del gasto está en el proveedor o en el subsistema de IA de Moodle.

## Constructor y redacción con IA
- Descripción para redactar con IA: hasta 12.000 caracteres. Decisiones aproximadas: de 2 a 8 (de fábrica, 4).
- Espera mínima de 120 segundos para el borrador con la IA del sitio con proveedor directo.
- Comprobación de la puntuación: hasta 3.000 recorridos; por encima, los valores son aproximados y se avisa.
- Títulos de escenario, de nodo y nombre en el banco: hasta 255 caracteres.
- Identificadores internos de nodos, opciones, variables y criterios: letras, números, guiones y guiones bajos, hasta 100 caracteres (los genera el constructor).
- Valores por defecto al crear: variable con inicial 50, mínimo 0, máximo 100, «cuanto más alto, mejor»; criterio con puntuación máxima 25.

## Informe
- 25 intentos por página. Filtros por estado, incidencia, estado de IA y nombre.
- Niveles de incidencia: «Atención» (revisión docente pendiente, IA pendiente, IA requiere revisión, IA con alertas) y «Crítica» (IA fallida).
