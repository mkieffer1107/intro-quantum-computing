OPENQASM 2.0;

// Pauli X gate
gate x a
{
    U(pi, 0, pi) a;
}

// define the classical and quantum registers
// q: |q2>|q1>|q0> == |q2,q1,q0> (qubits)
// c: c2, c1, c0 (bits)
qreg q[3];
creg c[3];

// apply an X gate to |q0>
// x is lowercase because it is a user-defined gate
x q[0];

// apply CNOT gate where |q0> is control and |q1> is target
// CX is capitalized because it is a primitive gate
CX q[0], q[1];

// measure |q> and store in classical register: |qi> --> ci
measure q -> c;