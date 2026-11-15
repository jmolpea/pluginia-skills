# Límites y valores de fábrica: Pluginia Analytics 1.1.1

Valores leídos en la versión 1.1.1 el 15-11-2026. Un límite documentado es un hecho; que haya causado un caso concreto es una conclusión aparte.

## Datos y actualización
| Elemento | Valor verificado |
|---|---|
| Recalculo de datos | Cada hora, en punto (hora del servidor; horario editable en Moodle) |
| Caducidad de la copia calculada | 3 horas |
| Aviso de datos desactualizados | Copia con más de 2 horas |
| Vista filtrada del panel del sitio | Se conserva 1 hora |
| Cursos incluidos | Solo visibles; se excluye la portada |
| Gráfico de usuarios activos por semana | Últimas 12 semanas |
| Mapa de calor de horarios | Eventos de los últimos 90 días |
| Evolución y cohortes del sitio | Últimos 12 meses |
| Tabla de cursos del panel del sitio | 50 por página |
| Clasificación de cursos | 5 mejores y 5 peores |
| Comparación de cursos | De 2 a 5 cursos |
| Países en la tabla del panel del sitio | Los 15 primeros |
| Lista «quién completó esta actividad» | Hasta 100 personas; respeta grupos separados |
| Valores distintos por categoría demográfica | Hasta 50; el resto se agrupa en «Otros» |

## Alumnos en riesgo
| Elemento | Valor |
|---|---|
| Umbral de inactividad (sitio) | 14 días; 0 o vacío = 14 |
| Umbral de progreso (sitio) | 50 %; fuera de 1–100 = 50 |
| Valores del curso | 0 = usar el del sitio; progreso admitido 1–100; inactividad máxima 9.999 días (un valor mayor se guarda como 9.999) |
| Alertas de comportamiento | Activadas de fábrica |
| «Vista, sin completar» | 7 días de fábrica; permitido 1–60; ventana de 90 días |
| «Caída de actividad» | 70 % de fábrica; permitido 20–100; compara los últimos 7 días con la media semanal de los 14 anteriores; exige al menos 20 eventos en esos 14 días |
| Alumnos listados por grupo en el panel | 50; el resto solo se cuenta |
| Exportación de alumnos en riesgo | Todos los alumnos de cada grupo (hasta 5.000 por grupo); en 1.1.0, solo los 50 listados |
| Cola de intervención | Hasta 200 cursos (por orden alfabético) y 500 filas; solo cursos visibles con datos ya calculados |
| Tiempo dedicado | Estimación: pausas de más de 30 minutos cierran sesión; cada sesión suma al menos 5 minutos |

## Mensajes automáticos
| Elemento | Valor |
|---|---|
| Hora de la tarea diaria | 09:00 del servidor (editable) |
| Envíos por curso en cada ejecución | Hasta 200; el resto queda para la siguiente |
| Candidatos examinados por automatización | Hasta 5.000 |
| Días mínimos entre mensajes | 7 de fábrica; opciones 1, 2, 3, 5, 7, 14, 21, 30; mínimo efectivo 1 |
| Tope de mensajes por alumno | No existe |
| Fechas del curso | No se tienen en cuenta: se envía también tras la fecha de fin mientras esté activado |
| Personal del curso | No recibe mensajes automáticos (desde 1.1.1) |
| Automatizaciones encendidas de fábrica | Nunca accedió, Inactivo |
| Asunto | Obligatorio; máximo 200 caracteres |
| Plantilla | Obligatoria; texto plano |
| Marcadores (13) | {firstname} {lastname} {fullname} {coursename} {courseurl} {progress} {activities_done} {activities_total} {last_access} {days_inactive} {days_enrolled} {pending_count} {pending_activities} |
| {pending_activities} | Nombra hasta 3 actividades |
| {progress} | Porcentaje sin decimales |
| {last_access} | Fecha, o «nunca» si no ha entrado; {days_inactive} queda vacío en ese caso |
| Historial en pantalla | 20 últimos |
| Marcadores del mensaje manual del panel | {firstname} {fullname} {coursename} {progress} {last_access} |
| Color de acento | #1f4e79 de fábrica; solo se aceptan colores de 3 o 6 cifras hexadecimales |
| Logotipo en los mensajes | Activado; sin logotipo se muestra el nombre del sitio |
| Resumen semanal | Lunes 08:00; periodo de 7 días; no se envía si no hubo nada |
| Exportación programada | Viernes 07:00; destinatarios: cuentas de Moodle no suspendidas con acceso al panel del sitio; la dirección no distingue mayúsculas |
| Limpieza por conservación | Domingo 03:00; 0 = conservar siempre (geolocalización y registro de mensajes) |

## Asistente de IA
| Elemento | Valor |
|---|---|
| Proveedor de fábrica | Desactivado |
| Longitud de la pregunta | 500 caracteres; lo que excede se recorta |
| Memoria de la conversación | 6 turnos anteriores, 2.000 caracteres por turno |
| Resumen de cifras enviado | Hasta 50 KB; si excede se van quitando secciones (primero demografía, ciudades, países…) |
| Cursos detallados en el panel del sitio | Los 25 más grandes (10 si no caben) |
| Grupo mínimo enviado | 2 personas en país/ciudad; 5 en demografía; o el umbral de supresión si es mayor |
| Etiquetas de texto | Recortadas a 80 caracteres |
| Respuesta | Hasta 4.096 tokens de salida; se le pide de 2 a 6 frases, texto plano, en el idioma de la pregunta |
| Tiempo de espera | 60 segundos (10 para conectar); sin reintentos por fallo de red; un único reintento sin parámetros opcionales si el proveedor los rechaza |
| Límite por usuario | 30 preguntas por hora; 0 = sin límite; compartido entre el chat y «Redactar con IA»; se consume aunque el proveedor falle |
| «Redactar con IA» | Toma hasta 1.500 caracteres del texto actual; pide de 60 a 120 palabras |
| Modelo personalizado | Solo letras, cifras, punto, guion, guion bajo, dos puntos y barra; manda sobre el desplegable y no se vacía al cambiar de proveedor |

Modelos del desplegable (el primero es el recomendado):
- Claude: claude-opus-5-5, claude-sonnet-5-5, claude-fable-5-1, claude-haiku-4-5.
- OpenAI: gpt-6.1-sol, gpt-6-astra, gpt-6-luna.
- Gemini: gemini-3.8-flash, gemini-3.5-flash, gemini-3.5-flash-lite, gemini-3.1-pro-preview, gemini-2.5-pro, gemini-2.5-flash.
- DeepSeek: deepseek-flash, deepseek-v4-pro.
Destinos de red: api.anthropic.com, api.openai.com, generativelanguage.googleapis.com, api.deepseek.com. El servidor de Moodle debe poder alcanzarlos.

## Privacidad y licencia
| Elemento | Valor |
|---|---|
| Umbral de supresión | 0 de fábrica (desactivado); recomendado 5 o más |
| Efecto | Panel del curso: «≤ N». Sitio, exportaciones e IA: se omite. Filtros con menos personas que el umbral: sin cifras |
| Ocultar la identidad | Desactivado; afecta a quien no puede configurar el plugin |
| Evaluación | 15 días |
| Gracia tras caducar | 30 días, contados desde la fecha de caducidad; la clave vale todo el día de esa fecha |
| Ligadura de la clave | Dirección exacta del sitio |

No hay límites verificados distintos de estos; no inventar topes (por ejemplo, de número de cursos del sitio o de alumnos por curso).
