
from __future__ import annotations
from dataclasses import dataclass, replace
from typing import Tuple, Dict, Any, Optional

@dataclass(frozen=True)
class PipelineState:
    # Commit
    git_hash: Optional[str] = None
    changed_files: Tuple[str, ...] = ()
    author: Optional[str] = None
    timestamp: Optional[str] = None

    # Analysis
    high_risk_components: Tuple[str, ...] = ()
    analyzer_features: Dict[str, Any] = None

    # Build
    build_artifacts: Tuple[str, ...] = ()
    build_meta: Dict[str, Any] = None

    # Test
    selected_tests: Tuple[str, ...] = ()
    test_results: Dict[str, Any] = None
    flaky_tests: Tuple[str, ...] = ()

    # Risk
    risk_score: float = 0.0

    # Deploy
    deploy_strategy: Optional[str] = None
    deploy_status: Optional[str] = None

    # Monitor
    live_metrics: Dict[str, Any] = None
    anomalies: Tuple[str, ...] = ()

    def with_updates(self, **kwargs) -> "PipelineState":
        return replace(self, **kwargs)
