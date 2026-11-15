# Límites y valores de fábrica de AI Live Session 1.0.0

Verificados leyendo el código de la versión 1.0.0 (interna 2026111301) el 15-11-2026. «Fijo» significa que no hay ajuste en pantalla para cambiarlo.

## Licencia
| Dato | Valor |
|---|---|
| Evaluación sin clave | 15 días desde el primer uso, con todas las funciones |
| Comprobación | Sin conexión, ligada a la dirección del sitio; cambiar de dirección exige otra clave |

## Ajustes del sitio
| Ajuste | De fábrica | Límite real |
|---|---|---|
| Proveedor de chat | OpenAI | OpenAI, Anthropic, Gemini o DeepSeek |
| Modelos ofrecidos | Todo el catálogo del proveedor | Si no se marca ninguno, se ofrece todo |
| Proveedor de reserva | Ninguno | Solo conversación en vivo; se ignora si coincide con el proveedor del modelo de la actividad |
| Proveedor de TTS | OpenAI | OpenAI, Gemini, voces del navegador o sin voz |
| Un tutor valida las notas | Activado, sin bloquear | Con avisos, siempre espera a un tutor |
| Moderación de OpenAI | Activada | Solo con modelos de conversación de OpenAI; si el filtro falla, no bloquea |
| Máximo de tokens por llamada | 4096 | Mínimo efectivo 256; se eleva solo para modelos que razonan |
| Tiempo de espera | 120 s | Mínimo efectivo 30 s |
| Llamadas por usuario y minuto | 30 | Mínimo efectivo 1 (0 no es «sin límite») |
| Llamadas por minuto, todo el sitio | 2000 | Mínimo efectivo 1; cuenta a todos los proveedores juntos |

## Catálogo de modelos (1.0.0)
| Proveedor | Recomendado | Otros |
|---|---|---|
| OpenAI | GPT-6 Sol | GPT-6 Luna (económico), GPT-6 Astra (premium) |
| Anthropic | Claude Sonnet 5 | Claude Haiku 4.5 (económico), Claude Opus 5.5 (premium), Claude Opus 5 |
| Gemini | Gemini 3.8 Flash | Gemini 3.5 Flash-Lite (económico), Gemini 3.1 Pro (vista previa) |
| DeepSeek | DeepSeek V4.1 Flash (conversación) y V4 Pro (evaluación) | — |
Los modelos de generaciones anteriores siguen funcionando en actividades que ya los usaban; algunos retirados por el proveedor se sustituyen solos por el actual. DeepSeek no lee imágenes ni ofrece voz; Anthropic no ofrece voz.
Voces: OpenAI 9 (Alloy, Ash, Coral, Echo, Fable, Onyx, Nova, Sage, Shimmer); Gemini 8 (Aoede, Charon, Fenrir, Kore, Leda, Orus, Puck, Zephyr); navegador o sin voz: «Automática».

## Ajustes de la actividad
| Ajuste | De fábrica | Límite |
|---|---|---|
| Pasos de la sesión | Vídeo, práctica y conversación | 3 opciones |
| Intentos permitidos | 2 | 0 = sin límite; por bloque; cuenta el mejor |
| Velocidad máxima | 1.5x | 1x, 1.25x, 1.5x o 2x |
| Subtítulos | Sí | Solo YouTube y Vimeo |
| Tiempo que el reloj puede detenerse | 15 min | Total por intento; 0 = nunca se detiene |
| Puntuación máxima | 100 | Usar tipo «Puntuación» |
| Un tutor valida la nota | El valor del sitio | Fijo si el administrador lo bloquea |

## Bloque
| Dato | De fábrica | Límite |
|---|---|---|
| Bloques por sesión | 1 | Mínimo 1; sin máximo fijado |
| Fuente del vídeo | YouTube | YouTube, Vimeo o archivo |
| Archivo de vídeo | — | MP4 o WebM, 1 archivo; tamaño según el límite de subida del sitio |
| Inicio / final | 0:00 / obligatorio | Final posterior al inicio |
| Título del bloque | Bloque N | 255 caracteres |
| Opciones por pregunta | 4 filas | Mínimo 2; se añaden de 2 en 2 |
| Puntos por pregunta | 1 | Las encuestas no puntúan |
| Aviso de tramo sin preguntas | — | Más de 5 minutos (fijo) |
| Preparación máxima / mínima | 10 min / 0 | Mínima no mayor que máxima |
| Entregable | Una imagen | Imagen PNG o JPG, 1 archivo, 10 MB; texto; o nada |
| Duración de la conversación | 10 min | Mayor que 0 |
| Tono | Neutro | Exigente, Neutro, Acompañante |
| Imagen propia del avatar | — | PNG o JPG, 2 MB (no SVG) |
| Criterios de la rúbrica | 3 filas vacías | Al menos 1; pesos que sumen 100 |
| Pesos de la nota | 30 / 20 / 50 | Entre 0 y 100; deben sumar 100 |

## Tiempos y tolerancias (fijos)
| Dato | Valor |
|---|---|
| Informe de posición del vídeo | Cada 10 s mientras se reproduce |
| Margen para avanzar el vídeo | Unos 5 s de tolerancia; como mucho 30 s de crédito por informe |
| Fin del vídeo | Cuenta a 3 s del final |
| Guardado automático de la preparación | Cada 15 s |
| Gracia tras acabar la preparación | 20 s |
| Gracia tras acabar la conversación | 45 s |
| Silencio del navegador para detener el reloj | 90 s |
| Tiempo devuelto por fallo de la IA | Hasta 120 s por fallo y 600 s por conversación |
| Espera máxima de un turno en el servidor | 45 s (o el tiempo de espera del sitio, si es menor) |
| Espera máxima de la voz | 25 s |
| Espera máxima de la moderación | 10 s |
| Espera del navegador por un turno | 120 s, con 2 reintentos automáticos |
| Reintentos del servidor ante fallo transitorio del proveedor | Hasta 3 |
| Cierre de conversaciones abandonadas | Tarea cada 5 min |
| Evaluación considerada atascada | 30 min |
| Sondeo del resultado en la página | Cada 5 s, 120 veces (10 min); después hay que recargar |

## Texto y recortes (fijos)
| Dato | Valor |
|---|---|
| Respuesta del alumno por turno | 5.000 caracteres |
| Notas de la preparación | 20.000 caracteres (al avatar llegan 4.000) |
| Texto entregado | 20.000 caracteres (al avatar llegan 6.000; al análisis, 20.000) |
| Cada dato corregido | 500 caracteres |
| Frase del avatar | Tope de salida corto, pensado para 1 a 3 frases |
| Conversación enviada a evaluar | Unos 60.000 caracteres; se conserva el final y se omite el principio |
| Misión enviada a evaluar | 6.000 caracteres |
| Instrucciones para la evaluadora | 8.000 caracteres |
| «Qué debe mostrar la imagen» | 4.000 caracteres |
| Resumen de cada bloque anterior para el avatar | 600 caracteres |
| Transcripción para borradores | 30.000 caracteres |
| Palabras mínimas del alumno | 20; menos genera aviso. Con 0 no se llama a la IA |

## Cuotas (fijas)
| Dato | Valor |
|---|---|
| «Evaluar de nuevo» | 5 min entre peticiones y 5 al día por tutor e intento |
| Borradores con IA | 30 por docente cada 24 h; hasta 8 preguntas; rúbrica de 3 a 5 criterios |
| Indicación del docente en un borrador | 2.000 caracteres |
| Problemas técnicos por intento | 50; detalle de 500 caracteres; se borran a los 180 días |
| Lista de problemas técnicos | Los 200 más recientes de la actividad |
| Informe de progreso | 50 alumnos por página |
| Excepciones | Una por usuario y una por grupo; intentos de 1 a 20 o ilimitado |

## Consumo orientativo
Cada turno de conversación hace dos llamadas (texto y voz de servidor): unas 8 por minuto y alumno. Además, por intento: una apertura, un análisis de entregable y una evaluación; y un comentario general por sesión con varios bloques. El plugin no calcula el coste en dinero.
