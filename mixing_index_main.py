import fluidfoam
import numpy as np
import os

cwd =  os.getcwd()
cases = [entry.name for entry in os.scandir() if entry.is_dir()]

mixing_index_final = []

# Loop through every case
for case in cases:
    case_path = os.path.join(cwd, case)
  
    # Time steps in folder
    times = [
        name for name in os.listdir(case_path)
        if os.path.isdir(os.path.join(case_path, name)) and name.isdigit()
    ]
  times = sorted(times, key=int)

  # Tracer variance at time = 0s
  variance_0 = np.var(fluidfoam.readfield(case, "0", "T"))

  # Create empty array for storing mixing index at each time of the case.
  mixing_indexes = []

  # Calculate mixing index at each time step
  for t in times:
    tracer_t =  fluidfoam.readfield(case, f"{t}", "T") # Read tracer at time t.
    variance_t = np.var(tracer_t)
    mixing_index_t = (1 - (variance_t / variance_0)**0.5)
    mixing_indexes.append(mixing_index_t)

  # Append time-averaged mixing index to list
  mixing_index_final.append(np.mean(mixing_indexes))


# Write results to text file
output_file = "mixing_results.txt"
with open(output_file, "w") as f:
    f.write("case\tmixing_index\n")  # header
    for case, m in zip(cases, mixing_index_final):
        f.write(f"{case}\t{m:.6f}\n")
