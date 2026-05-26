# Autoresearch Startup Interview

Ask only for information that is missing. If the user has already provided an answer, summarize it and move on.

## Required Questions

1. **Work directory**
   - What is the deep learning project run directory?
   - This is where `AUTORESEARCH.md` will be created.

2. **Task and metric**
   - What should be improved?
   - What is the primary metric?
   - Is higher or lower better?
   - What is the current best result?
   - What target result or practical effect should be reached?
   - Are there secondary constraints such as runtime, memory, stability, or model size?

3. **Research references**
   - Should each iteration ask whether a paper, method, or GitHub repository should be added as a reference?
   - If a reference is supplied, prioritize the official GitHub implementation or primary source before adapting the idea.

4. **Run command**
   - Which code or script should run the experiment?
   - If multiple commands/files are needed, should Codex create a unified `.sh` runner?
   - Where does the log file go?

5. **Reusable terminal**
   - Should the run use tmux or another reusable terminal?
   - Default: tmux.
   - Ask for session name or ID, or permission to create one.

6. **Allowed edit surface**
   - Which files may be changed?
   - Which exact functions, losses, modules, model blocks, configs, or code regions may be changed?
   - Which files or behaviors are forbidden?

7. **GPU resources**
   - Which GPU IDs are available?
   - Should Codex modify the run command, environment variables, or script arguments to use them?

8. **Experiment budget**
   - How long does one run take?
   - How many iterations should run automatically?
   - What early-stop or manual-stop rule should be used if the result is clearly poor?

## Confirmation Summary

Before editing code, summarize:

- workdir
- run command
- log path
- primary metric and target
- available GPUs
- tmux target
- allowed edit surface
- forbidden changes
- current experiment name
- recovery command
