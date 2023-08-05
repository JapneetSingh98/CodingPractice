class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        dictionary = {}
        highestPopularity = 0
        for i in range(len(creators)):
            if creators[i] not in dictionary:
                dictionary[creators[i]] = {
                    "popularity": views[i],
                    "highestViewedId": ids[i],
                    "highestViewCount": views[i]
                }
            else:
                if views[i] > dictionary[creators[i]]["highestViewCount"]:
                    dictionary[creators[i]]["highestViewCount"] = views[i]
                    dictionary[creators[i]]["highestViewedId"] = ids[i]
                elif views[i] == dictionary[creators[i]]["highestViewCount"] and ids[i] < dictionary[creators[i]][
                    "highestViewedId"]:
                    dictionary[creators[i]]["highestViewedId"] = ids[i]
                dictionary[creators[i]]["popularity"] += views[i]

            if dictionary[creators[i]]["popularity"] > highestPopularity:
                highestPopularity = dictionary[creators[i]]["popularity"]

            # print(dictionary)

        output = []
        for key in dictionary:
            if highestPopularity == dictionary[key]["popularity"]:
                output.append([key, dictionary[key]["highestViewedId"]])

        return output