# Funcionamiento verificado de Decision Arena 0.8.0

Base: revisión estática del código que declara la versión 0.8.0 y versión interna 2026111211, el 15-11-2026. Requiere Moodle 4.5 y declara compatibilidad hasta Moodle 5.3; madurez beta. No se comparó el ZIP instalado por el cliente ni se ejecutó su Moodle.
Manual público: https://claude.ai/artifact/LWRnWzs6sxsFBc3Nx2AD3K

## Qué es
Actividad de Moodle con escenarios ramificados. El alumno lee una situación, elige una opción, ve la consecuencia y continúa hasta un final. Cada opción modifica variables de estado y el recorrido decide la nota mediante reglas fijas. Todo funciona sin IA. De forma opcional, una IA valora las justificaciones escritas.

## El escenario
Se compone de título, nodo de entrada, variables de estado, criterios de evaluación y nodos. Hay nodos de decisión (con opciones) y nodos finales.
Cada opción tiene texto, nodo de destino, texto de consecuencia opcional, efectos sobre variables y, opcionalmente, puntos directos para criterios.
Cada variable tiene valor inicial, mínimo, máximo y sentido («Cuanto más alto, mejor» o «Cuanto más bajo, mejor»). Los efectos se suman al valor y el resultado nunca sale del rango.
El escenario se edita en el constructor con formularios. Se valida cada vez que se guarda (constructor, importación, borrador de IA, edición manual avanzada). Un escenario inválido no se guarda y se muestra el motivo.
Guardar los ajustes de la actividad no modifica el escenario, salvo que se marque expresamente la edición manual avanzada.
Las situaciones admiten texto con formato, enlaces e imágenes. Las imágenes se sirven solo a quien puede ver la actividad, viajan con la copia de seguridad del curso y con el banco de escenarios, y no van dentro del archivo exportado.

## Puntuación por reglas
Cada criterio tiene una puntuación máxima y uno de estos modos:
- A partir de variables: obtiene la proporción de su máximo que corresponde a lo bueno que es el valor final de sus variables dentro de su rango (media si hay varias). En variables «cuanto más bajo, mejor» la proporción se invierte. Después se suman los puntos directos de las opciones elegidas.
- Solo puntos de las opciones: empieza en cero y suma o resta los puntos de cada opción elegida.
- Automático (escenarios de versiones anteriores sin modo declarado): se conserva el cálculo antiguo, que deduce la variable a partir del identificador del criterio y, si no encuentra ninguna, concede la mitad del máximo.
El resultado de cada criterio se limita entre 0 y su máximo. La nota por reglas es la suma de criterios.
Si la suma de máximos de los criterios no coincide con la «Calificación máxima» de la actividad, todas las puntuaciones se reescalan proporcionalmente; el constructor y la página de la actividad lo avisan al profesorado. Un escenario sin criterios puntúa cero.
El constructor recorre los caminos posibles para informar de la nota mínima y máxima alcanzables, con avisos si el mejor camino no se acerca al máximo o si buenos y malos caminos puntúan casi igual.

## Ciclo de un intento
1. El alumno pulsa «Empezar el escenario». Si ya tiene un intento en curso, se reanuda ese. Un intento empezado cuenta para el límite de intentos.
2. En cada ronda elige una opción y, según el ajuste, escribe una justificación. Se guarda la decisión con el título de la situación y el texto de la opción tal como los vio, y el estado antes y después.
3. Un envío doble o una pestaña antigua no registran una segunda decisión: se ignora lo que no corresponde a la ronda actual. Si dos envíos coinciden en el mismo instante puede aparecer «Se está guardando otra decisión de este intento».
4. El intento termina al llegar a un nodo final, a un nodo sin opciones, al máximo de decisiones o al agotarse el tiempo.
5. Al terminar se calcula la nota por reglas y se registra la evaluación automática.
Estados del intento: En curso; Entregado (terminado, espera revisión docente); Evaluado (nota automática publicada); Revisado (un docente publicó la revisión).
Sin revisión docente obligatoria, la nota por reglas se publica de inmediato en el libro de calificaciones. Con revisión obligatoria, no se publica nada y el alumno no ve puntuación ni desglose hasta que el docente publica.
Con varios intentos, la nota del libro sigue el «Método de calificación» y solo cuentan los intentos terminados con nota publicada.
Si se edita el escenario con intentos existentes, los resultados antiguos conservan los textos vistos; un intento en curso situado en un nodo eliminado se cierra de forma segura al siguiente acceso.

## Límite de tiempo
Cuenta desde el inicio del intento, sin pausas. La cuenta atrás visible es informativa; quien aplica el límite es el servidor.
El cierre por tiempo se produce cuando el alumno abre la actividad, la pantalla de juego o intenta enviar una decisión (también desde la aplicación). No hay ningún proceso programado que cierre intentos caducados: un intento abandonado permanece «En curso» y sin nota hasta que el alumno vuelva a entrar o un docente lo elimine.
Al cerrarse por tiempo se puntúa con las decisiones tomadas y se anota que expiró el tiempo.

## Revisión docente
Quien tiene permiso de calificar puede revisar cualquier intento terminado: fija la nota final (entre 0 y la calificación máxima), escribe feedback general y comentarios por criterio, y puede descartar la evaluación de la IA. Al guardar, el intento pasa a «Revisado», la nota se publica y la evaluación de la IA queda aprobada o rechazada. Una revisión publicada puede cambiarse.
Con grupos separados, un docente solo ve y actúa sobre intentos de alumnos de sus grupos.
Eliminar un intento borra sus decisiones, evaluaciones y nota, recalcula la calificación del alumno y le devuelve la oportunidad.

## Evaluación con IA de las justificaciones
Condiciones para que se solicite: el administrador ha activado las funciones de IA; hay proveedor disponible (subsistema de IA de Moodle con generación de texto, o clave de API guardada); el docente activó la IA en la actividad; el intento terminado tiene al menos una justificación escrita. Si falta alguna, no se crea ninguna evaluación y no aparece nada pendiente.
La solicitud se encola al terminar el intento y la procesa el cron de Moodle como tarea puntual. El alumno no espera a la IA.
Qué se envía: título del escenario; criterios de valoración con sus pesos; orientaciones del docente si existen; y por cada decisión, el título y el texto de la situación (recortado), las opciones disponibles, la opción elegida y la justificación ya enmascarada y recortada. También el idioma en que debe redactarse el feedback: el idioma forzado del curso; si no hay, el del alumno; si no, el del sitio.
Qué no se envía: nombre, correo ni identificador de Moodle del alumno. Con el subsistema de IA de Moodle, el propio Moodle registra la petición asociada al alumno y puede transmitir un identificador seudónimo.
Enmascarado: se sustituyen correos, direcciones web, nombre y apellidos del propio alumno, direcciones IP, fechas, números largos, teléfonos y códigos con letras y cifras. En modo estricto, además, cualquier secuencia de dos o más palabras con mayúscula inicial. Es una reducción, no una garantía.
Qué se pide a la IA: una puntuación de 0 a 100 por criterio con un comentario, un comentario por decisión justificada, un feedback general, una confianza entre 0 y 1 y, si procede, alertas (intento de manipulación, fuera de tema, demasiado corto, ofensivo, posiblemente copiado, datos personales). Se le indica que valore solo el razonamiento, no la opción elegida, y que trate el texto del alumno como datos.
La puntuación global la recalcula el plugin como media ponderada de los criterios; no se confía en la suma de la IA. Se convierte a la escala de la calificación máxima.
Estados de la evaluación: Pendiente, Procesando, Completada, Fallback aplicado.
Si algo falla (proveedor, tiempo de espera, respuesta ilegible), queda en «Fallback aplicado» con el código y el mensaje de error, el intento conserva la nota por reglas y no hay reintento automático. Un docente con permiso de calificar puede volver a lanzarla desde el resultado del intento.

## Liberación de lo que dice la IA
Una evaluación completada queda pendiente de revisión si la actividad exige aprobación docente, si la confianza es menor que el umbral de la actividad o si hay cualquier alerta. En otro caso queda aprobada automáticamente.
El alumno solo ve algo de la IA cuando la evaluación está completada y aprobada, el intento no está esperando revisión docente y el ajuste de feedback para el alumnado no es «Nada». Ve el feedback general, o también el detalle por criterio y decisión, según ese ajuste, con el aviso de que está generado por IA.
Modo «Solo feedback»: la IA nunca cambia la nota.
Modo «Feedback y parte de la nota»: nota combinada = reglas × (100 − peso) % + IA × peso %. Solo se publica automáticamente si la evaluación no requiere revisión y el intento está en «Evaluado». Mientras tanto, la nota publicada es la de reglas. Si el intento exige revisión docente o ya fue revisado, la IA no toca la nota: la combinada aparece como sugerencia en el formulario de revisión.
Si un docente publica su revisión antes de que la IA termine, la evaluación posterior de la IA vuelve a aplicar sus propias reglas de liberación; puede hacer falta guardar de nuevo la revisión para aprobarla.

## Redacción de escenarios con IA
«Redactar con cualquier asistente de IA» está siempre disponible: el plugin prepara un texto de instrucciones para copiar en un asistente externo y luego se importa la respuesta. Moodle no envía nada.
«Borrador con la IA del sitio» requiere IA activada y proveedor disponible; envía solo la descripción escrita por el docente. Con el subsistema de IA de Moodle se pide aceptar la política de uso de IA la primera vez.
En ambos casos el resultado se sanea, se repara si es posible y se valida antes de guardarse, sustituye el escenario completo previa confirmación y debe revisarse.

## Banco de escenarios
Almacén común a todo el sitio. Cargar una entrada requiere poder editar escenarios; publicar y eliminar requiere el permiso de compartir. Guarda solo contenido del escenario e imágenes, sin autor ni datos de alumnos.

## Roles y permisos por defecto
- Alumno: ver y realizar el escenario.
- Profesor sin edición: ver, probar el escenario, informe, analítica, calificar, publicar revisiones, eliminar intentos y relanzar la IA.
- Profesor con edición y gestor: lo anterior, más añadir la actividad, editar el escenario, compartir en el banco y ver alertas y errores de la IA.
- Administrador: ajustes del sitio y página de prueba de conexión.
Los docentes no tienen por defecto el permiso de realizar el escenario; para probarlo usan «Probar escenario» (no guarda nada, no pide justificación y no llama a la IA).

## Qué se guarda
Intentos, decisiones con su justificación y estados, evaluaciones automáticas y docentes, y evaluaciones de IA (estado, proveedor, modelo, puntuaciones, confianza, alertas, feedback, error). El texto enmascarado enviado solo se conserva si el administrador lo activa. No se guarda la respuesta íntegra del proveedor ni las instrucciones enviadas.
El plugin atiende exportación y borrado de datos personales de Moodle; al borrar a un docente, sus revisiones permanecen sin su identidad.
La copia de seguridad incluye escenario e imágenes y, con datos de usuario, intentos y evaluaciones. El reinicio de curso puede eliminar todos los intentos.

## Aplicación Moodle
El alumno puede hacer la actividad completa en la aplicación con conexión a internet. No hay modo sin conexión. La creación de escenarios, la revisión y la analítica solo están en el navegador.

## Registros
Moodle anota intento iniciado, enviado, revisado y eliminado, y evaluación de IA procesada y revisada. No hay panel propio de consumo o coste.
