OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[3];


// set initial state of q2
// to be teleported
//h q[2];

// entangle q0, q1 in phi + bell state
h q[1];
cx q[1], q[0];

// teleport initial state from 
// q2 to q0
cx q[2], q[1];
h q[2];
cx q[1], q[0];
cz q[2], q[0];


//measure q[1] -> c[1];
//measure q[0] -> c[0];
//measure q[2] -> c[2];
//measure q -> c;

// @columns [0,1,2,3,4,5,6,7,8]