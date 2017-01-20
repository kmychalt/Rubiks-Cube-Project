class Moves:
    lst = 0
    chunk = 0
    rows = 0
    columns = 0
    sides = 0
    left = 0
    front = 0
    right = 0
    back = 0
    top = 0
    bottom = 0

    def __init__(self, lst, rows, columns, sides):
        self.lst = lst
        self.rows = rows
        self.columns = columns
        self.sides = sides

    def chunks(self, lst, rows, columns):
        self.chunk = [lst[x:x + (self.rows * self.columns)]
            for x in xrange(0, len(self.lst), (self.rows * self.columns))]
        self.left = self.chunk[0]
        self.front = self.chunk[1]
        self.right = self.chunk[2]
        self.back = self.chunk[3]
        self.top = self.chunk[4]
        self.bottom = self.chunk[5]

    def makeWhole(self):
        self.lst = self.left + self.front + self.right + self.back + self.top + self.bottom
        return self.lst

    def rotateFace(self, face):
        y = face[2]
        face[2] = face[0]
        face[0] = face[6]
        face[6] = face[8]
        face[8] = y
        z = face[1]
        face[1] = face[3]
        face[3] = face[7]
        face[7] = face[5]
        face[5] = z
        return face

    def rotateFaceI(self, face):
        y = face[2]
        face[2] = face[8]
        face[8] = face[6]
        face[6] = face[0]
        face[0] = y
        z = face[1]
        face[1] = face[5]
        face[5] = face[7]
        face[7] = face[3]
        face[3] = z
        return face

    def rotateR(self):
        z = 0
        rotR = [2, 5, 8] 
        l = [self.front[2], self.front[5], self.front[8]]
        for x in rotR:
            self.front[x] = self.bottom[x]
            self.bottom[x] = self.back[x]
            self.back[x] = self.top[x]
            self.top[x] = l[z]
            z += 1
        self.right = (self.rotateFace(self.right))
        self.lst = self.makeWhole()
        return self.lst

    def rotateRI(self):
        z = 0
        rotR = [2, 5, 8] 
        l = [self.front[2], self.front[5], self.front[8]]
        for x in rotR:
            self.front[x] = self.top[x]
            self.top[x] = self.back[x]
            self.back[x] = self.bottom[x]
            self.bottom[x] = l[z]
            z += 1
        self.right = (self.rotateFaceI(self.right))
        self.lst = self.makeWhole()              
        return self.lst

    def rotateL(self):
        z = 0
        rotL = [0, 3, 6]
        l = (self.front[0], self.front[3], self.front[6])
        for x in rotL:
            self.front[x] = self.bottom[x]
            self.bottom[x] = self.back[x]
            self.back[x] = self.top[x]
            self.top[x] = l[z]
            z += 1
        self.left = (self.rotateFace(self.left))
        self.lst = self.makeWhole()
        return self.lst

    def rotateLI(self):
        z = 0
        rotL = [0, 3, 6]
        l = (self.front[0], self.front[3], self.front[6])
        for x in rotL:
            self.front[x] = self.top[x]
            self.top[x] = self.back[x]
            self.back[x] = self.bottom[x]
            self.bottom[x] = l[z]
            z += 1
        self.left = (self.rotateFaceI(self.left))
        self.lst = self.makeWhole()              
        return self.lst

    def rotateBck(self):
        z = 0
        rotBck = [0, 1, 2]
        l = (self.top[0], self.top[1], self.top[2])
        for x in rotBck:
            self.top[x] = self.left[x]
            self.left[x] = self.bottom[x]
            self.bottom[x] = self.right[x]
            self.right[x] = l[z]
            z += 1
        self.back = (self.rotateFace(self.back))
        self.lst = self.makeWhole()
        return self.lst

    def rotateBckI(self):
        z = 0
        rotBck = [0, 1, 2]
        l = (self.top[0], self.top[1], self.top[2])
        for x in rotBck:
            self.top[x] = self.right[x]
            self.right[x] = self.bottom[x]
            self.bottom[x] = self.left[x]
            self.left[x] = l[z]
            z += 1
        self.back = (self.rotateFaceI(self.back))
        self.lst = self.makeWhole()
        return self.lst

    def rotateBot(self):
        z = 0
        rotBot = [6, 7, 8]
        l = (self.front[6], self.front[7], self.front[8])
        for x in rotBot:
            self.front[x] = self.left[x]
            self.left[x] = self.back[x]
            self.back[x] = self.right[x]
            self.right[x] = l[z]
            z += 1
        self.bottom = (self.rotateFace(self.bottom))
        self.lst = self.makeWhole()
        return self.lst

    def rotateBotI(self):
        z = 0
        rotBot = [6, 7, 8]
        l = (self.front[6], self.front[7], self.front[8])
        for x in rotBot:
            self.front[x] = self.right[x]
            self.right[x] = self.back[x]
            self.back[x] = self.left[x]
            self.left[x] = l[z]
            z += 1
        self.bottom = (self.rotateFaceI(self.bottom))
        self.lst = self.makeWhole()
        return self.lst

    def rotateFrn(self):
        z = 0
        rotFrn = [6, 7, 8]
        l = (self.top[6], self.top[7], self.top[8])
        for x in rotFrn:
            self.top[x] = self.left[x]
            self.left[x] = self.bottom[x]
            self.bottom[x] = self.right[x]
            self.right[x] = l[z]
            z += 1
        self.front = (self.rotateFace(self.front))
        self.lst = self.makeWhole()
        return self.lst

    def rotateFrnI(self):
        z = 0
        rotFrn = [6, 7, 8]
        l = (self.top[6], self.top[7], self.top[8])
        for x in rotFrn:
            self.top[x] = self.right[x]
            self.right[x] = self.bottom[x]
            self.bottom[x] = self.left[x]
            self.left[x] = l[z]
            z += 1
        self.front = (self.rotateFaceI(self.front))
        self.lst = self.makeWhole()
        return self.lst

    def rotateTop(self):
        z = 0
        rotTop = [0, 1, 2]
        l = (self.front[0], self.front[1], self.front[2])
        for x in rotTop:
            self.front[x] = self.right[x]
            self.right[x] = self.back[x]
            self.back[x] = self.left[x]
            self.left[x] = l[z]
            z += 1
        self.top = (self.rotateFace(self.top))
        self.lst = self.makeWhole()
        return self.lst

    def rotateTopI(self):
        z = 0
        rotTop = [0, 1, 2]
        l = (self.front[0], self.front[1], self.front[2])
        for x in rotTop:
            self.front[x] = self.left[x]
            self.left[x] = self.back[x]
            self.back[x] = self.right[x]
            self.right[x] = l[z]
            z += 1
        self.top = (self.rotateFaceI(self.top))
        self.lst = self.makeWhole()
        return self.lst
        

    
