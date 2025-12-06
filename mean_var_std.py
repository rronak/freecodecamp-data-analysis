import numpy as np

def calculate(input_list):
    # 1. Validate input
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    # 2. Convert to 3x3 matrix
    matrix = np.array(input_list).reshape(3, 3)

    # 3. Perform calculations
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            float(matrix.mean())         
        ],
        'variance': [
            np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            float(np.var(matrix))
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            float(matrix.std())
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            int(matrix.max())            
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            int(matrix.min())
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            int(matrix.sum())
        ]
    }


    return calculations

# Example test
print(calculate([0,1,2,3,4,5,6,7,8]))
