// 4-bit quantum ripple-carry adder -- 13 total qubits


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
qreg c[4]; // carry bits
qreg a[4]; // a input bits
qreg b[5]; // b input bits -> becomes a+b (add two n-bit numbers -> n+1 bit sum)

// declare classical registers
creg bc[5]; // we will measure the state of |b> and store here

// set the input states by applying X gates since states are intialized to |0>
// a = 1110
x a[1];
x a[2];
x a[3]; 

// b = 1011
x b[0];
x b[1];
x b[3]; 

// add the number so that |a>|b> becomes |a>|a+b>
carry c[0], a[0], b[0], c[1];
carry c[1], a[1], b[1], c[2];
carry c[2], a[2], b[2], c[3];
carry c[3], a[3], b[3], b[4];
cx a[3], b[3];
sum c[3], a[3], b[3];
carrydgr c[2], a[2], b[2], c[3];
sum c[2], a[2], b[2];
carrydgr c[1], a[1], b[1], c[2];
sum c[1], a[1], b[1];
carrydgr c[0], a[0], b[0], c[1];
sum c[0], a[0], b[0];

// measure state of the sum and store in classical register
measure b -> bc;

