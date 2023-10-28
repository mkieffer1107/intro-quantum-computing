// 2-bit quantum ripple-carry adder -- 7 total qubits (so I can run on IBM quantum processor)

// 10 + 11 = 101 in binary


OPENQASM 2.0;

// include standard gates from IBM Quantum Experience™ © 
include "qelib1.inc";

// quantum sum gate
gate sum cin, a, b
{
    cx a, b;
    cx cin, b;
}

// quantum carry gate
gate carry cin, a, b, cout
{
    ccx a, b, cout;
    cx a, b;
    ccx cin, b, cout;
}

// inverse of quantum carry gate (conjugate transpose)
gate carrydgr cin, a, b, cout
{
    ccx cin, b, cout;
    cx a, b;
    ccx a, b, cout;
}

// declare quantum registers 
qreg c[2]; // carry bits
qreg a[2]; // a input bits
qreg b[3]; // b input bits -> becomes a+b (add two n-bit numbers -> n+1 bit sum)

// declare classical registers
creg bc[3]; // we will measure the state of |b> and store here

// set the input states by applying X gates since states are intialized to |0>
// a = 11
x a[0];
x a[1];

// b = 10
x b[1];

// add the number so that |a>|b> becomes |a>|a+b>
carry c[0], a[0], b[0], c[1];
cx a[1], b[1];
sum c[1], a[1], b[1];
carrydgr c[0], a[0], b[0], c[1];
sum c[0], a[0], b[0];

// measure state of the sum and store in classical register
measure b -> bc;

