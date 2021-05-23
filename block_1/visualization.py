import random
from matplotlib import pyplot as plt, animation
# Modified from: https://www.geeksforgeeks.org/visualizing-bubble-sort-using-python/


# helper methods
def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


# function to recursively divide the array
def mergesort(A, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1

    # yield from statements have been used to yield
    # the array from the functions
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)


# function to merge the array
def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i in range(len(merged)):
        A[start + i] = merged[i]
        yield A


# algorithms
def bubblesort(A, *args):
    swapped = True

    for i in range(len(A) - 1):
        if not swapped:
            return
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A


def visualize(N, sorter, heading):
    A = list(range(1, N + 1))
    random.shuffle(A)

    if 'Bubble' in heading:
        subt = 'O(n\N{SUPERSCRIPT TWO})'
    else:
        subt = 'O(n log (n))'

    # creates a generator object containing all
    # the states of the array while performing
    # sorting algorithm
    generator = sorter(A, 0, len(A)-1)

    # creates a figure and subsequent subplots
    fig, ax = plt.subplots()
    ax.set_title(f"{heading} {subt}")
    bar_sub = ax.bar(range(len(A)), A, align="edge")

    # sets the maximum limit for the x-axis
    ax.set_xlim(0, N)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    # helper function to update each frame in plot
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")

    # creating animation object for rendering the iteration
    anim = animation.FuncAnimation(
        fig,
        func=update,
        fargs=(bar_sub, iteration),
        frames=generator,
        repeat=True,
        blit=False,
        interval=1,
        save_count=90000,
    )

    # for showing the animation on screen
    plt.show()
    plt.close()


if __name__ == "__main__":
    visualize(100, mergesort, 'Mergesort')
