
def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    else:
        return False
    
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percentage_value = generated_power / theoretical_max_power * 100
    if percentage_value >= 80:
        return "green"
    elif 60 <= percentage_value < 80:
        return "orange"
    elif 30 <= percentage_value < 60:
        return "red"
    else:
        return "black"
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if temperature * neutrons_produced_per_second < threshold * 90/100:
        return "LOW"
    elif threshold * 90/100 < temperature * neutrons_produced_per_second < threshold * 110/100 : 
        return "NORMAL"
    else:
        return "DANGER"
    
    