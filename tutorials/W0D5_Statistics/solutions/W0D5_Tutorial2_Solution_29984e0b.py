
mu = 5
sigma = 1

# Generate 1000 random samples from a Gaussian distribution
dataX = generate_normal_samples(mu, sigma, 1000)

# We define the function to optimise, the negative log likelihood
def negLogLike(theta):
  """ Function for computing the negative log-likelihood given the observed data
  and given parameter values stored in theta.

    Args:
      theta (ndarray): normal distribution parameters (mean is theta[0],
                            variance is theta[1])

    Returns:
      Calculated negative Log Likelihood value!
  """
  return -sum(np.log(norm.pdf(dataX, theta[0], theta[1])))

# Define bounds, var has to be positive
bnds = ((None, None), (0, None))

# Optimize with scipy!
# Uncomment once function above is implemented
optimal_parameters = sp.optimize.minimize(negLogLike, (2, 2), bounds = bnds)
print("The optimal mean estimate is: " + str(optimal_parameters.x[0]))
print("The optimal variance estimate is: " + str(optimal_parameters.x[1]))

# optimal_parameters contains a lot of information about the optimization,
# but we mostly want the mean and variance