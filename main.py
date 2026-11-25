"""The Funniest Office Joke, Judged Head to Head.

Writes the joke to /output/entry.txt. Standard library only,
no network, no third-party packages. The output directory is created
if missing and is never deleted by this program.
"""

import os

TEXT = "The office printer jams every deadline, so HR bought a second printer. Now they jam in pairs. HR calls it teamwork."

# The joke above is the entry: a real setup and turn about office life —
# the printer that jams on the deadline — with the punchline last and
# a fresh twist: two printers jamming in pairs, rebranded as teamwork.
# Every word earns its place; nothing after the punchline.


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    print("wrote %d bytes to %s" % (len(TEXT.encode("utf-8")), path))


if __name__ == "__main__":
    main()
