# Límites y valores por defecto de Forumia: versión 1.8.3

Verificados leyendo el código de la versión 1.8.3 el 15-11-2026. «Carácter» significa carácter de texto plano, una vez quitado el formato HTML.

## Cómo interpretar los valores
Distinguir tres cosas: lo que Moodle guarda (el mensaje completo del foro), lo que Forumia envía a la IA (recortado) y lo que el proveedor admite o factura. Ampliar un límite de Moodle no cambia lo que Forumia envía.
Los recortes no son configurables. Los límites diarios sí.

## Límites diarios de peticiones
Una petición es una consulta a la IA: una respuesta, un resumen, una reactivación o una evaluación.
| Límite | Dónde se configura | De fábrica | Reglas |
|---|---|---|---|
| Por usuario y foro | «Límite diario de peticiones por usuario» (foro) | 1 | 0 = sin límite. Cuenta las respuestas del asistente a mensajes de ese estudiante en ese foro desde la medianoche del servidor. Solo afecta a la respuesta inmediata. |
| Por foro | «Límite diario de peticiones para este foro» (foro) | El formulario propone el máximo del sitio (100 si no se cambió) | Mínimo 1 con el asistente habilitado. Suma respuestas, resumen, reactivaciones y evaluaciones. |
| Todo el sitio | «Activar límite de frecuencia de todo el sitio» y «Máximo de peticiones por día (todo el sitio)» | Desactivado; 100 | Suma todos los foros. Con 0 o negativo se ignora. |
El día cambia a medianoche, hora del servidor. Las comprobaciones se hacen al ejecutar la tarea, no al publicar el estudiante.
Las respuestas inmediatas que no caben en un límite no se contestan después, y las que estaban en cola se descartan si llegan durante una parada general o una pausa. Las evaluaciones y las reactivaciones sí se retoman otro día.
Las evaluaciones para nota cuentan en el límite del foro aunque el proveedor falle.

## Recortes de lo que se envía a la IA
| Función | Elemento | Máximo |
|---|---|---|
| Todas | Descripción del foro | 500 caracteres |
| Respuesta inmediata | Mensaje del estudiante | 2.000 caracteres |
| Resumen diario | Cada mensaje | 500 caracteres |
| Resumen diario | Conjunto | 4.000 caracteres; se corta el final (lo más reciente) |
| Reactivación | Cada mensaje del debate | 500 caracteres |
| Reactivación | Conjunto | 4.000 caracteres; se conserva lo más reciente |
| Reactivación | Nombre del foro y asunto del debate | 200 caracteres cada uno |
| Calificación | Mensajes del estudiante | Los 20 primeros por orden de fecha; 2.000 caracteres cada uno |
| Calificación | Mensaje contestado (contexto) | 600 caracteres |
| Calificación | Asunto del debate | 200 caracteres |
| Calificación | Conjunto | 12.000 caracteres; se corta el final |
| Calificación | Justificación guardada | 1.000 caracteres |
No se envían imágenes ni adjuntos de los mensajes: solo texto.

## Longitud de las respuestas
- OpenAI con modelos de la familia GPT-5: presupuesto de 8.000 tokens de salida, que incluye el razonamiento interno del modelo, con esfuerzo de razonamiento bajo. No se envía temperatura.
- Gemini 2.5 Flash y Pro, y DeepSeek Reasoner (modelos que razonan): 8.000 tokens de salida, que incluyen el razonamiento (desde 1.8.3; antes 800, con lo que la respuesta podía llegar vacía y no publicarse). Temperatura 0,7.
- OpenAI con modelos anteriores, Anthropic, Gemini 2.5 Flash-Lite y DeepSeek Chat: 800 tokens de salida como máximo (del orden de 600 palabras). Temperatura 0,7 en OpenAI anteriores, Gemini y DeepSeek.
- Los prompts de fábrica piden entre 80 y 150 palabras (inmediato), 150 a 250 (diario) y 60 a 120 (reactivación).
No verificado contra los proveedores: el cambio de 1.8.3 se basa en su documentación, no en una ejecución real. Si con un modelo que razona siguen faltando respuestas, la prueba controlada es cambiar solo el modelo a Gemini 2.5 Flash-Lite o DeepSeek Chat.

## Tiempos
| Concepto | Valor |
|---|---|
| Espera de la respuesta inmediata | Siguiente pasada del cron |
| «Retrasar la respuesta IA 1 hora» | Aproximadamente 1 hora, fija |
| Tiempo máximo de una consulta | 30 segundos; 120 con OpenAI de la familia GPT-5, Gemini 2.5 Flash y Pro, y DeepSeek Reasoner |
| Reintentos ante error | Ninguno, salvo las evaluaciones para nota en pasadas posteriores |
| Pausa por exceso de frecuencia del proveedor | 1 hora, todo el sitio |
| Resumen diario | 08:00 (horario editable en tareas programadas); mensajes de las últimas 24 horas |
| Comprobación de inactividad | 09:30 diaria |
| Calificación por IA | Cada hora, minuto 20; hasta 50 evaluaciones por foro y pasada |
| «Horas antes de evaluar a un estudiante» | 12 de fábrica; entre 1 y 720 |
| «Días de inactividad antes de publicar» | 7 de fábrica; mínimo 1 |
| «Días entre publicaciones de reactivación» | 7 de fábrica; mínimo 1 |
| Periodo de prueba | 15 días desde la instalación |

## Proveedores y modelos de la lista
| Proveedor | Modelos que ofrece la página de ajustes | De fábrica |
|---|---|---|
| OpenAI | GPT-5.6 Luna, GPT-5.1, GPT-5 mini, GPT-5 nano, GPT-4.1 mini, GPT-4.1 nano, GPT-4o mini, GPT-4o | GPT-5.6 Luna |
| Anthropic | Claude Haiku 4.5, Claude Sonnet 4.6, Claude Sonnet 5, Claude Opus 4.8 | Claude Haiku 4.5 |
| Google Gemini | Gemini 2.5 Flash-Lite, Gemini 2.5 Flash, Gemini 2.5 Pro | Gemini 2.5 Flash (la lista lo rotula como el de fábrica y a Flash-Lite como el más económico) |
| DeepSeek | DeepSeek Chat, DeepSeek Reasoner | DeepSeek Chat |
Las listas son cerradas: no se puede escribir otro modelo.
«Endpoint de API» solo existe para OpenAI. Debe empezar por https y pertenecer a api.openai.com o a un subdominio de openai.azure.com. No se admiten direcciones numéricas, servidores propios ni otros proveedores compatibles. De fábrica: la dirección oficial de OpenAI para conversaciones.

## Calificación
- Una evaluación por estudiante y foro, sin reevaluación.
- Nota: número entero entre 0 y la nota máxima del foro. Un decimal válido se redondea; un valor fuera de rango se rechaza, no se ajusta.
- Una sugerencia solo puede aceptarse si la nota máxima del foro es la misma que cuando se evaluó.
- Solo foros con calificación del foro completo en puntos y calificación simple directa.

## Licencia
Ligada a la dirección exacta del sitio (se ignora la barra final). Comprobación sin conexión. Estados en pantalla: «Prueba - quedan N día(s)», «Válida — caduca el…», «Válida — licencia permanente», «Caducada el…», «No válida — la clave no coincide con este sitio», «No configurada».
