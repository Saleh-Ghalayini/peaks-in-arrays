#defining the find_peak function that will search the list for where peaks are located
def find_peaks(array):

    #a list that will contain the peaks after finding them
    peaks = []

    #turning the string list into a an integer list which is better for the comparing operation
    for i in range(len(array)):
        array[i] = int(array[i])

    #comparing the indexes with their neighbors (the index before it and the one after it) and comparing if its bigger than them
    #if it is then it will get appended to the peaks list
    for i in range(1, len(array) - 1):
        if(array[i - 1] < array[i] and array[i] > array[i + 1]):
            peaks.append(array[i])
    #returning the list of peaks after going through the whole number list
    return peaks
#filling the numbers_sequence string with a series of numbers
numbers_sequence = input("please enter the numbers with spaces in between: ")
#turning the string into a list but they are still strings and will be turned into integers in the find_peak function
numbers = numbers_sequence.split()
#calling the find_peaks function and passing the numbers string list as an argument that will be printed after the return value is back
print(find_peaks(numbers))

