def blur(self, img.height, img.width):

    self.img.height = img.height
    self.img.width = img.width

    for row in range(1, img.height - 1):
        for col in range(1, img.width - 1):
            range = img.Create()