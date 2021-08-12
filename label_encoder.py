

arr = ["brian", "brian", "felix", "felix", "cepi", "cepi", "cepi"]

class LabelEncoder:
    def __init__(self, dataset):
        self.dataset = dataset
        self.dict = dict()
        self.labeled = []

    def createDict(self):
        temp = []
        
        for i in range(len(self.dataset)):
            if self.dataset[i] not in temp:
                temp.append(self.dataset[i])

        temp_dict = dict()
        for i in range(len(temp)):
            temp_dict[temp[i]] = i

        self.dict = temp_dict

    def fit(self):
        self.createDict()
        labeled = []

        for i in range(len(self.dataset)):
            val = self.dict[self.dataset[i]]
            labeled.append(val)

        self.labeled = labeled
        return labeled
    
    def return_key(self, dict, x):
        for key, value in dict.items():
            if x == value:
                return key

        return "None"


    def inverse_transform(self, labeled):
        inversed = []
        temp_dict = self.dict
        
        for i in range(len(labeled)):
            temp = self.return_key(temp_dict, labeled[i])
            inversed.append(temp)

        return inversed


new = LabelEncoder(arr)
new_arr = new.fit()
print(new.dict)
print(new.inverse_transform(new_arr))
