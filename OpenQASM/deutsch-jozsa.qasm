OPENQASM 2.0;
include "qelib1.inc";

// some quantum oracle with property:
// |x>|y> -> |x>|x XOR y>
// if |x> = |->, then we get a phase kickback
gate uf y, b0, b1, b2 {
  x b0;
  s b1;
  z b2;
  y y;
  s b1;
  z b2;
  y y;
  s b1;
  x b0;
  s b1;
}

// initialze registers
qreg q[4];
creg c[4];

// set q0 to state |-> for phase kickback
x q[0];
h q[0];

// put a Hadamard gate in front of each bit input
// this creates a superposition of every possible
// bit string of length 3
h q[1];
h q[2];
h q[3];

// apply the quantum oracle
uf q[0], q[1], q[2], q[3];

// apply Hadamard gates to each bit ouput
// in order to measure bits in z-basis
h q[1];
h q[2];
h q[3];

// if the function in Uf is contant, then
// the final state should be
//     |b2>|b1>|b0>|-> = |0>|0>|0>|-> = |000->
// if the function in Uf is balanced, then
// the final state should be anything else because
// there is a 0% chance of getting the above state
measure q -> c;

// we see that the output is either
// |0000> or |0001> so the function is constant
// note: measuring |-> gives a 50% chance
// of getting either |0> or |1>, so that 
// is why it is 50/50 between |0000> and |0001>