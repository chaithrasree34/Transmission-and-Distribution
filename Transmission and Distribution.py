# Transmission-and-Distribution
import math

# ==========================================
# TRANSMISSION & DISTRIBUTION CALCULATOR
# ==========================================

def three_phase_current(power_kw, voltage_kv, power_factor):
    """
    Calculate 3-phase line current.

    P = √3 × V × I × PF
    """

    power = power_kw * 1000
    voltage = voltage_kv * 1000

    current = power / (
        math.sqrt(3) * voltage * power_factor
    )

    return current


def transmission_calculation():

    print("\n" + "=" * 55)
    print("       TRANSMISSION LINE CALCULATOR")
    print("=" * 55)

    power_kw = float(input("Enter transmitted power (kW): "))
    voltage_kv = float(input("Enter transmission voltage (kV): "))
    power_factor = float(input("Enter power factor: "))

    resistance = float(
        input("Enter resistance per phase (Ω): ")
    )

    length = float(
        input("Enter transmission line length (km): ")
    )

    # Calculate current
    current = three_phase_current(
        power_kw,
        voltage_kv,
        power_factor
    )

    # Total resistance per phase
    total_resistance = resistance * length

    # Copper loss
    power_loss = (
        3 * current ** 2 * total_resistance
    )

    power_loss_kw = power_loss / 1000

    # Input power
    input_power_kw = power_kw + power_loss_kw

    # Efficiency
    efficiency = (
        power_kw / input_power_kw
    ) * 100

    # Voltage drop approximation
    voltage_drop = (
        math.sqrt(3)
        * current
        * total_resistance
        * power_factor
    )

    voltage_drop_kv = voltage_drop / 1000

    receiving_voltage = voltage_kv - voltage_drop_kv

    print("\n" + "-" * 55)
    print("                 RESULTS")
    print("-" * 55)

    print(f"Line Current        : {current:.2f} A")
    print(f"Total Resistance    : {total_resistance:.2f} Ω")
    print(f"Power Loss          : {power_loss_kw:.2f} kW")
    print(f"Voltage Drop        : {voltage_drop_kv:.3f} kV")
    print(f"Receiving Voltage   : {receiving_voltage:.3f} kV")
    print(f"Input Power         : {input_power_kw:.2f} kW")
    print(f"Transmission Loss   : {power_loss_kw:.2f} kW")
    print(f"Efficiency          : {efficiency:.2f} %")

    print("-" * 55)


def distribution_calculation():

    print("\n" + "=" * 55)
    print("       DISTRIBUTION SYSTEM CALCULATOR")
    print("=" * 55)

    voltage = float(
        input("Enter distribution voltage (V): ")
    )

    current = float(
        input("Enter load current (A): ")
    )

    power_factor = float(
        input("Enter power factor: ")
    )

    resistance = float(
        input("Enter line resistance (Ω): ")
    )

    # Single-phase real power
    power = (
        voltage
        * current
        * power_factor
    )

    # Line power loss
    loss = current ** 2 * resistance

    # Useful load power
    output_power = power - loss

    # Efficiency
    efficiency = (
        output_power / power
    ) * 100

    # Voltage drop
    voltage_drop = current * resistance

    receiving_voltage = voltage - voltage_drop

    print("\n" + "-" * 55)
    print("                 RESULTS")
    print("-" * 55)

    print(f"Load Power          : {power:.2f} W")
    print(f"Line Loss           : {loss:.2f} W")
    print(f"Voltage Drop        : {voltage_drop:.2f} V")
    print(f"Receiving Voltage   : {receiving_voltage:.2f} V")
    print(f"Output Power        : {output_power:.2f} W")
    print(f"Efficiency          : {efficiency:.2f} %")

    print("-" * 55)


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n")
    print("=" * 55)
    print("     TRANSMISSION & DISTRIBUTION SYSTEM")
    print("=" * 55)

    print("1. Transmission Line Calculation")
    print("2. Distribution System Calculation")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        transmission_calculation()

    elif choice == "2":

        distribution_calculation()

    elif choice == "3":

        print("\nProgram terminated.")
        break

    else:

        print("\nInvalid choice. Please try again.")
