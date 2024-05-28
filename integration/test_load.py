import subprocess
import pytest

def capture_command_output(command):
    """
    Captures the output of a command as a list of lines.

    Args:
        command: The command to execute.

    Returns:
        A list of lines from the command's output.
    """

    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate()

    # Check if there were any errors
    # if stderr:
        # print("Error:", stderr)

    # Split the output into lines and return
    return stdout.splitlines()


@pytest.mark.integration
@pytest.mark.medium
def test_load():
    """test command load"""
    out = capture_command_output("dundie load .\\tests\\assets\\people.csv")            

    assert len(out) == 3
    print(len(out))

