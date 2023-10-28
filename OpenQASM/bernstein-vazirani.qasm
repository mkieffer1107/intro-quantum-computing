OPENQASM 2.0;
include "qelib1.inc";

// quantum oracle
// |x>|y> -> |x>|x XOR y>
// if |x> = |->, then we get a phase kickback
gate uf y, x0, x1, x2, x3 {
  cx x3, y;
  cx x2, y;
  cx x0, y;
}

qreg q[5];
creg c[5];

// set |q0> = |0> to |-> state
x q[0];
h q[0];

// put a Hadamard gate in front of each bit input
// this creates a superposition of every possible
// bit string of length 4
h q[1];
h q[2];
h q[3];
h q[4];

// apply oracle 
uf q[0], q[1], q[2], q[3], q[4];


// apply Hadamard gates to each input bit
h q[1];
h q[2];
h q[3];
h q[4];

// the final state that is measured is
// |s>|->, so the |-> collapses with 1/2
// probability to either |0> or |1>, and
// the bit string s is the 
// hidden value that is dotted into 
// the input bits
measure q -> c;