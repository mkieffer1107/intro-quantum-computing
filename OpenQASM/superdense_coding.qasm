// we always start by creating a
// maximally entangled state (phi plus)
// then the messages correpsond to the 
// bell basis states:
//   phi + --> |00>
//   psi + --> |01>
//   phi - --> |10>
//   psi + --> |11>

OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

// first we entangle the two quibits by
// creating a maximally entangled state phi +
h q[1];
cx q[1], q[0];

// at this point, the two quibits are separated

// then we encode a message in one quibit
// phi plus -> psi minus
x q[1];
z q[1];

// now we send one qubit to the other

// then we decode the message
cx q[1], q[0];
h q[1];

measure q -> c;