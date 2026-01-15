#include "Vbarrel_shifter_8bit.h"
#include "verilated_fst_c.h"
#include <iostream>
#include <cstdlib>

int main(int argc, char** argv) {
    Verilated::commandArgs(argc, argv);
    Vbarrel_shifter_8bit* top = new Vbarrel_shifter_8bit;
    
    // Setup FST tracing
    VerilatedFstC* tfp = new VerilatedFstC;
    Verilated::traceEverOn(true);
    top->trace(tfp, 99);
    tfp->open("wave.fst");
    
    // Initialize inputs
    top->data_in = 0;
    top->shift_amount = 0;
    top->shift_direction = 0;
    
    // Test loop - no clock present, so just change inputs and eval
    for (int i = 0; i < 30; i++) {
        // Generate random test values
        top->data_in = rand() & 0xFF;           // Random 8-bit value
        top->shift_amount = rand() & 0x7;       // Random 3-bit shift amount
        top->shift_direction = rand() & 0x1;    // Random direction
        
        // Evaluate combinational logic
        top->eval();
        
        // Dump trace
        tfp->dump(i * 10);
        
        // Print some values for verification
        std::cout << "Step " << i << ": data_in=" << (int)top->data_in 
                  << ", shift_amount=" << (int)top->shift_amount 
                  << ", direction=" << (int)top->shift_direction 
                  << ", data_out=" << (int)top->data_out << std::endl;
    }
    
    // Cleanup
    tfp->close();
    delete tfp;
    delete top;
    return 0;
}