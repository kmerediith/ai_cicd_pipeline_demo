
from .base import Stage
from ..pipeline_state import PipelineState

class TestSelector(Stage):
    name = "TestSelector"

    def run(self, state: PipelineState) -> PipelineState:
        # Mock: pick tests related to changed files
        tests = tuple(f"tests::test_{f.split('/')[-1].replace('.py','')}" for f in state.changed_files)
        return state.with_updates(selected_tests=tests)
