THE COLLECTIVE — Fishing Planet reference site
================================================

WHAT'S IN THIS ZIP
- index.html         the site (Fish + Gear + Maps + Trends sections)
- data.json           the full database, incl. real player catch-report stats
- assets/maps/         all 30 real in-game map shapes (SVG), one per location
- .nojekyll            tells GitHub Pages to skip Jekyll processing

HOW TO RUN IT
This loads data.json with fetch(), so most browsers block it if you just
double-click index.html (file:// pages can't fetch local files). Two ways:

1) Local server (fully offline once loaded — no internet needed for data):
   - Open a terminal in this folder
   - Run:  python3 -m http.server 8000
   - Open: http://localhost:8000

2) Upload the whole folder (including assets/ and .nojekyll) to any static
   web host (Netlify, GitHub Pages, your own server, etc.).

WHAT'S NEW THIS ROUND

0) download_images.py — a script you can run on a machine with internet
   access to pull every fish/bait/lure/hook/etc. image down locally into
   assets/images/ and rewrite data.json to point at those local copies
   instead of api.fp-collective.com. This removes the dependency on their
   server entirely (no more hotlinking). Run it once from inside this
   folder:
       python3 download_images.py
   It only needs the Python standard library — nothing to install. Safe
   to re-run (skips files it already has). This can take a while and pull
   down a few hundred MB, since there are ~2,500 images across fish,
   baits, lures, hooks, jigheads, boilies/pellets, sinkers, and keepnets.
   After it finishes, re-zip the folder (including the new assets/images/
   folder) for a fully self-hosted copy.

1) All 30 maps now use their real in-game shape (SVG), matched by exact
   place slug — including separate shapes for the old vs. reworked
   versions of Texas (Lone Star Lake) and Czech Republic (Lesni Vila
   Fishery), which look different in-game and now render correctly.

2) Catch-report pin colors fixed to match fp-collective.com's real
   scheme: grey = Common, green = Trophy, gold = Unique.

3) Zoom & pan overhauled: the map now fits fully in view on open (no more
   cropping), the frame is much bigger (up to ~72% of viewport height),
   zoom goes up to 8x, and panning range scales with your zoom level so
   you can move freely around a zoomed-in map. Scroll/pinch to zoom, drag
   to pan, or use the +/-/reset buttons in the corner.

4) Trends tab: game-wide rankings built from ~15,700 real player catch
   reports — top baits, top lures, top lure types, top hooks,
   most-reported fish, and busiest maps. Click any entry to jump to it.

FISH PAGE SECTIONS (matches fp-collective.com's layout)
  Baits -> Most used baits -> Lures -> Most used lures ->
  Most used lure types -> Hooks -> Where to catch
"Most used" and "Hooks" use real "reported N catches" numbers wherever
player data exists; falls back to catalog picks (clearly labeled) if not.

DATA COVERAGE — complete
  fish: 279/279  baits: 126/126  lures: 1324/1324  hooks: 143/143
  lure types: 59/59  maps: 30/30 (all with real SVG shapes)
  jigheads: 266/266  boilies/pellets: 144/144  sinkers: 53/53
  keepnets/stringers: 41/41
  catch reports: ~15,700 (covering 277 of 279 fish, all 30 maps)
