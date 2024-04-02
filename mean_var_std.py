import numpy as np

def check_valid_input(input_list: list) -> bool:
    is_valid = False
    if (type(input_list) == list):
        if (len(input_list) == 9):
            is_valid = True
    return is_valid

def calculate_function(function: np.ufunc, matrix: np.array, axe : int) -> list:
    return function(matrix, axis = axe).tolist()

def calculate(input_list : list) -> dict:
    """
        This function uses Numpy to output the mean, variance, standard deviation, max, min and sum
        of the rows, columns and elements in a 3x3 matrix

        Parameters
        ----------
        input_list : list
            Lista which contains 9 digits
            If the lists have less than 9 digits, should rais a ValueError exception: "List must contain nine numbers."

        Returns
        --------
        calculations : dict
            Contains the mean, variance, std deviation, max, min and sum (lists)
            along both axes and for the flattended matrix.
    """
    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    if not check_valid_input(input_list=input_list):
        raise ValueError("List must contain nine numbers.")

    matrix = np.array((input_list[:3], input_list[3:6], input_list[6:]))

    for operation in calculations.keys():
        for axe in range(3):
            if operation == 'mean':
                if axe < 2:
                    calculations[operation].append(
                        calculate_function(function=np.mean, matrix=matrix, axe=axe)
                        )
                else:
                    calculations[operation].append(
                        np.mean(matrix)
                    )
            elif operation == 'variance':
                if axe < 2:
                    calculations[operation].append(
                        calculate_function(function=np.var, matrix=matrix, axe=axe)
                        )
                else:
                    calculations[operation].append(
                        np.var(matrix)
                    )
            elif operation == 'standard deviation':
                if axe < 2:
                    calculations[operation].append(
                        calculate_function(function=np.std, matrix=matrix, axe=axe)
                        )
                else:
                    calculations[operation].append(
                        np.std(matrix)
                    )
            elif operation == 'max':
                if axe < 2:
                    calculations[operation].append(
                        calculate_function(function=np.max, matrix=matrix, axe=axe)
                        )
                else:
                    calculations[operation].append(
                        np.max(matrix)
                    )
            elif operation == 'min':
                if axe < 2:
                    calculations[operation].append(
                        calculate_function(function=np.min, matrix=matrix, axe=axe)
                        )
                else:
                    calculations[operation].append(
                        np.min(matrix)
                    )
            elif operation == 'sum':
                if axe < 2:
                    calculations[operation].append(
                        calculate_function(function=np.sum, matrix=matrix, axe=axe)
                        )
                else:
                    calculations[operation].append(
                        np.sum(matrix)
                    )

    return calculations