# Configuración de AI Viva (versión 1.3.0)

Nombres tal como se ven en pantalla en español. Revisado el 15-11-2026. Manual público con fichas, maquetas y simuladores: https://claude.ai/artifact/RckemidnHhdYikr8HM2XHQ

## Ajustes del sitio
Dónde: Administración del sitio › Extensiones › Módulos de actividad › AI Viva. Una sola página con siete apartados. Solo administradores.

### Licencia
- Clave de licencia. Vacía = 15 días de evaluación. Debajo se ve el estado (evaluación, válida, caducada, no válida). Recomendación: pedir clave nueva antes de cambiar la dirección del sitio.

### Claves API de OpenAI
- Clave API principal de OpenAI. Imprescindible. Se guarda cifrada y no vuelve a mostrarse; el campo vacío no significa que falte. Recomendación: clave exclusiva para Moodle y límite de gasto mensual en OpenAI.
- Clave API secundaria de OpenAI (opcional). Si existe, la usan la transcripción y las voces. Solo para separar gasto o cuotas.

### Modelos de IA disponibles
- Modelos disponibles para el profesorado. Qué modelos salen en los desplegables de las actividades. Al desmarcar uno, las actividades que lo usaban pasan al recomendado o al primero permitido. Recomendación: desmarcar GPT-6 Astra si preocupa el gasto.
- Estimación de costes. Solo informativo.

### Seguridad
- Activar moderación de contenido de OpenAI. Filtra los textos del alumno antes de enviarlos. Un bloqueo en el tribunal permite repetir la respuesta; un bloqueo en la evaluación deja el intento pendiente y hay que calificar a mano. Recomendación: activado, salvo materias que el filtro marque por error.
- Máximo de tokens por llamada a la API. Longitud máxima de las respuestas de análisis y evaluación. No limita lo que la IA lee. Subir solo si aparece el error de respuesta cortada.
- Identificación del estudiante. Informativo: nombre y correo no se envían; el contenido sí.

### Almacenamiento y retención
- Tamaño máximo global de video (MB). Techo del sitio. Debe ser coherente con los límites de subida del servidor.
- Conservación de grabaciones por defecto (días). Valor propuesto en actividades nuevas; no cambia las existentes.

### Aviso RGPD
- Texto del aviso RGPD. Vacío = aviso incluido en el idioma del alumno. Un texto propio se muestra igual en todos los idiomas y debe decir qué se envía a OpenAI. El plazo de conservación de cada actividad se añade solo.

### Avanzado
- Tiempo de espera de la API (segundos). Subir solo si fallan por tiempo los documentos muy largos.
- Máximo de llamadas a la API por usuario por minuto. No bajar de 15; nunca 0.

## Ajustes de la actividad
Dónde: en el curso, Añadir una actividad o un recurso › AI Viva; después, Configuración en el menú de la actividad. Profesor con edición o gestor.

### General
- Nombre de la actividad y Descripción. La IA recibe ambos como «el encargo». Recomendación: describir en la descripción qué trabajo se defiende.
- Número máximo de intentos. El siguiente intento exige que el anterior esté calificado y publicado; cuenta la mejor nota publicada.
- Apertura · Cierre. Fuera de plazo no se puede empezar ni continuar, salvo un tribunal ya iniciado.

### Paso 1 — Documento PDF
- Instrucciones para el estudiante. Las ve el alumno y las recibe la IA.
- Prompt de análisis IA. Criterios para leer el documento; también se dan al evaluador final. Vacío = análisis genérico.
- Tamaño máximo del PDF (MB).
- Modelo IA para análisis de PDF.

### Paso 2 — Videopresentación
- Instrucciones para el estudiante.
- Prompt de análisis de video IA. Criterios para la presentación; también se dan al evaluador final.
- Duración máxima de la presentación.
- Tamaño máximo del archivo de video (MB). No puede superar el global.
- Modelo IA para el tribunal. Aparece en este apartado pero sirve para dos cosas: analizar la presentación y generar el informe y las preguntas del tribunal.

### Paso 3 — Tribunal de Defensa
- Duración de la sesión del tribunal (minutos). Sin pausa y sin final anticipado.
- Prompt de evaluación final. Instrucciones para quien pone la nota.
- Modelo IA para evaluación final. Una sola llamada por intento; es donde más rinde un modelo mejor.

### Miembro del tribunal 1, 2 y 3
- Nombre, Rol / Cargo (vienen en inglés: cambiarlos), Personalidad y estilo de interrogación, Voz TTS, Avatar y Subir imagen de avatar personalizado.
- El miembro 1 abre y cierra la sesión. Recomendación: tres perfiles complementarios (método, contenido, aplicación práctica) y tres voces distintas.

### Calificación y flujo de trabajo
- Calificación máxima. No cambiarla con intentos ya calificados: las notas guardadas no se reescalan.
- Peso del documento, de la presentación y del tribunal (%). Deben sumar 100.
- Retener las calificaciones para revisión del profesor. Recomendación: activado siempre que la nota cuente.
- Notificar al estudiante cuando se publique la nota.

### Seguridad de la actividad
- Conservar las grabaciones (días). Ajustar al plazo de reclamaciones; ver reglas exactas en el documento de límites.
- Restricciones de contenido adicionales (opcional). Reglas que se añaden a todas las instrucciones de la IA de la actividad.

### Finalización de la actividad
- El estudiante debe completar los tres pasos (documento, presentación y tribunal).

## Excepciones de usuario/grupo
Dónde: menú de la actividad › Excepciones de usuario/grupo › Añadir excepción.
Campos: Tipo de excepción, Usuario o Grupo, Número máximo de intentos, Apertura, Cierre. Hay que rellenar al menos uno de los tres últimos.

## Recomendaciones por escenario
| Escenario | Configuración sugerida |
|---|---|
| Defensa que cuenta para la nota | Retener notas; 1 o 2 intentos; Sol en todo (Astra en evaluación si los trabajos son largos); conservación igual al plazo de reclamaciones |
| Práctica o ensayo | Puede publicarse sola; 3 intentos; Luna en documento y tribunal; duraciones de 5 minutos |
| Grupo muy numeroso | Luna o Sol; presentación y tribunal cortos; límite de gasto en OpenAI; cierres escalonados por grupos |
| Énfasis en la defensa oral | Pesos del estilo 10 · 20 · 70; prompt de evaluación que pida coherencia entre lo escrito y lo dicho |
| Adaptaciones individuales | Excepción de usuario con más plazo o un intento más; el tiempo del tribunal no se puede ampliar por alumno |

## Cómo escribir buenos prompts
Decir qué se valora y con qué importancia relativa dentro del paso; evitar pedir una nota global, porque la calcula el plugin con los pesos.
Poner los criterios del documento en el prompt del paso 1 y los de la presentación en el del paso 2; el evaluador final los recibe los dos.
Usar las restricciones adicionales para reglas transversales (trato, aspectos que no deben valorarse).
No incluir datos personales ni soluciones que no deban aparecer en las preguntas: los examinadores trabajan con ese contexto.
