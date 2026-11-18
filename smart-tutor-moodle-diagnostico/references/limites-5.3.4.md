# Límites y valores de fábrica de Smart Tutor & Support AI 5.3.4
Verificados en el código de la versión 5.3.4 el 18-11-2026, salvo las filas marcadas «(revisado en 5.3.2)», que se comprobaron el 15-11-2026 y no constan cambios desde entonces. «De fábrica» es el valor de una instalación nueva; un sitio actualizado conserva lo que tenía. Salvo que se diga otra cosa, 0 significa «sin límite». Ningún límite ni valor de fábrica cambió entre la 5.3.2 y la 5.3.4.

## Compatibilidad y licencia
| Dato | Valor |
|---|---|
| Moodle | 4.5 a 5.3 |
| Periodo de prueba sin licencia | 15 días, con todas las funciones |
| Licencia | Ligada a la dirección web del sitio; se comprueba sin conexión; puede ser con fecha o vitalicia |
| Proveedores de chat | OpenAI, Anthropic, Google Gemini, DeepSeek y «Compatible con OpenAI (UE o servidor propio)» |
| Búsqueda por significado | OpenAI o Gemini; «Automático» sigue al proveedor del chat; «Desactivado» busca por palabras |
| Voz | OpenAI, Gemini o el navegador del alumno |
| Llamadas en tiempo real | OpenAI o Gemini |

## Chat
| Límite | De fábrica | Notas |
|---|---|---|
| Mensajes por usuario y minuto | 10 | Aviso: «Estás enviando mensajes demasiado rápido. Espera un momento e inténtalo de nuevo.» |
| Mensajes por usuario y día | 200 | Mismo aviso |
| Límite del proveedor de IA | El de la cuenta del cliente | Desde 5.3.3, aviso propio: «Estás enviando mensajes demasiado rápido o el asistente no está disponible temporalmente…». No lo cuenta Moodle |
| Reintento ante un fallo del proveedor | 1 | Desde 5.3.3: solo si la conexión se corta o hay un error interno del proveedor antes de mostrar nada; no tras un tiempo de espera agotado ni tras un rechazo |
| Longitud de un mensaje | 4.000 caracteres | Fijo. Aviso: «Tu mensaje es demasiado largo» |
| Respuesta máxima del tutor | 1.800 tokens | Unas 1.300 palabras; ajustable por sitio y por asistente |
| Respuesta máxima del asistente | 1.000 tokens | Ajustable |
| Temperatura | 0,25 tutor · 0,2 asistente | Muchos modelos recientes la ignoran. De 0 a 2 |
| Preguntas de ejemplo del bloque | 6 | Hasta 200 caracteres cada una (revisado en 5.3.2) |
| Imágenes adjuntas | 20 por participante y día, sumando cursos | PNG, JPEG, GIF o WebP de hasta 5 MB; se reducen antes de enviarse. Aquí 0 equivale a 20 (revisado en 5.3.2) |
| Borrador para revisar | 20.000 caracteres o 5 MB | No se guarda |
| Una respuesta a la vez | — | Aviso: «Todavía estoy terminando la respuesta anterior» |
| Espera del servidor compatible | 180 segundos | Solo proveedor «Compatible» |

## Material del tutor
| Límite | Valor |
|---|---|
| Documentos subidos al asistente | 20 citables y 20 internos; PDF, TXT o MD |
| Trozos de material por pregunta | 8; de ellos se reservan a los documentos subidos los que elija el docente (de 0 a 8; de fábrica 5) |
| Términos poco frecuentes | Una cuarta parte de los trozos se reserva a nombres o términos raros de la pregunta (revisado en 5.3.2) |
| Mensajes con dos o tres pedidos | Desde 5.3.4 cada pedido se busca por separado; el número de trozos no cambia |
| Tamaño de cada trozo | Unos 2.500 caracteres |
| Archivo más grande que se lee | 50 MB (ajuste del sitio) |
| PDF | Las 200 primeras páginas |
| Resto de documentos | 400.000 caracteres, unas 200 páginas (revisado en 5.3.2) |
| Recurso web con documentos | Hasta 300 documentos acompañantes |
| Trozos por asistente | Unos 4.000 (probable: valor interno no visible en pantalla); al superarlo, la actividad queda con error de límite |
| Modo «Todo el curso en cada respuesta» | Pensado para cursos pequeños: todo el texto viaja en cada pregunta y el coste sube; si el curso es demasiado grande se usa la búsqueda |
| Imágenes descritas | Solo si pesan al menos unos 6 KB y miden 120 píxeles de lado; hasta 100 nuevas por pasada y el resto en pasadas siguientes (la ayuda en pantalla del ajuste dice 30; el valor comprobado es 100); hasta 30 por PDF (revisado en 5.3.2); cada imagen se paga una vez |
| Examen del tutor | De 5 a 50 preguntas (de fábrica 30); uno al día por asistente |
| Estados de una actividad | Indexado, Pendiente, Sin texto, Error, Saltado, Excluido, Evaluable (no se indexa) |

## Voz y llamadas
| Límite | De fábrica | Notas |
|---|---|---|
| Grabación más larga | 60 segundos | Mínimo efectivo 5 (revisado en 5.3.2) |
| Minutos de voz por participante y día | 20 | Dictado más lectura; aviso: «Has usado los minutos de voz de hoy» |
| Minutos de voz por curso y mes | 0 | Suma voz y llamadas |
| Minutos de voz del sitio al mes | 0 | Suma voz y llamadas |
| Texto leído en voz alta | 1.200 caracteres por petición | Solo lo que el asistente acaba de decir (revisado en 5.3.2) |
| Velocidad de lectura | 0,8 a 1,3 (1,0) | Por asistente |
| Minutos de llamada por participante y día | 15 | Aviso: «Has usado el tiempo de llamada de hoy» |
| Duración máxima de una llamada | 20 minutos | Con 0, una llamada de Gemini en tiempo real ya no se corta a los 20 minutos (corregido en 5.3.2) |
| Latido de la llamada | Cada 30 segundos | Sin latidos durante 2 minutos, la llamada se da por terminada |
| Motor de la llamada | Paso a paso | Tiempo real necesita clave de OpenAI o Gemini |
| Frases de espera | Sí en el sitio | En cada asistente: encendidas en los nuevos, apagadas en los que ya existían; solo con el motor «Paso a paso» |
| Presentadores | 3 incluidos y hasta 3 propios | Foto JPG, PNG o WebP; vídeos MP4, WebM, GIF o WebP; 10 MB por archivo |

## Soporte por correo
| Límite | De fábrica |
|---|---|
| Consultas por participante y día (por curso) | 3 |
| Minutos entre consultas del mismo participante | 10 |
| Mensajes sin volver a ofrecerlo tras un «no» | 5 |
| Ventana sin duplicados | 24 horas (la consulta repetida devuelve la referencia existente) |
| Consultas por curso y día | 200 (al superarse, el asistente vuelve al enlace de soporte) |
| Mensajes de la conversación incluidos | 6, si se incluye la conversación |
| Borrador sin confirmar | Caduca a las 24 horas |
| Intentos de envío de un correo | 3 |
| Resumen agrupado | Apagado; cada 30 minutos si se activa |
| Prefijo de la referencia | OA, hasta 12 caracteres |

## Visitantes
| Límite | De fábrica |
|---|---|
| Mensajes por dirección | 10 cada 10 minutos |
| Tope diario del sitio | 300 mensajes |
| Longitud del mensaje | 500 caracteres |
| Memoria de la conversación | 4 mensajes |
| Tope por respuesta | 1.500 tokens |
| Conservación de conversaciones | 24 horas |
| Página abierta | A las 4 horas pide recargar («Esta página lleva demasiado tiempo abierta») (revisado en 5.3.2) |
| Puntuación mínima de reCAPTCHA v3 | 0,5 |

## Registro, retención e informes
| Dato | Valor |
|---|---|
| Retención de conversaciones | 30 días en instalaciones nuevas; 0 = no borrar nunca |
| Qué borra | Mensajes, consultas a soporte, valoraciones, llamadas y estadísticas por persona; las cifras por curso del panel se conservan |
| Uso de voz | Se conserva al menos 32 días, porque lo consultan los cupos mensuales |
| Análisis de temas del informe del curso | Semanal (lunes) y hasta 3 manuales al día por curso |
| Presupuesto mensual por asistente | Aviso a los docentes al 80 %; al 100 % pasa al modelo económico, no se detiene, y se vuelve a avisar; se reinicia cada mes |
| Coste del panel y del presupuesto | Estimación con los precios del plugin; la referencia es la factura del proveedor |

## Modelos
Los modelos se escriben a mano en los ajustes; cada campo muestra el recomendado para el proveedor guardado y un enlace a la lista oficial. No dar nombres de modelo de memoria: remitir al recomendado que enseña la pantalla tras guardar el proveedor. Si un proveedor retira un modelo, basta con escribir el nuevo nombre, sin actualizar el plugin.
