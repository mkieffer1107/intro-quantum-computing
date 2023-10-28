// ripple-carry adder handles 3 bit addition operations 
module halfadd(S,C,A,B);
    input A, B;
    output S, C;
    
    xor xor1(S,A,B);
    and and1(C,A,B);
endmodule

module fulladd(S,Cout,Cin,A,B);
    input Cin, A, B;
    output S, Cout;
    wire w1, w2, w3;
    
    halfadd half1(w1, w2, A, B);
    halfadd half2(S, w3, Cin, w1);
    or or1(Cout, w3, w2);
endmodule

module rippleadd(S,A,B);
    input [3:0] A, B;
    output [4:0] S;
    output Cout;
    wire [3:1] C;
    
    halfadd half1(S[0], C[1], A[0], B[0]);
    fulladd full1(S[1], C[2], C[1], A[1], B[1]);
    fulladd full2(S[2], C[3], C[2], A[2], B[2]);
    fulladd full3(S[3], S[4], C[3], A[3], B[3]);
endmodule 

module main;
    reg [3:0] A, B;
    wire [4:0] S;
    wire Cout;
    
    rippleadd ripple1(S,A,B);

    initial
        begin
            A = 4'b1011;
            B = 4'b0011;
            #5; // wait 5 time units
            $display(A, " + ", B, " = " S);
            $display("%b", A, " + %b", B, " = %b", S);
        end
endmodule

