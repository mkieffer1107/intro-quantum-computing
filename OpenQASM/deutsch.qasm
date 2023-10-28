OPENQASM 2.0;
include "qelib1.inc";

// |x>|y> -> |x>|x XOR y>
// if |x> = |->, then we get a phase kickback
gate uf y, x {
  cx x, y;
  x y;
}

qreg q[2];
creg c[2];


// q0 from |0> to |->
x q[0]; // |1>
h q[0]; // |->

// Deutsch's algorithm 
h q[1];
uf q[0], q[1];
h q[1];

// input:  |x>|->
// output: |0>|->, if b0 = b1
//         |1>|->, if b0 != b1
// upon measuring, we see that we get
// state |q1>|q2> = |1>|->, which 
// collapses with 1/2 probability 
// to |1>|0> or |1>|1> because we
// are measuring in the Z basis

// because the first qubit is |1>,
// then we know that b0 != b1, and
// thus the parity of the bits is odd
measure q -> c;