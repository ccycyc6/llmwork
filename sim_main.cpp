#include "Vcounter_8bit.h"
#include "verilated_fst_c.h"
#include <iostream>
#include <cstdlib>

int main(int argc, char** argv) {
    // Initialize Verilator
    Verilated::commandArgs(argc, argv);
    Verilated::traceEverOn(true);

    // Create instance of the module
    Vcounter_8bit* top = new Vcounter_8bit;

    // Setup FST tracing
    VerilatedFstC* tfp = new VerilatedFstC;
    top->trace(tfp, 99); // Trace 99 levels of hierarchy
    tfp->open("wave.fst");

    // Initialize inputs
    top->clk = 0;
    top->rst_n = 0; // Start with reset active (low)
    top->en = 0;

    // Simulation loop for 50 steps
    for (int i = 0; i < 50; ++i) {
        // Toggle clock: 0->1->0 for each cycle
        top->clk = 0;
        top->eval();
        tfp->dump(2*i); // Dump at even time steps

        top->clk = 1;
        top->eval();
        tfp->dump(2*i + 1); // Dump at odd time steps

        // Control inputs based on simulation step
        if (i == 1) {
            top->rst_n = 1; // Deassert reset after first cycle
        }
        if (i >= 2 && i < 10) {
            top->en = 1; // Enable counting for steps 2-9
        } else if (i >= 10 && i < 15) {
            top->en = 0; // Disable for steps 10-14
        } else if (i >= 15 && i < 30) {
            top->en = 1; // Re-enable for steps 15-29
        } else if (i >= 30 && i < 35) {
            top->en = 0; // Disable again for steps 30-34
        } else if (i >= 35) {
            top->en = 1; // Enable for remaining steps
        }

        // Optional: Print count value for debugging
        // std::cout << "Step " << i << ": clk=" << (int)top->clk
        //           << ", rst_n=" << (int)top->rst_n
        //           << ", en=" << (int)top->en
        //           << ", count=" << (int)top->count << std::endl;
    }

    // Cleanup
    tfp->close();
    delete tfp;
    delete top;
    return 0;
}