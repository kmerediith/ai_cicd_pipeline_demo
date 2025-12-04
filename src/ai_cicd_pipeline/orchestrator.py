
from typing import List
from rich.console import Console
from rich.table import Table

from .pipeline_state import PipelineState
from .config import DeclarativeConfig
from .stages.commit_ingestor import CommitIngestor
from .stages.analyzer_ai import AnalyzerAI
from .stages.test_selector import TestSelector
from .stages.flaky_test_manager import FlakyTestManager
from .stages.risk_predictor_ai import RiskPredictorAI
from .stages.build_executor import BuildExecutor
from .stages.test_runner import TestRunner
from .stages.deployment_planner import DeploymentPlanner
from .stages.deployer import Deployer
from .stages.monitor_agent import MonitorAgent
from .stages.rollback_controller import RollbackController
from .stages.base import GuardrailViolation

console = Console()

class PipelineOrchestrator:
    def __init__(self, cfg: DeclarativeConfig):
        self.cfg = cfg
        self.timeline: List[str] = []

        self.stages = [
            CommitIngestor(),
            AnalyzerAI(),
            TestSelector(),
            FlakyTestManager(),
            RiskPredictorAI(),
            BuildExecutor(),
            TestRunner(),
            DeploymentPlanner(cfg),
            Deployer(),
            MonitorAgent(),
            RollbackController(),
        ]

    def run(self) -> PipelineState:
        state = PipelineState()
        for s in self.stages:
            try:
                state = s.run(state)
                self.timeline.append(f"{s.name} ✓")
            except GuardrailViolation as e:
                self.timeline.append(f"{s.name} ✗ GuardrailViolation: {e}")
                break
        self._print_timeline(state)
        return state

    def _print_timeline(self, state: PipelineState) -> None:
        table = Table(title=f"Pipeline run: {self.cfg.name}")
        table.add_column("Stage", style="bold")
        for item in self.timeline:
            table.add_row(item)
        console.print(table)
        console.print("""
[bold]Summary[/bold]:
- git_hash: {git}
- changed_files: {files}
- risk_score: {risk}
- deploy_strategy: {strategy}
- deploy_status: {status}
- anomalies: {anoms}
""".format(
            git=state.git_hash,
            files=state.changed_files,
            risk=state.risk_score,
            strategy=state.deploy_strategy,
            status=state.deploy_status,
            anoms=state.anomalies,
        ))
