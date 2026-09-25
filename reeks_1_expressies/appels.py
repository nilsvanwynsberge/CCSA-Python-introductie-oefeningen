appels = int(input())



def aantal(appels):
    array = []
    array.append(appels // 20 // 35) 
    appels = appels - array[0] * 20 * 35
    array.append(appels // 20)
    appels = appels - array[1] * 20
    array.append(appels)
    return array


array = aantal(appels)
print(str(array[0]) + "\n" + str(array[1]) + "\n" + str(array[2]))
