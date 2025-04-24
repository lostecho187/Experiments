# Experiments
## Dataset and Preprocessing
### Get the public data
Access to the [Los Alamos National Laboratory (LANL) Dataset (auth.txt.gz)](https://csr.lanl.gov/data/cyber1/)

### Run lms and gfe
**lms:**
Put auth.txt in lms folder then run:

    python lms/main.py

**gfe:**
Don't need to put anything in this folder. Run following commands one by one.

    python gfe/data.py
    python gfe/graph_map.py
    python gfe/features.py
    python gfe/data.py

After running these scripts, you'll find a file named 'auth.csv' under gfe folder. This is LAMD's training data. 
