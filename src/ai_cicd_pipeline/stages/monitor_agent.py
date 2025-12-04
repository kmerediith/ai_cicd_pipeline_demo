
from .base import Stage
from ..pipeline_state import PipelineState

class MonitorAgent(Stage):
    name = "MonitorAgent"

    def run(self, state: PipelineState) -> PipelineState:
        # Mock: minimal live metrics; no anomalies
        metrics = {"latency_p99_ms": 420, "error_rate_pct": 0.1}
        return state.with_updates(live_metrics=metrics, anomalies=())
