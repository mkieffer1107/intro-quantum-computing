// measuring in A'B basis
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

// A' basis
h q[1];
cx q[1], q[0];
h q[1];

// B basis
s q[0];
h q[0];
t q[0];
h q[0];

measure q -> c;