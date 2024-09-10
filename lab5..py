from abc import ABC, abstractmethod

class AnalysisError(Exception):
    """Custom exception for errors in the analysis process."""
    def __init__(self, message):
        super().__init__(message)

# (a)
class DataAnalyzer(ABC):
    @abstractmethod
    def analyze(self, data):
        pass

# (b)
class TextDataAnalyzer(DataAnalyzer):
    def analyze(self, data):
        try:
            
            if not isinstance(data, dict):
                raise TypeError("Expected a dictionary for text data.")
            if 'text' not in data:
                raise KeyError("'text' key is missing in the data.")

            text = data['text']
            if not isinstance(text, str):
                raise ValueError("The 'text' value must be a string.")
            
            word_count = len(text.split())
            return f"Text data analyzed. Word count: {word_count}"
        
        except KeyError as e:
            raise AnalysisError(f"KeyError during text analysis: {e}")
        except TypeError as e:
            raise AnalysisError(f"TypeError during text analysis: {e}")
        except ValueError as e:
            raise AnalysisError(f"ValueError during text analysis: {e}")

# (b)
class NumericDataAnalyzer(DataAnalyzer):
    def analyze(self, data):
        try:
            
            if not isinstance(data, dict):
                raise TypeError("Expected a dictionary for numeric data.")
            if 'numbers' not in data:
                raise KeyError("'numbers' key is missing in the data.")
            
            numbers = data['numbers']
            if not isinstance(numbers, list):
                raise ValueError("The 'numbers' value must be a list.")
            
            if not all(isinstance(n, (int, float)) for n in numbers):
                raise ValueError("All items in 'numbers' must be numeric.")
            
            total = sum(numbers)
            return f"Numeric data analyzed. Sum: {total}"
        
        except KeyError as e:
            raise AnalysisError(f"KeyError during numeric analysis: {e}")
        except TypeError as e:
            raise AnalysisError(f"TypeError during numeric analysis: {e}")
        except ValueError as e:
            raise AnalysisError(f"ValueError during numeric analysis: {e}")

# (e)

# (i)
analyzers = [TextDataAnalyzer(), NumericDataAnalyzer()]

# (ii)
sample_data_entries = [
    {'text': "This is a sample text for analysis."},
    {'text': 123},
    {'numbers': [1, 2, 3, 4, 5]}, 
    {'numbers': "1, 2, 3"},  
    {'invalid_key': "missing required key"}, 
]

# (iii)
for analyzer in analyzers:
    for data in sample_data_entries:
        try:
            result = analyzer.analyze(data)
            print(result)
        except AnalysisError as e:
            print(f"Analysis failed: {e}")


'''
Text data analyzed. Word count: 7
Analysis failed: ValueError during text analysis: The 'text' value must be a string.
Analysis failed: KeyError during text analysis: "'text' key is missing in the data."
Analysis failed: KeyError during text analysis: "'text' key is missing in the data."
Analysis failed: KeyError during text analysis: "'text' key is missing in the data."
Analysis failed: KeyError during numeric analysis: "'numbers' key is missing in the data."
Analysis failed: KeyError during numeric analysis: "'numbers' key is missing in the data."
Numeric data analyzed. Sum: 15
Analysis failed: ValueError during numeric analysis: The 'numbers' value must be a list.
Analysis failed: KeyError during numeric analysis: "'numbers' key is missing in the data."
'''
