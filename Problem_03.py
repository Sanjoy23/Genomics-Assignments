def hammingDist(str1, str2):
    i = 0
    count = 0

    while (i < len(str1)):
        if (str1[i] != str2[i]):
            count += 1
        i += 1
    return count

def firstOccurence(T, P, K):
    cnt = 0
    for i in range(len(T)):
        if(i+len(P)<len(T)):
            cnt +=1
            mismatch = hammingDist(P, T[i: i+len(P)])
            if(mismatch <= int(K)):
                return i, mismatch
                break


def main():
    T = input("Enter a string T: ")
    P = input("Enter a string P: ")
    K = input("Enter a integer K: ")

    index, step = firstOccurence(T,P, K)
    print("First occurrence found at index: "+str(index))
    print("Hamming Distance: " +str(step))
    #print(T[0:9])
main()



