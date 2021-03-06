"""30: Split Screen Without Tabs

Get your code and tests side-by-side without resorting to tabs.

- Side-by-side without tabs

- Split Vertically

- Alt-Tab to go to next splitter

- Open ``tests/test_examples.py``

- Run tests

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

from fortytwo import App
from fortytwo.models import Greeter


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter('Larry')
        return greeting


if __name__ == '__main__':
    print(main())
