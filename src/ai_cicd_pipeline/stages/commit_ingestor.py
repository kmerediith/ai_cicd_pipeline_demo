
from .base import Stage
from ..pipeline_state import PipelineState

class CommitIngestor(Stage):
    name = "CommitIngestor"

    def run(self, state: PipelineState) -> PipelineState:
        # Mock: initialize from environment or placeholders
        return state.with_updates(
            git_hash="abc123",
            changed_files=("src/app.py", "tests/test_app.py"),
            author="dev@example.com",
            timestamp="2025-09-27T14:00:00Z",
        )
