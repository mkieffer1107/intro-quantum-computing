// half adder handles the least significant bit addition (right-most 2 bit operation)

module halfadd(S,C,A,B);
    // input bits A and B (registers)
    input A, B;
    // Sum and Carry output bits
    output S, C;
    
    // the sum bit is given by XOR(A,B)
    xor xor1(S,A,B);
    
    // the carry bit is given by AND(A,B)
    and and1(C,A,B);

endmodule


module main;
    reg A, B;
    wire S, C;
    
    halfadd half1(S,C,A,B);     
        
    initial
        begin
            // bits to add
            A = 0;
            B = 0; 
            
            #5; // wait 5 time units
            $display("Sum = ", S);
            $display("Carry = ", C);
        end
endmodule

