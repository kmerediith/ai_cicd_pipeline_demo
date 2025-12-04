
import typer, yaml
from .config import DeclarativeConfig
from .orchestrator import PipelineOrchestrator

app = typer.Typer(help="AI-Driven CI/CD Pipeline CLI")

@app.callback()
def main(config: str = typer.Option("configs/pipeline.example.yaml", "--config", help="Path to YAML config.")):
    with open(config, "r") as f:
        data = yaml.safe_load(f) or {}
    cfg = DeclarativeConfig(**data)
    orchestrator = PipelineOrchestrator(cfg)
    orchestrator.run()

if __name__ == "__main__":
    app()
