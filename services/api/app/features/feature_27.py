"""Feature module 27.

A small, realistic slice of code to emulate a growing service.
"""

from dataclasses import dataclass
from typing import Any

@dataclass
class FeatureResult:
    ok: bool
    detail: str
    data: dict[str, Any] | None = None

def run(input_value: str) -> FeatureResult:
    if not input_value:
        return FeatureResult(ok=False, detail="missing input")
    return FeatureResult(ok=True, detail="processed", data={"input": input_value, "len": len(input_value)})
