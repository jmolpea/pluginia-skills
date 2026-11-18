# Configuración de Smart Tutor & Support AI (5.3.4)
Nombres tal como aparecen en pantalla en español. Detalle y ejemplos de cada ajuste, con simuladores: https://claude.ai/artifact/Ko6vHpvgSzUBNEcF9Nxs8R

## Dónde está cada cosa
| Qué | Dónde | Quién |
|---|---|---|
| Ajustes del sitio (siete pestañas) | Administración del sitio › Extensiones › Bloques › Smart Tutor & Support AI | Administrador |
| Panel de uso, informes y herramientas de prueba | Enlaces al final de la barra de pestañas | Administrador o gestor con el permiso de configuración global |
| Ajustes del bloque (nombre y aspecto) | Engranaje del bloque › Configurar | Quien edita el curso |
| Configuración del asistente | Menú «Más» del curso (o ajustes de la categoría o de la portada); con varios asistentes en el curso, un enlace por cada uno con su nombre | Docente con edición, gestor |
| Tareas programadas | Administración del sitio › Servidor › Tareas › Tareas programadas | Administrador |
| Base de conocimiento del aula | Enlace en la sección «Base de conocimiento» de la configuración | Docente con edición, gestor |
| Informe «Asistente de IA: uso y temas» | Curso › Informes | Docentes, gestor |

## Sitio · General e IA
- «Clave de licencia»: activa el plugin; debajo se ve el estado (prueba, válida, caducada, no válida para este sitio). Si cambia la dirección del sitio hace falta otra clave.
- «Habilitar el plugin» (sí): interruptor general. Apagado, desaparece el chat y también se detienen la voz y las llamadas.
- «Proveedor de IA» (OpenAI): tras cambiarlo hay que guardar; la página recarga las claves y los modelos recomendados.
- Claves de API: solo es imprescindible la del proveedor elegido. Las de OpenAI y Gemini se ven siempre porque sirven además para la búsqueda por significado, la voz y las llamadas.
- Servidor compatible (dirección, clave, espera de 180 s): para Azure OpenAI en Europa, Mistral o un modelo propio. Lo configura el equipo técnico.
- «Proveedor de embeddings» (Automático): con Anthropic o DeepSeek hay que elegir OpenAI o Gemini y poner su clave.
- Modelos de enrutador, tutor y asistente: se escriben; dejar el recomendado salvo retirada de un modelo.
- «Presupuesto mensual por asistente» (no) y «Modelo cuando se agota el presupuesto».
- «Mostrar las respuestas palabra a palabra»: sí en instalaciones nuevas, no al actualizar hasta comprobar que el servidor deja pasar la respuesta en directo.
- «Mensajes por usuario y minuto» (10) y «por día» (200).

## Sitio · Contenido y aprendizaje
Interruptores que permiten cada función en los cursos: «Permitir bases de conocimiento del aula» (sí), «Examen del tutor sobre su material» (no; 30 preguntas), «Describir las imágenes del material del curso» (no), «Comprobar las respuestas con el material del curso» (no), «Archivo más grande que se lee» (50 MB), «Permitir feedback personalizado (coaching)» (sí) con «Máximo que puede permitir un curso», y los de experiencia, todos apagados de fábrica: fuentes bajo cada respuesta, valorar las respuestas, asistente en todas las páginas del curso, fórmulas, imágenes en el chat (20 al día), pistas, Practicar, Revisar mi borrador y lectura fácil.
Recomendación: activar primero la base de conocimiento en un curso piloto; después fuentes y valoraciones; lo que añade coste por respuesta (comprobación, imágenes) solo donde aporte.

## Sitio · Voz y llamadas
«Permitir la voz» (no), «Proveedor de voz» (OpenAI; también Gemini o «Navegador (Web Speech)»), «Voz por defecto» (la recomendada del proveedor de voz), grabación más larga (60 s), minutos por participante y día (20), por curso y mes (0) y del sitio al mes (0); los dos mensuales suman también las llamadas. «Permitir el modo llamada» (no), minutos de llamada por participante y día (15), duración máxima (20), «Motor de la llamada» (Paso a paso), «Frases de espera en las llamadas» (sí), voces de tiempo real y hasta tres presentadores propios.
Con el motor «Paso a paso» hace falta un proveedor de voz del servidor: con «Navegador» no hay botón «Llamar». Los motores de tiempo real no dependen del proveedor de voz.
Recomendación: poner un tope mensual del sitio desde el primer día y no dejar a la vez en 0 los minutos diarios y la duración máxima de las llamadas.

## Sitio · Soporte
«Activar el escalado por correo» (no), «URL del formulario de soporte», «Dirección de soporte», «Copia a», «Dominios de destino permitidos», «Prefijo de las referencias» (OA), plantillas de asunto y mensaje, firma, plazo de respuesta previsto, incluir la conversación (sí; 6 mensajes), copia al participante (no) y los límites contra el exceso de correos: «Máximo de consultas por participante y día» (3), «Minutos entre consultas» (10), «Turnos de silencio tras un rechazo» (5), «Ventana de deduplicación (horas)» (24) y «Máximo de consultas por curso y día» (200).
En un asistente de categoría o de portada, desde 5.3.3 el nombre de curso del correo es el del curso al que se refiere la consulta, no el del sitio.
Recomendación: rellenar «Dominios de destino permitidos» con el dominio de la institución para que ningún curso pueda enviar datos de alumnos fuera.

## Sitio · Visitantes, Registro y analítica, Avanzado
- Visitantes: límites por dirección, tope diario, longitud, memoria, conservación y captcha invisible (Cloudflare Turnstile o reCAPTCHA v3). Activar el captcha siempre que se abra un asistente a visitantes.
- Registro y analítica: «Registrar contenido de los mensajes» (sí), «Retención de conversaciones (días)» (30), «Informe del curso» y «Análisis de temas recurrentes» (no), «Precios de modelos» (vacío: los del plugin).
- Avanzado: direcciones base de cada proveedor (solo si sistemas lo pide), modelo de embeddings (cambiarlo obliga a releer todo el material), esfuerzo de razonamiento, temperaturas, tokens máximos de salida, modelos de voz y de tiempo real, resumen agrupado de soporte, puntuación mínima de reCAPTCHA, registro de payloads y modo depuración (solo a petición del soporte, y apagarlos después).

## Bloque
«Nombre del Asistente» (Asistente IA), «Mensaje de Bienvenida» (aviso permanente arriba del chat; de fábrica ya avisa de que es una IA), «Subtítulo de la tarjeta» (¿Cómo puedo ayudarte hoy?), «URL del avatar (imagen o GIF)» (vacío), «Preguntas de ejemplo» (ninguna; hasta seis). En una categoría: «Catálogo de cursos» (solo esta categoría y sus subcategorías) y «Usar las herramientas del curso dentro de los cursos de esta categoría» (sí). En portada o categoría, solo gestores: «Abrir este asistente a visitantes sin iniciar sesión» (no).

## Configuración del asistente (por curso)
Entre paréntesis, el valor de fábrica de un asistente nuevo.
- General: «Habilitar el asistente en este curso» (sí), «Mostrar el asistente en todas las páginas del curso» (no), «Presupuesto mensual (US$)» (0, sin tope), fórmulas (no), lectura fácil (no), imágenes (no), habilitar el tutor y el asistente (sí los dos; al menos uno o no deja guardar), «Guardar el texto de las conversaciones» (sí), análisis semanal de temas (no; necesita guardar las conversaciones), «Política de idioma» (Automático).
- Tutor y base de conocimiento: modo de pistas (no) y su nivel (pistas graduadas), comprobación de respuestas (no), Practicar (no), Revisar mi borrador (no), «Personalizar las instrucciones» de cada modo (no), bloque de evaluación (siempre activo), documentos citables e internos, prompt del tutor del curso (viene con un texto probado).
- Base de conocimiento del aula: «Usar el contenido del curso como base de conocimiento» (no), «Cómo la usa el tutor» (mapa del curso + búsqueda), «Actividades que se indexan» (todas), citar y enlazar (sí), plazas reservadas a los documentos del tutor (5), bloquear las preguntas de los cuestionarios (sí), describir las imágenes (no).
- Feedback personalizado: No (de fábrica) / Entregas, feedback, rúbricas y mensajes propios en foros / Todo lo que Moodle ya le muestra al participante.
- Voz: voz (no), nombre de la voz (vacío: la del sitio), velocidad (1,0), tono, modo llamada (no), frases de espera (sí en asistentes nuevos; solo con el motor «Paso a paso»), avatar en las llamadas (la imagen del asistente).
- Asistente: prompt de sistema (viene con un texto probado) y FAQs (texto que consulta antes que nada).
- Escalado a soporte: «Heredar la configuración del sitio» (de fábrica), activado o desactivado; direcciones y enrutado por categoría (solo gestores; se puede usar el comodín de profesores del curso); textos; incluir conversación; copia. Vacío o «Heredar»: lo del sitio.
- Herramientas: qué puede consultar el asistente en Moodle (todas activas de fábrica).
- Avanzado: listas de documentos, actividades protegidas, textos de respuesta, modelo, temperatura (de 0 a 2) y tokens propios del curso (vacíos: los del sitio), prompt del enrutador (no tocar salvo indicación del soporte).
En un asistente de portada o categoría el formulario tiene «Herramientas de plataforma» y no muestra botón flotante, fórmulas, imágenes, pistas, comprobación, Practicar, borrador, base de conocimiento del aula, feedback personalizado, voz ni análisis semanal.

## Permisos (de fábrica)
Añadir el bloque: profesor con edición y gestor (al Área personal, nadie). Usar el chat: cualquier usuario con sesión. Configurar el asistente y gestionar la base de conocimiento: profesor con edición y gestor. Ver el informe del curso: profesores y gestor. Voz, llamadas y pedir soporte desde un curso: alumnos, profesores y gestor. Pedir soporte desde portada o categoría: usuarios con sesión. Cambiar el destino del soporte, abrir a visitantes y ver los informes del administrador: gestor. Usar como visitante: invitado.
