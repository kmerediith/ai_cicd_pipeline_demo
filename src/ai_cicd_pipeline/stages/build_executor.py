
from .base import Stage
from ..pipeline_state import PipelineState

class BuildExecutor(Stage):
    name = "BuildExecutor"

    def run(self, state: PipelineState) -> PipelineState:
        # Mock: build produces an artifact
        artifacts = ("dist/app-abc123.tar.gz",)
        meta = {"duration_s": 30}
        return state.with_updates(build_artifacts=artifacts, build_meta=meta)
