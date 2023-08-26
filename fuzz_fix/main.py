from __future__ import annotations

from typing import Sequence

from fuzz_fix import reproduce as reproduce_mod


def main(argv: Sequence[str] | None = None) -> int:
    # TODO; use the 2 layer argparse from seg_sim_creator here. for now just test
    reproduce_mod.reproduce('.', '1234', 'https://arti')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
