import re
class Solution:
    def mostCommonWord(self, finalListgraph, banned):
        d = {}
        tempList = re.sub('[^A-Za-z0-9]+', ' ', finalListgraph).lower().split(" ")
        finalList = [x for x in tempList if x not in banned]
        for i in range(len(finalList)):
            if finalList[i] in d:
                d[finalList[i]] += 1
            else:
                d[finalList[i]] = 1
        return max(d, key=d.get)
if __name__ == '__main__':
    s = Solution()
    finalListgraph = "Bob. hIt, baLl"
    banned = ["bob", "hit"]
    print(s.mostCommonWord(finalListgraph,banned))




