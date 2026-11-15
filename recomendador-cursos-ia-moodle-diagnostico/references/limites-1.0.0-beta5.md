# Límites y valores por defecto: 1.0.0-beta5

Valores leídos en el código de 1.0.0-beta5 el 15-11-2026. «Fijo» significa que no hay ajuste para cambiarlo.

## Ajustes numéricos y su rango
Desde 1.0.0-beta5 la página de ajustes valida estos campos: un valor fuera de rango no se guarda y se muestra el mínimo (o el rango) admitido. Un valor fuera de rango guardado con una versión anterior sigue activo hasta que se guarde la página.
| Ajuste (nombre en pantalla) | De fábrica | Rango admitido y notas |
|---|---|---|
| Duración de la caché del ranking | 1 día | Mínimo efectivo de 1 minuto. |
| Peticiones a la IA por usuario y día | 5 | 1 o más. No hay «sin límite». Un 0 heredado de una versión anterior bloquea todos los rankings nuevos. |
| Máximo de cursos por petición | 120 | 1 o más. |
| Resúmenes de curso por ejecución | 50 | 0 o más; 0 no genera resúmenes. |
| Cursos mostrados | 4 | 1 o más. |
| Cursos en el ranking | 24 | 1 o más. Si es menor que «Cursos mostrados», no habrá «Ver más». |
| Rutas mostradas | 2 | 1 o más. Para no mostrar rutas se usa «Recomendar rutas de aprendizaje». |
| Rutas en el ranking | 6 | 1 o más. |
| Umbral de relevancia para notificaciones | 70 | 0 a 100; 0 avisa de cualquier curso nuevo devuelto. |
| Días ocultos tras un pulgar abajo | 90 | 0 o más; 0 no oculta nada. |
| Actividad del usuario (días) | 90 | 1 o más. |
| Usuarios por ejecución | 200 | 1 o más. |
| Conservación de datos (días) | 365 | 0 o más; 0 conserva siempre; mínimo efectivo de 30. |

## Límites fijos
| Elemento | Límite |
|---|---|
| Preguntas | 6 como máximo; 4 activas de fábrica con texto traducido (inglés, español, portugués); al menos 1 activa. |
| Respuesta a una pregunta | 1.000 caracteres. |
| Historial de respuestas | Últimas 50 versiones por persona. |
| Motivo de un pulgar abajo | 200 caracteres. |
| Valoraciones negativas enviadas a la IA | Las 10 más recientes. |
| Motivo de cada recomendación | 300 caracteres, texto plano, sin enlaces ni correos. |
| Puntuación | 0 a 100; se pide a la IA incluir solo 40 o más. |
| Campo de perfil enviado | 500 caracteres; descripción del perfil, 1.500. |
| Nombre de campo personalizado | 100 caracteres; valor de campo personalizado de curso, 300. |
| Descripción de curso para generar su resumen | 4.000 caracteres. |
| Descripción de curso enviada si aún no hay resumen | 600 caracteres. |
| Resumen de curso | Unas 80 palabras, en inglés; se guarda con un máximo de 700 caracteres. |
| Descripción de ruta enviada a la IA | 500 caracteres; resumen de cada curso de la ruta, 200. |
| Descripción de ruta generada | 60 a 120 palabras por idioma instalado. |
| Texto usado para la imagen de una ruta | 600 caracteres de la descripción y 1.000 del estilo corporativo. |
| Título de ruta | 1.333 caracteres. |
| Imagen de ruta | 1 archivo JPG, PNG, GIF o WebP. SVG no admitido. Generada: apaisada, una por petición. |
| Reintentos por respuesta mal formada | 1. Cuenta para el límite diario. |
| Peticiones de ranking simultáneas por persona | 1; la segunda espera hasta 60 segundos y, si no, recibe el mensaje de «estamos preparando…». |
| Avisos de cursos nuevos | 3 por persona y ejecución; una revisión por persona cada 12 horas como mucho. |
| Clic en una tarjeta | El registro del clic retrasa la navegación 0,7 segundos como máximo. |
| Dictado por voz | Depende del navegador (Chrome, Edge, Safari); sin soporte, el botón no aparece. |
| Ubicación del bloque | Portada del sitio y Área personal; una instancia por página. |

## Qué cuenta para el límite diario
Cuentan las peticiones de ranking lanzadas por la persona desde su medianoche, también las fallidas y el reintento. No cuentan la tarea nocturna, los resúmenes ni las acciones de IA de las rutas. «Borrar mis datos» no reinicia el contador.
Al alcanzarlo: con ranking previo se muestra ese ranking con aviso; sin ranking previo, mensaje de límite y nada más hasta el día siguiente.

## Límites que no son del plugin
El proveedor de IA de Moodle tiene sus propios topes por usuario y globales, su modelo, su longitud máxima de entrada y sus precios. Los resúmenes se piden en nombre del administrador principal, así que su ritmo real lo marca el tope por usuario del proveedor (el README del plugin cita 10 por usuario y hora como valor habitual del proveedor de OpenAI de Moodle; comprobarlo en el sitio).
El plugin no impone tiempo de espera propio a las peticiones: aplica el de Moodle y el del proveedor.

## Coste orientativo
Estimación del mantenedor con valores de fábrica: unos 900 tokens fijos más unos 150 por curso candidato de entrada, y unos 70 por elemento devuelto. Un ranking con 20 candidatos ronda 4.000 tokens de entrada y 1.500 de salida; con 120, unos 19.000 y 2.200. Resumen de curso: 500 a 1.500 de entrada y unos 150 de salida. Son aproximaciones: el gasto real se ve en la columna «Tokens» del informe, si el proveedor la comunica.

## Compatibilidad
Moodle 4.5 a 5.3. La generación de imágenes con el proveedor de OpenAI falla en Moodle 4.5.0 a 4.5.13 por un problema del propio Moodle; se resuelve con 4.5.14 o posterior y un modelo de imagen actual.
