# Configuración de Smart Tutor & Support AI (5.3.2)
Nombres tal como aparecen en pantalla en español. Detalle y ejemplos de cada ajuste, con simuladores: https://claude.ai/artifact/Ko6vHpvgSzUBNEcF9Nxs8R

## Dónde está cada cosa
| Qué | Dónde | Quién |
|---|---|---|
| Ajustes del sitio (siete pestañas) | Administración del sitio › Extensiones › Bloques › Smart Tutor & Support AI | Administrador |
| Panel de uso, informes y herramientas de prueba | Enlaces al final de la barra de pestañas | Administrador o gestor con el permiso de configuración global |
| Ajustes del bloque (nombre y aspecto) | Engranaje del bloque › Configurar | Quien edita el curso |
| Configuración del asistente | Menú «Más» del curso (o ajustes de la categoría o de la portada) | Docente con edición, gestor |
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
«Permitir la voz» (no), «Proveedor de voz» (OpenAI), «Voz por defecto», grabación más larga (60 s), minutos por participante y día (20), por curso y mes (0) y del sitio al mes (0). «Permitir el modo llamada» (no), minutos de llamada por participante y día (15), duración máxima (20), «Motor de la llamada» (Paso a paso), «Frases de espera en las llamadas» (sí), voces de tiempo real y hasta tres presentadores propios.
Recomendación: poner un tope mensual del sitio desde el primer día y no dejar a la vez en 0 los minutos diarios y la duración máxima de las llamadas.

## Sitio · Soporte
«Activar el escalado por correo» (no), «URL del formulario de soporte», «Dirección de soporte», «Copia a», «Dominios de destino permitidos», prefijo de las referencias, plantillas de asunto y mensaje, firma, plazo de respuesta previsto, incluir la conversación (sí; 6 mensajes), copia al participante (no) y los límites contra el exceso de correos.
Recomendación: rellenar «Dominios de destino permitidos» con el dominio de la institución para que ningún curso pueda enviar datos de alumnos fuera.

## Sitio · Visitantes, Registro y analítica, Avanzado
- Visitantes: límites por dirección, tope diario, longitud, memoria, conservación y captcha invisible (Cloudflare Turnstile o reCAPTCHA v3). Activar el captcha siempre que se abra un asistente a visitantes.
- Registro y analítica: «Registrar contenido de los mensajes» (sí), «Retención de conversaciones (días)» (30), «Informe del curso» y «Análisis de temas recurrentes» (no), «Precios de modelos» (vacío: los del plugin).
- Avanzado: direcciones base de cada proveedor (solo si sistemas lo pide), modelo de embeddings (cambiarlo obliga a releer todo el material), esfuerzo de razonamiento, temperaturas, tokens máximos de salida, modelos de voz y de tiempo real, resumen agrupado de soporte, puntuación mínima de reCAPTCHA, registro de payloads y modo depuración (solo a petición del soporte, y apagarlos después).

## Bloque
«Nombre del asistente», «Mensaje de bienvenida» (aviso permanente arriba del chat: usarlo para decir que es una IA), «Subtítulo de la tarjeta», «URL del avatar», «Preguntas de ejemplo». En una categoría: «Catálogo de cursos» y usar las herramientas del curso dentro de los cursos de la categoría. En portada o categoría, solo gestores: «Abrir este asistente a visitantes sin iniciar sesión».

## Configuración del asistente (por curso)
- General: habilitar el asistente, mostrarlo en todas las páginas, presupuesto mensual, fórmulas, lectura fácil, imágenes, habilitar el tutor y el asistente (al menos uno), guardar el texto de las conversaciones, análisis semanal de temas, política de idioma.
- Tutor: modo de pistas y su nivel, comprobación de respuestas, Practicar, Revisar mi borrador, «Personalizar» las instrucciones de cada modo, bloque de evaluación (siempre activo), documentos citables e internos, prompt del tutor del curso.
- Base de conocimiento del aula: usar el contenido del curso, cómo la usa el tutor, actividades que se indexan, citar y enlazar, plazas reservadas a los documentos del tutor, bloquear las preguntas de los cuestionarios, describir las imágenes.
- Feedback personalizado: No / Entregas, feedback, rúbricas y foros / Todo lo que Moodle ya le muestra.
- Voz y llamadas: voz, nombre de la voz, velocidad, tono, modo llamada, frases de espera, presentador.
- Asistente: prompt de sistema y FAQs (texto que consulta antes que nada).
- Escalado a soporte: heredar, activado o desactivado; direcciones y enrutado por categoría (solo gestores; se puede usar el comodín de profesores del curso); textos; incluir conversación; copia.
- Herramientas: qué puede consultar el asistente en Moodle (todas activas de fábrica).
- Avanzado: actividades protegidas, listas de documentos, textos de respuesta, modelo, temperatura y tokens propios del curso, prompt del enrutador (no tocar salvo indicación del soporte).

## Permisos (de fábrica)
Usar el chat: cualquier usuario con sesión. Configurar el asistente y gestionar la base de conocimiento: profesor con edición y gestor. Ver el informe del curso: profesores y gestor. Voz, llamadas y pedir soporte desde un curso: alumnos, profesores y gestor. Pedir soporte desde portada o categoría: usuarios con sesión. Cambiar el destino del soporte, abrir a visitantes y ver los informes del administrador: gestor. Usar como visitante: invitado.
