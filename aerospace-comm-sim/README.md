# Aerospace Communication Simulation Project

This project simulates multiple aircraft communicating with each other in a defined region to ensure seamless flights. The simulation includes various components such as aircraft agents, communication protocols, and environmental factors.

## Project Structure

```
aerospace-comm-sim
├── src
│   ├── sim
│   │   ├── __init__.py
│   │   ├── simulation.py
│   │   ├── scheduler.py
│   ├── agents
│   │   ├── __init__.py
│   │   ├── aircraft.py
│   │   ├── traffic_manager.py
│   ├── comms
│   │   ├── __init__.py
│   │   ├── link.py
│   │   ├── protocol.py
│   ├── environment
│   │   ├── __init__.py
│   │   ├── region.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── kinematic.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── cli.py
│   │   └── config.py
├── configs
│   ├── default.yaml
├── experiments
│   ├── example_scenario.yaml
├── tests
│   ├── test_simulation.py
│   ├── test_comms.py
├── scripts
│   ├── run_sim.sh
├── notebooks
│   ├── prototype.ipynb
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd aerospace-comm-sim
pip install -r requirements.txt
```

## Usage

To run the simulation, execute the following command:

```bash
bash scripts/run_sim.sh
```

You can modify the simulation parameters in the `configs/default.yaml` file or define your own scenarios in the `experiments/example_scenario.yaml` file.

## Testing

Unit tests are provided to ensure the functionality of the simulation and communication components. To run the tests, use:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.