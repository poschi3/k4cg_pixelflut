import yaml

class SimpleConfig:

    def __init__(self):
        self.__config = []

    def load(self, filePath):
        self.__config = []
        with open(filePath, 'r') as stream:
            try:
                self.__config = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return self

    def getServerHost(self):
        return self.__config['server']['host']

    def getServerPort(self):
        return self.__config['server']['port']

    def getImageFilePath(self):
        return self.__config['image']['filepath']

    def useColorBasedImageTransparency(self):
        return self.__config['image']['color_transparency']['enabled']

    def getImageTransparencyColor(self):
        return self.__config['image']['color_transparency']['color']

    def getStrategy(self):
        return self.__config['draw']['strategy']

    def getDrawWidth(self):
        return self.__config['draw']['width']

    def getDrawPositionX(self):
        return self.__config['draw']['position']['x']

    def getDrawPositionY(self):
        return self.__config['draw']['position']['y']