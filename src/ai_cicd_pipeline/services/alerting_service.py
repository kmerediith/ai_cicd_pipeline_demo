
from dataclasses import dataclass

@dataclass
class AlertingService:
    def send(self, message: str) -> None:
        print(f"[ALERT] {message}")
