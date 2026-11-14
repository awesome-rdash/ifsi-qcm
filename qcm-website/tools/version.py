"""Écrit site/data/version.json depuis git : numéro de version (nombre de commits), date de mise
à jour et changelog (sujet des 10 derniers commits). À lancer après convert_apkg.py, qui vide
site/data/. Dans l'Action, le checkout doit avoir tout l'historique (fetch-depth: 0).
"""
import json
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent


def git(*args):
    return subprocess.run(["git", *args], cwd=RACINE, check=True, capture_output=True,
                          encoding="utf-8").stdout


def main(sortie):
    # Commits du site seulement : ni l'historique du skill (fusionné par subtree) ni ses commits.
    site = ["--first-parent", "HEAD", "--", ":/", ":(top,exclude)skill", ":(top,exclude)qcm-generation"]
    total = int(git("rev-list", "--count", *site))
    lignes = git("log", "-10", "--format=%cI%x1f%s", *site).splitlines()
    changelog = [{"version": total - i, "date": d, "raison": s}
                 for i, (d, s) in enumerate(l.split("\x1f", 1) for l in lignes)]
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(json.dumps({"version": total, "date": changelog[0]["date"],
                                  "changelog": changelog}, ensure_ascii=False, indent=1), "utf-8")
    print(f"version {total} du {changelog[0]['date']}")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else RACINE / "site" / "data" / "version.json")
