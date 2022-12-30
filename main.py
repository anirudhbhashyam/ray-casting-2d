import os
import sys

CPD = os.path.abspath(
    os.path.join(
        os.path.abspath(__file__),
        *(1 * [os.pardir]),
    )
)

sys.path.append(
    os.path.join(CPD, "src")
)


def main() -> int:
    return 0

if __name__ == "__main__":
    sys.exit(main())