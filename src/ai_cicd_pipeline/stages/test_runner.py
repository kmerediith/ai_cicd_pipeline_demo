
from .base import Stage
from ..pipeline_state import PipelineState

class TestRunner(Stage):
    name = "TestRunner"

    def run(self, state: PipelineState) -> PipelineState:
        # Mock: mark all tests as passed
        results = {t: "passed" for t in state.selected_tests}
        return state.with_updates(test_results=results)
