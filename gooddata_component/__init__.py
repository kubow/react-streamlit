import streamlit.components.v1 as components
from pathlib import Path

# Determine the absolute path to the build directory using pathlib
current_dir = Path(__file__).parent.absolute()
build_dir = current_dir / "gooddata-react" / "esm"

_component_func = components.declare_component(
    "gooddata_component",
    path=str(build_dir),
)

def gooddata_component(name, key=None):
    return _component_func(name=name, key=key)
