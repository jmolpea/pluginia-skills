# Configuración: ajustes de sitio y de curso (1.2.0)

Nombres tal como se ven en pantalla en español. Manual público con ejemplos y simuladores: https://claude.ai/artifact/CZfR9hAnk2UnCQRgFTBH3R

## Ajustes del sitio
Ruta: Administración del sitio › Extensiones › Extensiones locales › Pluginia Analytics. Una sola página con apartados.

### Licencia
- Clave de licencia (vacío): activa el plugin. Debajo, el estado: «Evaluación: quedan N día(s)», «Válida: caduca el…», «Válida: licencia permanente», «Caducada el…», «No válida: la clave no corresponde a este sitio», «Periodo de evaluación terminado…». Recomendación: si cambia la dirección del sitio, pedir clave de sustitución.

### Proveedor de IA (opcional)
- Proveedor de IA (Desactivado): Anthropic Claude, OpenAI, Google Gemini o DeepSeek. Sin clave no surte efecto.
- Clave de API (vacío): un único campo para el proveedor elegido; al cambiar de proveedor hay que cambiarla.
- Modelo de Claude / OpenAI / Gemini / DeepSeek («Valor recomendado»): solo se ve el del proveedor elegido.
- ID de modelo personalizado (avanzado) (vacío): sustituye al desplegable. Recomendación: vacío.
- Preguntas a la IA por usuario y hora (30): 0 quita el límite. Recomendación: 10–30.

### Asignación de campos demográficos
- Campo de género, de grupo de edad, de tipo de organización, de discapacidad, de grupo étnico (sin asignar): campo de perfil personalizado que guarda el dato. Mejor campos de tipo menú desplegable. Sin asignar, la categoría no se muestra.
- Campo de país (campo propio de Moodle: País): o un campo personalizado; reconoce nombres y códigos.
- Campo de departamento (sin asignar): campo propio de Moodle o personalizado.
Género, edad y tipo de organización sirven además de filtros en el panel del sitio.

### Privacidad y presentación de datos
- Umbral de supresión por privacidad (0): oculta grupos con menos personas. Recomendación: 5 o más si los paneles se comparten.
- Ocultar la identidad de los alumnos (no): «Alumno n.º N» para quien no puede configurar el plugin; sin acciones en lote ni exportación con nombres.
- Conservación de la geolocalización (días) (0): borrado semanal de ubicaciones antiguas.
- Conservación del registro de mensajes (días) (0): borrado semanal del registro; no ponerlo por debajo del plazo mínimo entre mensajes de los cursos.

### Detección de alumnos en riesgo
- Umbral de inactividad (días) (14).
- Umbral de progreso (%) (50).
- Alertas de comportamiento (sí): si se apaga, desaparecen las dos señales tempranas en todos los cursos y sus automatizaciones no encuentran destinatarios.

### Mensajes automáticos
- Enlace a «Plantillas de mensajes automáticos»: textos y valores de partida de las cuatro automatizaciones para todo el sitio. No encienden envíos.
- Color de acento de los mensajes (#1f4e79).
- Mostrar el logotipo del sitio (sí).
- Firma de los mensajes (vacío): texto plano o HTML de firma; admite multiidioma.

### Ajustes de satisfacción
- ID de la pregunta NPS (valor manual), ID del cuestionario inicial (valor manual), ID del cuestionario final (valor manual) (vacíos): fuerzan una actividad concreta en todo el sitio. Recomendación: dejarlos vacíos y nombrar bien las actividades.
Palabras clave de detección: encuesta con «satisfaction», «satisfacción», «feedback» o «valoración» y pregunta 0–10 con «recommend», «recomienda» o «NPS»; prueba inicial con «pre-test», «pretest», «evaluación inicial», «conocimientos previos» o «diagnóstico»; prueba final con «post-test», «posttest», «evaluación final» o «prueba final».

### Horas de formación
- Campo de duración del curso (sin asignar): campo personalizado de curso de tipo Número.

### Exportaciones programadas
- Destinatarios de la exportación (vacío): correos de cuentas de Moodle con acceso al panel del sitio, uno por línea o separados por comas.

## Ajustes de Moodle de los que depende
Seguimiento de finalización (sitio, curso y actividades); cron; almacén de registros estándar; nota de aprobado del curso; base GeoIP en Administración del sitio › Ubicación (opcional); logotipo del sitio; correo saliente y mensajería; plugin Questionnaire para el NPS (opcional).

## Ajustes del curso
Ruta: Curso › Informes › Pluginia Analytics › botón «Configurar mensajes automáticos» (al final de la pestaña Resumen). Requiere el permiso de configurar los mensajes.

### Formulario «Mensajes automáticos»
- Activar los mensajes automáticos (no): interruptor general del curso. Sigue enviando tras la fecha de fin del curso hasta que se desactiva. El personal del curso no los recibe.
- Inactividad para estar en riesgo (días) (0 = valor del sitio): también cambia el panel de alumnos en riesgo, con los mensajes activados o no.
- Progreso para estar en riesgo (%) (0 = valor del sitio).
- Días mínimos entre mensajes (7): solo visible con los mensajes activados.
- Enviar un resumen semanal de este curso a sus tutores (no): llega a todos los que pueden configurar los mensajes del curso.

### Tabla «Automatizaciones»
Columnas: Automatización, Quién lo recibe, Estado (Activada/Desactivada), Texto del mensaje («Texto incorporado», «Plantilla del sitio» o «Texto propio de este curso»), Acciones (Editar, Activar/Desactivar, Restaurar el texto por defecto).

### Formulario de cada automatización
- Ejecutar esta automatización.
- Días desde que abrió la actividad (solo «Vista, sin completar»; 7; 1–60).
- Caída de la actividad (%) (solo «Caída de actividad»; 70; 20–100).
- Asunto (máx. 200).
- Plantilla del mensaje (texto plano con marcadores).
- Redactar con IA (si hay IA configurada).
- Marcadores disponibles.
- Vista previa (alumno de ejemplo); se actualiza al guardar.

### Otros elementos de la página
- Enviar mensajes ahora: procesa el curso al momento respetando el plazo mínimo. Envía mensajes reales.
- Qué pasó después de los mensajes.
- Historial de mensajes (últimos 20).

## Recomendaciones por situación
| Situación | Configuración sugerida |
|---|---|
| Solo administración ve los paneles | Valores de fábrica |
| El profesorado gestiona a sus alumnos en riesgo | Dar al rol de profesor el permiso de ver nombres de alumnos en riesgo |
| El profesorado ve cifras pero no nombres | Mantener permisos de fábrica, o dar el permiso y activar «Ocultar la identidad de los alumnos» |
| Paneles compartidos con terceros | Umbral de supresión 5–10; exportaciones anonimizadas |
| Cursos cortos (2–4 semanas) | Inactividad de 4–7 días en el curso; plazo mínimo 3–5 días |
| Cursos largos | Inactividad 14–21; plazo mínimo 14–21 |
| Alumnado en varios idiomas | No personalizar las plantillas, o usar bloques multiidioma |
| Curso terminado | Desactivar los mensajes automáticos del curso |
| Sitio muy grande con tarea horaria lenta | Valorar apagar «Alertas de comportamiento» |
