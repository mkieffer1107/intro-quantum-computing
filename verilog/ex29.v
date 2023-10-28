
module main;
    reg A, B;
    wire out1, out2, C;
    
    not not1(out1, B);
    or or1(out2, out1, B);
    or or2(C, out2, A);
       
        
    initial
        begin
            // bits to add
            A = 0;
            B = 0; 
            
            #5; // wait 5 time units
            $display("Result = ", C);
            
            // bits to add
            A = 1;
            B = 0; 
            
            #5; // wait 5 time units
            $display("Result = ", C);
            
            // bits to add
            A = 0;
            B = 1; 
            
            #5; // wait 5 time units
            $display("Result = ", C);
            
            // bits to add
            A = 1;
            B = 1; 
            
            #5; // wait 5 time units
            $display("Result = ", C);
            
        end
endmodule

