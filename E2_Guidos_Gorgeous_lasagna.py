# Define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(n):
    """
    Returns time left to bake.
    
    Parameters:
    - n: int, time already spent on baking
    
    Returns:
    - int, time remaining for baking
    """
    return EXPECTED_BAKE_TIME - n

def preparation_time_in_minutes(layers):
    """
    Returns preparation time in minutes for each layer.
    
    Parameters:
    - layers: int, number of layers
    
    Returns:
    - int, total preparation time
    """
    return layers * 2

def elapsed_time_in_minutes(layers, bake_time):
    """
    Returns total elapsed time in minutes.
    
    Parameters:
    - layers: int, number of layers
    - bake_time: int, time already spent on baking
    
    Returns:
    - int, total elapsed time
    """
    return preparation_time_in_minutes(layers) + bake_time
