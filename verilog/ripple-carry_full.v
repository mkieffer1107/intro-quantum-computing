// 4-bit ripple-carry adder with all full adders

// adding two n-bit strings results in one n+1 bit string
// first full adder handles the least significant bit addition 
//      (right-most 2 bit operation: A_0 + B_0 + C_0, where C_0 == 0)
// full adders handle 3 bit addition operations (A_i + B_i + C_i) 
module halfadd(S,C,A,B);
    input A, B;
    output S, C;
    
    xor xor1(S,A,B);
    and and1(C,A,B);
endmodule

module fulladd(S,Cout,Cin,A,B);
    input Cin,A,B;
    output S,Cout;
    wire w1,w2,w3;
    
    halfadd half1(w1,w2,A,B);
    halfadd half2(S,w3,Cin,w1); 
    or or1(Cout,w3,w2);
endmodule

module rippleadd(S,A,B);
    // create two inclusive, indexable arrays (4 indices: 4-bit adder)
    // e.g. A[3]A[2]A[1]A[0] + B[3]B[2]B[1]B[0]
    input [3:0] A,B;
    
    // 5-bit sum: Cout = S[4]S[3]S[2]S[1]S[0]
    output [4:0] S;
    output Cout;
    
    // 4 carry bits: C[3], C[2], C[1] (C[4] == S[4])
    wire [3:1] C;
    
    // C[0] == 0
    fulladd full1(S[0], C[1], 1'b0, A[0], B[0]);
    fulladd full2(S[1], C[2], C[1], A[1], B[1]);
    fulladd full3(S[2], C[3], C[2], A[2], B[2]);
    fulladd full4(S[3], S[4], C[3], A[3], B[3]);
endmodule

module main;
    reg [3:0] A,B;
    wire [4:0] S;
    wire Cout;
 
    rippleadd ripple1(S,A,B);
 
    initial
        begin
        A=4'b0110;
        B=4'b1110;
        #5; // Wait 5 time units.
        $display(A," + ",B," = ",S);
        $display("%b ",A,"+ %b ",B,"= %b",S);
    end
endmodule