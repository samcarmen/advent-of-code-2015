def get_signal(wire_id, circuit, cache):
    # If the wire's signal is already cached, return it
    if wire_id in cache:
        return cache[wire_id]

    # If the wire's signal is numeric (e.g., "123"),
    # return the parsed integer value
    if wire_id.isdigit():
        return int(wire_id)

    # Get the instruction for the wire
    instruction = circuit[wire_id]

    # Parse the instruction
    parts = instruction.split()

    if len(parts) == 1:
        # Simple assignment without an operator (e.g., "1674 -> b")
        signal = get_signal(parts[0], circuit, cache)
    elif len(parts) == 2:
        # NOT operation (e.g., "NOT ac -> ad")
        _, x = parts[0], parts[1]
        signal = ~get_signal(x, circuit, cache) & 0xFFFF
    else:
        # Binary operations (e.g., "x AND y -> z" or "x RSHIFT 1 -> y")
        x = parts[0]
        op = parts[1]
        y = parts[2]

        if op == "AND":
            signal = get_signal(x, circuit, cache) & get_signal(
                y,
                circuit,
                cache,
            )
        elif op == "OR":
            signal = get_signal(x, circuit, cache) | get_signal(
                y,
                circuit,
                cache,
            )
        elif op == "LSHIFT":
            amount = int(y)
            signal = (get_signal(x, circuit, cache) << amount) & 0xFFFF
        elif op == "RSHIFT":
            amount = int(y)
            signal = (get_signal(x, circuit, cache) >> amount) & 0xFFFF

    # Cache the computed signal for the wire
    cache[wire_id] = signal
    return signal


if __name__ == "__main__":
    # Read the instructions from the input file
    with open("./input/D7.txt", "r") as file:
        instructions = file.read().splitlines()

    # Create a dictionary to store the circuit instructions
    circuit = {}

    # Populate the circuit dictionary with the provided instructions
    for instruction in instructions:
        parts = instruction.split(" -> ")
        circuit[parts[1].strip()] = parts[0]

    # Create a cache to store computed signals
    signal_cache = {}

    # Calculate the signal for wire 'a'
    result_signal = get_signal("a", circuit, signal_cache)

    print("Signal on wire 'a':", result_signal)

    # Store the original signal on wire 'a'
    original_signal_a = result_signal

    # Update the circuit dictionary to override wire 'b' 
    # with the original signal on 'a'
    circuit["b"] = str(original_signal_a)

    # Create a cache to store computed signals
    signal_cache = {}

    # Calculate the new signal for wire 'a' with the updated circuit
    new_signal_a = get_signal("a", circuit, signal_cache)

    print("New signal on wire 'a':", new_signal_a)
