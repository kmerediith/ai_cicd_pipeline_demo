
from .base import Stage, GuardrailViolation
from ..pipeline_state import PipelineState
from ..config import DeclarativeConfig

class DeploymentPlanner(Stage):
    name = "DeploymentPlanner"

    def __init__(self, cfg: DeclarativeConfig):
        self.cfg = cfg

    def run(self, state: PipelineState) -> PipelineState:
        # Simple policy check
        if state.risk_score > self.cfg.stage_policy.block_deploy_if_risk_gt:
            raise GuardrailViolation(f"Risk {state.risk_score:.2f} exceeds threshold")

        strategy = self.cfg.stage_policy.allow_strategies[0]
        return state.with_updates(deploy_strategy=strategy)
