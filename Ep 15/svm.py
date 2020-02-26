from classification import ClassificationModel

class SVM(ClassificationModel):
    def computeModel(XTrain, yTrain, k, d):
        from sklearn.svm import SVC

        classifier = SVC(kernel=k, degree=d)
        classifier.fit(XTrain[0], yTrain)

        return classifier

    def computeExample(filename, kernel, degree):
        XTrain, XTest, yTrain, yTest = ClassificationModel.preprocessData(filename)

        classifier = SVM.computeModel(XTrain, yTrain, kernel, degree)
        yPred = ClassificationModel.predictModel(classifier, XTest)
        return ClassificationModel.evaluateModel(yPred, yTest)

if __name__ == "__main__":
    print(SVM.computeExample("titanic.csv", "linear"))
