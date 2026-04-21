import pandas as pd

class ABTestResultAnalyzer:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def calculate_conversion_rate(self, group):
        return self.data[self.data['group'] == group]['conversion'].mean()

    def calculate_statistical_significance(self, group1, group2):
        conversion_rate1 = self.calculate_conversion_rate(group1)
        conversion_rate2 = self.calculate_conversion_rate(group2)
        return 2 * (conversion_rate1 - conversion_rate2) / (conversion_rate1 + conversion_rate2)**0.5

    def determine_winner(self, group1, group2):
        significance = self.calculate_statistical_significance(group1, group2)
        if significance > 1.96:
            return group1
        else:
            return group2

    def analyze_results(self):
        group1 = 'A'
        group2 = 'B'
        winner = self.determine_winner(group1, group2)
        print(f"Winner: {winner}")
        print(f"Conversion Rate for {group1}: {self.calculate_conversion_rate(group1)}")
        print(f"Conversion Rate for {group2}: {self.calculate_conversion_rate(group2)}")

# Misol
data = {
    'group': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'conversion': [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
}
analyzer = ABTestResultAnalyzer(data)
analyzer.analyze_results()
```

Kodda quyidagilar mavjud:

- `ABTestResultAnalyzer` klassi yaratildi, unda `calculate_conversion_rate`, `calculate_statistical_significance`, `determine_winner` va `analyze_results` metodlari mavjud.
- `calculate_conversion_rate` metodida, bir guruh uchun konversiya darajasini hisoblaydi.
- `calculate_statistical_significance` metodida, ikki guruh uchun statistik muhimlikni hisoblaydi.
- `determine_winner` metodida, guruhlardan birining statistik muhimligi 1,96 dan yuqori bo'lsa, u guruh g'olib deb topiladi.
- `analyze_results` metodida, guruhlardan birining statistik muhimligi 1,96 dan yuqori bo'lsa, u guruh g'olib deb topiladi va natijalar chiqariladi.
