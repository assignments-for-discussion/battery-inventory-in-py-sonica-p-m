import pandas as pd
def count_batteries_by_health(present_capacities):
  for i in present_capacities:
    soh=100*i/120
    if soh>80:
    return 'healthy'
  elif 62<=soh<=80:
    return 'exchange'
  else:
    return 'failed'
  
  
  

  


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
