# Ajustes y pruebas antes de escalar

## Regla de intervención
Buscar primero una solución con la configuración del sitio, la de la actividad, la redacción (escenario, rol, personalidad, instrucciones de evaluación, restricciones), las excepciones o las condiciones del alumno. Cambiar solo el elemento que explique el problema.
Conservar los objetivos de aprendizaje y la exigencia de la actividad. No proponer desactivar la revisión del profesor ni subir límites para ocultar un problema.
Explicar las limitaciones que ninguna configuración resuelve: rúbrica y pesos fijos, profesores sin acceso a la sesión, tiempo real solo con un avatar, reconocimiento de voz dependiente del navegador, sin pausa del reloj.

## Lista de revisión
| Elemento | Revisar | Ajuste que se puede probar |
|---|---|---|
| Licencia | Estado y dirección del sitio | Pegar la clave completa; pedir una nueva si cambió la dirección |
| Claves y proveedor | Prueba de conexión; proveedor del modelo de la actividad | Guardar la clave; elegir en la actividad un modelo del proveedor actual |
| Voz de avatares | Proveedor de TTS y su clave; voz elegida | Cambiar de proveedor de TTS; volver a elegir voz en la actividad |
| Micrófono | Navegador, permiso, https, ruido | Cambiar el modo de micrófono; usar Chrome o Edge; respuestas escritas como alternativa |
| Ritmo y cuotas | Intervenciones por minuto, alumnos simultáneos | Subir el límite por usuario o el del sitio |
| Tiempo | Duración frente a lo que exige el escenario | Cambiar la duración; simplificar el objetivo |
| Intentos y fechas | Cupo, apertura y cierre | Excepción de usuario o grupo |
| Conversación pobre | Escenario, rol y personalidad | Añadir objetivo, tensión y condiciones para ceder en la personalidad |
| Evaluación discutida | Avisos, palabras, desglose, instrucciones | Precisar las instrucciones de evaluación; modelo recomendado para evaluar |
| Publicación | Revisión del profesor, bloqueo, avisos | Publicar desde «Entregas»; ajustar la revisión |
| Contenido | Moderación y restricciones | Activar la moderación; añadir restricciones a la actividad |
| Coste | Modelo, voz, duración, intentos, motor | Modelo económico, voz del navegador, sesiones más cortas, motor por turnos |

## Cómo redactar para que funcione
- Escenario: lugar, antecedentes, objetivo de cada parte y cómo acaba bien. Lo esencial al principio, porque el evaluador usa los primeros 3.000 caracteres.
- Rol del participante: qué puede y qué no puede hacer el alumno; es la base de la «adherencia al rol».
- Personalidad del avatar: carácter, tono, lo que oculta y cuándo cede. No repetir normas que el plugin ya impone (idioma, brevedad, no salirse del personaje).
- Instrucciones de evaluación: comportamientos observables en lo que dice el alumno, redactados como «valora…» y «penaliza…». No pedir cambiar pesos ni añadir criterios: no tiene efecto garantizado.
- Restricciones adicionales: normas breves y concretas; primeros 2.000 caracteres.

## Pruebas controladas
Condiciones: copia de la actividad en un curso de prueba, cuenta con rol de estudiante, Chrome o Edge, https, sesión de 5 minutos. Avisar de que cada sesión y cada recálculo tienen coste de IA.
Cambiar una sola variable por prueba y anotar: configuración, qué se hizo, mensaje o resultado literal y hora.
| Objetivo | Prueba | Resultado esperado según las referencias |
|---|---|---|
| Conexión | Ejecutar la prueba de conexión | Licencia, modelos y voz en OK |
| Voz de avatares | Misma actividad con TTS de servidor y luego del navegador | Con servidor suena la voz elegida; con navegador, la del dispositivo |
| Micrófono | La misma frase en los tres modos | Manos libres envía tras la pausa; los otros, al pulsar o soltar |
| Sin micrófono | Denegar el permiso | Aviso y cuadro para escribir |
| Reanudar | Recargar la página a mitad de sesión | Vuelve la conversación y el tiempo restante real |
| Final abandonado | Cerrar la pestaña y esperar | Cierre en unos minutos y evaluación en segundo plano, con el cron activo |
| Participación nula | Sesión sin decir nada | Nota 0, aviso y revisión obligatoria |
| Participación escasa | Menos de 20 palabras | Aviso de poca participación; queda en revisión |
| Publicación | Revisión activada y desactivada | En revisión hasta publicar, o publicación automática |
| Instrucciones de evaluación | Recalcular el mismo intento tras cambiarlas | Cambian comentarios y, quizá, puntuaciones; no los pesos |
| Límite por usuario | Turnos muy seguidos | Mensaje de demasiadas solicitudes al superar el límite |
| Excepción | Excepción de usuario con más intentos | Aparece «Empezar un nuevo intento» |
Recalcular tiene espera de 5 minutos y máximo de 5 al día por intento: planificar las pruebas de evaluación con eso en cuenta.
No comparar notas de dos recálculos como si debieran coincidir: la evaluación de una IA varía.

## Cuándo y cómo escalar al mantenedor
Escalar solo si, con la configuración correcta y las pruebas hechas, el comportamiento contradice las referencias o no hay ajuste que cumpla el requisito.
Entregar: versión del plugin y de Moodle, navegador, configuración relevante, pasos numerados, resultado esperado y obtenido, mensajes literales, capturas sin datos personales, ajustes ya probados y su resultado, y el criterio con el que se daría por resuelto.
Peticiones habituales que no son defectos sino límites del diseño actual: rúbrica o pesos personalizados, pausa del reloj, que un profesor haga la sesión con su rol, tiempo real con varios avatares, informe de gasto en dinero.
