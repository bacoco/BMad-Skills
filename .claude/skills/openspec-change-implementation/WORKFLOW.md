# Workflow — OpenSpec Implementation

1. **Readiness Check**
   - Ensure proposal and tasks are approved and Level 0-1 in scope.
   - Confirm environment setup and access permissions.

2. **Planning**
   - Identify affected files and commands.
   - Prepare rollback or backup steps if needed.

3. **Execution**
   - Complete tasks sequentially, logging actions with `scripts/update_execution_log.py` (or manual edits using the template).
   - Keep commits small and traceable to proposal tasks.

4. **Verification**
   - Run tests or validations aligning with acceptance signals.
   - Capture outputs and evidence for reviewers.

5. **Closure**
   - Update proposal/tasks with status and follow-ups.
   - Notify stakeholders or orchestrator about completion and next steps.
