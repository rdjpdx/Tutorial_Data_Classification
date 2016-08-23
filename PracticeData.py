import numpy as np

"""Creates data sets for practice problems in classification and statistics
"""
class PracticeData:
    def __init__(self):
        self.sample_size = 200
        self.variables = []

    def __repr__(self):
        return "Practice_Data Object; for creating small data sets."

    def add_normal_variable(self, mean=0.0, std=1.0):
        self.variables.append({"dist":"normal", "mean":mean, "std":std})

    def add_uniform_variable(self, min_value=0.0, max_value=1.0):
        self.variables.append({"dist":"uniform", "min":min_value, "max":max_value})

    def add_class_variable(self,class_labels=[0]):
        self.variables.append({"dist":"class", "labels":class_labels})

    def generate_data_set(self):
        data_set = []
        for v in self.variables:
            if v["dist"] == "normal":
                data_set.append( np.random.normal(v["mean"], v["std"], self.sample_size) )

            elif v["dist"] == "uniform":
                data_set.append( np.random.uniform(v["min"], v["max"], self.sample_size) )

            elif v["dist"] == "class":
                data_set.append( np.random.choice( v["labels"], self.sample_size))

        return data_set



    def output_data(self):
        pass
