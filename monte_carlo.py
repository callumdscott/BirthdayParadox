#  performs a naiive monte-carlo siimulation for estimating the probability of an event
def monte_carlo_simulation(probability_instance, sample_size: int = 10, 
                           experiment_instance_count: int = 10, experiment_cycle_count: int = 1000) -> float:
  probability_outcomes = []
  for i in range(experiment_cycle_count):
    results = []
    
    for i in range(experiment_instance_count):
      result = probability_instance(sample_size)
      results.append(result)
    
    event_occurances = sum(results)
    event_probability = event_occurances / experiment_instance_count
    probability_outcomes.append(event_probability)
  average_probablity = sum(probability_outcomes) / experiment_cycle_count
  return average_probablity