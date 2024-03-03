import sys
from math import sqrt

input = sys.stdin.readline


def main():
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())

    BAx, BAy = ax - bx, ay - by
    BCx, BCy = cx - bx, cy - by
    CAx, CAy = ax - cx, ay - cy
    CBx, CBy = bx - cx, by - cy

    # BAとBCのなす角が90度以上
    if (BAx * BCx + BAy * BCy) < 0:
        dist = sqrt(BAx ** 2 + BAy ** 2)
    # CAとCBのなす角が90度以上
    elif (CAx * CBx + CAy * CBy) < 0:
        dist = sqrt(CAx ** 2 + CAy ** 2)
    else:
        area = abs(BAx * BCy - BAy * BCx)
        dist = area / sqrt(BCx ** 2 + BCy ** 2)

    return dist


if __name__ == '__main__':
    ans = main()
    print(f'{ans:.12f}')
