def get_value(wire_signals, cmd):
    # If it's a number, return its integer value
    if cmd.isdigit():
        return int(cmd)

    # If the command is a known signal, return its value
    if cmd in wire_signals:
        return wire_signals[cmd]

    return None


def evaluate(wires, wire_signals):
    while wires:
        for cmd in list(wires.keys()):
            if "AND" in cmd:
                x, _, y, _, z = cmd.split()
                val_x = get_value(wire_signals, x)
                val_y = get_value(wire_signals, y)
                if val_x is not None and val_y is not None:
                    wire_signals[z] = val_x & val_y
                    del wires[cmd]
            elif "OR" in cmd:
                x, _, y, _, z = cmd.split()
                val_x = get_value(wire_signals, x)
                val_y = get_value(wire_signals, y)
                if val_x is not None and val_y is not None:
                    wire_signals[z] = val_x | val_y
                    del wires[cmd]
            elif "LSHIFT" in cmd:
                x, _, n, _, z = cmd.split()
                val_x = get_value(wire_signals, x)
                if val_x is not None:
                    wire_signals[z] = val_x << int(n)
                    del wires[cmd]
            elif "RSHIFT" in cmd:
                x, _, n, _, z = cmd.split()
                val_x = get_value(wire_signals, x)
                if val_x is not None:
                    wire_signals[z] = val_x >> int(n)
                    del wires[cmd]
            elif "NOT" in cmd:
                _, x, _, z = cmd.split()
                val_x = get_value(wire_signals, x)
                if val_x is not None:
                    wire_signals[z] = 65535 - val_x
                    del wires[cmd]
            else:
                _, z = cmd.split(" -> ")
                val_x = get_value(wire_signals, z)
                if val_x is None:
                    x = cmd.split(" -> ")[0]
                    val_x = get_value(wire_signals, x)
                    if val_x is not None:
                        wire_signals[z] = val_x
                        del wires[cmd]

    return wire_signals["a"]


def main():
    wires = {}
    wire_signals = {}
    instructions = []

    with open("./input/D7.txt") as data:
        for instruction in data:
            instructions.append(instruction)

    for line in instructions:
        # Extract the command and destination wire from each line
        cmd, wire = line.split(" -> ")
        wires[cmd] = wire

    return evaluate(wires, wire_signals)


print(main())
