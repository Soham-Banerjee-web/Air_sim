import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Aerospace Communication Simulation")
    parser.add_argument('--config', type=str, default='configs/default.yaml', 
                        help='Path to the configuration file')
    parser.add_argument('--run', action='store_true', 
                        help='Run the simulation')
    parser.add_argument('--scenario', type=str, 
                        help='Path to the scenario file for the simulation')
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    if args.run:
        print(f"Running simulation with config: {args.config}")
        if args.scenario:
            print(f"Using scenario: {args.scenario}")
        # Here you would typically initialize and run the simulation
    else:
        print("Use --run to start the simulation.")

if __name__ == "__main__":
    main()