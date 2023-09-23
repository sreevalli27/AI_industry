import heapq

class Patient:
    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0  # Initialize waiting time to 0
        self.turnaround_time = 0  # Initialize turnaround time to 0

    def __repr__(self):
        return self.name

def fcfs(patients):
    patients.sort(key=lambda p: p.arrival_time)
    current_time = 0

    for patient in patients:
        patient.waiting_time = max(0, current_time - patient.arrival_time)
        current_time += patient.burst_time
        patient.turnaround_time = patient.waiting_time + patient.burst_time

    return patients

def sjf(patients):
    patients.sort(key=lambda p: p.burst_time)
    current_time = 0

    for patient in patients:
        patient.waiting_time = max(0, current_time - patient.arrival_time)
        current_time += patient.burst_time
        patient.turnaround_time = patient.waiting_time + patient.burst_time

    return patients

def ps(patients):
    patients.sort(key=lambda p: (p.arrival_time, -p.priority))  # Sort by arrival time and priority (higher priority first)
    current_time = 0

    for patient in patients:
        patient.waiting_time = max(0, current_time - patient.arrival_time)
        current_time += patient.burst_time
        patient.turnaround_time = patient.waiting_time + patient.burst_time

    return patients

# Example usage:
patients = [
    Patient('A', 0, 30, 3),
    Patient('B', 10, 20, 5),
    Patient('C', 15, 40, 2),
    Patient('D', 20, 15, 4)
]

fcfs_patients = fcfs(patients.copy())
sjf_patients = sjf(patients.copy())
ps_patients = ps(patients.copy())

# Calculate and print average waiting time for FCFS, SJF, and PS
avg_waiting_time_fcfs = sum(p.waiting_time for p in fcfs_patients) / len(fcfs_patients)
avg_waiting_time_sjf = sum(p.waiting_time for p in sjf_patients) / len(sjf_patients)
avg_waiting_time_ps = sum(p.waiting_time for p in ps_patients) / len(ps_patients)

# Calculate and print average turnaround time for FCFS, SJF, and PS
avg_turnaround_time_fcfs = sum(p.turnaround_time for p in fcfs_patients) / len(fcfs_patients)
avg_turnaround_time_sjf = sum(p.turnaround_time for p in sjf_patients) / len(sjf_patients)
avg_turnaround_time_ps = sum(p.turnaround_time for p in ps_patients) / len(ps_patients)

# Print results including waiting time and turnaround time for FCFS, SJF, and PS
print('FCFS:')
for patient in fcfs_patients:
    print(f'{patient.name} - Waiting Time: {patient.waiting_time}, Turnaround Time: {patient.turnaround_time}')
print(f'Average Waiting Time (FCFS): {avg_waiting_time_fcfs}')
print(f'Average Turnaround Time (FCFS): {avg_turnaround_time_fcfs}')
print()

print('SJF:')
for patient in sjf_patients:
    print(f'{patient.name} - Waiting Time: {patient.waiting_time}, Turnaround Time: {patient.turnaround_time}')
print(f'Average Waiting Time (SJF): {avg_waiting_time_sjf}')
print(f'Average Turnaround Time (SJF): {avg_turnaround_time_sjf}')
print()

print('PS:')
for patient in ps_patients:
    print(f'{patient.name} - Waiting Time: {patient.waiting_time}, Turnaround Time: {patient.turnaround_time}')
print(f'Average Waiting Time (PS): {avg_waiting_time_ps}')
print(f'Average Turnaround Time (PS): {avg_turnaround_time_ps}')
print()


# Calculate average waiting time for each scheduling algorithm
avg_waiting_time_fcfs = sum(p.waiting_time for p in fcfs_patients) / len(fcfs_patients)
avg_waiting_time_sjf = sum(p.waiting_time for p in sjf_patients) / len(sjf_patients)
avg_waiting_time_ps = sum(p.waiting_time for p in ps_patients) / len(ps_patients)

# Determine the best scheduling algorithm based on average waiting time
scheduling_algorithms = ["FCFS", "SJF", "PS"]
avg_waiting_times = [avg_waiting_time_fcfs, avg_waiting_time_sjf, avg_waiting_time_ps]

best_schedule_waiting = scheduling_algorithms[avg_waiting_times.index(min(avg_waiting_times))]
print(f"The best schedule based on Average Waiting Time is: {best_schedule_waiting}")
