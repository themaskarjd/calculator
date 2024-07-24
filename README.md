# Calculator

This is a Python-based calculator project that supports basic arithmetic operations, expression parsing, and evaluation. The calculator is implemented using multiple modules to handle different aspects of the calculation process.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Expression parsing and tokenization
- Expression tree generation and evaluation
- Error handling for invalid expressions

## Project Structure

The project is divided into several modules:

1. **calcExceptions.py**: Defines custom exceptions used for error handling in the calculator.
2. **calculator.py**: Contains the main Calculator class which integrates various components to perform calculations.
3. **evaluators.py**: Provides functionality for evaluating parsed expressions.
4. **expressionTree.py**: Implements the expression tree data structure used to represent and evaluate expressions.
5. **parsers.py**: Contains the parser logic to convert tokenized input into an expression tree.
6. **scanner.py**: Handles the scanning and tokenization of input expressions.
7. **token.py**: Defines the tokens used in the parsing process.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/themaskarjd/calculator.git
   cd calculator
   \`\`\`

2. Run the calculator:
   \`\`\`bash
   python calculator.py
   \`\`\`

## Usage

You can use the calculator to perform basic arithmetic operations. The input expressions are parsed, converted into an expression tree, and then evaluated.

Example:
\`\`\`python
from calculator import Calculator

calc = Calculator()
result = calc.evaluate("3 + 5 * (2 - 4) / 2")
print(result)  # Output: 1.0
\`\`\`

## Modules Overview

### calcExceptions.py

Defines custom exceptions such as \`CalculatorError\` and \`ParserError\` to handle errors during calculation and parsing.

### calculator.py

Contains the \`Calculator\` class that integrates the scanner, parser, and evaluator to process and compute the result of expressions.

### evaluators.py

Implements the \`Evaluator\` class responsible for evaluating the expression tree and returning the result.

### expressionTree.py

Defines the \`ExpressionTree\` class, which represents the hierarchical structure of mathematical expressions.

### parsers.py

Includes the \`Parser\` class, which converts a list of tokens into an expression tree.

### scanner.py

Contains the \`Scanner\` class that tokenizes the input string into a list of tokens for further processing.

### token.py

Defines the \`Token\` class and related constants used during the scanning and parsing processes.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or bug reports.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
