if __name__ == "__main__":
    args = parse_args()
    setup_logging(args.v)
    sim = Simulation(args.steps)
    sim.run()
    with open(args.output, "w") as f:
        f.write(sim.get_state())

    if args.gui != 0: # condition for launching the GUI mode
        from gui import run_gui
        run_gui(sim, args.tile_size, args.ant_color, args.fps) # where run_gui is still to be written...