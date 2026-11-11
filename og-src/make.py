# Makes og.png, the picture shown when the site's link is shared: first a screenshot of the home page
# (og-src/home.png), then the card around it (og-src/card.html). Run from anywhere: python og-src/make.py
import pathlib, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'og-src'
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
PROFILE = SRC / '.chrome'


def shot(page, size, out, wait=4000):
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files',
                    f'--user-data-dir={PROFILE}', f'--window-size={size}', f'--virtual-time-budget={wait}',
                    f'--screenshot={out}', page.as_uri()], check=True, capture_output=True)


shot(ROOT / 'index.html', '1280,820', SRC / 'home.png')   # the page, once its opening motion has finished
shot(SRC / 'card.html', '1200,630', ROOT / 'og.png', 6000)  # the card, once its fonts have loaded
print('og.png written')
