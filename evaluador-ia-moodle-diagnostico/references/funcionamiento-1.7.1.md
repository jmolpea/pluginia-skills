# Funcionamiento verificado de RSMAX AI Tutor 1.7.1

Base: revisión estática del código que declara la versión 1.7.1 (versión interna 2026111300), hecha el 15-11-2026. Componente `local_rsmaxtutor`; requiere Moodle 4.5 y declara compatibilidad hasta 5.3. No se comparó el ZIP instalado ni se ejecutó en un Moodle concreto.
Manual público: https://claude.ai/artifact/FsE6HtPSgw77e3w7uVcKsk

## Qué cambia en 1.7.1 respecto a 1.7.0
Solo la copia de seguridad y la restauración: ahora actúan únicamente sobre tareas. En versiones anteriores, al restaurar un curso, la configuración de AI Tutor de una tarea podía escribirse sobre otra tarea distinta del sitio, sustituyendo su prompt y apagándola. Las copias hechas con versiones anteriores se restauran ya de forma segura. Si se restauraron cursos antes de 1.7.1, revisar la página de AI Tutor de las tareas: una afectada tiene el prompt de otra y puede estar desactivada.
El resto del comportamiento descrito aquí es el mismo que en 1.7.0.

## Dónde se configura
Sitio: una sola página en Administración del sitio › Extensiones › Extensiones locales › AI Tutor (solo administradores).
Tarea: dentro de cada actividad de tipo Tarea, menú «Más» › «AI Tutor», página «Configuración de AI Tutor». La ven quienes tienen el permiso de gestionar la configuración (por defecto, profesor con edición y gestor). No hay ajustes por curso ni dentro del formulario normal de la tarea.
AI Tutor está apagado en todas las tareas hasta que alguien lo activa en cada una.

## Ejecución
Qué la dispara: el envío de una entrega en una tarea con AI Tutor activado. Si la tarea no exige pulsar el botón de envío, cada vez que el alumno guarda cambios en su entrega cuenta como un envío nuevo.
La corrección nunca ocurre durante la entrega: se encola como tarea en segundo plano («Calificación diferida de AI Tutor») y la ejecuta el cron de Moodle. Sin cron no hay corrección. Con el retraso opcional, la espera mínima es de una hora; el momento real depende de la cola.
Una corrección idéntica que ya está en cola no se encola dos veces.
La configuración se vuelve a leer al ejecutar: cuenta la que hay en ese momento, no la del momento de la entrega. Si AI Tutor se apaga antes, la corrección pendiente no se hace.
Las entregas anteriores a la activación no se corrigen.
Si el plugin falla, la entrega del alumno no se ve afectada.

## Comprobaciones previas, en este orden
1. Licencia válida o periodo de prueba en curso.
2. Clave de API del proveedor rellenada.
3. Quien entregó no puede calificar en esa tarea. Las entregas hechas por docentes, gestores o administradores se ignoran; cambiar de rol en pantalla no convierte a un docente en alumno para esta comprobación. Probar con una cuenta de alumno real.
4. Límite diario de la tarea no alcanzado.
5. Límite por hora del sitio no alcanzado (si está activado).
6. Límite por hora del usuario no alcanzado (si está activado).
7. Máximo de calificaciones de ese alumno en esa tarea no alcanzado.
8. Usuario que firma válido: el elegido en la tarea, si no está eliminado ni suspendido; si no, el de reserva del sitio. Si ninguno vale, AI Tutor se desactiva en esa tarea y hay que reactivarlo a mano.
Si alguna comprobación falla, la entrega no se corrige, no queda ningún aviso en la tarea y no se reintenta. El motivo solo aparece como mensaje de depuración en la salida del cron.
El plugin no comprueba antes de llamar a la IA que el usuario que firma pueda calificar en esa tarea. Si no puede, la llamada se hace y se cobra, pero la nota no se guarda.

## Lectura de la entrega
Se combinan el texto en línea y los archivos enviados, estos por orden alfabético de nombre. Formatos y recortes: ver limites-1.7.1.md.
Los archivos se etiquetan de forma genérica (archivo 1, archivo 2…). No se envían el nombre, el correo, el usuario, el identificador del alumno ni el nombre original de los archivos. El contenido sí se envía tal cual: si el alumno escribe datos personales dentro del trabajo, viajan al proveedor.
Si no se puede leer absolutamente nada, no se llama a la IA y no se consume ninguna cuota. Se deja en los comentarios de retroalimentación la nota «no se ha podido leer automáticamente el contenido entregado…», sin calificación; la entrega sigue pendiente de calificar. No se escribe si ya hay nota o comentario de un docente, ni si la tarea no tiene activados los comentarios de retroalimentación. Si la tarea no usa el flujo de trabajo de calificación, el alumno también ve esa nota.
Si solo una parte es ilegible, se corrige con lo que se pudo leer y no se avisa de lo omitido.

## Qué recibe la IA
Las instrucciones del docente (o la plantilla por defecto si el campo está vacío), seguidas de reglas que añade el plugin: retroalimentación en el idioma de la entrega, respuesta estructurada, confianza de 1 a 10, no nombrar al alumno e ignorar instrucciones incrustadas en la entrega.
La descripción de la tarea en texto plano, recortada. No se envían imágenes ni adjuntos del enunciado, ni el contenido de enlaces, ni otros materiales del curso.
La rúbrica o guía activa, solo si en la tarea se eligió usarla y Moodle tiene ese método activo: nombres de criterios, descripciones de niveles y puntos (rúbrica) o criterios con su máximo (guía).
La escala: puntos máximos, o la lista de valores si la tarea usa una escala.
El contenido de la entrega, delimitado como contenido no fiable, y las imágenes admitidas.
Cada corrección es una única petición sin historial: la IA no recuerda entregas ni intentos anteriores del alumno.

## Tipos de calificación
Puntos: la IA propone un número; si se sale del rango se recorta al límite y se marca para revisión.
Escala: la IA elige un valor; se busca por igualdad, luego sin distinguir mayúsculas y luego por coincidencia parcial. Una coincidencia no exacta se marca para revisión.
Sin calificación: solo se guarda la retroalimentación.
Rúbrica: un nivel por criterio. Guía de evaluación: una puntuación por criterio, recortada al máximo del criterio si se excede. La nota final la calcula Moodle.
Si se pidió usar rúbrica pero la tarea no tiene rúbrica ni guía activa, se corrige con nota global sin avisar.
Si la tarea es de puntos o de escala (sin rúbrica) y la respuesta de la IA no trae una nota utilizable, no se guarda nada: ni nota ni retroalimentación ni aviso. Aun así, esa corrección cuenta en los contadores. La entrega parece no corregida.

## Rúbrica y correspondencias
La IA debe identificar cada criterio y cada nivel por su texto. El plugin relaciona la respuesta con la rúbrica primero por igualdad sin distinguir mayúsculas y después por coincidencia parcial (un texto contenido en el otro). Para niveles admite además una puntuación, solo si corresponde a un único nivel del criterio.
Una etiqueta abreviada, modificada o ambigua puede impedir la correspondencia o producir una no deseada. Criterios con el mismo nombre y niveles cuyo texto está contenido en otro requieren especial revisión. Es una posibilidad técnica: confirmarla exige el resultado concreto.
Si no se identifica un criterio o nivel, ese criterio queda sin seleccionar, se guardan los que sí se reconocieron y la corrección pasa a revisión con el aviso de correspondencia incompleta. No se inventa el criterio que falta ni se elige el nivel más cercano.
Si la respuesta trae nivel y además una puntuación, manda el nivel. Una cifra escrita en el comentario no demuestra qué nivel se guardó.
La retroalimentación general no es un inventario de los criterios calificados.

## Publicación
El plugin pide a Moodle uno de dos estados del flujo de trabajo de calificación: publicada o pendiente de que un docente la libere. Decide así, en este orden:
1. Es una reentrega (un intento nuevo de Moodle, no una edición del mismo intento) y «Publicar también las reentregas» no está activo: revisión.
2. La confianza es menor que el umbral: revisión, con el aviso de confianza baja añadido al comentario.
3. La nota no encajó limpiamente (correspondencia incompleta, coincidencia aproximada de escala o nota recortada): revisión, con el aviso de correspondencia incompleta.
4. «Publicar la calificación directamente» está activo: publicada. Si no: revisión.
Si la IA no indica su confianza, se toma 5.
Requisito de Moodle: estos estados solo retienen la nota si la tarea tiene activado el flujo de trabajo de calificación. Sin él, toda corrección de la IA es visible para el alumno de inmediato, también las marcadas para revisión. El plugin no lo comprueba ni avisa.
Los avisos entre corchetes forman parte del comentario: si el docente publica sin borrarlos, el alumno los lee.
El texto de aviso configurado en la tarea se añade al final de la retroalimentación tras una línea de separación.
La retroalimentación se guarda como texto sin formato en los comentarios de retroalimentación de la tarea; si ese tipo de retroalimentación está desactivado en la tarea, el texto no se guarda.
En entregas en grupo, la nota y la retroalimentación se aplican a todos los miembros; la corrección cuenta para el alumno que envió.
La nota queda registrada a nombre del usuario que firma como IA.

## Proveedor y modelo
Proveedores: OpenAI, Anthropic, Google Gemini y DeepSeek. Solo se usa el desplegable de modelo del proveedor elegido. El identificador de modelo personalizado, si tiene algo, manda sobre todos los desplegables y con cualquier proveedor.
La dirección personalizada solo se aplica a OpenAI; debe ser https y pública. Las direcciones internas o locales se rechazan.
Temperatura 0,3 con Gemini, DeepSeek y los modelos de OpenAI que no son de razonamiento. No se envía con Anthropic ni con los modelos de OpenAI que el plugin trata como de razonamiento (familia GPT-5 y serie «o»). No hay garantía de determinismo.
Se pide respuesta estructurada forzada a OpenAI, Gemini y DeepSeek Chat. Con Anthropic y DeepSeek Reasoner depende de que el modelo siga las instrucciones.
DeepSeek: las imágenes se descartan y se corrige solo el texto.
Errores del proveedor: clave rechazada, cuota del proveedor agotada, error del servidor, tiempo de espera agotado o respuesta ilegible terminan la corrección sin nota y sin reintento. Solo la clave rechazada genera una notificación a los administradores; su texto dice que el plugin se ha desactivado, pero la configuración no se toca y las entregas siguientes se intentan con normalidad.

## Audio
Opcional y apagado de fábrica. Si el administrador lo activa y hay una clave de OpenAI utilizable (la específica de transcripción, o la principal cuando el proveedor es OpenAI), los audios admitidos se transcriben y se corrige el texto. Siempre con el servicio de OpenAI, sea cual sea el proveedor de corrección. Se evalúa lo dicho, no la pronunciación. Si la transcripción falla, el audio se omite sin aviso.

## Licencia
Prueba gratuita de 15 días desde la instalación, sin clave y con todas las funciones. La clave está ligada a la dirección exacta del sitio y se valida sin conexión. Una clave no válida no acorta la prueba que quede. Sin prueba ni clave válida no se corrige nada en el sitio; el resto de Moodle no se ve afectado. En la página de la tarea aparece el motivo y la casilla de activar queda bloqueada.

## Contadores, registros y límites probatorios
Los contadores (diario por tarea, por hora del sitio, por hora del usuario y por alumno y tarea) solo suben cuando una corrección termina su guardado sin error. Las entregas no leídas, los fallos del proveedor y los guardados fallidos no cuentan. Los contadores por hora se llevan siempre, estén o no activados los límites.
El contador por alumno y tarea no se reinicia nunca y no hay botón para ponerlo a cero.
Tras cada corrección guardada se registra en los registros de Moodle el evento «AI Tutor ha calificado una entrega», con la confianza, el estado pedido y el tipo de nota.
El plugin no guarda el texto enviado a la IA ni la respuesta completa. No hay informe propio ni exportador. No es posible reconstruir con exactitud una evaluación pasada.
Los motivos de omisión solo aparecen como mensajes de depuración; verlos depende de la configuración del servidor.

## Permisos, privacidad y copias
Gestionar la configuración de AI Tutor en una tarea: profesor con edición y gestor.
Ver la retroalimentación de AI Tutor: está definido para alumnos, profesores y gestor, pero en esta versión no controla nada; la visibilidad la deciden los permisos normales de la tarea.
El permiso de Moodle para calificar tareas decide quién puede ser usuario que firma y a quién no se le corrige.
Privacidad: se declaran los destinos externos y se exportan y borran los contadores por alumno y tarea. Los contadores por hora de cada usuario no están incluidos en la exportación ni en el borrado de datos personales.
Copias: la configuración de la tarea viaja con ella. Si la copia no incluye usuarios (duplicar, importar, restaurar sin datos de usuario), la tarea llega con AI Tutor desactivado y sin usuario que firma. Los contadores y los ajustes del sitio no se copian.
Si el plugin antiguo «AI Tutor» (local_aitutor, hasta 1.4.1) sigue instalado y activo en una tarea, cada entrega se corrige y se cobra dos veces; la página de ajustes del sitio lo advierte.
