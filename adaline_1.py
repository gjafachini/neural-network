import numpy as np

class adalineAlgorithm(object):
    """adaline neuron"""
    def __init__(self, learningRate=0.025, maxIterations=100, weights=[0,0,0]):
        self.learningRate = learningRate
        self.maxIterations = maxIterations
        self.weights = weights

    def procces(self, trainingData, iters):
        output = 0
        for j in range(0, len(trainingData[iters])):
                output += trainingData[iters][j] * self.weights[j]
        return output

    def train(self, trainingData, outputElements):
        for iters in range(0, self.maxIterations):
            output = 0
            quad_erros = []
            print "---------------------------------------"
            print "Iteratio: " + str(iters)
            for i in range(0, len(trainingData)):
                output = self.procces(trainingData, i)
                error = outputElements[i] - output

                quad_erros.append(error**2)
                
                for data in range(0, len(trainingData[i])):
                    self.weights[data] = self.weights[data] + self.learningRate * error * trainingData[i][data]
            print 'Weights: ' + str(self.weights)
            print 'EQM: ' + str(np.mean(quad_erros))
            print "---------------------------------------"
#
#trainingData = [[1, 1, 1],
#                [1, 1, -1],
#                [1, -1, 1],
#                [1, -1, -1]]
#outputElements = [1, -1, -1, -1]

#learningRate = 0.00095
learningRate = 0.0025
maxIterations = 100
weights = [0,0,0]

trainingData = []
outputElements = []

with open('dados2.txt') as f:
    for line in f:
        data = line.split()
        trainingData.append([1, float(data[0]), float(data[1])])
        outputElements.append(float(data[2]))

norm_output = outputElements / np.max(outputElements)

adaline = adalineAlgorithm(learningRate, maxIterations, weights)
adaline.train(trainingData, norm_output)

print trainingData
print '------'
print outputElements
print '------'
print norm_output