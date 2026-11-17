# Configuración de AI Roleplay (versión 1.1.2)

Nombres tal como aparecen en pantalla en español. Entre paréntesis, el valor de fábrica. Revisado el 17-11-2026. Explicación ampliada para personas: https://claude.ai/artifact/9rrxnBoMsHAgMzhKErn92D

## Ajustes del sitio
Ruta: Administración del sitio › Extensiones › Módulos de actividad › AI Roleplay. Una sola página con secciones; arriba hay un enlace al manual de configuración. Todo se aplica tras «Guardar cambios».

### Licencia
- Clave de licencia (vacía). Ligada a la dirección exacta del sitio. Recomendación: pedir clave nueva ante cualquier cambio de dirección (http/https, www, subcarpeta).

### Claves API de proveedores de IA
- Clave API principal de OpenAI. Modelos GPT, voces de OpenAI, OpenAI Realtime y moderación.
- Clave API secundaria de OpenAI (opcional). Solo para las voces de OpenAI; sirve para separar ese gasto.
- Clave API de Anthropic. Modelos Claude. Sin voces.
- Clave API de Google Gemini. Modelos Gemini, voces de Gemini y Gemini Live.
- Clave API de DeepSeek. Modelos DeepSeek. Sin voces. Trata datos en China: consultar con protección de datos.
- Probar la conexión con la IA › «Ejecutar la prueba de conexión». Comprueba licencia, los dos modelos recomendados del proveedor de chat y el proveedor de voz, con los ajustes guardados. No comprueba el modelo concreto de cada actividad ni el tiempo real.
Recomendación: una clave dedicada a Moodle y un límite de gasto mensual en la cuenta del proveedor.

### Texto a voz (voces de los avatares)
- Proveedor de TTS (OpenAI): OpenAI, Google Gemini, Voces del navegador, Sin voz. Determina la lista de voces de las actividades. Al cambiarlo, las actividades suenan con las voces por defecto del nuevo proveedor hasta que el docente vuelva a elegir.
Recomendación: OpenAI o Gemini para calidad; navegador para coste cero; con Anthropic o DeepSeek como proveedor de chat hay que elegir aquí otra opción.

### Voz en tiempo real
- Motor de voz (Por turnos): Por turnos, OpenAI Realtime, Gemini Live.
- Modelo de OpenAI Realtime / Modelo de Gemini Live. Visibles solo con su motor.
- Voz en tiempo real por defecto (marin / Kore). Se usa cuando la voz del avatar no existe en el motor en directo.
Recomendación: activar solo tras actualizar el aviso de privacidad, con actividades de un avatar y empezando por un grupo pequeño; cuesta bastante más por minuto.

### Proveedor de chat y modelos
- Proveedor de chat (OpenAI): OpenAI, Anthropic (Claude), Google Gemini, DeepSeek. Vale para conversación y evaluación de las actividades nuevas.
- Modelos de OpenAI / Anthropic / Gemini / DeepSeek (todos). Qué modelos puede elegir el docente. Vacío equivale a todos.
- Estimaciones de coste. Texto informativo.
Recomendación: no retirar la clave de un proveedor anterior mientras haya actividades con sus modelos.

### Calificación
- Revisión del profesor antes de publicar (marcada, sin bloquear). Valor inicial de las actividades nuevas. Con «Bloqueado» se impone a todas, incluidas las existentes.

### Seguridad
- Activar moderación de contenido de OpenAI (sí). Solo con modelos de OpenAI y por turnos.
- Máximo de tokens por llamada API (4096). Afecta en la práctica a la evaluación.
- Anonimización de estudiantes. Informativo; siempre activa. El nombre de pila sí se envía.
- Sal de anonimización (vacía). Normalmente no se toca.

### Aviso RGPD
- Texto del aviso RGPD (texto estándar). HTML. Vacío: se muestra el estándar. Recomendación: nombrar al proveedor real, enlazar la política de privacidad y mencionar el tiempo real si se usa. Tras actualizar desde versiones antiguas, comprobar que el texto guardado no esté desfasado.

### Avanzado
- Tiempo de espera de la solicitud API (segundos) (120).
- Máx. llamadas API por usuario por minuto (10).
- Máximo de llamadas a la API por minuto (todo el sitio) (300).
Recomendación: subir el límite por usuario a 16-20 en práctica de idiomas con frases cortas; dimensionar el del sitio a 5 llamadas por alumno simultáneo.

## Ajustes de la actividad
Ruta: en el curso, Añadir una actividad o un recurso › AI Roleplay. Arriba del formulario hay un enlace al manual de configuración.

### General
- Nombre de la actividad (obligatorio).
- Descripción. Texto para el curso; la IA no lo usa.
- Intentos máximos (2).
- Entrega grupal (no). Solo anota el grupo del alumno en cada intento; no crea trabajo en equipo.

### Disponibilidad
- Permitir sesiones desde (desactivado).
- Cerrar sesiones a partir de (desactivado).

### Escenario y rol del participante
- Descripción del escenario (vacía). La ven el alumno, los avatares y el evaluador. Poner lo esencial al principio.
- Rol del participante (vacío). Se muestra como «Tu rol en este escenario».
- Duración de la sesión (minutos) (10).
- Micrófono (Manos libres (envío tras una pausa)); otras: Pulsar para hablar y pulsar para enviar; Mantener pulsado para hablar. Las actividades anteriores a 1.1.0 conservan «Mantener pulsado».
- Instrucciones de evaluación (vacías). Orientan al evaluador; no cambian la rúbrica ni los pesos. El alumno no las ve.

### Avatares
- Número de avatares (1).
- Por avatar: Nombre (Alex, Jordan, Morgan); Rol / Título (Interlocutor); Personalidad y estilo de interacción (vacía; el alumno no la ve); Voz TTS; Apariencia del avatar (el avatar incluido de su número); Subir imagen personalizada del avatar.
Recomendación: lo que el alumno no debe saber va en la personalidad, no en el escenario. Nombres distintos y fáciles de pronunciar si hay varios avatares.

### Modelos de IA
- Modelo de IA para la conversación del juego de roles (recomendado del proveedor). Prima la rapidez.
- Modelo de IA para evaluación final (recomendado del proveedor). Prima el criterio; se ejecuta una vez por intento.

### Calificación y flujo de trabajo
- Calificación máxima (100). Conviene fijarla antes de que haya intentos; si se cambia después, las notas guardadas se convierten a la nueva escala.
- Revisión del profesor antes de publicar (valor del sitio). En gris si el administrador la bloquea.
- Notificar al estudiante cuando se publique la calificación (sí).

### Seguridad de la actividad
- Restricciones de contenido adicionales (opcional). Normas extra para los avatares; se aplican también en tiempo real.

### Ajustes comunes y finalización
- Modo de grupo y agrupamiento: filtran y limitan lo que ve cada profesor en «Entregas».
- Finalización › El estudiante debe completar una sesión de roleplay. Se cumple al terminar una sesión, antes de la evaluación. Para exigir nota, usar las condiciones de calificación de Moodle.

## Páginas del profesorado
- Entregas: lista de intentos y detalle con avisos, resumen, conversación, desglose, «Recalcular evaluación final», nota y comentario, «Publicar calificación», «Guardar cambios», «Retirar la nota y devolverla a revisión» y borrado.
- Excepciones de usuario/grupo: Tipo de excepción, Usuario o Grupo, Intentos máximos, Apertura, Cierre.
- Reinicio del curso: casillas para borrar intentos y evaluaciones, y para borrar excepciones (marcadas de fábrica).

## Perfiles de configuración recomendados
| Objetivo | Sitio | Actividad |
|---|---|---|
| Coste mínimo | TTS del navegador, motor por turnos | Modelo económico para conversar, 5 minutos, 1-2 intentos |
| Experiencia más natural | Motor OpenAI Realtime o Gemini Live, aviso RGPD actualizado | Un avatar |
| Prueba con nota | Revisión del profesor activada | 1 intento, fechas, modelo recomendado para evaluar |
| Práctica de idiomas | Límite por usuario 16-20 | Intentos ilimitados, publicación automática, «Pulsar para hablar» |
| Menores o temas delicados | Moderación activada, modelos de OpenAI | Restricciones adicionales, revisión del profesor |
