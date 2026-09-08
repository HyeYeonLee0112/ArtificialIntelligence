"""Write a traceable experiment record without inventing measured results."""
import json
import math
from pathlib import Path


def save_metrics(path, *, question, seed, device, baseline, changed, metrics):
    if not question.strip():
        raise ValueError("question must not be empty")
    if not isinstance(seed, int) or isinstance(seed, bool):
        raise ValueError("seed must be an integer")
    if not device.strip():
        raise ValueError("device must not be empty")
    keys = set(baseline) | set(changed)
    differences = [k for k in keys
                   if k not in baseline or k not in changed or baseline[k] != changed[k]]
    if len(differences) != 1:
        raise ValueError("change exactly one experimental condition")
    if not metrics or any(isinstance(v, bool) or not isinstance(v, (int, float))
                          or not math.isfinite(v) for v in metrics.values()):
        raise ValueError("metrics must contain finite measured numbers")
    record = dict(question=question, seed=seed, device=device, baseline=baseline,
                  changed=changed, changed_variable=differences[0], metrics=metrics)
    content = json.dumps(record, ensure_ascii=False, indent=2, allow_nan=False)
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content + "\n", encoding="utf-8")
    return record
