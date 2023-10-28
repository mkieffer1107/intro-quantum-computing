// 8-bit ripple-carry adder with a half adder and full adderss

// adding two n-bit strings results in one n+1 bit string
// half adder handles the least significant bit addition 
//          (right-most 2 bit operation: A_0 + B_0)
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
    // create two inclusive, indexable arrays (8 indices: 8-bit adder)
    // e.g. A[7]...A[3]A[2]A[1]A[0] + B[7]...B[3]B[2]B[1]B[0]
    input [7:0] A,B;
    
    // 9-bit sum: Cout = S[8]...S[4]S[3]S[2]S[1]S[0]
    output [8:0] S;
    output Cout;
    
    // 8 carry bits: C[7],..., C[3], C[2], C[1] (C[8] == S[8])
    wire [7:1] C;
    
    halfadd half1(S[0], C[1], A[0], B[0]);
    fulladd full1(S[1], C[2], C[1], A[1], B[1]);
    fulladd full2(S[2], C[3], C[2], A[2], B[2]);
    fulladd full3(S[3], C[4], C[3], A[3], B[3]);
    fulladd full4(S[4], C[5], C[4], A[4], B[4]);
    fulladd full5(S[5], C[6], C[5], A[5], B[5]);
    fulladd full6(S[6], C[7], C[6], A[6], B[6]);
    fulladd full7(S[7], S[8], C[7], A[7], B[7]);
    

    
    
endmodule

module main;
    reg [7:0] A,B;
    wire [8:0] S;
    wire Cout;
 
    rippleadd ripple1(S,A,B);
 
    initial
        begin
        A=8'b10101101;
        B=8'b00111001;
        #5; // Wait 5 time units.
        $display(A," +",B," = ",S);
        $display("%b ",A,"+ %b ",B,"= %b",S);
    end
endmodule