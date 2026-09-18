import subprocess
import sys

print("Starting pipeline..")

#clean and validate customer data
subprocess.run(
  [sys.executable, "src/transform.py"],
  check=True
)
# load customers to PostgreSQL
subprocess.run(
    [sys.executable, "src/load.py"],
    check=True
)

# load orders to PostgreSQL
subprocess.run(
    [sys.executable, "src/load_orders.py"],
    check=True
)

print("Pipeline finished successfully")