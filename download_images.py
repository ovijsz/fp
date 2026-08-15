#!/usr/bin/env python3
"""
Downloads every image referenced in data.json into ./assets/images/<category>/
and rewrites data.json so all "image" fields point to the local copies instead
of https://api.fp-collective.com/...

Run this on a machine WITH internet access, from inside the site folder
(next to data.json and index.html):

    python3 download_images.py

Requires only the Python standard library (urllib) - no extra installs needed.
Safe to re-run: already-downloaded files are skipped.
"""
import json, os, re, time, random, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(HERE, "data.json")
IMG_ROOT = os.path.join(HERE, "assets", "images")

CATEGORIES = ["fish", "baits", "lures", "hooks", "luretypes", "jigheads",
              "boilies", "sinkers", "keepnets", "places"]

HEADERS = {"User-Agent": "Mozilla/5.0 (offline reference tool; personal use)"}

def safe_name(url, item_id):
    ext = os.path.splitext(url.split("?")[0])[1] or ".png"
    base = re.sub(r"[^a-zA-Z0-9_-]", "-", str(item_id))
    return f"{base}{ext}"

def download(url, dest):
    if os.path.exists(dest):
        return True
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp, open(dest, "wb") as f:
            f.write(resp.read())
        return True
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        print(f"  FAILED: {url} -> {e}")
        return False

def main():
    with open(DATA_PATH, encoding="utf-8") as f:
        data = json.load(f)

    total, ok, failed, skipped = 0, 0, 0, 0

    for cat in CATEGORIES:
        items = data.get(cat, [])
        if not items:
            continue
        cat_dir = os.path.join(IMG_ROOT, cat)
        os.makedirs(cat_dir, exist_ok=True)
        print(f"\n=== {cat}: {len(items)} items ===")
        for item in items:
            url = item.get("image")
            if not url or not url.startswith("http"):
                continue
            total += 1
            fname = safe_name(url, item.get("id", total))
            dest = os.path.join(cat_dir, fname)
            local_rel = f"assets/images/{cat}/{fname}"
            already = os.path.exists(dest)
            success = download(url, dest)
            if success:
                item["image"] = local_rel
                if already:
                    skipped += 1
                else:
                    ok += 1
                    time.sleep(0.15 + random.uniform(0, 0.15))  # be polite, slower + jittered pace between real downloads
            else:
                failed += 1
            if total % 50 == 0:
                print(f"  ...{total} images processed so far")

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    print(f"\nDone. Downloaded: {ok}, already had: {skipped}, failed: {failed}, total referenced: {total}")
    print("data.json has been rewritten to point at the local assets/images/ copies.")
    if failed:
        print("Some images failed (network hiccup or removed asset) - their entries still point at the original fp-collective URL as a fallback.")

if __name__ == "__main__":
    main()
