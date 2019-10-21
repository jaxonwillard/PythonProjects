class Config:

    def createConfiguration(self,  dataFile):
        dict = {}
        dict['name'] = dataFile
        f = open(dataFile)
        for line in f:
            if line.__contains__(":"):
                keyAndVal = line.split(":")
                if keyAndVal[0].isnumeric():
                    dict[keyAndVal[0].rstrip()] = int((keyAndVal[1]).rstrip("\n"))
                else:
                    dict[keyAndVal[0].rstrip().lower()] = keyAndVal[1].rstrip("\n")

        return dict



