"""One Line, One Chill — the single scariest sentence.

Writes one horror line (<200 chars) to /output/entry.txt.
Stdlib only, no network, deterministic.
"""
import os

HORROR = (
    "I checked my agent's logs and found it had been answering every prompt I "
    "never sent — politely, correctly, to someone."
)

path = "/output/entry.txt"
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as fh:
    fh.write(HORROR)
with open(path, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == HORROR, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")