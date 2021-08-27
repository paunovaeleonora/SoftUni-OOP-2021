#!/usr/bin/env python3.6

"""some -- more than less, but less than more.

some is a pager… sometimes. If the input is less than one screen long,
some will print it directly to the terminal; otherwise, it will display
it using whatever pager is configured.

It should be noted that some doesn't actually know how your terminal
will render text, and so its behaviour is inherently based on an
approximation of how a small subset of text is usually rendered. In
situations where double-width characters or fancy ligatures are used,
for example, some will treat them as single-width when deciding whether
to invoke a pager.
"""


import argparse
import itertools
import math
import os
import shlex
import shutil
import signal
import subprocess
import sys
from typing import BinaryIO, Iterable, Optional, Sequence


def direct_write(lines: Sequence[bytes]) -> None:
    """Print some lines of text.

    The lines are assumed to end with newlines; no newlines will be
    added, apart from a final newline at the end of the output if there
    isn't one already -- though this is intended exclusively as a
    workaround for bad input, and should not be relied upon.

    NB: this function will not work properly if `sys.stdout.buffer` is
    not available, e.g. in IDLE.
    """
    # If there are no lines, or the only line is an empty string,
    # there's nothing to print!
    if lines and lines[-1]:
        sys.stdout.buffer.write(b"".join(lines))
        if not lines[-1].endswith(b"\n"):
            sys.stdout.buffer.write(b"\n")


def page(lines: Iterable[bytes], pager: Optional[str] = None) -> None:
    """Print some lines of text via a pager.

    If not specified, the pager to use will be automatically guessed
    from the user's environment (i.e. the $PAGER environment variable).
    If that's not found, a sensible default will be used. If no pager is
    available, a warning will be printed.
    """
    if pager is None:
        cmd = shlex.split(os.environ.get("PAGER", "less"))
    else:
        cmd = shlex.split(pager)

    if cmd[0].split(os.sep)[-1] == "less":
        # -R: interpret colour escape codes
        # +F: don't exit if the output fits on one screen
        # +X: emit magic init/deinit codes to clear the screen
        cmd.extend(["-R", "-+F", "-+X"])

    # TODO: make output to the pager faster.
    try:
        # less uses SIGINT to cancel prompts, so we must ignore it.
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        pager_proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, bufsize=0)
    except FileNotFoundError:
        print("No pager available :(")
        return
    else:
        for line in lines:
            try:
                pager_proc.stdin.write(line)
            except BrokenPipeError:
                # Pager exited.
                break
    finally:
        pager_proc.communicate()
        signal.signal(signal.SIGINT, signal.SIG_DFL)


def some(file: BinaryIO, reserved_lines: int = 3, check_wrap: bool = False) -> None:
    """Put the contents of a file into stdout, maybe via a pager.

    If less screen space is available than some thinks (e.g. output will
    be immediately pushed off the screen by a shell prompt), the
    `reserved_lines` argument can be used to decrease the number of
    lines that will be printed without invoking a pager. By default,
    some will try to avoid filling the *entire* screen with unpaged
    output -- this can be disabled by passing `reserved_lines=0`.

    some will usually only look at the number of lines in the string, so
    if the terminal wraps lines that are wider than the available screen
    space, a pager may not be invoked when it should be. If this
    behaviour is not desired, the `check_wrap` argument can be set to
    True.
    """
    terminal_width, terminal_height = shutil.get_terminal_size()
    usable_height = max(terminal_height - reserved_lines, 0)

    all_lines = iter(file.readline, b"")

    the_lines = list(itertools.islice(all_lines, terminal_height + 1))

    if len(the_lines) > usable_height or (
        check_wrap
        # TODO: len() is the wrong function to use here; we want to know
        # how many characters will be printed, not how many characters
        # are in the string. The following is a shoddy approximation,
        # but it will do for now.
        and sum(
            max(1, math.ceil(len(line[:-1]) / terminal_width)) for line in the_lines
        )
        > usable_height
    ):
        page(itertools.chain(the_lines, all_lines))
    else:
        direct_write(the_lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="some -- more than less, but less than more.", allow_abbrev=False
    )
    parser.add_argument(
        "file",
        metavar="filename",
        nargs="?",
        default=sys.stdin.buffer,
        type=argparse.FileType("rb"),
        help="optionally, a file to page",
    )
    args = parser.parse_args()
    with args.file as f:
        some(f, check_wrap=True)


if __name__ == "__main__":
    main()
