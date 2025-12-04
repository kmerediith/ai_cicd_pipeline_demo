
from .base import Stage
from ..pipeline_state import PipelineState

class Deployer(Stage):
    name = "Deployer"

    def run(self, state: PipelineState) -> PipelineState:
        # Mock: pretend deploy succeeded
        return state.with_updates(deploy_status="success")
