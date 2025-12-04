
from .base import Stage
from ..pipeline_state import PipelineState

class FlakyTestManager(Stage):
    name = "FlakyTestManager"

    def run(self, state: PipelineState) -> PipelineState:
        # Mock: pretend none are flaky (starter)
        return state.with_updates(flaky_tests=())
