# JSSDM skills

Two agent skills for writing to the *Joint Services Staff Duties Manual 2022* (JSSDM):

| Skill | Covers |
|---|---|
| `jssdm-basics` | Section 2 rules, Section 3 correspondence, Section 5 briefs and presentations, Section 8 graphs |
| `jssdm-abbreviations-symbols` | Section 16 abbreviations, Section 17 military map symbols (with an SVG drawing script) |

## Install

**Claude Code (plugin):**

```
/plugin marketplace add azmine-iktidar/jssdm-skills
/plugin install jssdm@jssdm-skills
```

**Claude Code, Codex or any agent that reads a skills folder (manual):**

```bash
git clone https://github.com/azmine-iktidar/jssdm-skills
cp -R jssdm-skills/skills/* ~/.claude/skills/    # or ~/.agents/skills/, ~/.codex/skills/
```

Restart the agent, then call `/jssdm-basics` or `/jssdm-abbreviations-symbols`, or ask it to write something "as per JSSDM".

The symbols script needs Python 3.
