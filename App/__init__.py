from pathlib import Path

_BACKEND_APP = Path(__file__).resolve().parent.parent / "backend" / "App"
__path__ = [str(_BACKEND_APP)]
