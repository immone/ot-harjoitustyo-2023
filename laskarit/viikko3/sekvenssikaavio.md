sequenceDiagram
	main->>machine: Machine()
	machine->>tank: FuelTank()
	machine->>tank: tank.fill(40)
	machine->>engine: Engine(tank)
    machine->>engine: start()
    engine-)machine: true
    machine->>engine: use_energy()
    engine->>tank: tank.consume(10)
    tank-)main