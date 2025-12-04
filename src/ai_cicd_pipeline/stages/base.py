
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Tuple
from ..pipeline_state import PipelineState

class Stage(ABC):
    name: str

    @abstractmethod
    def run(self, state: PipelineState) -> PipelineState:
        ...

class GuardrailViolation(Exception):
    pass
