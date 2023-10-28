OPENQASM 2.0;
include "qelib1.inc";

// https://arxiv.org/pdf/1707.03429.pdf Section 3.1 shows the contents of qelib1.inc

// define the classical and quantum registers
// q: |q2>|q1>|q0> == |q2,q1,q0>
// c: c3, c2, c1
qreg q[3];
creg c[3];

// apply an X gate to |q0>
// x is lowercase because it is a user-defined gate
x q[0];

// apply CNOT gate where |q0> is control and |q1> is target
// note that CX has been replaced with cx because this is a user-defined gate
cx q[0], q[1];   // could also use uppercase native CX

// measure |q> and store in classical register: |qi> --> ci
measure q -> c;