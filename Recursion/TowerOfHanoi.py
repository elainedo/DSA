def towerOfHanoi(n, source, destination, aux):
    if n==1:
        print("move ", n, " from ", source, " to ", destination)
        return
    towerOfHanoi(n-1, source, aux, destination)
    print("move ", n, " from ", source, " to ", destination)
    towerOfHanoi(n-1, aux, destination, source)

towerOfHanoi(4, "A", "C", "B")