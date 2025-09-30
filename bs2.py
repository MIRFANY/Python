#python program to implemetn bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        #last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



def main():
    arr = [64, 34, 25, 12, 11]
    print("Original array:", arr)
    bubble_sort(arr)
    print("Sorted array:", arr)


if __name__ == "__main__":
    main()


# if __name__ == "__main__"
#
##
#