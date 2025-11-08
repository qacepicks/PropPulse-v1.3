import subprocess
import json

def run_prop_ev(player, stat, line, odds):
    """
    Wrapper that runs prop_ev.py with arguments and returns JSON result.
    Works in both local and Streamlit Cloud environments.
    """
    try:
        result = subprocess.run(
            [
                "python",
                "prop_ev.py",
                "--player", str(player),
                "--stat", str(stat),
                "--line", str(line),
                "--odds", str(odds)
            ],
            capture_output=True,
            text=True,
            check=False
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        # Debug logging for troubleshooting
        print("=== DEBUG STDOUT ===")
        print(stdout)
        if stderr:
            print("=== DEBUG STDERR ===")
            print(stderr)

        # Try to parse JSON output from prop_ev.py
        try:
            data = json.loads(stdout)
            return data
        except json.JSONDecodeError:
            return {
                "Player": player,
                "Error": "Failed to parse output",
                "RawOutput": stdout
            }

    except Exception as e:
        return {"Player": player, "Error": str(e)}
