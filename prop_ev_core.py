import sys, os, json, subprocess

# Path to your main model folder
PROP_EV_PATH = os.path.expanduser("~/OneDrive/Desktop/propulse v1.1 beta")

def run_prop_ev(player, stat, line, odds):
    """
    Runs the real PropPulse model logic headlessly (no manual inputs).
    Returns parsed JSON result.
    """
    try:
        # Run the model via subprocess and return the structured output
        cmd = [
            "python",
            os.path.join(PROP_EV_PATH, "prop_ev.py"),
            "--player", player,
            "--stat", stat,
            "--line", str(line),
            "--odds", str(odds)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout.strip()

        # Optional: extract the final EV JSON block if your model prints one
        if "{" in output and "}" in output:
            json_block = output[output.find("{"):output.rfind("}")+1]
            return json.loads(json_block)

        # Fallback: raw text
        return {"Player": player, "Output": output}

    except Exception as e:
        return {"Player": player, "Error": str(e)}
