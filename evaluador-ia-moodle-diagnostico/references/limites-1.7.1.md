# Límites y valores por defecto: 1.7.1

Verificados en el código de la versión 1.7.1 el 15-11-2026. Sin cambios respecto a 1.7.0.

## Cómo interpretar los valores
Distinguir cuatro cosas: límite del formulario, carga permitida por Moodle o el servidor, lectura del plugin y presupuesto del proveedor. Aumentar el máximo de subida de Moodle no aumenta lo que lee el plugin.
Los tamaños en MB son múltiplos de 1.048.576 bytes.
Ninguno de estos límites se puede cambiar desde la configuración, salvo las cuotas.

## Lectura de entregas
| Elemento | Límite o tratamiento verificado |
|---|---|
| Prompt docente | Máximo 16.000 caracteres, comprobado en el navegador. Se guarda como texto sin formato. Vacío = plantilla por defecto. |
| Descripción de la tarea | Primeros 8.000 caracteres tras quitar el HTML. Sin imágenes, adjuntos ni enlaces. |
| Texto en línea | Hasta 150.000 caracteres, sin formato. |
| TXT | Hasta 150.000 caracteres. Sin tope de tamaño de archivo propio. |
| PDF | Hasta 20 MB. Texto hasta 150.000 caracteres. Hasta 5 imágenes incrustadas por PDF. |
| Imágenes dentro de PDF | Hasta 1 MB cada una; solo las que son JPEG o PNG tal cual. No se convierte cada página en imagen: un escaneado sin texto no aporta texto, y los gráficos vectoriales no llegan. |
| DOCX | Hasta 20 MB y 150.000 caracteres. Texto y tablas del cuerpo del documento. Las imágenes no se envían. |
| XLSX | Hasta 20 MB, 150.000 caracteres y 2.000 filas por hoja. Valores almacenados (el resultado, no la fórmula). Sin gráficos ni imágenes. |
| PPTX | Hasta 20 MB, 150.000 caracteres y 200 diapositivas. Texto de diapositivas y notas del orador. Sin imágenes ni diseño. |
| JPG, JPEG, PNG sueltos | Hasta 4 MB por archivo. Se comprueba el formato real, no solo la extensión. |
| Audio | MP3, M4A, WAV, OGG y FLAC; hasta 25 MB por archivo; transcripción limitada a 150.000 caracteres. Solo si la transcripción está activada y hay clave de OpenAI utilizable. |
| Otros formatos | DOC, XLS, PPT, ODT, RTF, ZIP, GIF, vídeo, etc.: se omiten aunque Moodle permita subirlos. |

## Topes del conjunto de la entrega
| Elemento | Límite |
|---|---|
| Texto total enviado | 200.000 caracteres, separadores incluidos. Se pierde el final. |
| Imágenes totales enviadas | 5 por entrega, sumando las de los PDF y las sueltas. Se conservan las primeras según el orden de los archivos. |
| Orden | Primero el texto en línea; después los archivos por orden alfabético de nombre. |

No recomendar renombrar archivos como solución de fondo a una entrega demasiado extensa.
Un archivo que supera su tope de tamaño se omite entero, sin aviso en la tarea. Si era lo único de la entrega, queda la nota de «no se ha podido leer».
No afirmar que convertir a PDF conserva lo visual: comprobar texto e imágenes con una prueba.

## Cuotas y valores de fábrica
| Ajuste | De fábrica | Notas |
|---|---|---|
| Límite diario de peticiones para esta tarea | 50 | Mínimo 1. Se reinicia a medianoche, hora del sitio. |
| Número máximo de calificaciones por alumno | 3 | Mínimo 1. Por alumno y tarea. No se reinicia. |
| Umbral mínimo de confianza | 7 | De 1 a 10. |
| Máximo de peticiones por hora (todo el sitio) | 100 | Desactivado de fábrica. Hora de reloj, hora del sitio. Con 0 o negativo no se aplica. |
| Máximo de peticiones por hora (por usuario) | 10 | Desactivado de fábrica. Suma todas las tareas del alumno. Con 0 o negativo no se aplica. |
| Retraso opcional de la respuesta | 1 hora | Fijo; no se puede elegir otra duración. Desactivado de fábrica. |
| Periodo de prueba | 15 días | Desde la instalación. |

Todas las cuotas cuentan correcciones guardadas, no intentos fallidos. Una entrega que choca con una cuota no se corrige después sola.
Las comprobaciones de cuota y el incremento del contador no son simultáneos: con muchas entregas a la vez, el total puede superar ligeramente el tope.
No confundir «calificaciones por alumno» del plugin con los intentos de entrega que permite la tarea de Moodle.

## Modelos disponibles en los desplegables
| Proveedor | De fábrica | Otras opciones |
|---|---|---|
| OpenAI | GPT-5.6 Luna | GPT-5.1, GPT-5 Mini, GPT-5 Nano, GPT-4.1, GPT-4.1 Mini, GPT-4.1 Nano (no recomendado), GPT-4o, GPT-4o Mini |
| Anthropic | Claude Sonnet 4.6 | Claude Opus 4.8, Claude Sonnet 5, Claude Haiku 4.5 |
| Google Gemini | Gemini 2.5 Flash | Gemini 2.5 Pro, Gemini 2.5 Flash-Lite (no recomendado), Gemini 2.0 Flash |
| DeepSeek | DeepSeek Chat | DeepSeek Reasoner |

Que un modelo esté en la lista no garantiza que el proveedor lo siga ofreciendo. Para otro modelo, usar «Identificador de modelo personalizado».

## Respuesta del proveedor
Presupuesto de salida: 3.000 tokens, con o sin imágenes. Para los modelos de OpenAI que el plugin trata como de razonamiento (familia GPT-5 y serie «o»): 8.000 tokens, que incluyen el razonamiento interno.
Estas cifras no son caracteres ni el límite de entrada del modelo. El plugin no comprueba que la entrada quepa en el modelo elegido: 200.000 caracteres pueden superar la capacidad de un modelo pequeño, y entonces el proveedor rechaza la petición.
Una rúbrica con muchos criterios, que la IA debe repetir en su respuesta, presiona ese presupuesto. Sin la respuesta original ni el motivo de finalización, tratar el truncamiento como hipótesis. Con modelos que razonan internamente, parte del presupuesto se gasta en razonar.
Tiempo de espera: 45 segundos para la corrección y 120 para la transcripción. Si se agota, la entrega queda sin corregir.
Reintentos: ninguno, ante ningún tipo de fallo.
Confianza por defecto si la IA no la indica: 5.

## Comprobación de integridad
Antes de declarar ausencia de aprendizaje, localizar la evidencia: texto, tabla, fórmula, imagen, gráfico, audio o página escaneada.
Comprobar si ese formato la transporta, si supera algún límite y si el proveedor acepta ese contenido.
Si solo una parte no se puede leer, el plugin corrige el resto y no avisa de la omisión.
