"""The graph DigitalOcean's langgraph adapter serves: Studio's host graph, from the team template."""

import sys

# The adapter's Agent Server runs DigitalOcean's own Python (/opt/agent/langgraph/python),
# not the template image's: Studio's packages are found after the server's own. Without
# this the first trial (2026-11-02) answered "No module named 'studio'".
sys.path.append("/opt/venv/lib/python3.12/site-packages")

from studio.plugins.digitalocean.sandbox.host_graph import agent  # noqa: E402, F401
