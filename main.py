from input_handler import handle_input
from monte_carlo import monte_carlo_simulation
from experiments.options import function_options
from experiments.birthday_paradox import birthday_paradox_instance


if __name__ == "__main__":
  #  can be extended to allow user to select a different experiment
  experiment_func_key = 1
  experiment_title = "birthday paradox"
  
  #  can also extract out the input handlers too, creating a controller for the experiment
  sample_size = handle_input("Please Enter the toal people present in the room")
  instance_count = handle_input("Please Enter the number of experiment instances you'd like to run")
  cycle_count = handle_input("Please Enter the number of experiment cycles you wouold like to run")
  
  # can chuck this in a main loop to allow users to run experiements until they've decided they're done
  event_likelihood = monte_carlo_simulation(function_options[experiment_func_key], sample_size, instance_count, cycle_count)
  readable_percentage = f"{(event_likelihood * 100):.1f}"
  
  # could allow users to use the main loop to generate a set of points and to plot the probability of an event within a certain range of values
  print(f"the probability of the {experiment_title} for a sample size of {sample_size} is approximately {readable_percentage}%")