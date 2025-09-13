# openfoam-mixing-index

A script that calculates the time-averaged mixing index for each case in the directory.

## Installation

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```


## Usage

Place file in folder which contains all the cases and run the script. The two scripts are used in different ways as follows:

#### mixing_index_main
This is intended for the following scenarios:
- A two-phase case in which one phase is being agitated by the other (originally, steel agitated by argon gas)
- Mixing in the entire geometry is of interest
- A tracer field "T" is present

#### mixing_index_portion
This is intended for the following scenarios:
- A two-phase case in which one phase is being agitated by the other (originally, steel agitated by argon gas)
- Mixing in a portion of the geometry is not of interest (in this example at the top)
- A tracer field "T" is present


