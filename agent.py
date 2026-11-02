"""The graph DigitalOcean's langgraph adapter serves: Studio's host graph, from the team template."""

import sys

# The adapter's Agent Server runs DigitalOcean's own Python (/opt/agent/langgraph/python),
# not the template image's: Studio's packages are found after the server's own. Without
# this the first trial (2026-11-02) answered "No module named 'studio'". They are built
# for Python 3.12 (compiled ones too), so another Python is refused here, in words.
if sys.version_info[:2] != (3, 12):
    raise RuntimeError(
        "the Agent Server's Python is not 3.12, the image's packages are"
    )
sys.path.append("/opt/venv/lib/python3.12/site-packages")

from studio.plugins.digitalocean.sandbox.host_graph import agent  # noqa: E402, F401
