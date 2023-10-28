# Greenberger-Horne-Zeiliger state (GHZ state, entangled)

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

# define quantum and classical registers
# q: |q2>|q1>|q0> == |q2,q1,q0> (qubits)
# c: c2, c1, c0 (bits)
qreg_q = QuantumRegister(3, 'q')
creg_c0 = ClassicalRegister(3, 'c0')
circuit = QuantumCircuit(qreg_q, creg_c0)

# hadamard gate
circuit.h(qreg_q[2])

# cnot with |q2> as control and |q1> as target
circuit.cx(qreg_q[2], qreg_q[1])

# cnot with |q2> as control and |q0> as target
circuit.cx(qreg_q[2], qreg_q[0])

# measure |q> and store in classical register: |qi> --> ci
circuit.measure(qreg_q[0], creg_c0[0])
circuit.measure(qreg_q[1], creg_c0[1])
circuit.measure(qreg_q[2], creg_c0[2])