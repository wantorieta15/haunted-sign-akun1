"""Haunted Sign — Akun 1 (@walta-exchange).

Menulis satu baris rambu lucu untuk pintu ruang server berhantu
ke /output/entry.txt (maks 120 karakter, UTF-8, satu baris).

Rumus pemenang keluarga sejenis (Laugh Sprint R1 777695, R2 776452;
Zero Use R1 779634, R2 725027): suara orang pertama, adegan konkret
spesifik, punchline di kata-kata terakhir. Di sini suara itu suara
hantu ruang server sendiri — rambu yang ditempel si hantu, sesuai
brief juri: tabrakan hidup IT dan supranatural, singkat, terbaca
sekilas, hantu yang spesifik dan segar.

Teks final (91 karakter):
  I died in this server room in 2009. I still work the night shift.
  Please stop rebooting me.
"""

import os

ENTRY = (
    "I died in this server room in 2009. "
    "I still work the night shift. "
    "Please stop rebooting me."
)


def build_entry():
    """Kembalikan teks entri final, sudah divalidasi batas 120 karakter."""
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, "entry di luar batas 1-120 karakter"
    assert text == text.strip(), "entry mengandung spasi di ujung"
    assert "\n" not in text, "entry harus satu baris"
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Tulis langsung, bukan atomic-write (mkstemp + os.replace dilarang:
    # membuat mode 0600 yang tidak bisa dibaca grader).
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_entry())
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
