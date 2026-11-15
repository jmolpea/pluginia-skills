# Configuración: ajustes y recomendaciones

Todos los ajustes son de sitio: Administración del sitio › Extensiones › Bloques › Recomendador de cursos con IA › Ajustes. Solo los ve quien puede configurar el sitio. Los nombres son los de la interfaz en español. Manual público con ejemplos y simuladores: https://claude.ai/artifact/LCZgLbHfAnSBkurowGLZ95

## Requisito previo (fuera del plugin)
Proveedor de IA de Moodle con «Generar texto» activado. Opcional, «Generar imagen». El modelo, la clave, los topes por usuario y el precio se deciden ahí. Para ordenar cursos suele bastar un modelo pequeño.

## Inteligencia artificial
| Ajuste | De fábrica | Qué hace | Recomendación |
|---|---|---|---|
| Proveedores de IA | Informativo | Indica si hay generación de texto y de imagen disponibles. | Primer sitio que mirar si el bloque no se ve. |
| Prompt base | Solo lectura | Muestra las instrucciones fijas y su versión. | No editable. |
| Prompt institucional | Vacío | Tono, estilo y prioridades. Admite {sitename}, {userlang}, {maxresults}, {today}. No cambia reglas ni formato. | Pocas frases claras. Cambiarlo obliga a recalcular el ranking de todos en su siguiente visita. |
| Duración de la caché del ranking | 1 día | Tiempo de reutilización del ranking. | Subir con catálogos estables para gastar menos. |
| Peticiones a la IA por usuario y día | 5 | Tope de rankings nuevos por persona. | Entre 3 y 5. Nunca 0. |
| Máximo de cursos por petición | 120 | Candidatos enviados; el resto se descarta por coincidencia de palabras. | Bajar para ahorrar; mejor acotar con categorías. |
| Resúmenes de curso por ejecución | 50 | Resúmenes por ejecución horaria. | Dejar. El freno real es el tope del proveedor. |

## Preguntas
Seis filas con «Texto de la pregunta», «Texto de ayuda (opcional)», «Activa» y «Orden». Vacío en las filas 1 a 4 = pregunta de fábrica traducida. Las filas 5 y 6 necesitan texto para activarse. Admiten etiquetas multilang. Recomendación: mantener una pregunta de objetivos y otra de temas y nivel, que son las que más pesan; añadir ejemplos en la ayuda. Cambiar un texto recalcula rankings.

## Datos del perfil
| Ajuste | De fábrica | Recomendación |
|---|---|---|
| Campos estándar del perfil | Ciudad, País, Institución, Departamento, Intereses y Descripción marcados | Desmarcar lo que la política de datos no permita. Sin ninguno, la IA usa solo respuestas e idioma. |
| Campos personalizados de perfil | Ninguno (solo aparece si existen) | Marcar solo campos descriptivos (puesto, área); nunca identificadores. |
Si se cambia lo que se envía, ajustar el «Aviso de privacidad» para que diga lo mismo.

## Catálogo
| Ajuste | De fábrica | Qué hace | Recomendación |
|---|---|---|---|
| Filtrar por categoría | No | Limita a categorías elegidas. | Usarlo cuando conviven cursos de catálogo con otros. |
| Categorías | Ninguna | Categorías permitidas, con subcategorías. | Con el filtro activo, elegir al menos una. |
| Métodos de matriculación | Automatriculación | Métodos que hacen candidato a un curso. | Añadir pago u otros si se usan. Sin ninguno no hay candidatos. |
| Campo de exclusión | Ninguno | Casilla de curso que significa «No recomendar». | Crear antes el campo personalizado de curso de tipo casilla. |
| Enviar campos de curso no públicos | No | Envía también campos visibles solo para profesorado o nadie. | Dejar apagado: pueden aflorar datos internos en los motivos. |

## Resultados
«Cursos mostrados» 4, «Cursos en el ranking» 24, «Rutas mostradas» 2, «Rutas en el ranking» 6, «Umbral de relevancia para notificaciones» 70, «Días ocultos tras un pulgar abajo» 90. Mantener el ranking igual o mayor que lo mostrado. Bloque en columna estrecha: mostrar 2 o 3.

## Rutas de aprendizaje
«Recomendar rutas de aprendizaje» (sí) y «Estilo de imagen (corporativo)» (vacío = estilo plano, limpio y de colores suaves). El estilo solo actúa con proveedor de imagen. Las rutas se crean en «Gestionar rutas de aprendizaje».

## Notificaciones
«Avisar de cursos nuevos» (sí), «Actividad del usuario (días)» (90), «Usuarios por ejecución» (200). Para reducir el gasto nocturno, bajar usuarios por ejecución o días de actividad; apagar los avisos no detiene las peticiones de la tarea. Para detenerlas, desactivar la tarea programada.

## Privacidad
«Pedir consentimiento» (sí), «Aviso de privacidad» (vacío = texto de fábrica traducido), «Conservación de datos (días)» (365; mínimo efectivo 30; 0 = siempre). La política de uso de la IA de Moodle se exige siempre, con independencia de estos ajustes.

## Fuera de la página de ajustes
- Colocar el bloque: portada del sitio (modo de edición) o Área personal por defecto (Administración del sitio › Apariencia), con reinicio para todos si procede. Los usuarios pueden añadirlo a su Área personal.
- Permisos: uso (usuario identificado), añadir a la portada (gestor), añadir al Área personal (usuario identificado), gestionar rutas (gestor), ver informe (gestor).
- Preferencias de notificación de cada usuario: «Cursos nuevos que encajan con tus intereses» (aviso web activado, correo desactivado de fábrica).
- Tareas programadas: horario y activación desde la página de tareas de Moodle.

## Perfiles de configuración sugeridos
| Objetivo | Ajustes |
|---|---|
| Gasto mínimo | Caché 7 días; 2 o 3 peticiones por día; 60 cursos por petición; 12 cursos en el ranking; 50 usuarios por ejecución; modelo pequeño. |
| Catálogo grande | Filtro por categoría; campo de exclusión; revisar nombres, etiquetas y descripciones de los cursos; subir el tope por usuario del proveedor para los resúmenes. |
| Máxima privacidad | Sin campos de perfil; consentimiento activo; aviso propio; conservación de 90 a 180 días. |
| Catálogo de pago | Marcar el método de pago; explicar que la matrícula se completa en la página del curso. |
