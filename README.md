# TII Quantum Cloud Client

## Install

Install first the package dependencies with the following commands.

We recommend to start with a fresh virtual environment to avoid dependencies
conflicts with previously installed packages.

```bash
python -m venv ./env
source activate ./env/bin/activate
```

The `tii-quantum` package can be installed through `pip`:

```bash
pip install tii-quantum
```

## Quick start

Once installed, the provider allows to run quantum circuit computations on TII's labs.

:warning: Note: to run jobs on the remote cluster it is mandatory to own a
validated account.
Please, sign up to your preferred institution to
obtain the needed token to run computations on the cluster.

The following snippet provides a basic usage example.
Replace the `your-token` string with your user token received during the
registration process. To check which devices are available with your account
please visit the dashboard at your institution.

```python
import qibo
import tii_quantum

# create the circuit you want to run
circuit = qibo.models.QFT(5)

# authenticate to server through the client instance
token = "your-token"
client = tii_quantum.Client(token)

# run the circuit
device = "device_name"
project = "project_name"
job = client.run_circuit(circuit, device=device, project=project, nshots=1024)
result = job.result()
print(result)
```

The `device` name indicates the specific system or machine that will process the
job. The `project` name corresponds to the project or group to which the user
belongs and which will be charged for the service usage.
