import unittest
from sklearn.linear_model import LinearRegression

class TestModel(unittest.TestCase):

    def test_prediction(self):
        x = [[10], [7], [5]]
        y = [20, 14, 10]

        model = LinearRegression()
        model.fit(x, y)

        pred = model.predict([[6]])

        self.assertTrue(len(pred) == 1)

if __name__ == "__main__":
    unittest.main()