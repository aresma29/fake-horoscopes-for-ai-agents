from pathlib import Path

# Print the fake horoscope line stored in entry.txt (next to this file).
entry_path = Path(__file__).resolve().parent / "entry.txt"
line = entry_path.read_text(encoding="utf-8").rstrip("\n")
print(line)
