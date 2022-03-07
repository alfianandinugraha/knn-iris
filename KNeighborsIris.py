from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

class KNeighborsIris:
  data = []
  target = []
  feature_names = []
  target_names = []
  train_test = []
  n_neighbors = 0

  def __init__(self, n_neighbors = 3):
    iris = load_iris()

    self.data = iris.data
    self.target = iris.target
    self.feature_names = iris.feature_names
    self.target_names = iris.target_names

    self.train_test = train_test_split(
      self.data, self.target,
      test_size = 0.4,
      random_state = 1
    )

    self.n_neighbors = n_neighbors

  def accurate(self):
    _, data_test, _, target_test = self.train_test
    predict = self.predict(data_test)
    result = metrics.accuracy_score(target_test, predict)
    return result

  def predict(self, data):
    knn = KNeighborsClassifier(
      n_neighbors = self.n_neighbors
    )
    data_train, _, target_train, _ = self.train_test
    knn.fit(data_train, target_train)
    predict = knn.predict(data)
    return predict

  def find(self, data):
    predict = self.predict([data])[0]
    result = self.target_names[predict]
    return result