def get_grade_point(marks):

    if marks >= 80:
        return 4.0
    elif marks >= 75:
        return 3.75
    elif marks >= 70:
        return 3.5
    elif marks >= 65:
        return 3.25
    elif marks >= 60:
        return 3.0
    elif marks >= 55:
        return 2.75
    elif marks >= 50:
        return 2.5
    elif marks >= 45:
        return 2.25
    elif marks >= 40:
        return 2.0
    else:
        return 0.0


def calculate_gpa(courses):

    total_weighted_gp = 0
    total_credits = 0
    for course in courses:


        gp = get_grade_point(course['marks'])

        total_weighted_gp += (gp * course['credit'])
        total_credits += course['credit']

    gpa = round(total_weighted_gp / total_credits, 2)
    return gpa, float(total_credits)

def calculate_effective_hours(hours):

    if hours <= 4:
        return float(hours)
    else:

        eff = 4 - 0.5 * (hours - 4)
        return float(max(eff, 0.0))


def get_study_analysis(hours_list):

    effective_hours_list = [calculate_effective_hours(h) for h in hours_list]

    total_actual = float(sum(hours_list))
    total_effective = float(sum(effective_hours_list))


    most_productive_day = effective_hours_list.index(max(effective_hours_list)) + 1

    return {
        'total_actual_hours': total_actual,
        'total_effective_hours': total_effective,
        'most_productive_day': most_productive_day
    }


# --- Part 3: Energy Modeling & Graphing ---

def calculate_energy(hours, k=100, a=-8, h=3):
    """Quadratic equation: E = k + a(hours - h)^2"""
    energy = k + a * (hours - h) ** 2
    return float(max(energy, 0.0))


def get_energy_analysis(hours_list, k=100, a=-8, h=3):

    energies = [calculate_energy(h, k, a, h_val := h) for h in hours_list]

    max_day = energies.index(max(energies)) + 1
    min_day = energies.index(min(energies)) + 1

    return {
        'energies': energies,
        'max_energy_day': max_day,
        'min_energy_day': min_day
    }


def plot_energy_graph():

    import    numpy as np
    import   matplotlib.pyplot as plt
    k, a, h = 100, -8, 3
    hours_range = np.linspace(0, 8, 100)
    energy_values = [calculate_energy(hr, k, a, h) for hr in hours_range]


    plt.figure(figsize=(10, 6))
    plt.plot(hours_range, energy_values, label='Mental Energy Curve', color='blue', linewidth=2)

    # ৭ দিনের ডেটা পয়েন্ট (hours_list = [2, 3, 4, 5, 6, 4, 3])
    study_hours = [2, 3, 4, 5, 6, 4, 3]
    day_energies = [calculate_energy(hr, k, a, h) for hr in study_hours]
    plt.scatter(study_hours, day_energies, color='red', label='Actual Study Days')

    plt.title("Mental Energy Model During Fasting")
    plt.xlabel("Study Hours")
    plt.ylabel("Energy Level")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)


    plt.savefig('energy_graph.png')
    print("Graph saved as energy_graph.png")


