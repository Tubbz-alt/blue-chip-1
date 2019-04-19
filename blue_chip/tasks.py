"""
blue_chip.tasks.py
~~~~~~~~~~~~~~~~~~
Invoke tasks file
"""
from invoke import task

from blue_chip import constants


@task(
    help={
        "line-length": "How many characters per line to allow. [default: {}]".format(
            constants.LINE_LENGTH
        ),
        "targets": "Paths/directories to format. [default: . ]",
    }
)
def fmt(ctx, line_length=constants.LINE_LENGTH, targets="."):
    """Format python source code."""
    if isinstance(targets, (list, tuple, set)):
        targets = " ".join(targets)
    ctx.run(f"black --line-length {line_length} {targets}")


@task
def lint(ctx, targets="."):
    """Run static analysis on python source code."""
    ctx.run(f"prospector {targets}")