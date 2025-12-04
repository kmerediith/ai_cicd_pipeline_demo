import sys
import os

# Ensure the package in src/ is importable
sys.path.insert(0, os.path.join(os.getcwd(), "src"))

from ai_cicd_pipeline.config import DeclarativeConfig
from ai_cicd_pipeline.orchestrator import PipelineOrchestrator
import yaml

cfg_path = os.path.join(os.getcwd(), "configs", "pipeline.example.yaml")
with open(cfg_path, "r") as f:
    data = yaml.safe_load(f) or {}

cfg = DeclarativeConfig(**data)
orc = PipelineOrchestrator(cfg)
orc.run()
