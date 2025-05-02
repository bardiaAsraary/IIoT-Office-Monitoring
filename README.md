1. Install the TLA+ VS Code extensions
2. Open the `verification` folder in VS Code
3. The specification includes:
   - Temperature bounds (15-30°C)
   - Humidity bounds (30-80%)
   - Occupancy comfort requirements

To verify:
```bash
# In VS Code command palette:
TLA+: Check Model with TLC
```

Verification results show:
- All safety properties are maintained
- No deadlocks in the system
- All processes are live