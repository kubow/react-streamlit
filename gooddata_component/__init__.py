import streamlit.components.v1 as components
from pathlib import Path

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "gooddata-react",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # Determine the absolute path to the build directory using pathlib
    current_dir = Path(__file__).parent.absolute()
    build_dir = current_dir / "gooddata-react" / "build"
    _component_func = components.declare_component(
        "gooddata_component",
        path=str(build_dir),
    )

def gooddata_component(name, key=None):
    return _component_func(name=name, key=key, default=0)
