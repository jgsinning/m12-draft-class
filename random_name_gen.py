import random
import time


# start_time = time.time()
first_hundreds = [77.639195, 93.221026, 101.150554, 105.767182, 108.873667, 110.920598, 112.412527, 113.581553,
                  114.479297, 115.17493, 115.72142, 116.159568, 116.521354, 116.817385, 117.061399, 117.262823,
                  117.426525, 117.560112, 117.671585, 117.763676, 117.839499, 117.90212, 117.953961, 117.996373,
                  118.030295, 118.057213, 118.077962, 118.094333, 118.106943, 118.116883, 118.124469,
                  118.130184000001,
                  118.135272000001, 118.139753, 118.141068]

last_thousands = [40581.55, 48934.29, 53918.75, 57412.76, 60112.14, 62265.81, 64053.53, 65574.17, 66897.72,
                  68063.88, 69106.62, 70038.25, 70884.13, 71650.09, 72350.1, 72992.1, 73589.24, 74137.77,
                  74644.04,
                  75118.41, 75568.33, 75992.44, 76386.52, 76754.29, 77111.06, 77453.16, 77770.31, 78075.8,
                  78369.36,
                  78648.89, 78914.37, 79180.01, 79423.44, 79662.01, 79891.83, 80122.57, 80332.25, 80536.07,
                  80742.64,
                  80928.25, 81129.56, 81307.65, 81485.75, 81650.75, 81827.55, 81988.87, 82144.25, 82301.52,
                  82455.26,
                  82599.42, 82742.81, 82891.95, 83020.2, 83157.9, 83292.42, 83433.37, 83552.85, 83672.93,
                  83790.66,
                  83915.36, 84016.73, 84130.87, 84258.26, 84355.5, 84465.67, 84561.23, 84680.01, 84785.22,
                  84878.85,
                  84961.81, 85062.14, 85159.07, 85260.48, 85359.5, 85442.92, 85534.55, 85618.4, 85692.77,
                  85767.3,
                  85868.19, 85933.17, 86021.84, 86103.45, 86187.74, 86262.6, 86334.83, 86409.1, 86472.51,
                  86548.6,
                  86636.09, 86695.79, 86778.22, 86832.88, 86893.82, 86959.27, 87030.27, 87107.1, 87176.77,
                  87217.15,
                  87289.41, 87340.25, 87395.82, 87483.23, 87520.8, 87606.27, 87657.61, 87704.62, 87749.57,
                  87837.52,
                  87882.87, 87922.52, 88003.0, 88041.21, 88078.28, 88156.16, 88185.64, 88259.26, 88280.06,
                  88353.75,
                  88407.26, 88444.6, 88510.64, 88545.35, 88587.08, 88651.26, 88706.96, 88720.73, 88785.22,
                  88835.64,
                  88889.45, 88921.5, 88940.91, 88997.3, 89046.29, 89095.19, 89141.83, 89185.24, 89227.14,
                  89270.01,
                  89310.27, 89350.43, 89391.67, 89429.52, 89467.6, 89505.12, 89538.79, 89571.07, 89596.25,
                  89630.45,
                  89692.05, 89747.41, 89753.48]


class NameGen:
    def __init__(self):
        csv_first = open('data/firstnames.csv', 'r')
        self.first_names = []
        self.first_pop = []

        csv_first.readline()
        for i in range(3437):
            row = csv_first.readline().split('\n')[0].split(',')
            self.first_names.append(row[0])
            self.first_pop.append(float(row[2]))

        csv_last = open('data/lastnames.csv', 'r')
        self.last_names = []
        self.last_pop = []

        csv_last.readline()
        for i in range(151671):
            row = csv_last.readline().split('\n')[0].split(',')
            self.last_names.append(row[0])
            self.last_pop.append(float(row[1]))

    def gen_names(self, num_names):
        gen_names = []

        for i in range(num_names):
            name = []

            # optimized for faster search
            first_index = random.uniform(0.0, 118.141068)
            for k in range(len(first_hundreds)):
                if first_index <= first_hundreds[k]:
                    for j in range(k * 100, (k + 1) * 100 + 1):
                        if first_index <= self.first_pop[j]:
                            name.append(self.first_names[j])
                            break
                    break

            # checks for length under 15 and optimized for faster search
            not_found = True
            while not_found:
                last_index = random.uniform(0.0, 89753.48)
                for k in range(len(last_thousands)):
                    if last_index <= last_thousands[k]:
                        for j in range(k * 1000, (k + 1) * 1000 + 1):
                            if last_index <= self.last_pop[j]:
                                if len(self.last_names[j]) < 15:
                                    name.append(self.last_names[j])
                                    not_found = False
                                    break
                                break
                        break
            gen_names.append(name)
        return gen_names

# print(gen_names)
# print(gen_names[0:10])
# print(len(gen_names))
# print(redos)
# print(f'executed in {time.time() - start_time} seconds')
