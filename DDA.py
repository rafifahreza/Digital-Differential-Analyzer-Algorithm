'''
    Digital Differential Analyzer

    a) 0 < m < 1 => y(k+1) = yk +- 1
                    x(k+1) = xk +- 1
                    
    b) m > 1     => x(k+1) = xk + (1/m)
                    y(k+1) = yk +- 1

    Batasan Masalah :
        - Hanya bisa menggunakan 2 titik
        
    * * * Program by prokoding * * *
'''

class DDA:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def start(self):

        #untuk menampung nilai delta x dan delta y
        d_x = self.x[-1] - self.x[-2]
        d_y = self.y[-1] - self.y[-2]

        m = round(abs(float(d_y / d_x)),2)
        x_n = []
        y_n = []
        
        if m > 0 and m < 1:
            if d_x > 0 and d_y > 0:
                #put x0, y0
                x_first = self.x[0] + 1
                x_n.append(x_first)

                y_first = self.y[0] + m
                y_n.append(y_first)

                #Comparing deltax and delta y
                if (self.x[-1] - self.x[-2]) > (self.y[-1] - self.y[-2]):
                    for i in range(abs(self.x[-1] - self.x[-2]) - 1):
                        xj = x_n[-1] + 1
                        x_n.append(xj)
                        yj = y_n[-1] + m
                        y_n.append(yj)
                        
                elif (self.y[-1] - self.y[-2]) > (self.x[-1] - self.x[-2]):
                    for i in range(abs(self.y[-1] - self.y[-2]) - 1):
                        xj = x_n[-1] + 1
                        x_n.append(xj)
                        yj = y_n[-1] + m
                        y_n.append(yj)

            elif d_x < 0 and d_y > 0:
                x_first = self.x[0] - 1
                x_n.append(x_first)

                y_first = self.y[0] + m
                y_n.append(y_first)

                #Comparing deltax and delta y
                if (self.x[-1] - self.x[-2]) > (self.y[-1] - self.y[-2]):
                    for i in range(abs(self.x[-1] - self.x[-2]) - 1):
                        xj = x_n[-1] - 1
                        x_n.append(xj)
                        yj = y_n[-1] + m
                        y_n.append(yj)
                        
                elif (self.y[-1] - self.y[-2]) > (self.x[-1] - self.x[-2]):
                    for i in range(abs(self.y[-1] - self.y[-2]) - 1):
                        xj = x_n[-1] - 1
                        x_n.append(xj)
                        yj = y_n[-1] + m
                        y_n.append(yj)

            elif d_x > 0 and d_y < 0:
                x_first = self.x[0] + 1
                x_n.append(x_first)

                y_first = self.y[0] - m
                y_n.append(y_first)

                #Comparing deltax and delta y
                if (self.x[-1] - self.x[-2]) > (self.y[-1] - self.y[-2]):
                    for i in range(abs(self.x[-1] - self.x[-2]) - 1):
                        xj = x_n[-1] + 1
                        x_n.append(xj)
                        yj = y_n[-1] - m
                        y_n.append(yj)
                        
                elif (self.y[-1] - self.y[-2]) > (self.x[-1] - self.x[-2]):
                    for i in range(abs(self.y[-1] - self.y[-2]) - 1):
                        xj = x_n[-1] + 1
                        x_n.append(xj)
                        yj = y_n[-1] - m
                        y_n.append(yj)

            elif d_x < 0 and d_y < 0:
                x_first = self.x[0] - 1
                x_n.append(x_first)

                y_first = self.y[0] - m
                y_n.append(y_first)

                #Comparing deltax and delta y
                if (self.x[-1] - self.x[-2]) > (self.y[-1] - self.y[-2]):
                    for i in range(abs(self.x[-1] - self.x[-2]) - 1):
                        xj = x_n[-1] - 1
                        x_n.append(xj)
                        yj = y_n[-1] - m
                        y_n.append(yj)
                        
                elif (self.y[-1] - self.y[-2]) > (self.x[-1] - self.x[-2]):
                    for i in range(abs(self.y[-1] - self.y[-2]) - 1):
                        xj = x_n[-1] - 1
                        x_n.append(xj)
                        yj = y_n[-1] - m
                        y_n.append(yj)

        elif m >= 1:
            if d_x > 0 and d_y > 0:
                #put x0, y0
                x_first = self.x[0] + round((1/m),2)
                x_n.append(x_first)

                y_first = self.y[0] + 1
                y_n.append(y_first)
                
                #Comparing deltax and delta y
                if (self.x[-1] - self.x[-2]) > (self.y[-1] - self.y[-2]):
                    #put x(n) and y(n)
                    for i in range(abs(self.x[-1] - self.x[-2]) - 1):
                        xj = round(x_n[-1],2) + round((1/m),2)
                        x_n.append(xj)
                        yj = y_n[-1] + 1
                        y_n.append(yj)
                        
                elif (self.y[-1] - self.y[-2]) > (self.x[-1] - self.x[-2]):
                    for i in range(abs(self.y[-1] - self.y[-2]) - 1):
                        xj = round(x_n[-1],2) + round((1/m),2)
                        x_n.append(xj)
                        yj = y_n[-1] + 1
                        y_n.append(yj)

            elif d_x < 0 and d_y > 0:
                x_first = self.x[0] - round((1/m),2)
                x_n.append(x_first)

                y_first = self.y[0] + 1
                y_n.append(y_first)

                #Comparing deltax and delta y
                if (self.x[-1] - self.x[-2]) > (self.y[-1] - self.y[-2]):
                    for i in range(abs(self.x[-1] - self.x[-2]) - 1):
                        xj = round(x_n[-1],2) - round((1/m),2)
                        x_n.append(xj)
                        yj = y_n[-1] + 1
                        y_n.append(yj)
                        
                elif (self.y[-1] - self.y[-2]) > (self.x[-1] - self.x[-2]):
                    for i in range(abs(self.y[-1] - self.y[-2]) - 1):
                        xj = round(x_n[-1],2) - round((1/m),2)
                        x_n.append(xj)
                        yj = y_n[-1] + 1
                        y_n.append(yj)

            elif d_x > 0 and d_y < 0 :
                x_first = self.x[0] + round((1/m),2)
                x_n.append(x_first)

                y_first = self.y[0] - 1
                y_n.append(y_first)

                #Comparing delta x and delta y
                if (self.x[-1] - self.x[-2]) > (self.y[-1] - self.y[-2]):
                    for i in range(abs(self.x[-1] - self.x[-2]) - 1):
                        xj = round(x_n[-1],2) + round((1/m),2)
                        x_n.append(xj)
                        yj = y_n[-1] - 1
                        y_n.append(yj)
                        
                elif (self.y[-1] - self.y[-2]) > (self.x[-1] - self.x[-2]):
                    for i in range(abs(self.y[-1] - self.y[-2]) - 1):
                        xj = round(x_n[-1],2) + round((1/m),2)
                        x_n.append(xj)
                        yj = y_n[-1] - 1
                        y_n.append(yj)

            elif d_x < 0 and d_y < 0 :
                x_first = self.x[0] - round((1/m),2)
                x_n.append(x_first)

                y_first = self.y[0] - 1
                y_n.append(y_first)

                #Comparing deltax and delta y
                if (self.x[-1] - self.x[-2]) > (self.y[-1] - self.y[-2]):
                    for i in range(abs(self.x[-1] - self.x[-2]) - 1):
                        xj = round(x_n[-1],2) - round((1/m),2)
                        x_n.append(xj)
                        yj = y_n[-1] - 1
                        y_n.append(yj)
                        
                elif (self.y[-1] - self.y[-2]) > (self.x[-1] - self.x[-2]):
                    for i in range(abs(self.y[-1] - self.y[-2]) - 1):
                        xj = round(x_n[-1],2) - round((1/m),2)
                        x_n.append(xj)
                        yj = y_n[-1] - 1
                        y_n.append(yj)
        return x_n, y_n

    def printPoints(self):
        x, y = self.start()
        print('x : ',self.x[0], ' | y : ',self.y[0])
        for i in range(len(x)):
            print('x : ',x[i], ' | y : ',y[i])



if __name__ == "__main__":
    x = []
    y = []
    for i in range(2):
        xk = int(input('Masukan x'+str(i)+' : '))
        x.append(xk)
        yk = int(input('Masukan y'+str(i)+' : '))
        y.append(yk)
    clf = DDA(x,y)
    clf.printPoints()














        
