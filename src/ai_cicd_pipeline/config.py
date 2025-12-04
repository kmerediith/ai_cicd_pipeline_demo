
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Dict

class StagePolicy(BaseModel):
    block_deploy_if_risk_gt: float = Field(0.8, description="Block deploy if risk score greater than this.")
    min_coverage_for_deploy: float = Field(0.7, description="Require at least this coverage to deploy.")
    allow_strategies: List[Literal["canary", "blue_green", "rolling"]] = ["canary", "blue_green", "rolling"]

class MonitoringRules(BaseModel):
    latency_p99_ms: int = 1000
    error_rate_pct: float = 1.0
    auto_rollback_on_violation: bool = True

class DeclarativeConfig(BaseModel):
    name: str = "AI Driven Intelligent CI/CD Pipeline"
    stage_policy: StagePolicy = StagePolicy()
    monitoring: MonitoringRules = MonitoringRules()
    parameters: Dict[str, str] = {}
