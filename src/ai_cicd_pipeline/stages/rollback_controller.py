
from .base import Stage
from ..pipeline_state import PipelineState

class RollbackController(Stage):
    name = "RollbackController"

    def run(self, state: PipelineState) -> PipelineState:
        # Mock: no rollback triggered in starter
        return state
