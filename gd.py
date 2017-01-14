def gradient_descent_update(x, gradx, learning_rate):
    """
    Performs a gradient descent update.
    """
    x += - (gradx * learning_rate)

    # Return the new value for x
    return x
