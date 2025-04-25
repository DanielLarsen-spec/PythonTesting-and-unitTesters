# Km to miles converter. 1 miles is 1.6 km.

def kmToMilesConverter(km):
    miles = km / 1.6
    return miles


def unitTester():
    assert kmToMilesConverter(1) == 0.625, "Test case 1 failed"
    assert kmToMilesConverter(2) == 1.25, "Test case 2 failed"
    assert kmToMilesConverter(3) == 1.875, "Test case 3 failed"
    assert kmToMilesConverter(4) == 2.5, "Test case 4 failed"
    print("All test cases passed!")
unitTester()    
userInput = int(input("Enter the distance in km:"))
print("The distance in miles is:", kmToMilesConverter(userInput))

