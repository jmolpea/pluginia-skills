# Pluginia · Asistentes de los plugins (skills)

Skills para Claude y ChatGPT que acompañan a los plugins de Moodle de Pluginia (RSMAX Consulting S.L.).
Cada una resuelve cualquier duda sobre un plugin: qué hace, cómo se configura cada ajuste, qué límites
tiene y cómo conseguir un resultado concreto. También ayuda a diagnosticar y probar casos reales.

Contienen documentación funcional, no código: no necesitan acceso a su Moodle ni a ningún repositorio.

## Descargar

| Plugin | Versión documentada | Skill (zip) | Manual de configuración |
|---|---|---|---|
| Smart Tutor & Support AI (`block_openaiagent`) | 5.3.2 | [smart-tutor-moodle-diagnostico](https://github.com/jmolpea/pluginia-skills/raw/main/dist/smart-tutor-moodle-diagnostico.zip) | [Manual](https://claude.ai/artifact/Ko6vHpvgSzUBNEcF9Nxs8R) |
| AI Tutor (`local_rsmaxtutor`) | 1.7.2 | [evaluador-ia-moodle-diagnostico](https://github.com/jmolpea/pluginia-skills/raw/main/dist/evaluador-ia-moodle-diagnostico.zip) | [Manual](https://claude.ai/artifact/FsE6HtPSgw77e3w7uVcKsk) |
| AI course recommender (`block_aicourserecommender`) | 1.0.0-beta5 | [recomendador-cursos-ia-moodle-diagnostico](https://github.com/jmolpea/pluginia-skills/raw/main/dist/recomendador-cursos-ia-moodle-diagnostico.zip) | [Manual](https://claude.ai/artifact/LCZgLbHfAnSBkurowGLZ95) |
| Forumia (`local_forumia`) | 1.8.3 | [forumia-moodle-diagnostico](https://github.com/jmolpea/pluginia-skills/raw/main/dist/forumia-moodle-diagnostico.zip) | [Manual](https://claude.ai/artifact/Qg9adYg7HtbnatxfFCi825) |
| AI Roleplay (`mod_airoleplay`) | 1.1.1 | [ai-roleplay-moodle-diagnostico](https://github.com/jmolpea/pluginia-skills/raw/main/dist/ai-roleplay-moodle-diagnostico.zip) | [Manual](https://claude.ai/artifact/9rrxnBoMsHAgMzhKErn92D) |
| Pluginia Analytics (`local_pluginia_analytics`) | 1.1.1 | [pluginia-analytics-moodle-diagnostico](https://github.com/jmolpea/pluginia-skills/raw/main/dist/pluginia-analytics-moodle-diagnostico.zip) | [Manual](https://claude.ai/artifact/CZfR9hAnk2UnCQRgFTBH3R) |
| Course custom head assets (`local_coursehead`) | 1.2.1 | [coursehead-moodle-diagnostico](https://github.com/jmolpea/pluginia-skills/raw/main/dist/coursehead-moodle-diagnostico.zip) | [Manual](https://claude.ai/artifact/S1C8aFgCzaqxcegdHXqanX) |
| AI Viva (`mod_aiviva`) | 1.3.1 | [ai-viva-moodle-diagnostico](https://github.com/jmolpea/pluginia-skills/raw/main/dist/ai-viva-moodle-diagnostico.zip) | [Manual](https://claude.ai/artifact/RckemidnHhdYikr8HM2XHQ) |
| RSMAX (`theme_rsmax`) | 1.4.3 | [tema-rsmax-moodle-diagnostico](https://github.com/jmolpea/pluginia-skills/raw/main/dist/tema-rsmax-moodle-diagnostico.zip) | [Manual](https://claude.ai/artifact/UgYL8Job3Sh5p6a56HMjSQ) |
| Peer Review Studio (`mod_peerreviewstudio`) | 1.0.1 | [peer-review-studio-moodle-diagnostico](https://github.com/jmolpea/pluginia-skills/raw/main/dist/peer-review-studio-moodle-diagnostico.zip) | [Manual](https://claude.ai/artifact/RzMxCe9u5hXWWZy9kPUcXq) |
| Decision Arena (`mod_decisionarena`) | 0.8.1 | [decision-arena-moodle-diagnostico](https://github.com/jmolpea/pluginia-skills/raw/main/dist/decision-arena-moodle-diagnostico.zip) | [Manual](https://claude.ai/artifact/LWRnWzs6sxsFBc3Nx2AD3K) |
| AI Live Session (`mod_ailivesession`) | 1.0.2 | [ai-live-session-moodle-diagnostico](https://github.com/jmolpea/pluginia-skills/raw/main/dist/ai-live-session-moodle-diagnostico.zip) | [Manual](https://claude.ai/artifact/J58N9JJybXxofoznCsvqro) |
| Registro por email con retorno al curso (`auth_coursereturn`) | 1.1.0 | [coursereturn-moodle-diagnostico](https://github.com/jmolpea/pluginia-skills/raw/main/dist/coursereturn-moodle-diagnostico.zip) | [Manual](https://claude.ai/artifact/S9nVg3PK3GW412ms6GScy9) |

Los enlaces de descarga no cambian: siempre bajan la última versión de la skill.

## Instalar

- **Claude (claude.ai o la app):** Ajustes › Capacidades › Skills › Subir skill, y elija el zip.
- **Claude Code:** descomprima el zip en `~/.claude/skills/`.
- **ChatGPT / Codex:** suba el zip donde su plan permita añadir skills.

Después, pregunte con normalidad: «¿Qué límite de mensajes tiene Forumia por foro?», «Esta entrega se
ha quedado sin nota, ¿qué reviso?».

## Qué esperar

- Cada skill indica la versión del plugin que documenta. Si usted tiene otra, le dirá qué parte sigue
  siendo aplicable.
- Proponen primero cambios de configuración y una prueba controlada. No modifican su Moodle.
- Antes de compartir un caso real, quite nombres, correos e identificadores de alumnos.

## Estructura de cada skill

```
NOMBRE-SKILL/
  SKILL.md                     cuándo usarla y cómo trabaja
  references/
    funcionamiento-X.Y.Z.md    cómo funciona el plugin
    limites-X.Y.Z.md           límites y valores de fábrica
    configuracion.md           cada ajuste del sitio y de la actividad
    protocolo-diagnostico.md   qué datos recoger y árbol de síntomas
    ajustes-y-pruebas.md       qué puede cambiar usted y cómo probarlo
    casos-validacion.md        casos de comprobación
```

`build.py` empaqueta una skill en `dist/` y comprueba que no incluye código.
